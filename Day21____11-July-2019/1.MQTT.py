# It is a kind of socket programming 

import paho.mqtt.client as mqtt
client=mqtt.Client()
def on_connect(client,u,c,rc):
    print("Connected Successfully",rc)


# u= user data
# c= client method
# rc= return connect(status - which tell us whether connect or not)

def on_msg(client,u,m):
# m=Message

##    print(str(m.topic),m.payload.decode('utf-8'))
    print(str(m.topic)) # for know who has send the message
    print(m.payload.decode('utf-8'))

client.on_connect=on_connect
client.on_message=on_msg

subtopic=input("Enter Your Subscriber Topic: ")
pubtopic=input("Enter Your Publisher Topic: ")
client.connect('iot.eclipse.org',1883)
client.loop_start()

client.subscribe(subtopic)
while(1):
    chat=input(" ")
    if(chat=='q'):
        break
    else:
        client.publish(pubtopic,chat)
client.loop_stop()
