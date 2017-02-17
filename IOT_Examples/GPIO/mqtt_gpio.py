# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

outPin= 40

GPIO.setmode(GPIO.BOARD)

GPIO.setup(outPin, GPIO.OUT)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
	client.subscribe("gpiotest")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)
	if str(msg.payload) == "high":
		GPIO.output(outPin, GPIO.HIGH)
	else:
		GPIO.output(outPin, GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.username_pw_set("gsm_user","gsm_pass")
client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
