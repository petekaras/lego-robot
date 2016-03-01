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



## Installation on Raspian Jessie

* sudo apt-get update
* sudo apt-get install motion
* sudo apt-get install python-dev python-pip
* sudo pip install pubnub
* sudo apt-get install apache2 -y
* git clone https://github.com/petekaras/lego-robot.git into apache web folder

## Configure motion
### /etc/motion/motion.conf


| Property  			| value 		|
| --------------------- | ------------- |
| daemon  				| on  			|
| ffmpeg_output_movies  | off  			|
| output_pictures  		| off  			|
| stream_maxrate		| 30			|
| width					| 480			|
| height				| 360			|

You can vary the `stream_maxrate` to increase the quality of the video. Also play around with the width and height settings.

### /etc/default/motion

| Property  			| value 		|
| --------------------- | ------------- |
| start_motion_daemon  	| yes  			|

## auto run services on start up
add the following lines to `\etc\rc.local`

```
#Robot starts webcam
sudo motion

#Robot listens to commands
nohup sudo python /home/pi/lego-robot/server/robot.py &
```
