# -*- coding: utf-8 -*-
import time
import grovepi
import paho.mqtt.client as mqtt
import json
import constants

client = mqtt.Client()
client.connect(constants.BROKER, constants.PORT, 60)
client.loop_start()

# Connect the Rotary Angle Sensor to analog port A2
potentiometer = 2

time.sleep(1)

oldValue = -1
newValue = 0

while True:
    try:
        # Read resistance from Potentiometer
        newValue = grovepi.analogRead(potentiometer)
        print("valeur potentiomètre: " + str(newValue))
        if newValue != oldValue:
            oldValue = newValue
            sentMessage = {
                "roomID": 1,
                "sensorType": "ROTARY",
                "measurement": newValue,
            }
            jsonMessage = json.dumps(sentMessage)
            print("Sending: " + jsonMessage)
            client.publish(constants.TOPIC, jsonMessage)

        time.sleep(1)

    except KeyboardInterrupt:
        break

    except IOError:
        print("Error")

client.loop_stop()
