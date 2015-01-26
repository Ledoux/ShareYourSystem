//Define collections
Patches = new Meteor.Collection('patches');
Systems = new Meteor.Collection('systems');
Coops = new Meteor.Collection('coops');
Boxes = new Meteor.Collection('boxes');
Connectors = new Meteor.Collection('connectors');
Messages = new Meteor.Collection('messages');

//client side
if (Meteor.isClient) {

  //starup
  Meteor.startup(function () {

      mySet = PatchRaphael.set();
      mySet.push(PatchRaphael.circle(400, 150, 50).attr('fill', 'red'));
      mySet.push(PatchRaphael.circle(400, 150, 40).attr('fill', 'white'));
      mySet.draggable();
      //mySet.drag(
      //    Raphael.st.dragSetMove,
      //    Raphael.st.dragSetStart,
      //    Raphael.st.dragSetStop
      //)

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
  
  //
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

      mongo:function(_CollectionStr,_MethodStr,_CollectionDict)
      {
        //Debug
        console.log(
                  'l 86 GUI.js \n',
                  'mongo method \n',
                  "_CollectionStr is : \n",
                  _CollectionStr,
                  '\n',
                  "_MethodStr is : \n",
                  _MethodStr,
                  '\n',
                  "_CollectionDict is : \n",
                  _CollectionDict
                )

        //get
        Meteor.Collection.get(_CollectionStr)[_MethodStr](_CollectionDict)
      },

      box:function(_BoxDict){

        //Debug
        console.log(
            'We box here',
            '_BoxDict is ',
            _BoxDict,
            ''
        )

        //Give x and y
        if(_BoxDict['ParentPathStr']==''){

          //Debug
          console.log('This is the top')

          //set
          _BoxDict['x']=400
          _BoxDict['y']=100
        }

        //insert
        Boxes.insert(_BoxDict)

      }

    }
  )
}


