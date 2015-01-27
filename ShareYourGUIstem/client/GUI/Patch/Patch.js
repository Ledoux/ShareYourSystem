/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Patch defines the svg support for displaying all the views of the instances
defining in a certain Patch.

*/

Template.Patch.created = function()
{
  /*
  //Debug
  console.log(
      'System created l 17'
    )
  */

  //Define
  var LocalPatchBlaze=this

  //Debug
  /*
  console.log(
      'Patch created l 28',
    )
  */

  //init
  init(
      this,
      {
        'TemplateStr':'Patch',
        'ChildCollectionStrsArray':['systems'],
        'DefaultObject':{    
                      }
      }
    )
}

Template.Patch.helpers(
    {
        'systems': function () 
        {

            /*
            //Debug
            console.log(
              'Template Patch helpers l 21'
            )
            */
            
            //return
            return Systems.find(
                {
                    PatchStr:
                   {
                    $in:
                    Session.get('PatchStrsArray')
                    //CollectionsDictObject['Patches'].find({},{name:true}).map(function(object){return object['name']})
                   }
               }
           )
        }
    }
)



