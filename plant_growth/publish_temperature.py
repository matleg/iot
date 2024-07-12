import json
import time

import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT

CounterFitConnection.init("127.0.0.1", 5000)

sensor = DHT("11", 5)
# CounterFit simulates this combined humidity and temperature sensor
# by connecting to 2 sensors, a humidity sensor on the pin given when the DHT class is created, and a temperature
# sensor that runs on the next pin. If the humidity sensor is on pin 5,
# the shim expects the temperatures sensor to be on pin 6.

client_name = "plant_growth"

client_telemetry_topic = client_name + "/telemetry"

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set("mqtt_user", "mqtt_password")
mqtt_client.connect("192.168.1.62")

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    _, temp = sensor.read()
    telemetry = json.dumps({"temperature": temp})

    print("Sending telemetry ", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(1)
