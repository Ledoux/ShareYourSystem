/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

models

*/

CollectionsDictObject={}
CollectionListsList=[
    ["patch","patches"],
    ["system","systems"],
    ["box","boxes"],
    ["coop","coops"],
    ["connector","connectors"],
    ["message","messages"],
    ["ghost","ghosts"]
  ]
CollectionStrsList=_.map
(
    CollectionListsList,
    function(__CollectionList)
    {
      return __CollectionList[1]
    }
)
SingularToPluralDict=_.object(CollectionListsList)

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

//Check
if (Meteor.isClient)
{

  Meteor.startup(
    function()
    {
      //Debug
      console.log('models client starup')

      //Global ref
      BlazesDict={}
    }
  )

  //map subscribe
  _.map(
    CollectionStrsList,
    function(__CollectionStr)
    {
      Meteor.subscribe(__CollectionStr)
    }
  )

}


//Check
if (Meteor.isServer)
{

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
        /*
        console.log(
                  'l 150 models.js \n',
                  'mongo method \n',
                  'CollectionKeyStr is \n',
                  CollectionKeyStr,
                  '\n'
                  //"CollectionsDictObject[CollectionKeyStr] is : \n",
                  //CollectionsDictObject[CollectionKeyStr]
                )
        */

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
          console.log(
            'Return the fetch'
          )

          //return
          return OutputObject.fetch()
        }

      }
    
    }

  )
}