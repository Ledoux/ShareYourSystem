/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Box defines the svg support for displaying instances (Object, collection Dicts) coming
from a Python call.

*/

BoxAbstraction=new AbstractionClass(
    {
        'ParentTemplateStr':"System",
        'TemplateStr':'Box',
        'CollectionStr':'boxes',
        'DefaultObject':{
            'x':200,
            'y':200,
            'coopx':50
        },
        'ChildHelpersObject':
        {
          'coops':function()
           {

                //Define
                var Find=Coops.find(
                    {'ParentNameStr':this.NameStr}
                )

                //Debug
                /*
                console.log(
                    'System coops helpers l 24 \n',
                    'this.NameStr is \n',
                    this.NameStr,
                    '\n',
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

Template.Box.created = function()
{

    //get
    var LocalBlaze=this

    //Debug
    /*
    console.log(
            'Box created l 46\n',
            'LocalBlaze is \n',
            LocalBlaze.data
        )
    */

    //get
    var LocalInstance=InstancesDictObject[this.data._id]
    if(LocalInstance!=undefined)
    {
        LocalBlaze.data.x=LocalInstance.x
        LocalBlaze.data.y=LocalInstance.y
    }

    IsRaphaelBool=true
    if(IsRaphaelBool)
    {
        //init
        LocalBlaze.Sticker=new StickerClass(
                {
                    'CollectionStr':'boxes'
                }
            )
        LocalBlaze.Sticker.Blaze=LocalBlaze

        //Init the anchor Rect
        LocalBlaze.Sticker.AnchorRect=PatchRaphael.rect(
                LocalBlaze.data.x,
                LocalBlaze.data.y,
                10,
                10
            ).attr(
                {
                    fill : 'green',
                    cursor : 'move'
                }
            )
        
        //Init the anchor Rect
        LocalBlaze.Sticker.InfoRect=PatchRaphael.rect(
                LocalBlaze.data.x,
                LocalBlaze.data.y+10,
                50,
                20,
                5
            ).attr(
                {
                    fill : '#F5F5F5',
                    cursor : 'move',
                    stroke : 'black',
                    'stroke-width' : 3,
                }
            )
        LocalBlaze.Sticker.InfoText = PatchRaphael.text(
                LocalBlaze.data.x+25, 
                LocalBlaze.data.y+19, 
                LocalBlaze.data.NameStr
            ).attr(
                {
                    fill: '#000040'
                }
            )
        LocalBlaze.Infox = new ReactiveVar;
        LocalBlaze.Infoy = new ReactiveVar;
        LocalBlaze.Infox.set(LocalBlaze.data.x)
        LocalBlaze.Infoy.set(LocalBlaze.data.y)

        //push
        LocalBlaze.Sticker.set.push(
            LocalBlaze.Sticker.AnchorRect,
            LocalBlaze.Sticker.InfoRect,
            LocalBlaze.Sticker.InfoText
        )   

        //Debug
        /*
        console.log(
            'l 228 Box \n',
            'Make it drag'
        )
        */

        //make it draggable
        LocalBlaze.Sticker.set.drag(
            LocalBlaze.Sticker.dragStickerSetMove, 
            LocalBlaze.Sticker.dragStickerSetStart, 
            LocalBlaze.Sticker.dragStickerSetStop
        );

        //Debug
        /*
        console.log(
                'Box rendered l 290',
                'PatchRaphael.StickerSetsSet is : \n',
                PatchRaphael.StickerSetsSet
            )
        */

        //Give to the StickerSetsSet
        StickerSetsSet.push(LocalBlaze.Sticker.set)
    }

}

Template.Box.helpers(
    _.extend(
        BoxAbstraction.ChildHelpersObject,
        {
            Infox:function()
            {
                return Template.instance().Blaze.Infox.get();
            },
            Infoy:function()
            {
                return Template.instance().Blaze.Infoy.get();
            }
        }
    )
)

Template.Box.destroyed = function(){

    //get
    var LocalBlaze=this

    if(IsRaphaelBool)
    {
        //exclude 
        StickerSetsSet.exclude(LocalBlaze.Sticker.set)

        //remove
        LocalBlaze.Sticker.set.remove()
    }

}


Meteor.startup(
    function()
    {
        
        //Bind an observe of the Instances data
        var IsObserveBool=true
        if(IsObserveBool)
        {
            Boxes.find().observe(
                {
                    changed:function(_NewObject, _OldObject)
                    {
                        //Debug
                        /*
                        console.log(
                          'Boxes observe changed',
                          '_NewObject is \n',
                          _NewObject,
                          '\n',
                          '_OldObject is \n',
                          _OldObject,
                          '\n'
                        )
                        */
                        
                        //translate(_NewObject._id)

                        //set
                        var BoxInstance=InstancesDictObject[_NewObject._id]

                        /*
                        console.log(
                            BoxInstance.ChildIdStrsDictsObject
                        )
                        */

                        //Coops.find(
                        //    {ParentIdStr:_NewObject._id}
                        //).fetch()

                        
                    }
                }
            )
        }

    }
)


translate = function(_NewObject)
{

    //find the translation
    var LocalBlaze=InstancesDictObject[_NewObject._id]
    if (LocalBlaze!=undefined && LocalBlaze!=null)
    {

        //set
        var dx=_NewObject.x-LocalBlaze.Sticker.AnchorRect.attr('x')
        var dy=_NewObject.y-LocalBlaze.Sticker.AnchorRect.attr('y')
    
        //Debug
        /*
        console.log(
        'dx is \n',
        dx,
        '\n',
        'dy is \n',
        dy,
        '\n'
        )
        */

        if(dx!=undefined && dx!=null)
        {
          if(dy!=undefined && dy!=null) 
            {
                //Debug
                /*
                console.log(
                    'Boxes observe changed 224 \n',
                    'We can drag'
                )
                */

                //drag
                LocalBlaze.Sticker.dragStickerSetStart()
                LocalBlaze.Sticker.dragStickerSetMove(dx,dy)
                LocalBlaze.Sticker.dragStickerSetStop()
            }
        }
        
    }
}

