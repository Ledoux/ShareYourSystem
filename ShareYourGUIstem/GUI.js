//Define collections
Patches = new Meteor.Collection('patches');
Systems = new Meteor.Collection('systems');
Coops = new Meteor.Collection('coops');
Instances = new Meteor.Collection('instances');
Connectors = new Meteor.Collection('connectors');
Messages = new Meteor.Collection('messages');

//client side
if (Meteor.isClient) {

  //subscribe
  Meteor.subscribe('instances')

  //starup
  Meteor.startup(
    function () 
    {

      /*
      mySet = PatchRaphael.set();
      mySet.push(PatchRaphael.circle(400, 150, 50).attr('fill', 'red'));
      mySet.push(PatchRaphael.circle(400, 150, 40).attr('fill', 'white'));
      mySet.draggable();
      //mySet.drag(
      //    Raphael.st.dragSetMove,
      //    Raphael.st.dragSetStart,
      //    Raphael.st.dragSetStop
      //)
      */
      
	  }
  );

  Template.GUI.helpers(
    {
      'patches': function () {
          return Patches.find();
      },
      'DisplayPatchStrsList':function()
      {
        return Session.get('PatchStrsList')
      }
    }
  );
  
  //Set
  Session.set('PatchStrsList',['Default','Default2'])

  //Bond an observe of the Instances data
  Instances.find().observe(
      {
          changed:function(_NewObject, _OldObject)
          {
              //Debug
              console.log(
                  'Instances observe changed',
                  '_NewObject is \n',
                  _NewObject,
                  '\n',
                  '_OldObject is \n',
                  _OldObject,
                  '\n'
              )

              //find the translation
              var LocalInstance=PatchRaphael.InstancesDict[_NewObject._id]
              dx=_NewObject.x0-LocalInstance.Box.AnchorRect.attr('x')
              dy=_NewObject.y0-LocalInstance.Box.AnchorRect.attr('y')

              //Debug
              console.log(
                'dx is \n',
                dx,
                '\n',
                'dy is \n',
                dy,
                '\n'
              )

              //drag
              LocalInstance.Box.dragBoxSetStart()
              LocalInstance.Box.dragBoxSetMove(dx,dy)
              LocalInstance.Box.dragBoxSetStop()



          }
      }
  )

}

//server side
if (Meteor.isServer) {

  Meteor.publish(
      "instances", 
      function () 
      {
        return Instances.find();
      }
  );

  //methods
  Meteor.methods(
    {

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
      
      }
    
    }
  
  )
}


