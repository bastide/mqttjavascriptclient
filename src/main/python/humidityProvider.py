# -*- coding: utf-8 -*-
import time
from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import json
import constants

sense = SenseHat()
client = mqtt.Client()
client.connect(constants.BROKER, constants.PORT, 60)
client.loop_start()

time.sleep(1)

oldValue = -1
newValue = 0

while True:
    try:
        # Capteur d'humidité sur sensehzt
        newValue = sense.get_humidity()
        print("valeur humidité: " + str(newValue))
        if newValue != oldValue:
            oldValue = newValue
            sentMessage = {
                "roomID": 1,
                "sensorType": "HUMIDITY",
                "measurement": newValue,
            }
            jsonMessage = json.dump(sentMessage)
            print("Sending: " + jsonMessage)
            client.publish(constants.TOPIC, jsonMessage)

        time.sleep(1)

    except KeyboardInterrupt:
        break

    except IOError:
        print("Error")

client.loop_stop()
