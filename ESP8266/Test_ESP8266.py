#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys, serial
from time import *
import datetime, string


if len(sys.argv) != 3:
	print "Usage: Test_ESP8266.py SSID Password"
else:
	ssid = sys.argv[1]
	print "SSID:", ssid
	pwd = sys.argv[2]
	print "Pwd:", pwd

FILE = None

BAUD = 9600
SCNT = 0
servIP = "192.168.0.24"  # Server IP Address
servPort = 9990
#servIP = "74.125.225.6"	  # Google's IP Number
#servPort = 80

REG_OFF = True
REG_ON = False

ser = serial.Serial( '/dev/ttyUSB0', BAUD, timeout=2.5, rtscts=False )

# Power Cycle ESP8266 - The RTS pin is used to control the 3.3V regulator.
print "Pwr Off - 10s"
ser.setRTS( REG_OFF )	# Turn off 3.3V power.
sleep( 10 )
print "Pwr On - 3s"
ser.setRTS( REG_ON )	# Turn on 3.3V power.
sleep( 3 )		# and wait for WiFi to stabablize.


# ----------------------------------------
def wifiCommand( sCmd, waitTm=1, sTerm='OK' ):
	lp = 0
	ret = ""

	print	
	print "Cmd: %s" % sCmd
	ser.flushInput()
	ser.write( sCmd + "\r\n" )
	ret = ser.readline()	# Eat echo of command.
	sleep( 0.2 )
	while( lp < waitTm ):
		while( ser.inWaiting() ):
			ret = ser.readline().strip( "\r\n" )
			print ret
			lp = 0
		if( ret == sTerm ): break
		#if( ret == 'ready' ): break
		if( ret == 'ERROR' ): break
		sleep( 1 )
		lp += 1
	return ret

# ------------------------------------------
def wifiCheckRxStream():
	while( ser.inWaiting() ):
		s = ser.readline().strip( "\r\n" )

wifiCommand( "AT" )				# Should just return an 'OK'.
wifiCommand( "AT+CIPCLOSE" )			# Close any open connection.
#wifiCommand( "AT+RST", 5, sTerm='ready' )	# Reset the radio. Returns with a 'ready'.
wifiCommand( "AT+GMR" )			# Report firmware number.
wifiCommand( "AT+CWMODE=1" )			# Set mode to 'Sta'.
wifiCommand( "AT+CWLAP", 10 )			# Scan for AP nodes. Returns SSID / RSSI.

# Join Access Point given SSID and Passcode.
wifiCommand( "AT+CWJAP=\""+ssid+"\",\""+pwd+"\"", 5 )
wifiCommand( "AT+CWJAP?" )


# Sometimes it takes a couple querries until we get a IP number.
sIP = wifiCommand( "AT+CIFSR", 3, sTerm="ERROR" )
if( sIP == 'ERROR' ):
	i = 10	# Retry n times.
	while( (sIP == 'ERROR') and (i > 0) ):
		print i
		sIP = wifiCommand( "AT+CIFSR", 3, sTerm="ERROR" )
		if( sIP == 'ERROR' ): sleep( 3 )
		i -= 1
	if( i > 0 ):
		print "IP Num:", sIP
	else:
		print "Bad IP Number."
else:
		print "IP Num:", sIP

wifiCommand( "AT+CIPMUX=0" )	# Setup for single connection mode.
print "Delay - 5s"gt
sleep( 5 )

s = wifiCommand( "AT+CIPSTART=\"TCP\",\""+servIP+"\","+str(servPort), 10, sTerm="Linked" )

if( s == 'Linked' ):
	#cmd = 'GET / HTTP/1.0\r\n\r\n'
	cmd = "Now is the time for all good men to come to the aid of their country.\r\n"
	#cmd = "Bridgeport 30 34 31 35 31 34 41 42 43 34\r\n" 
	cmdLn = str( len(cmd) )
	s = wifiCommand( "AT+CIPSEND=" + cmdLn, sTerm=">" )
	#sleep( 1 )
	wifiCommand( cmd, sTerm="SEND OK" )
	#sleep( 2 )
	#wifiCommand( "+IPD" )
	i = 5
	while( i > 0 ):		# Dump whatever comes over the TCP link.
		while( ser.inWaiting() ): 
			sys.stdout.write( ser.read() )
			i = 5 	# Keep timeout reset as long as stuff in flowing.
		sys.stdout.flush()
		i -= 1
		sleep( 1 )
else:
	print "Error:"
	ser.write( "\r\n" )
	sleep( 0.5 )
	i = 5
	while( (i > 0) and ser.inWaiting() ):	# Dump whatever is in the Rx buffer.
		while( ser.inWaiting() ): 
			sys.stdout.write( ser.read() )
			i = 5 	# Keep timeout reset as long as stuff in flowing.
		sys.stdout.flush()
		i -= 1
		sleep( 1 )
		

