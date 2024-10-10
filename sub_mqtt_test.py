import paho.mqtt.client as mqttClient
import time
  
def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
        print("Connection to Broker failed, retrying in 5 seconds")
        #time.sleep(5)
        #client.reconnect()
  
def on_message(client, userdata, message):
    message.payload=message.payload.decode("utf-8")
    if client==client_one:

        print("\nMessage received from Client:",message.payload)
        print("\t\n")
    elif client==client2:
        print("\nMessage received from Client2:",message.payload)
        print("\t\n")  
    elif client==client3:
        print("\nMessage received from Client3:",message.payload)
        print("\t\n")

    elif client==client4:
        print("\nMessage received from Client4:",message.payload)
        print("\t\n")
    
  
Connected = False   #global variable for the state of the connection
  
broker_address= "129.161.136.168"  #Broker address
port = 1883                         #Broker port
#user = "yourUser"                    #Connection username
#password = "yourPassword"            #Connection password
  
client_one = mqttClient.Client("Python")               #create new instance
client2= mqttClient.Client("Python1")
client3=mqttClient.Client("Python2")
client4=mqttClient.Client("Python3")

#client.username_pw_set(user, password=password)    #set username and password
client_one.on_connect= on_connect                      #attach function to callback
client_one.on_message= on_message   
                   #attach function to callback
client2.on_connect=on_connect
client2.on_message=on_message  

client3.on_connect=on_connect
client3.on_message=on_message

client4.on_connect=on_connect
client4.on_message=on_message

client_one.connect(broker_address, port)    
client2.connect(broker_address, port)
client3.connect(broker_address, port)
client4.connect(broker_address, port)
      #connect to broker
  
client_one.loop_start()        #start the loop

client2.loop_start()

client3.loop_start()

client4.loop_start()
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)

client_one.subscribe("home/sensors")

client2.subscribe("floor")

client3.subscribe("floor/location")

client4.subscribe("floor/location/destination")

  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print("exiting")
    client_one.disconnect()
    client_one.loop_stop()

    client2.disconnect()
    client2.loop_stop()

    client3.disconnect()
    client3.loop_stop()

    client4.disconnect()
    client4.loop_stop()    