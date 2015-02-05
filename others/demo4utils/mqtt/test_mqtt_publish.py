import mosquitto
import json
import time
device_id = "868850013067326"
device_id = "862620024748586"

def on_publish():
    print 'published'
    
client = mosquitto.Mosquitto("soualgou-publish-client")
client.on_publish = on_publish
client.connect("localhost", "18833")
message = json.dumps(dict(message=str(time.time())))
client.publish('vneigbor/%s' % device_id, message.encode("UTF-8"), 1)
print 'push', message
client.disconnect()
