# -*- coding: utf-8 -*-
import constants
import grovepi
import paho.mqtt.client as mqtt
import json


# Connect the LED to digital port D5
led = 5

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	print("Connected, subscribing")
	client.subscribe(constants.TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	receivedMessage = json.loads(msg.payload)
	print "Topic: " + msg.topic + "\nValue: " + receivedMessage
	# Send PWM signal to LED
	grovepi.analogWrite(led, receivedMessage["measurement"] / 4)


grovepi.pinMode(led, "OUTPUT")
    
client = mqtt.Client("bastideGroveConsumer")
client.on_connect = on_connect
client.on_message = on_message
    
client.connect(constants.BROKER, constants.PORT)
client.loop_start()

raw_input('Hit enter to stop\n')

client.disconnect()
client.loop_stop()

grovepi.analogWrite(led, 0)
