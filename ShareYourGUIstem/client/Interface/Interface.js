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

Template.Interface.rendered=function()
{
    //require
    //require('raphael')

    //Debug
    console.log(
      'init a Raphael patch\n',
      '$("#PatchSvg").get(0) is \n',
      $('#PatchSvg').get(0)
    )
    
    //build the Raphael environment
    PatchRaphael=Raphael($('#PatchSvg').get(0))
    Meteor.PatchRaphael=PatchRaphael

    //get
    PatchSvg=$('#PatchSvg')
    PatchSvgOffset=PatchSvg.offset()

    //init
    StickerSetsSet=PatchRaphael.set()

    //set that will receive the selected items
    PatchSelection=new SelectionClass()

    //init
    var BackRect = PatchRaphael.rect(
                    0, 0, PatchRaphael.width, PatchRaphael.height
                  ).attr(
                    "fill", "#FDFDFD"
                  );
    BackRect.drag(
            PatchSelection.dragSelectionRectMove, 
            PatchSelection.dragSelectionRectStart, 
            PatchSelection.dragSelectionRectStop
        );
}


