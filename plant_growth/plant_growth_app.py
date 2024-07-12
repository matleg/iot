import csv
import json
import time
from datetime import datetime
from pathlib import Path

import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection

CounterFitConnection.init("127.0.0.1", 5000)


temperature_file_name = "temperature.csv"
fieldnames = ["date", "temperature"]

if not Path.is_file(Path.cwd() / temperature_file_name):
    with open(temperature_file_name, mode="w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

client_name = "plant_growth"

client_telemetry_topic = client_name + "/telemetry"

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("mqtt_user", "mqtt_password")
mqtt_client.connect("192.168.1.62")

mqtt_client.loop_start()

print("MQTT connected!")


def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    with open(temperature_file_name, mode="a") as temperature_file:
        temperature_writer = csv.DictWriter(temperature_file, fieldnames=fieldnames)
        temperature_writer.writerow(
            {
                "date": datetime.now().astimezone().replace(microsecond=0).isoformat(),
                "temperature": payload["temperature"],
            }
        )


mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(1)
