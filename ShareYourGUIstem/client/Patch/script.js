/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Patch defines the svg support for displaying all the views of the instances
defining in a certain Patch.

*/


Template.Patch.helpers(
    {
        'instances': function () 
        {

            //Debug
            /*
            console.log(
              'Template Patch helpers l 21'
            )
            */
            
            //return
            return Instances.find(
                {
                    PatchStr:
                   {
                    $in:
                    Session.get('PatchStrsList')
                    //Patches.find({},{name:true}).map(function(object){return object['name']})
                   }
               }
           )
        },

        'connectors': function () {
            return Connectors.find();
        }
    }
)



