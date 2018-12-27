'''
Contains mapping from movements to gpio pins
'''
import RPi.GPIO as GPIO
import stepper


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

stepMotor = stepper.Motor([10,9,11,25], 15)

class RobotMoves:
    def right(self):
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,1)
        GPIO.output(23,0)
        print("right")

    def left(self):
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,0)
        GPIO.output(23,1)
        print("left")

    def forwards(self):
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,1)
        GPIO.output(23,0)
        print("forwards")

    def backwards(self):
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,1)
        print("backwards")

    def stop(self):
        GPIO.output(17,0)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,0)
        print("stop")

    def lightOn(self):
        GPIO.output(21,1)
        GPIO.output(20,1)
        print("light on")

    def lightOff(self):
        GPIO.output(21,0)
        GPIO.output(20,0)
        print("light off")

    def stepCW(self):
        stepMotor.move_cw(10)
        print("cw")

    def stepACW(self):
        stepMotor.move_acw(10)
        print("acw")
