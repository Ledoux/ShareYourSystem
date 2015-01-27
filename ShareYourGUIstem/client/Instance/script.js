/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Instance defines the svg support for displaying an instance coming
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
        PatchRaphael.InstancesDict={}

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
                        'l 188 dragBoxSetStart \n',
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
                Instances.update(
                    {_id:LocalBox.Instance.data._id},
                    {
                        $set:{
                            x0:LocalBox.AnchorRect.attr('x'),
                            y0:LocalBox.AnchorRect.attr('y')
                        }
                    }
                )
                */

                //set
                LocalBox.Instance.Infox.set(LocalBox.AnchorRect.attr('x'))
                LocalBox.Instance.Infoy.set(LocalBox.AnchorRect.attr('y'))
            }

            LocalBox.dragBoxSetStop = function() {

                //Debug
                console.log(
                        'l 264 dragBoxSetStop \n',
                        'LocalBox.Instance.data._id is \n',
                        LocalBox.Instance.data._id
                    )
                
                //update the db
                Instances.update(
                    {_id:LocalBox.Instance.data._id},
                    {
                        $set:{
                            x0:LocalBox.AnchorRect.attr('x'),
                            y0:LocalBox.AnchorRect.attr('y')
                        }
                    }
                )

            }

            //Debug
            /*
            console.log(
                'l155 Instance',
                'End of the BoxClass definition'
                )
            */
        }


        //InstanceReactiveClass = new ReactiveClass(Instances);
        //InstanceReactiveClass.prototype.getName = function() {
        //  return this.name;
        //}

    } 
)

Template.Instance.created = function()
{
    //Debug
    /*
    console.log(
        'l 190 Instance created',
        'this is : \n',
        this
    )
    */

    //alias
    var LocalInstance=this

    //init position
    DefaultInstanceDataDict={
        'x0':200,
        'y0':200,
        'NodeKeyStr':"Default"
    }

    //map
    UpdateKeyStrsList=_.filter(
        _.keys(DefaultInstanceDataDict),
        function(__KeyStr){

            //Debug
            /*
            console.log(
                'Template Instance rendered \n',
                '\n',
                '__KeyStr is \n',
                __KeyStr,
                '\n'
                )
            */

            return LocalInstance.data[
                __KeyStr] === undefined || LocalInstance.data[
                __KeyStr] === null
        }
    )

    //object
    UpdateObject=_.object(
                        _.map(
                            UpdateKeyStrsList,
                            function(__UpdateKeyStr){
                                return [
                                    __UpdateKeyStr,
                                    DefaultInstanceDataDict[__UpdateKeyStr]
                                ]
                            }
                        )
                    )

    //Debug
    /*
    console.log(
        'Tempate Instance rendered l 238 \n',
        'UpdateObject is \n',
        UpdateObject
    )
    */

    //update
    _.each(UpdateObject,function(__Value,__Key){LocalInstance.data[__Key]=__Value})
    Instances.update(
                {_id:LocalInstance.data._id},
                {
                    $set:UpdateObject
                }
            )

    //Init the anchor Rect
    LocalInstance.AnchorRect=PatchRaphael.rect(
            LocalInstance.data.x0,
            LocalInstance.data.y0,
            20,
            20
        ).attr(
            {
                fill : 'green',
                cursor : 'move'
            }
        )
    
    //Init the anchor Rect
    LocalInstance.InfoRect=PatchRaphael.rect(
            LocalInstance.data.x0,
            LocalInstance.data.y0+20,
            20,
            20
        ).attr(
            {
                fill : 'gray',
                cursor : 'move'
            }
        )
    this.Infox = new ReactiveVar;
    this.Infoy = new ReactiveVar;
    this.Infox.set(LocalInstance.data.x0)
    this.Infoy.set(LocalInstance.data.y0)

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
    LocalInstance.Box=new BoxClass()

    //Debug
    /*
    console.log(
        'l 253 Box rendered \n',
        'Box is \n',
        Box
    )
    */

    //Link
    LocalInstance.Box.Instance=LocalInstance
    LocalInstance.Box.AnchorRect=LocalInstance.AnchorRect

    //push
    LocalInstance.Box.set.push(
        LocalInstance.AnchorRect,
        LocalInstance.InfoRect
    )   

    //Debug
    /*
    console.log(
        'l 228 Box \n',
        'Make it drag'
    )
    */


    //make it draggable
    LocalInstance.Box.set.drag(
        LocalInstance.Box.dragBoxSetMove, 
        LocalInstance.Box.dragBoxSetStart, 
        LocalInstance.Box.dragBoxSetStop
    );

    //Debug
    /*
    console.log(
            'Box rendered l 290',
            'PatchRaphael.BoxSetsSet is : \n',
            PatchRaphael.BoxSetsSet,
            '\n',
            'PatchRaphael.InstancesDict is : \n',
            PatchRaphael.InstancesDict,
            '\n',
        )
    */

    //Give to the BoxSetsSet
    PatchRaphael.BoxSetsSet.push(LocalInstance.Box.set)
    PatchRaphael.InstancesDict[LocalInstance.data._id]=LocalInstance
 
}
Template.Instance.helpers(
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
Template.Instance.rendered = function()
{

    //Debug
    /*
    console.log(
        'Template.Instance.rendered l 374'
    )
    */

    //alias
    var LocalInstance=this

    //update
    LocalInstance.Box.AnchorRect.attr(
            {
                x:LocalInstance.data.x0,
                y:LocalInstance.data.y0
            }
        )
}

Template.Instance.destroyed = function(){

    //Debug
    /*
    console.log(
        'l 213 Instance destroyed',
        'this is : \n',
        this
    )
    */

    //alias
    var LocalInstance=this

    //exclude 
    PatchRaphael.BoxSetsSet.exclude(LocalInstance.Box.set)

    //remove
    LocalInstance.Box.set.remove()

    //delete
    delete PatchRaphael.InstancesDict[LocalInstance.data._id]

}
