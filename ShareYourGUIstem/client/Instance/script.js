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
        BoxProto = function() {

            //Debug
            /*
            console.log(
                'l 24 BoxProto \n',
                'We init a new Box \n',
                'PatchRaphael is ',
                PatchRaphael
            )
            */

            //alias
            var LocalBox=this

            //
            LocalBox.set=PatchRaphael.set()
            LocalBox.set.Box=LocalBox
            LocalBox.lx = 0
            LocalBox.ly = 0
            if(LocalBox.ox == undefined || LocalBox.ox == null)
            {
                LocalBox.ox=0
            }
            if(LocalBox.oy == undefined || LocalBox.oy == null)
            {
                LocalBox.oy=0
            }
            //LocalBox.Instance={}
            //LocalBox.AnchorRect={}

            //Debug
            /*
            console.log(
                'LocalBox l 39',
                'LocalBox.set is',
                LocalBox.set,
                '\n',
                'LocalBox.ox is \n',
                LocalBox.ox,
                '\n',
                'LocalBox.oy is \n',
                LocalBox.oy,
                '\n',
                'LocalBox.lx is \n',
                LocalBox.lx,
                '\n',
                'LocalBox.ly is \n',
                LocalBox.ly
            )
            */

            LocalBox.dragBoxSetStart = function() {

                //Debug
                /*
                console.log(
                        'l 188 dragBoxSetStart \n',
                        'LocalBox.ox is \n',
                        LocalBox.ox,
                        '\n',
                        'LocalBox.oy is \n',
                        LocalBox.oy,
                        '\n',
                        'lx is \n',
                        LocalBox.lx,
                        '\n',
                        'LocalBox.ly is \n',
                        LocalBox.ly
                    )
                */

            }

            LocalBox.dragBoxSetMove = function(_dx,_dy) {

                //Debug
                /*
                console.log(
                        'l 242 dragBoxSetMove \n',
                        'LocalBox.set is \n',
                        LocalBox.set,
                        '\n',
                        'LocalBox.ox is \n',
                        LocalBox.ox,
                        '\n',
                        'LocalBox.oy is \n',
                        LocalBox.oy,
                        '\n',
                        '_dx is : \n',
                        _dx,
                        '\n',
                        '_dy is : \n',
                        _dy
                    )
                */

                //transform the local set
                LocalBox.lx = LocalBox.ox+_dx;
                LocalBox.ly = LocalBox.oy+_dy;
                LocalBox.set.transform('T' + LocalBox.lx + ',' + LocalBox.ly);
                
            }

            LocalBox.dragBoxSetStop = function() {

                //set
                LocalBox.ox = LocalBox.lx;
                LocalBox.oy = LocalBox.ly;

                //Debug
                /*
                console.log(
                        'l 264 dragBoxSetStop \n',
                        'LocalBox.ox is \n',
                        LocalBox.ox,
                        '\n',
                        'LocalBox.oy is \n',
                        LocalBox.oy,
                        '\n',
                        'LocalBox.lx is \n',
                        LocalBox.lx,
                        '\n',
                        'LocalBox.ly is \n',
                        LocalBox.ly
                    )
                */

                //update the db
                var newX=LocalBox.AnchorRect.attr('x')+LocalBox.lx
                var newY=LocalBox.AnchorRect.attr('y')+LocalBox.ly
              
                //better to not update directly the boxes to not overload the db queries
                Instances.update(
                    {_id:LocalBox.Instance.data._id},
                    {$set:{x0:newX,y0:newY}}
                )
            }

            //Debug
            /*
            console.log(
                'l155 Instance',
                'End of the BoxProto definition'
                )
            */
        } 

        Template.Instance.rendered = function(){

            //Debug
            console.log(
                'l 213 Instance rendered',
                'this is : \n',
                this
            )

            //alias
            var LocalInstance=this

            //init position
            CoordinateStrsList=["x","y"]
            for(var __AxisIndexInt in CoordinateStrsList)
            {

                //set
                var InitAxisKeyStr=CoordinateStrsList[__AxisIndexInt]+"0"

                //Debug
                //console.log(__AxisIndexInt,InitAxisKeyStr)

                //Check
                if (LocalInstance.data[
                    InitAxisKeyStr] === undefined || LocalInstance.data[
                    InitAxisKeyStr] === null) {
                    
                    //init value
                    LocalInstance.data[InitAxisKeyStr]=200

                    //update dict
                    var UpdateDict={}
                    UpdateDict[InitAxisKeyStr]=LocalInstance.data[InitAxisKeyStr]

                    //Debug
                    //console.log(UpdateDict)

                    //update
                    Instances.update(
                        {_id:LocalInstance.data._id},
                        {$set:UpdateDict}
                    )
                }
            }

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
            LocalInstance.Box=new BoxProto()

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

            //Debug
            console.log(
                'Instance rendered l 309 \n',
                'Instance.Box.AnchorRect.getBBox() is \n',
                LocalInstance.Box.AnchorRect.getBBox(),
                'LocalInstance.data._id is \n',
                LocalInstance.data._id
            )
            LocalInstance.Box.AnchorRect.BBox=LocalInstance.Box.AnchorRect.getBBox()

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

    }
)

