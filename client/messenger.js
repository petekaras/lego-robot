function sendMessage(direction){
    var doc = document.getElementById("channel");
    var value = doc.options[doc.selectedIndex].value;
    console.log(value);
    if(value==='green'){
      green.publish({
          channel: 'dog-bot',
          message: {"move":direction}
        });
    }
    if(value==='blue'){
      blue.publish({
          channel: 'other-bot',
          message: {"move":direction}
        });
    }

  }
