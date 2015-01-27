//Define collections

//Degub
/*
console.log(
  'GUI l.4',
  'We define the collections'
)
*/

CollectionsDictObject={}
CollectionStrsList=[
      "patches",
      "systems",
      "boxes",
      "coops",
      "connectors",
      "messages"
    ]
_.map(
    CollectionStrsList,
    function(__CollectionStr)
    {
      //Debug
      /*
      console.log(
        'GUI l 18\n',
        '__CollectionStr[0]+__CollectionStr.slice(1) is \n',
        __CollectionStr[0].toUpperCase()+__CollectionStr.slice(1)
      )
      */

      //Define
      var CollectionKeyStr= __CollectionStr[0].toUpperCase() + __CollectionStr.slice(1)
      
      //eval
      eval(
            CollectionKeyStr+" = new Meteor.Collection(\"" + __CollectionStr + "\")"
          )

      //Debug
      /*
      console.log(
        'GUI l 35\n',
        'OK collection is defined'
      )
      */

      //eval
      eval(
            "CollectionsDictObject[\"" + CollectionKeyStr + "\"] = " + CollectionKeyStr
          )

      //Set
      /*
      CollectionsDictObject[
        CollectionKeyStr
      ]= new Meteor.Collection(__CollectionStr)
      */
    }
)

//Degub
/*
console.log(
  'GUI l.4',
  'Collections are defined',
  'CollectionsDictObject is \n',
  CollectionsDictObject
)
*/

//client side
if (Meteor.isClient) {

  //map subscribe
  _.map(
    CollectionStrsList,
    function(__CollectionStr)
    {
      Meteor.subscribe(__CollectionStr)
    }
  )
  
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
      'DisplayPatchStrsList':function()
      {
        return Session.get('PatchStrsList')
      },

      'patches': function () 
      {

          /*
          //Debug
          console.log(
            'Template Patch helpers l 21'
          )
          */
          
          //return
          return Patches.find(
              {
                  PatchStr:
                 {
                  $in:
                  Session.get('PatchStrsList')
                 }
             }
         )
      }
    }
  );
  
  //Set
  Session.set('PatchStrsList',['Default','Default2'])

  

}

//server side
if (Meteor.isServer) {

  //map a publish
  _.map(
      CollectionStrsList,
      function(__CollectionStr)
      {

        //publish
        Meteor.publish(
            __CollectionStr, 
            function () 
            {
              
              //return
              return Meteor.Collection.get(
                        __CollectionStr
                      ).find();

              //Define
              /*
              var CollectionKeyStr=__CollectionStr[0].toUpperCase()+__CollectionStr.slice(1)
              return CollectionsDictObject[
                        __CollectionStr
                      ].find();
              */
            }
        );

      }
    )
  
  //methods
  Meteor.methods(
    {

      mongo:function(_CollectionStr,_MethodStr,_OptionDict)
      {

        //Debug
        /*
        console.log(
                  'l 86 GUI.js \n',
                  'mongo method \n',
                  "_CollectionStr is : \n",
                  _CollectionStr,
                  '\n',
                  "_MethodStr is : \n",
                  _MethodStr,
                  '\n',
                  "_OptionDict is : \n",
                  _OptionDict,
                  //"CollectionsDictObject is \n",
                  //CollectionsDictObject,
                  "_.keys(CollectionsDictObject) is \n",
                  _.keys(CollectionsDictObject)
                )
        */

        //Define
        var CollectionKeyStr=_CollectionStr[0].toUpperCase()+_CollectionStr.slice(1)

        //Debug
        /*
        console.log(
                  'l 150 GUI.js \n',
                  'mongo method \n',
                  'CollectionKeyStr is \n',
                  CollectionKeyStr,
                  '\n',
                  "CollectionsDictObject[CollectionKeyStr] is : \n",
                  CollectionsDictObject[CollectionKeyStr]
                )
        */

        //get
        //Meteor.Collection.get(_CollectionStr)[_MethodStr](_OptionDict)
        CollectionsDictObject[CollectionKeyStr][_MethodStr](_OptionDict)

      }
    
    }
  
  )
}


