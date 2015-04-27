__author__ = 'dhanish'
import serial
import time
import sys
from gsm_class import gsm

gsm_ser = serial.Serial()
gsm_ser.port = "/dev/ttyUSB0"
gsm_ser.baudrate = 9600
gsm_ser.timeout = 3
gsm_ser.xonxoff = False
gsm_ser.rtscts = False
gsm_ser.bytesize = serial.EIGHTBITS
gsm_ser.parity = serial.PARITY_NONE
gsm_ser.stopbits = serial.STOPBITS_ONE


try:
    gsm_ser.open()
    gsm_ser.flushInput()
    gsm_ser.flushOutput()
except:
    print 'Cannot open serial port'
    sys.exit()

GSM = gsm(gsm_ser)

GSM.sendCommand("AT+IPR=9600;&W")
print GSM.getResponse()

time.sleep(.1)

GSM.sendCommand("AT+CMGF=1;&W")
print GSM.getResponse()

time.sleep(.1)

GSM.sendCommand("AT+CREG?")
print GSM.getResponse()

time.sleep(.1)

GSM.sendCommand("AT+CMGD=1")
print GSM.getResponse()

time.sleep(.1)

# if (GSM.sendMessage("8129025513", "HELLO MISTER") == True):
#     print 'Message sending Success'
# else:
#     print 'Message sending Failed'
# time.sleep(.1)


status,msg = GSM.readMessage()
if status == 0:
    print 'no new messages'
else:
    print 'new messages arrived: ' + msg




gsm_ser.close()