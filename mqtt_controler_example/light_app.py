"""
this is the client,
it subscribes to the command topic, and publish its state on the client topic so that the server reads it.
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


def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload["led_on"]:
        led.on()
    else:
        led.off()


mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

while True:
    light = light_sensor.light
    telemetry = json.dumps({"light": light})
    print("Sending telemetry ", telemetry)
    mqtt_client.publish(client_telemetry_topic, telemetry)
    time.sleep(5)
