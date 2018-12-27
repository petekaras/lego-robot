'''
Contains mapping from movements with empty implementations
You can use this for testing on a non raspberry pi laptop, or a base for some other robot implementation 
'''

class RobotMoves:
    def right(self):
        print("right")

    def left(self):
        print("left")

    def forwards(self):
        print("forwards")

    def backwards(self):
        print("backwards")

    def stop(self):
        print("stop")

    def lightOn(self):
        print("light on")

    def lightOff(self):
        print("light off")

    def stepCW(self):
        print("cw")

    def stepACW(self):
        print("acw")
