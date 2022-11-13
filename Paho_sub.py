import paho.mqtt.client as mqtt
# 서버로부터 CONNTACK 응답을 받을 때 호출되는 콜
def on_connect(client,userdata,flags,rc):
    print("연결되었습니다 "+str(rc))
    client.subscribe("MOGRITHS")

# 서버로부터 publish message를 받을 때 호출되는 콜백 함수
def on_message(client,userdata,msg):
    print(msg.topic+": "+str(msg.payload))
    
client=mqtt.Client() #클라이언트 오브젝트 생성
client.on_connect=on_connect #콜백 설정
client.on_message=on_message
client.connect("localhost",1883,60)
client.loop_forever()