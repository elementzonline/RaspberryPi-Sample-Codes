from Adafruit_CharLCD import Adafruit_CharLCD   # Importing Adafruit library for LCD
import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 

lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)
lcd.clear()



while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:        
         lcd.clear() #Clear the LCD screen
         lcd.message ('Temp = %.1f C' % temperature)  # Display the value of temperature
         lcd.message ('\nHum = %.1f %%' % humidity)   #Display the value of Humidity 
         time.sleep(2)  #Wait for 2 sec then update the values
