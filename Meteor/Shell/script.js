
if (Meteor.isServer) {
  Meteor.methods({
    'getPythonShell': function() {
      	
      	//Require
      	PythonShell = Meteor.npmRequire('python-shell');
      
    	//Define a python shell
		ApiPythonShell = new PythonShell('my_script.py');

		//Return
 	    return ApiPythonShell;	
    }
  });
}

//Define db
Commands = new Meteor.Collection(null)

if (Meteor.isClient) {

	//Set
	Session.set('ApiPythonShell',Meteor.call('getPythonShell'))

	//Define events
	Template.Shell.events(
	{
		'keypress input#NewCommand': function(_Event) { 
			
			//Debug
			console.log('In keypress input.NewCommand, _Event.key is',_Event.key)

			//Check
			if (_Event.key === "Enter")
			{

				//Insert in the db
				Commands.insert({
					InputString:_Event.key
				})

				//Get
				var ApiPythonShell=Meteor.Session.get('ApiPythonShell')

				//Sends a message to the Python script via stdin
				ApiPythonShell.send(InputString);

				//Received a message sent from the Python script (a simple "print" statement)
				ApiPythonShell.on('message', function (_Message) {
			  		console.log(_Message);
				});

				//End the input stream and allow the process to exit
				ApiPythonShell.end(function (err) {
			  	if (err) throw err;
			  		console.log('finished');
					}
				);

			}

		} 
	})


}


