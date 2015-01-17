Messages = new Meteor.Collection('messages');

Boxes = new Meteor.Collection('boxes');

if (Meteor.isClient) {

	Meteor.startup(function () {
	    // code to run on client at startup
	    
	  });

}


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




