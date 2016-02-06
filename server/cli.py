#lego-robot
from sys import exit
import RPi.GPIO as GPIO
from pubnub import Pubnub

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

def right():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,1)
        GPIO.output(23,0)

def left():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,0)
        GPIO.output(23,1)

def forwards():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,1)
        GPIO.output(23,0)

def backwards():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,1)

def stop():
        GPIO.output(17,0)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,0)

pubnub = Pubnub(publish_key="pub-c-a20fde3e-257d-4c7b-ac2b-6e734e0270d3", subscribe_key="sub-c-bb03bdaa-a812-11e5-9dba-0619f8945a4f")
def callback(message, channel):
    print(message['move'])
    if message['move'] == 'forwards':
        forwards()
    elif message['move'] == 'backwards':
        backwards()
    elif message['move'] == 'left':
        left()
    elif message['move'] == 'right':
        right()
    elif message['move'] == 'stop':
        stop()        
    else:
        stop()
  
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

try:
    while 1:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(1)