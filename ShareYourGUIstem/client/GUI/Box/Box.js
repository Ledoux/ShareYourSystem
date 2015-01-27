/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Box defines the svg support for displaying instances (Object, collection Dicts) coming
from a Python call.

*/

Meteor.startup(
    function()
    {
        //require
        require('raphael')

        //build the Raphael environment
        PatchRaphael=Raphael($('#PatchSvg').get(0))

        //get
        PatchSvg=$('#PatchSvg')
        PatchSvgOffset=PatchSvg.offset()

        //init
        PatchRaphael.BoxSetsSet=PatchRaphael.set()
        PatchRaphael.BoxeBlazesDict={}

        //define
        BoxClass = function() {

            //Debug
            /*
            console.log(
                'l 24 BoxClass \n',
                'We init a new Box \n',
                'PatchRaphael is ',
                PatchRaphael
            )
            */

            //alias
            var LocalBoxObject=this

            //Define the set
            LocalBoxObject.set=PatchRaphael.set()
            LocalBoxObject.set.BoxObject=LocalBoxObject

            //Debug
            /*
            console.log(
                'LocalBoxObject l 39',
                'LocalBoxObject.set is',
                LocalBoxObject.set,
                '\n'
            )
            */

            LocalBoxObject.dragBoxSetStart = function() {

                //Debug
                /*  
                console.log(
                        'l 188 dragBoxSetStart \n',
                    )
                */

                //map
                LocalBoxObject.set.items.map(
                        function(__Element){

                            //set
                            __Element.ox=__Element.attr('x')
                            __Element.oy=__Element.attr('y')

                            //Debug
                            /*
                            console.log(
                                'dragBoxSetStart l 113',
                                '__Element.ox is \n',
                                __Element.ox,
                                '\n',
                                '__Element.oy is \n',
                                __Element.oy,
                                '\n'
                            )
                            */     
                        }

                    )

            }

            LocalBoxObject.dragBoxSetMove = function(_dx,_dy) {

                //Debug
                /*
                console.log(
                        'l 242 dragBoxSetMove \n',
                    )
                */

                LocalBoxObject.set.items.map(
                        function(__Element){

                            //Debug
                            /*
                            console.log(
                                'dragBoxSetMove l 113',
                                '__Element.ox is \n',
                                __Element.ox,
                                '\n',
                                '__Element.oy is \n',
                                __Element.oy,
                                '\n'
                            )
                            */

                            //set
                            __Element.attr(
                                    {
                                        x:__Element.ox+_dx,
                                        y:__Element.oy+_dy
                                    }
                                )
                        }

                    )


                //update the db... 
                /*

                Boxes.update(
                    {_id:LocalBoxObject.BoxBlaze.data._id},
                    {
                        $set:{
                            x0:LocalBoxObject.AnchorRect.attr('x'),
                            y0:LocalBoxObject.AnchorRect.attr('y')
                        }
                    }
                )
                */

                //set
                LocalBoxObject.BoxBlaze.Infox.set(LocalBoxObject.AnchorRect.attr('x'))
                LocalBoxObject.BoxBlaze.Infoy.set(LocalBoxObject.AnchorRect.attr('y'))
            }

            LocalBoxObject.dragBoxSetStop = function() {

                //Debug
                /*
                console.log(
                        'l 264 dragBoxSetStop \n',
                        'LocalBox.BoxBlaze.data._id is \n',
                        LocalBoxObject.BoxBlaze.data._id
                    )
                */

                //update the db
                Boxes.update(
                    {_id:LocalBoxObject.BoxBlaze.data._id},
                    {
                        $set:{
                            x0:LocalBoxObject.AnchorRect.attr('x'),
                            y0:LocalBoxObject.AnchorRect.attr('y')
                        }
                    }
                )

            }

            //Debug
            /*
            console.log(
                'l 155 BoxClass',
                'End of the BoxClass definition'
                )
            */
        }

        //Bond an observe of the Instances data
        Boxes.find().observe(
            {
                changed:function(_NewObject, _OldObject)
                {
                    //Debug
                    /*
                    console.log(
                      'Instances observe changed',
                      '_NewObject is \n',
                      _NewObject,
                      '\n',
                      '_OldObject is \n',
                      _OldObject,
                      '\n'
                    )
                    */

                    //find the translation
                    var LocalBoxBlaze=PatchRaphael.BoxeBlazesDict[_NewObject._id]
                    dx=_NewObject.x0-LocalBoxBlaze.BoxObject.AnchorRect.attr('x')
                    dy=_NewObject.y0-LocalBoxBlaze.BoxObject.AnchorRect.attr('y')

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

                    //drag
                    LocalBoxBlaze.BoxObject.dragBoxSetStart()
                    LocalBoxBlaze.BoxObject.dragBoxSetMove(dx,dy)
                    LocalBoxBlaze.BoxObject.dragBoxSetStop()

                }
            }
        )

    } 
)

