#!/usr/bin/env python
# encoding: utf-8
"""
lego-robot
This code was adapted from RyanTeks example scripts
https://github.com/ryanteck
"""
import keys
import time
#change to otherInterface.py if you want to test with a dummy implmenentation
from robotGpio import RobotMoves
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory


##########
# setup pubnub
##########
pnconfig = PNConfiguration()
pnconfig.subscribe_key = keys.SUBSCRIBE
pnconfig.publish_key = keys.PUBLISH
pnconfig.ssl = False

pubnub = PubNub(pnconfig)
## robotmoves handles the mapping from command to gpio pins
robotMoves = RobotMoves()


###############
# Pubnub listener
# This class handles messages being sent from pubNub to the robot
###############
class MyListener(SubscribeCallback):
    def message(self, pubnub, messageResult):
        message = messageResult.message
        if message['move'] == 'forwards':
            robotMoves.forwards()
        elif message['move'] == 'backwards':
            robotMoves.backwards()
        elif message['move'] == 'left':
            robotMoves.left()
        elif message['move'] == 'right':
            robotMoves.right()
        elif message['move'] == 'nudge-left':
            robotMoves.left()
            time.sleep(0.1)
            robotMoves.stop()
        elif message['move'] == 'nudge-right':
            robotMoves.right()
            time.sleep(0.1)
            robotMoves.stop()
        elif message['move'] == 'stop':
            robotMoves.stop()
        elif message['move'] == 'lightOn':
    	    robotMoves.lightOn()
        elif message['move'] == 'lightOff':
    	    robotMoves.lightOff()
        elif message['move'] == 'stepCW':
            robotMoves.stepCW()
        elif message['move'] == 'stepACW':
            robotMoves.stepACW()
        else:
            robotMoves.stop()
    def status(self, pubnub, status):
        pass
    def presence(self, pubnub, presence):
        pass
################
# Set up pubnub listener and subscriber
################
my_listener = MyListener()
pubnub.add_listener(my_listener)
pubnub.subscribe().channels(keys.CHANNEL).execute()
print("SUBSCRIBED TO CHANNEL: " + keys.CHANNEL + " listening for messages....")
