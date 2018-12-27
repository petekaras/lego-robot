
/*
* PUBNUB keys
*/
//this is should match the channel that the robot.py code uses
var channel = 'robot'

/*green and blue are options on the ui, you can choose between them so that you can have 2 robots
* working from the same controller code. these key sets will need to be created within the same pubnub
* app (specified by the var channel above)
*/
var green = new PubNub({
    subscribeKey: 'sub-c-xxxxx',
    publishKey: 'pub-c-xxxx',
    ssl: false
});

var blue = new PubNub({
    subscribeKey: 'sub-c-xxx',
    publishKey: 'pub-c-xxx',
    ssl: false
});
