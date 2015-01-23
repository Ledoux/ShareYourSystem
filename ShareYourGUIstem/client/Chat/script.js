/**
* Templates
*/
Template.messages.helpers({
    messages: function() {
        return Messages.find({}, { sort: { time: -1}});
    }
})

Template.input.events = {
  'keydown input#message' : function (event) {
    if (event.which == 13) { // 13 is the enter key event
      if (Meteor.user())
        var name = Meteor.user().profile.name;
      else
        var name = 'Anonymous';
      var message = document.getElementById('message');

      if (message.value != '') {

        //Print
        //console.log(message.value)
        //console.log(message.value.substring(1))

        //It is a command
        if (message.value[0] == '>') {

            //Print
            console.log(message.value.substring(1))
            console.log(message.value.substring(1).toString())
            eval(message.value.substring(1).toString())
            console.log('t=4',message.value.substring(1))
            eval('A=5')
            console.log(A)
            console.log(t)
        }
        else
        {
          //It is an insert
          Messages.insert({
            name: name,
            message: message.value,
            time: Date.now(),
          });
        }
        
        //Reset
        document.getElementById('message').value = '';
        message.value = '';
      }
    }
  }
}
