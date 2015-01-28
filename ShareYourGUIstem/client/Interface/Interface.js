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
    'DefaultDataObject':{},
    'ChildHelpersObject':
    {
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
                  Session.get('PatchStrsArray')
                 }
             }
         )
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
Session.set('PatchStrsArray',['Default','Default2'])

