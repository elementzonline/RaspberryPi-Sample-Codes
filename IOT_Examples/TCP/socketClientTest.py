'''
https://docs.python.org/2/library/socket.html#example
'''

#!/usr/bin/env python

import socket
import time


TCP_IP = '127.0.0.1'    # Need to change here 
TCP_PORT = 9999        #  use appropraite port
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "connected"
s.send(MESSAGE)
print 'message send'
data = s.recv(BUFFER_SIZE)
time.sleep(1)
s.close()

print "received data:", data
