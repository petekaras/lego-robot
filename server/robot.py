from pubnub import Pubnub

pubnub = Pubnub(publish_key="pub-c-a20fde3e-257d-4c7b-ac2b-6e734e0270d3", subscribe_key="sub-c-bb03bdaa-a812-11e5-9dba-0619f8945a4f")
def callback(message, channel):
    print(message['move'])
  
  
def error(message):
    print("ERROR : " + str(message))
  
  
def connect(message):
    print("CONNECTED")
    print pubnub.publish(channel='my_channel', message='Hello from the PubNub Python SDK')
  
  
  
def reconnect(message):
    print("RECONNECTED")
  
  
def disconnect(message):
    print("DISCONNECTED")
  
  
pubnub.subscribe(channels='lego-home', callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)