/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Patch defines the svg support for displaying all the views of the instances
defining in a certain Patch.

*/

PatchAbstraction=new AbstractionClass(
  {
      'TemplateStr':'Patch',
      'CollectionStr':'patches',
      'ChildHelpersObject':
      {
        'systems': function () 
          {

              //Debug
              /*
              console.log(
                'Template Patch helpers l 25 \n',
                'Session.get("PatchStrsArray") is \n',
                Session.get('PatchStrsArray')
              )
              */
              
              //find
              var Find=Systems.find(
                  {
                      ParentPatchStr:
                     {
                      $in:
                      Session.get('PatchStrsArray')
                     }
                 }
              )

              //Debug
              console.log(
                'Template Patch helpers l 45 \n',
                'Find.fetch() is \n',
                Find.fetch()
              )

              //return
              return Find
          }
      }
  }
)

Template.Patch.created = function()
{
  //Debug
  /*
  console.log(
      'Patch created l 61'
    )
  */

  //init
  var LocalData=new DataClass(
      {
        'Blaze':this,
        'Abstraction':PatchAbstraction
      }
    )

  //datafy
  LocalData.datafy()

}

Template.Patch.helpers(
    PatchAbstraction.ChildHelpersObject
)



