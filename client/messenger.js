function sendMessage(direction, keySet){
    console.log("[KeySet]:" + keySet, "[Value]:" + direction, '[Channel]:' + channel);
    var app = eval(keySet)
    app.publish(
        {
            message: {'move': direction},
            channel: channel,
            sendByPost: false,
            storeInHistory: false
        },
        function (status, response) {
            // handle status, response
        }
    );
  }
