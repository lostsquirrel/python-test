import mosquitto
import json
import time
device_id = "868850013067326"

def on_publish():
    print 'published'
    
client = mosquitto.Mosquitto("soualgou-publish-client")
client.on_publish = on_publish
client.connect("localhost")
message = json.dumps(dict(message="123xdlfjsd"))
client.publish('soulagou/%s' % device_id, message.encode("UTF-8"), 1)
print message
client.disconnect()
