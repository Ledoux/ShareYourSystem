/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>



*/

TestPatch=function()
{

    //Debug
    /*
    console.log(
      'TestPatch',
      'We remove all in the db...'
    )
    */

    //remove all
    _.map(
      _.keys(CollectionsDictObject),
      function(__CollectionStr)
      {

        //Debug
        /*
        console.log(
          'TestPatch',
          '__CollectionStr is \n',
          __CollectionStr
        )
        */

        //call
        Meteor.call(
              'mongo',
              __CollectionStr,
              'remove',
              {}
          )
      }
    )

    //Debug
    /*
    console.log(
      'TestPatch',
      'We insert a Patch...'
    )
    */

    //call
    Meteor.call(
            'mongo',
            'patches',
            'insert',
            {
              'NameStr':"DefaultPatch"
            }
          )

    //Debug
    /*
    console.log(
      'TestPatch',
      'Patches.find({}).fetch() is \n',
      Patches.find({}).fetch(),
      '\n',
      'We insert a System...'
    )
    */
    
    //call
    _.map(
      ["MySystem","YourSystem"],
      function(__SystemStr)
      {
        Meteor.call(
          'mongo',
          'systems',
          'insert',
          {
            'ParentNameStr':"DefaultPatch",
            'NameStr':__SystemStr
          }
        )
      }
    ) 

    //Debug
    /*
    console.log(
      'TestPatch',
      'We insert boxes...'
    )
    */

    //call
    _.map(
      ['MySystem','YourSystem'],
      function(__SystemStr)
      {
        _.map(
          ["TopBox","ChildBox"],
          function(__BoxStr)
          {
            Meteor.call(
              'mongo',
              'boxes',
              'insert',
              {
                'ParentNameStr':__SystemStr,
                'NameStr':__BoxStr
              }
            )
          }
        )
      }
    ) 

    //Debug
    /*
    console.log(
      'TestPatch',
      'We insert coops...'
    )
    */

    //call
    _.map(
      ["FirstCoop","SecondCoop","ThirdCoop"],
      function(__CoopStr)
      {
        Meteor.call(
          'mongo',
          'coops',
          'insert',
          {
            'ParentNameStr':"TopBox",
            'GrandParentNameStrsArray':['MySystem'],
            'NameStr':__CoopStr
          }
        )
      }
    ) 
      
    //Debug
    /*
    console.log(
      'TestPatch',
      'We insert one ghost...'
    )
    */
    
    //call
    Meteor.call(
            'mongo',
            'ghosts',
            'insert',
            {
              'ParentNameStr':"FirstCoop",
              'NameStr':"MyGhost"
            }
          )

    //Debug
    /*
    console.log(
      'TestPatch',
      'OK'
    )
    */
}



