import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ledPin = 40
inputPin = 3

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(inputPin, GPIO.IN)


while(1):
	print GPIO.input(inputPin)


