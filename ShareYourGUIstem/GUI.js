//Define collections
Pacthes = new Meteor.Collection('pacthes');
Messages = new Meteor.Collection('messages');
Boxes = new Meteor.Collection('boxes');
Connectors = new Meteor.Collection('connectors')

//client side
if (Meteor.isClient) {

	Meteor.startup(function () {
	    // code to run on client at startup
	    
	  });
}

//server side
if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });

  Meteor.methods({

      removeAllPosts: function() {
        return Messages.remove({});

      },

      control:function(CollectionStr,MethodStr,CollectionDict)
      {
        console.log(CollectionStr,MethodStr,CollectionDict)
        Meteor.Collection.get(CollectionStr)[MethodStr](CollectionDict)

      }


    }
  )

  
}


Template.patches.helpers({
    patches: function() {
        return Patches.find({}, { sort: { time: -1}});
    }
  })

