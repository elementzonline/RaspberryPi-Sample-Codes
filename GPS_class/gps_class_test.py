__author__ = 'dhanish'

import serial
from gps_class import gps


serGPS = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=None,
                    xonxoff=False, rtscts=False,
                    writeTimeout=None, dsrdtr=False,
                    interCharTimeout=None)

gps_ser = gps(serGPS)
while(True):
    print gps_ser.readGPS()