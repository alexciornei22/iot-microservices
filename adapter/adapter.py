import paho.mqtt.client as mqtt
import influxdb_client as influxdb
from config import INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG, MQTT_BROKER_URL, MQTT_BROKER_PORT
from mqtt_handler import MqttHandler

if __name__ == "__main__":
    influxdb_client = influxdb.InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)

    handler = MqttHandler(influxdb_client)

    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.on_connect = handler.on_connect
    mqtt_client.on_message = handler.on_message
    mqtt_client.connect(MQTT_BROKER_URL, MQTT_BROKER_PORT, 60)

    mqtt_client.loop_forever()
