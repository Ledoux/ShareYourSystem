/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

GUI client

*/



Template.GUI.helpers(
  {
    'DisplayPatchStrsArray':function()
    {
      return Session.get('PatchStrsArray')
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
                Session.get('PatchStrsArray')
               }
           }
       )
    }
  }
);

//Set
Session.set('PatchStrsArray',['Default','Default2'])

