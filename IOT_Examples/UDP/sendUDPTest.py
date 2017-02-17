__author__ = 'dhanish'

import socket
import time

# UDP_IP = '192.168.1.155'
# UDP_IP = '0.0.0.0'
UDP_PORT = 1995
BUFFER_SIZE = 1024
SERVERIP = ""
# print len(MESSAGE)

# aa = MESSAGE.encode('hex')
# print aa

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
i = 0
s.bind(('0.0.0.0', UDP_PORT))
print "connected"
#while(True):
    #i = i+1
    # s.sendto('{"ssid":"Elementz_Broadband","password":"4716006699"}', ("192.168.4.1", UDP_PORT))
    #s.sendto('{"ssid":"Dhanish","password":"reset123@","mqtt_server":"iot.eclipse.org","mqtt_port":"1883","mqtt_ctrl":"/Control","mqtt_stat":"/Status"}', ("192.168.4.1", UDP_PORT))
    #rcvData, rcvAddress = s.recvfrom(1024)
    #print rcvData, rcvAddress
    # s.sendto("hello" + str(i), (rcvAddress[0], UDP_PORT))
    # time.sleep(1)
    # print 'sending data - ', time.localtime()

s.sendto("hello" + str(i), (SERVERIP, UDP_PORT))
print 'message send'

rcvData, rcvAddress = s.recvfrom(1024)
print rcvData, rcvAddress
time.sleep(1)
s.close()
