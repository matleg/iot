"""
server subscribes to client topic, and publish the command so that the client reads and execute it
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


client_name = "nightlight_client"

client_telemetry_topic = client_name + "/telemetry"
server_command_topic = client_name + "/commands"

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("mqtt_user", "mqtt_password")
mqtt_client.connect("192.168.1.62")

mqtt_client.loop_start()

print("MQTT connected!")


def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    command = {"led_on": payload["light"] < 300}
    print("Sending message:", command)

    client.publish(server_command_topic, json.dumps(command))


mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)
