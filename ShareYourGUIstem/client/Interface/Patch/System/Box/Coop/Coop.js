/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Coop defines the svg support for displaying a collection dict instance coming
from a Python call.

*/

CoopAbstraction=new AbstractionClass(
   {
	    'ParentTemplateStr':"Box",
	    'TemplateStr':'Coop',
	    'CollectionStr':'coops',
	    'DefaultObject':{
	        'x':200,
	        'y':200
	    }
	}
)

Template.Coop.created = function()
{

	//define
	var LocalBlaze=this

	//get
	var LocalInstance=InstancesDictObject[this.data._id]
    if(LocalInstance!=undefined)
    {
    	//init
    	LocalBlaze.data.x=LocalInstance.x
        LocalBlaze.data.y=LocalInstance.y

    	//Check for coordinates compared to an alredy parent box
    	if(LocalInstance.ParentInstance!=undefined)
    	{
    		
    		if(
    			LocalInstance.ParentInstance.x==BoxAbstraction.DefaultObject.x && LocalInstance.ParentInstance.y==BoxAbstraction.DefaultObject.y
    		)
    		{
    			//Debug
    			console.log(
    					'LocalInstance.ParentInstance.NameStr is \n',
    					LocalInstance.ParentInstance.NameStr
    				)

    			//Check
    			if(LocalInstance.ParentInstance.CoopInt==undefined)
    			{
    				LocalInstance.ParentInstance.CoopInt=0
    			}

    			//set
    			if (_.size(
    					LocalInstance.ParentInstance.ChildInstancesDictsObject['coops']
    				)>0)
    			{
	    			LocalBlaze.data.x=LocalInstance.ParentInstance.x-(LocalInstance.ParentInstance.coopx/2.)+(
	    				LocalInstance.ParentInstance.coopx*LocalInstance.ParentInstance.CoopInt/_.size(
	    					LocalInstance.ParentInstance.ChildInstancesDictsObject['coops']
	    				)
	    			)
	    			LocalBlaze.data.y=LocalInstance.ParentInstance.y+10
				}

    			//inc
    			LocalInstance.ParentInstance.CoopInt+=1
    		}
    	} 
    }

    //Debug
    /*
    console.log(
            'Coop created l 46\n',
            'LocalInstance is \n',
            LocalInstance
        )
    */
    
    IsRaphaelBool=true
    if(IsRaphaelBool)
    {
        //init
        LocalBlaze.Sticker=new StickerClass(
                {
                    'CollectionStr':'coops'
                }
            )
        LocalBlaze.Sticker.Blaze=LocalBlaze

        //Init the anchor Rect
        LocalBlaze.Sticker.AnchorRect=PatchRaphael.rect(
                LocalBlaze.data.x,
                LocalBlaze.data.y,
                3,
                3
            ).attr(
                {
                    fill : 'green',
                    cursor : 'move'
                }
            )
        
        //Init the anchor Rect
        LocalBlaze.Sticker.InfoRect=PatchRaphael.rect(
                LocalBlaze.data.x-3,
                LocalBlaze.data.y+2,
                10,
                10,
                50
            ).attr(
                {
                    fill : '#002182',
                    cursor : 'move',
                    stroke : 'black',
                    'stroke-width' : 3,
                }
            )

        LocalBlaze.Infox = new ReactiveVar;
        LocalBlaze.Infoy = new ReactiveVar;
        LocalBlaze.Infox.set(LocalBlaze.data.x)
        LocalBlaze.Infoy.set(LocalBlaze.data.y)

        //push
        LocalBlaze.Sticker.set.push(
            LocalBlaze.Sticker.AnchorRect,
            LocalBlaze.Sticker.InfoRect
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
                'Coop rendered l 290',
                'StickerSetsSet is : \n',
                StickerSetsSet
            )
        */

        //Give to the StickerSetsSet
        StickerSetsSet.push(LocalBlaze.Sticker.set)
    }
}

Template.Coop.destroyed = function(){

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

Template.Coop.helpers(
    CoopAbstraction.ChildHelpersObject
)

