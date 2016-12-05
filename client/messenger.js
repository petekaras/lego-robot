function sendMessage(direction,channel){

    console.log("Channel: " + channel, "Value: " + direction);


    if(channel==='green'){
      green.publish({
          channel: 'dog-bot',
          message: {"move":direction}
        });
    }

    if(channel==='blue'){
      blue.publish({
          channel: 'other-bot',
          message: {"move":direction}
        });
    }


  }
