import paho.mqtt.client as mqtt
import time

mqtt=mqtt.Client("MOGRITHS")
mqtt.connect("localhost",1883) #MQTT서버에 연결
while True:
    count=0
    for i in range(100):
        if(count==10):
            break
        
        if(i==90):
            mqtt.publish("MOGRITHS","i is 89")
            mqtt.publish("MOGRITHS","----------------")
        
            

mqtt.loop(2000) #timeout 2sec