from pyngrok import ngrok
import paho.mqtt.client as mqtt
import time
mqttc=mqtt.Client()
mqttc.connect("test.mosquitto.org", 1883, 60)                                  # Mqtt broker
ngrok.set_auth_token("ADD YOUR NGROCK TOKEN HERE")      # Enter the registered Auth_Token
public_url = ngrok.connect("http://192.168.43.145:5001")                       # tunnel to host:port instead of localhost

print(public_url)                                                              # Displaying the ngrok_tunnel url 

while True:
    time.sleep(1)
    mqttc.publish("ngrok_test",public_url)                                      # Publishing the created URL to "ngrok_test" Topic 
	mqttc.loop(2)
	time.sleep(120) # send mqtt message every 2 minutes





