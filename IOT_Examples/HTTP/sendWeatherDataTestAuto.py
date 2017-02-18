'''
https://thingspeak.com
ThinkSpeak API data visalisation sample code
Get weather data from OpenWhethermap API
'''

import requests
import json
import time


apiKey_OpenWhetherMap = "6e9770a6cfc7c3a60009efc5c900d082"
apiKey_Thingspeak = "ZP1PZO62773HXWVU"

cityName = raw_input("Enter city name to get the temperature data ")

queryStr = "http://api.openweathermap.org/data/2.5/find?q=" + str(cityName) + "&units=metric&appid=" + apiKey_OpenWhetherMap

res = requests.get(queryStr)

jsonData = json.loads(res.text)
city = jsonData['list'][0]['name']
print "getting data from ", city
data = jsonData['list'][0]['main']
print "normal temperature is ", data["temp"]
print "max temperature is ", data["temp_max"]
print "min temperature is ", data["temp_min"]

curr_temp = str(data["temp"])

queryStr = "http://184.106.153.149/update.html?key="+apiKey_Thingspeak+"&field1="+curr_temp
res = requests.get(queryStr)
time.sleep(15)