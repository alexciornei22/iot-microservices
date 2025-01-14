import json
import logging
import sys
from datetime import datetime as dt, UTC
from typing import Any
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from paho.mqtt.client import MQTTMessage, Client
from paho.mqtt.properties import Properties
from paho.mqtt.reasoncodes import ReasonCodes
from config import INFLUXDB_BUCKET, INFLUXDB_ORG, DEBUG_DATA_FLOW


class MqttHandler:
    def __init__(self, influxdb_client: InfluxDBClient):
        self._influxdb_write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        self._logger = logging.getLogger(__name__)

    def on_connect(self, client: Client, userdata: Any, flags: dict[str, int], rc: ReasonCodes, props: Properties):
        client.subscribe("#")

    def on_message(self, client: Client, userdata, msg: MQTTMessage):
        try:
            payload = json.loads(msg.payload)

            time = payload.get("timestamp", dt.now(UTC).isoformat())
            time = dt.fromisoformat(time)

            location, station = msg.topic.split("/")
            for key, value in payload.items():
                if isinstance(value, (int, float)):
                    point = Point(key) \
                        .tag("location", location) \
                        .tag("station", station) \
                        .field("value", value) \
                        .time(time)

                    self._influxdb_write_api.write(
                        bucket=INFLUXDB_BUCKET,
                        org=INFLUXDB_ORG,
                        record=point
                    )

                    if DEBUG_DATA_FLOW:
                        self._logger.debug({
                            "message": "Message sent to InfluxDB",
                            "topic": msg.topic,
                            "timestamp": time.isoformat(),
                            "payload": json.dumps(payload)
                        })

        except Exception as e:
            self._logger.error({
                "message": "Error while processing the message",
                "error": e,
                "topic": msg.topic,
                "payload": msg.payload
            })
