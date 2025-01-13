import os

MQTT_BROKER_URL = os.environ.get("MQTT_BROKER_URL", "mosquitto")
MQTT_BROKER_PORT = int(os.environ.get("MQTT_BROKER_PORT", 1883))

INFLUXDB_URL = os.environ.get("INFLUXDB_URL", "http://influxdb:8086")
INFLUXDB_TOKEN = os.environ.get("INFLUXDB_TOKEN", "token")
INFLUXDB_ORG = os.environ.get("INFLUXDB_ORG", "org")
INFLUXDB_BUCKET = os.environ.get("INFLUXDB_BUCKET", "bucket")
