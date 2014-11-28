import mosquitto
import json
import time
device_id = "868850013067326"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(mosq, userdata, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('vneigbor/%s' % device_id)

# The callback for when a PUBLISH message is received from the server.
def on_message(mosq, userdata, message):
    print message.topic, message.payload

client = mosquitto.Mosquitto("mosq-rec")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", "18833")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
