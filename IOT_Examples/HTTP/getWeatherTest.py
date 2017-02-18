'''
http://docs.python-requests.org/en/master/user/quickstart/
OpenWhethermap API
'''

import requests
import json

appid = "6e9770a6cfc7c3a60009efc5c900d082"

cityName = raw_input("Enter city name to get the temperature data ")

queryStr = "http://api.openweathermap.org/data/2.5/find?q=" + str(cityName) + "&units=metric&appid=" + appid

res = requests.get(queryStr)

jsonData = json.loads(res.text)
city = jsonData['list'][0]['name']
print "getting data from ", city
data = jsonData['list'][0]['main']
print "normal temperature is ", data["temp"]
print "max temperature is ", data["temp_max"]
print "min temperature is ", data["temp_min"]