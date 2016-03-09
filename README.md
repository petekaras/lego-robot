# lego-robot

## Hardware

* Raspberry Pi model ??
* Ryanteck RTK-000-001 Motor Controller Board 
* Motor Robot Car chassis kit with Speed encoder (bought from Amazon)
* Recharge battery pack for power source
* 4 AA batteries for motor power
* Lots of bits of Lego form my sons lego sets and some from my old lego set


## Software
* PubNub realtime infrastructure-as-a-service
* Raspbian wheezy
* Apache 
* Python
* Javascript virtual joystick

## What I did

* Raspberry Pi model ??
* Ryanteck RTK-000-001 Motor Controller Board 


## Installation on Raspian Jessie

* sudo apt-get update
* sudo apt-get install python-dev python-pip
* sudo pip install pubnub
* sudo apt-get install apache2 -y
* git clone https://github.com/petekaras/lego-robot.git into apache web folder

## Running
* sudo python cli.py
* UI available from where you installed client.html

## Creating a disk image
Find the name of the device of the plugged in SD-card, by typing:

`ls -la /dev/sd*`

plug and unplug the USB reader to find out which device to use. Now write the image:

`sudo dd if=2016-02-26-raspbian-jessie.img of=/dev/sdb`

Might take a while over USB 2.