
from socket import *
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)  # motor 2
GPIO.setup(6, GPIO.OUT)  # motor 2
GPIO.setup(13, GPIO.OUT)  # motor 1
GPIO.setup(19, GPIO.OUT)  # motor 1
GPIO.setup(26, GPIO.OUT)  # enable 2
GPIO.setup(16, GPIO.OUT)  # enable 1

GPIO.output(16, True)  # enable 1
GPIO.output(26, True)  # enable 2

state = True

HOST = "192.168.0.66"  # local host
PORT = 9000  # open port 7000 for connection
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)  # how many connections can it receive at one time
conn, addr = s.accept()  # accept the connection
print "Connected by: ", addr  # print the address of the person connected
while True:
    data = conn.recv(1024)  # how many bytes of data will the server receive

    data.rstrip()

    if data == "u":
        GPIO.output(5, True)
        GPIO.output(6, False)
        GPIO.output(13, True)
        GPIO.output(19, False)
    elif data == 'l':
        GPIO.output(5, True)
        GPIO.output(6, False)
        GPIO.output(13, False)
        GPIO.output(19, True)
    elif data == 'r':
        GPIO.output(5, False)
        GPIO.output(6, True)
        GPIO.output(13, False)
        GPIO.output(19, True)
    elif data == 'd':
        GPIO.output(5, False)
        GPIO.output(6, True)
        GPIO.output(13, False)
        GPIO.output(19, True)
    else :
        GPIO.output(5, False)
        GPIO.output(6, False)
        GPIO.output(13, False)
        GPIO.output(19, False)

    print "Received: ", repr(data)
# reply = raw_input("Reply: ") #server's reply to the client
    reply = ("ok")
    conn.sendall(reply)
conn.close()
