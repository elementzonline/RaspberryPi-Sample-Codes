'''
https://thingspeak.com
ThinkSpeak API data visalisation sample code
'''

import requests
import json

curr_temp = raw_input("What is the temperatre today? ")
apiKey = "ZP1PZO62773HXWVU"
queryStr = "http://184.106.153.149/update.html?key="+apiKey+"&field1="+curr_temp
res = requests.get(queryStr)