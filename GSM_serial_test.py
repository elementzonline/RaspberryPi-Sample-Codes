"""
author: dhanish
company: Elementz Engineers Guild Pvt Ltd
Created on: Tue Aug 12 20:17:12 2014

"""

import serial
import time

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1) # 9600 is the default Baudrate for SIM900A modem
ser.flush()
ser.write('ATD9020XXXXXX;\r') # AT command to call a number using GSM Modem
#ser.read(2)    # read 2 bytes of data from the serial port
time.sleep(10)  # wait for 10 seconds

ser.write('ATH\r')  # Hold the call
ser.close()    # close the serial port
