/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

publish

*/


CollectionStrsList=[
    "interfaces",
    "patches",
    "systems",
    "boxes",
    "coops",
    "connectors",
    "messages",
    "musics",
    "scales",
    "patterns",
    "progressions",
    "voices",
    "views",
    "figures",
    "plots"
]
CollectionsDictObject={}

//map collections init
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
                '\n',
                "_.keys(CollectionsDictObject) is \n",
                _.keys(CollectionsDictObject)
              )
      */

      //Define
      var CollectionKeyStr=_CollectionStr[0].toUpperCase()+_CollectionStr.slice(1)

      //Debug
      console.log(
                '\n',
                'l 150 models.js \n',
                'mongo method \n',
                'CollectionKeyStr is \n',
                CollectionKeyStr,
                '\n',
                "CollectionsDictObject[CollectionKeyStr]!=undefined is : \n",
                CollectionsDictObject[CollectionKeyStr]!=undefined
              )

      //get
      //var OutputObject=Meteor.Collection.get(_CollectionStr)[_MethodStr](_OptionDict)
      var OutputObject=CollectionsDictObject[CollectionKeyStr][_MethodStr](_OptionDict)

      //Debug
      /*
      console.log(
        'l 191 models.js mongo \n',
        'OutputObject is \n',
        OutputObject 
      )
      */
      
      if(_MethodStr=='find')
      {
        //Debug
        /*
        console.log(
          'Return the fetch'
        )
        */
        
        //return
        return OutputObject.fetch()
      }

    }
  
  }
)

var exec = Npm.require('child_process').exec;
var Fiber = Npm.require('fibers');
var Future = Npm.require('fibers/future');

Meteor.methods({

  callPython: function() {

    console.log('We call python');

    var fut = new Future();
    return exec('python -c "print 3+3"', function (error, stdout, stderr) {

      // if you want to write to Mongo in this callback
      // you need to get yourself a Fiber
      new Fiber(function() {
        fut.return('Python was here');
      }).run();

      //console.log('jjjj\n',stdout)
      return stdout
    });



    //return fut.wait();
  },

});