Template.Box.created = function()
{
    //Debug
    /*
    console.log(
        'l 236 Box created \n',
        'this is : \n',
        this
    )
    */
    
    //alias
    var LocalBoxBlaze=this

    //init
    init(
            this,
            {
                'ParentTemplateStr':"System",
                'TemplateStr':'Box',
                'ChildCollectionStrsArray':['coops'],
                'DefaultObject':{
                                'x0':200,
                                'y0':200
                            }
            }
        )

    //Debug
    /*
    console.log(
        'l 259 Box created \n',
        'LocalBoxBlaze is : \n',
        LocalBoxBlaze
    )
    */
    
    //Init the anchor Rect
    LocalBoxBlaze.AnchorRect=PatchRaphael.rect(
            LocalBoxBlaze.data.x0,
            LocalBoxBlaze.data.y0,
            20,
            20
        ).attr(
            {
                fill : 'green',
                cursor : 'move'
            }
        )
    
    //Init the anchor Rect
    LocalBoxBlaze.InfoRect=PatchRaphael.rect(
            LocalBoxBlaze.data.x0,
            LocalBoxBlaze.data.y0+20,
            20,
            20
        ).attr(
            {
                fill : 'gray',
                cursor : 'move'
            }
        )
    LocalBoxBlaze.Infox = new ReactiveVar;
    LocalBoxBlaze.Infoy = new ReactiveVar;
    LocalBoxBlaze.Infox.set(LocalBoxBlaze.data.x0)
    LocalBoxBlaze.Infoy.set(LocalBoxBlaze.data.y0)

    //Debug
    /*
    console.log(
        'l 242 Box rendered \n',
        //'Box is \n',
        //Box
        'init a new Box'
    )
    */

    //init
    LocalBoxBlaze.BoxObject=new BoxClass()

    //Debug
    /*
    console.log(
        'l 253 Box rendered \n',
        'Box is \n',
        Box
    )
    */

    //Link
    LocalBoxBlaze.BoxObject.BoxBlaze=LocalBoxBlaze
    LocalBoxBlaze.BoxObject.AnchorRect=LocalBoxBlaze.AnchorRect

    //push
    LocalBoxBlaze.BoxObject.set.push(
        LocalBoxBlaze.AnchorRect,
        LocalBoxBlaze.InfoRect
    )   

    //Debug
    /*
    console.log(
        'l 228 Box \n',
        'Make it drag'
    )
    */


    //make it draggable
    LocalBoxBlaze.BoxObject.set.drag(
        LocalBoxBlaze.BoxObject.dragBoxSetMove, 
        LocalBoxBlaze.BoxObject.dragBoxSetStart, 
        LocalBoxBlaze.BoxObject.dragBoxSetStop
    );

    //Debug
    /*
    console.log(
            'Box rendered l 290',
            'PatchRaphael.BoxSetsSet is : \n',
            PatchRaphael.BoxSetsSet,
            '\n',
            'PatchRaphael.BoxeBlazesDict is : \n',
            PatchRaphael.BoxeBlazesDict,
            '\n',
        )
    */

    //Give to the BoxSetsSet
    PatchRaphael.BoxSetsSet.push(LocalBoxBlaze.BoxObject.set)
    PatchRaphael.BoxeBlazesDict[LocalBoxBlaze.data._id]=LocalBoxBlaze
 
}
Template.Box.helpers(
    {
        Infox:function()
        {
            return Template.instance().Infox.get();
        },
        Infoy:function()
        {
            return Template.instance().Infoy.get();
        }
    }
)
Template.Box.rendered = function()
{

    //Debug
    /*
    console.log(
        'Template.Box.rendered l 374'
    )
    */

    //alias
    var LocalBoxBlaze=this

    //update
    LocalBoxBlaze.BoxObject.AnchorRect.attr(
            {
                x:LocalBoxBlaze.data.x0,
                y:LocalBoxBlaze.data.y0
            }
        )
}

Template.Box.destroyed = function(){

    //Debug
    /*
    console.log(
        'l 213 Box destroyed',
        'this is : \n',
        this
    )
    */

    //alias
    var LocalBoxBlaze=this

    //exclude 
    PatchRaphael.BoxSetsSet.exclude(LocalBoxBlaze.BoxObject.set)

    //remove
    LocalBoxBlaze.BoxObject.set.remove()

    //delete
    delete PatchRaphael.BoxeBlazesDict[LocalBoxBlaze.data._id]

}
