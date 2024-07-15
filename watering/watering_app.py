import json
import time

import paho.mqtt.client as mqtt

id = "123"

client_telemetry_topic = id + "/telemetry"
server_command_topic = id + "/commands"
client_name = id + "soilmoisturesensor_server"

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("mqtt_user", "mqtt_password")
mqtt_client.connect("192.168.1.62")

mqtt_client.loop_start()


def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    command = {"relay_on": payload["soil_moisture"] > 450}
    print("Sending message:", command)

    client.publish(server_command_topic, json.dumps(command))


mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)
