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
        'DefaultObject':{
            'x':200,
            'y':200
        },
        'ChildHelpersObject':
        {
          'coops':function()
           {

                //return
                return Coops.find(
                    {
                        'ParentBoxStr':this.BoxStr
                    }
               )
           }
        }
    }
)

Template.Box.created = function()
{
    //Debug
    /*
    console.log(
            'Box created l 40'
        )
    */

    //init
    var LocalData=new DataClass(
      {
        'Blaze':this,
        'Abstraction':BoxAbstraction
      }
    )

    //datafy
    LocalData.datafy()

    //Debug
    /*
    console.log(
        'l 60 Box created \n'
    )
    */

    //init
    LocalData.Box=new BoxClass()
    LocalData.Box.Data=LocalData

    //Init the anchor Rect
    LocalData.Box.AnchorRect=PatchRaphael.rect(
            LocalData.Blaze.data.x,
            LocalData.Blaze.data.y,
            20,
            20
        ).attr(
            {
                fill : 'green',
                cursor : 'move'
            }
        )
    
    //Init the anchor Rect
    LocalData.Box.InfoRect=PatchRaphael.rect(
            LocalData.Blaze.data.x,
            LocalData.Blaze.data.y+20,
            20,
            20
        ).attr(
            {
                fill : 'gray',
                cursor : 'move'
            }
        )
    LocalData.Infox = new ReactiveVar;
    LocalData.Infoy = new ReactiveVar;
    LocalData.Infox.set(LocalData.Blaze.data.x)
    LocalData.Infoy.set(LocalData.Blaze.data.y)

    //Debug
    /*
    console.log(
        'l 242 Box rendered \n',
        //'Box is \n',
        //Box
        'init a new Box'
    )
    */

    

    //Debug
    /*
    console.log(
        'l 253 Box rendered \n',
        'Box is \n',
        Box
    )
    */

    //push
    LocalData.Box.set.push(
        LocalData.Box.AnchorRect,
        LocalData.Box.InfoRect
    )   

    //Debug
    /*
    console.log(
        'l 228 Box \n',
        'Make it drag'
    )
    */


    //make it draggable
    LocalData.Box.set.drag(
        LocalData.Box.dragBoxSetMove, 
        LocalData.Box.dragBoxSetStart, 
        LocalData.Box.dragBoxSetStop
    );

    //Debug
    /*
    console.log(
            'Box rendered l 290',
            'PatchRaphael.BoxSetsSet is : \n',
            PatchRaphael.BoxSetsSet,
            '\n',
            'BlazesDict['boxes'] is : \n',
            BlazesDict['boxes'],
            '\n',
        )
    */

    //Give to the BoxSetsSet
    PatchRaphael.BoxSetsSet.push(LocalData.Box.set)

}

Template.Box.helpers(
    _.extend(
        BoxAbstraction.ChildHelpersObject,
        {
            Infox:function()
            {
                return Template.instance().Data.Infox.get();
            },
            Infoy:function()
            {
                return Template.instance().Data.Infoy.get();
            }
        }
    )
)

Meteor.startup(
    function()
    {
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
            var LocalBox=this

            //Define the set
            LocalBox.set=PatchRaphael.set()
            LocalBox.set.Box=LocalBox

            //Debug
            /*
            console.log(
                'LocalBox l 39',
                'LocalBox.set is',
                LocalBox.set,
                '\n'
            )
            */

            LocalBox.dragBoxSetStart = function() {

                //Debug
                /*
                console.log(
                        'l 212 dragBoxSetStart \n'
                    )
                */
                
                //map
                LocalBox.set.items.map(
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

            LocalBox.dragBoxSetMove = function(_dx,_dy) {

                //Debug
                /*
                console.log(
                        'l 242 dragBoxSetMove \n',
                    )
                */

                LocalBox.set.items.map(
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
                    {_id:LocalBox.BoxBlaze.data._id},
                    {
                        $set:{
                            x:LocalBox.AnchorRect.attr('x'),
                            y:LocalBox.AnchorRect.attr('y')
                        }
                    }
                )
                */

                //set
                LocalBox.Data.Infox.set(LocalBox.AnchorRect.attr('x'))
                LocalBox.Data.Infoy.set(LocalBox.AnchorRect.attr('y'))
            }

            LocalBox.dragBoxSetStop = function() {

                //Debug
                /*
                console.log(
                        'l 264 dragBoxSetStop \n',
                        'LocalBox.BoxBlaze.data._id is \n',
                        LocalBox.BoxBlaze.data._id
                    )
                */

                //update the db
                Boxes.update(
                    {_id:LocalBox.Data.Blaze.data._id},
                    {
                        $set:{
                            x:LocalBox.AnchorRect.attr('x'),
                            y:LocalBox.AnchorRect.attr('y')
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

        //Bind an observe of the Instances data
        var isObserveBool=false
        if(isObserveBool)
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
                        
                        //find the translation
                        var LocalData=BlazesDict['boxes'][_NewObject._id]
                        if (LocalData!=undefined && LocalData!=null)
                        {

                            //set
                            var dx=_NewObject.x-LocalData.Box.AnchorRect.attr('x')
                            var dy=_NewObject.y-LocalData.Box.AnchorRect.attr('y')
                        
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
                                    LocalData.Box.dragBoxSetStart()
                                    LocalData.Box.dragBoxSetMove(dx,dy)
                                    LocalData.Box.dragBoxSetStop()
                                }
                            }
                            
                        }
                    }
                }
            )
        }

    }
)

