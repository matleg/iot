"""
see also command in readme:

mosquitto_sub -h localhost -u mqtt_user -P mqtt_password -t '#' -v
"""

import json
import time

import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor

CounterFitConnection.init("127.0.0.1", 5000)


light_sensor = GroveLightSensor(0)
led = GroveLed(5)


mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("mqtt_user", "mqtt_password")
mqtt_client.connect("192.168.1.62")

mqtt_client.loop_start()

print("MQTT connected!")

mqtt_client.subscribe("#")  # subscribe to all topics


def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("All msgs:", payload)


mqtt_client.on_message = handle_command

while True:
    time.sleep(2)
