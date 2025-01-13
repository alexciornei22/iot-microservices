import json
import random
import string
from datetime import datetime as dt, UTC
from time import sleep

import paho.mqtt.client as mqtt

LOCATION = "UPB"
STATION = "RPi_1"
NR_SENSORS = 10


class Sensor:
    def __init__(
            self,
            location: str,
            station: str,
            battery: float,
            temperature: float,
            battery_step: float,
            temperature_step: float
    ):
        self.location = location
        self.station = station

        self.battery = battery
        self.temperature = temperature
        self.battery_step = battery_step
        self.temperature_step = temperature_step

    def update(self):
        self.battery += self.battery_step
        self.temperature += self.temperature_step
        if self.battery <= 0 or self.battery >= 100:
            self.battery_step *= -1
        if self.temperature <= -10 or self.temperature >= 30:
            self.temperature_step *= -1

    def to_json(self):
        return json.dumps({
            "timestamp": dt.now(UTC).isoformat(),
            "temperature": self.temperature,
            "BAT": self.battery,
            "PRJ": "SCD"
        })


if __name__ == '__main__':
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.connect("localhost", 1883, 60)

    sensors = [
        Sensor(
            ''.join(random.choices(string.ascii_uppercase, k=3)),
            ''.join(random.choices(string.ascii_uppercase, k=3)),
            random.uniform(50, 100),
            random.uniform(20, 30),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        )
        for _ in range(NR_SENSORS - 1)
    ]
    sensors.append(Sensor(LOCATION, STATION, 100.0, 25.0, -1.0, -1.0))

    while True:
        for sensor in sensors:
            mqtt_client.publish(f"{sensor.location}/{sensor.station}", sensor.to_json())
            sensor.update()

        sleep(1)
