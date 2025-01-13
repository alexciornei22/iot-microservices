import json
from datetime import datetime as dt, UTC
from time import sleep

import paho.mqtt.client as mqtt

LOCATION = "UPB"
STATION = "RPi_1"

if __name__ == '__main__':
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.connect("localhost", 1883, 60)

    battery = 100.0
    battery_step = -0.2
    temperature = 20.0
    temperature_step = 0.2

    while True:
        payload = json.dumps({
            "timestamp": dt.now(UTC).isoformat(),
            "temperature": temperature,
            "BAT": battery,
            "PRJ": "SCD"
        })

        mqtt_client.publish(f"{LOCATION}/{STATION}", payload)

        sleep(1)

        battery += battery_step
        temperature += temperature_step
        if battery <= 50 or battery >= 100:
            battery_step *= -1
        if temperature >= 30 or temperature <= 20:
            temperature_step *= -1
