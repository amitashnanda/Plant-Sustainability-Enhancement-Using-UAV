import time
import paho.mqtt.client as mqtt

# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("temperature/#")

# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    print ( str(msg.payload) )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("goyqkibb", "g4lPf1Q32AtU")
client.connect("m15.cloudmqtt.com", 17143, 60)

# client.loop_forever()
client.loop_start()
time.sleep(1)
while True:
    client.publish("Hello World!")
    print ("Message Sent")
    time.sleep(15)

client.loop_stop()
client.disconnect()