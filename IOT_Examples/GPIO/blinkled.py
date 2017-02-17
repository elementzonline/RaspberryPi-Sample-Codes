'''
General: https://www.raspberrypi.org/documentation/usage/gpio/

Python help: https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/


'''


import RPi.GPIO as GPIO
import time

blueled = 40 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(blueled,GPIO.OUT)

while (1):
	GPIO.output(blueled,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(blueled,GPIO.LOW)
	time.sleep(1)
