'''import paho.mqtt.client as mqtt
import os

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("iot")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Topic: {} / Message: {}".format("home","sensors"))
    if(msg.payload.decode("UTF-8") == "Reply"):
        client.publish("python", os.environ.get('OS',''))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Use the IP address of your MQTT server here
SERVER_IP_ADDRESS = "128.113.147.169"
client.connect(SERVER_IP_ADDRESS, 1883, 60)

client.loop_forever()'''
"""import paho.mqtt.client as paho
from serial import Serial

broker="129.161.209.248"
port=1883

ser=Serial("COM11",baudrate=115200)
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
#ret= client1.publish("home/sensors",14) 

while True:
    data = input("Enter data to send: ")
    ser.write(data.encode())

    response = ser.readline().decode()
    print(response)

    client1.publish("home/sensors", response)"""
import paho.mqtt.client as mqtt
import serial

broker = "192.168.1.193"
port = 1883
topic = "home/sensors"

ser = serial.Serial("COM11", baudrate=115200)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, message):
    print("Received message: " + message.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)

while True:
    data = input("Enter data to send: ")
    ser.write(data.encode())

    response = ser.readline().decode()
    print(response)

    client.publish(topic, response)