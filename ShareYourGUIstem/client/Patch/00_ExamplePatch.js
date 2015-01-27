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
      CollectionStrsList,
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
              'PatchStr':"Default"
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
    Meteor.call(
            'mongo',
            'systems',
            'insert',
            {
              'PatchStr':"Default",
              'SystemStr':"MySystem"
            }
          )

    //Debug
    /*
    console.log(
      'TestPatch',
      'We insert a Box...'
    )
    */

    //call
    Meteor.call(
            'mongo',
            'boxes',
            'insert',
            {
              'SystemStr':"MySystem",
              'BoxStr':"TopSystemer"
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
      ["1","2","3"],
      function(__CoopStr)
      {
        Meteor.call(
          'mongo',
          'coops',
          'insert',
          {
            'BoxStr':"TopSystemer",
            'CoopStr':__CoopStr
          }
        )
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



