import time

import paho.mqtt.client as mqtt
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor

CounterFitConnection.init("127.0.0.1", 5000)


light_sensor = GroveLightSensor(0)
led = GroveLed(5)

id = "test_"

client_name = id + "nightlight_client"

mqtt_client = mqtt.Client(client_id=client_name)
mqtt_client.username_pw_set("mqtt_user", "mqtt_password")
mqtt_client.connect("192.168.1.62")

mqtt_client.loop_start()

print("MQTT connected!")


while True:
    light = light_sensor.light
    print("Light level:", light)

    if light < 300:
        led.on()
    else:
        led.off()

    time.sleep(1)
