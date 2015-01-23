//Define collections
Patches = new Meteor.Collection('patches');
Messages = new Meteor.Collection('messages');
Boxes = new Meteor.Collection('boxes');
Connectors = new Meteor.Collection('connectors')

//client side
if (Meteor.isClient) {

	Meteor.startup(function () {
	    // code to run on client at startup
	    
	  });

  Template.GUI.helpers({
    'patches': function () {
        return Patches.find();
    },
    'DisplayPatchStrsList':function()
    {
      return Session.get('PatchStrsList')
    }
  });
  
  Session.set('PatchStrsList',['Default','Default2'])
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

      mongo:function(CollectionStr,MethodStr,CollectionDict)
      {
        console.log(CollectionStr,MethodStr,CollectionDict)
        Meteor.Collection.get(CollectionStr)[MethodStr](CollectionDict)

      }


    }
  )
}


