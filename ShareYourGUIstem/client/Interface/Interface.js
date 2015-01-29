/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Interface client

*/

InterfaceAbstraction=new AbstractionClass(
  {
    'TemplateStr':'Interface',
    'CollectionStr':"interfaces",
    'DefaultInstanceObject':{},
    'ChildHelpersObject':
    {
      'patches': function () 
      {

          //set
          var Find=Patches.find(
              {
                  NameStr:
                 {
                  $in:
                  Session.get('PatchStrsArray')
                 }
             }
         )

          //Debug
          /*
          console.log(
            'Template Interface helpers l 35 \n',
            'Find.fetch() is \n',
            Find.fetch()
          )
          */

          //return
          return Find
      }
    }
  }
)

Template.Interface.helpers(
  _.extend(
    InterfaceAbstraction.ChildHelpersObject,
    {
      'DisplayPatchStrsArray':function()
      {
        return Session.get('PatchStrsArray')
      }
    }
  )
);

//Set
Session.set('PatchStrsArray',[
            'DefaultPatch'
          ]
        )

//End to set up the abstractions
_.map(
    AbstractionsDictObject,
    function(__Abstraction)
    {
      //Debug
      /*
      console.log(
        'l 74 Interface',
        '__Abstraction is \n',
        __Abstraction
      )
      */
      
      //tini
      __Abstraction.tini()
    }
  )
