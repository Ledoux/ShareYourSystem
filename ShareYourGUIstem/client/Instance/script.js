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

        //define
        Box = function() {

            //alias
            Box=this

            Box.set=PatchRaphael.set()
            Box.lx = 0
            Box.ly = 0
            if(Box.ox == undefined || Box.ox == null)
            {
                Box.ox=0
            }
            if(Box.oy == undefined || Box.oy == null)
            {
                Box.oy=0
            }
            Box.Instance={}
            Box.AnchorRect={}

            //Debug
            /*
            console.log(
                'Box l 39',
                'Box.set is',
                Box.set,
                '\n',
                'Box.ox is \n',
                Box.ox,
                '\n',
                'Box.oy is \n',
                Box.oy,
                '\n',
                'Box.lx is \n',
                Box.lx,
                '\n',
                'Box.ly is \n',
                Box.ly
            )
            */

            Box.dragBoxStart = function() {

                //Debug
                /*
                console.log(
                        'l 188 dragBoxStart \n',
                        'Box.ox is \n',
                        Box.ox,
                        '\n',
                        'Box.oy is \n',
                        Box.oy,
                        '\n',
                        'lx is \n',
                        Box.lx,
                        '\n',
                        'Box.ly is \n',
                        Box.ly
                    )
                */

                //update the x and y in the elements
                for(var __KeyStr in Box.set.items) {

                    //get
                    RaphObject=Box.set.items[__KeyStr]

                    //Debug
                    /*
                    console.log(
                            'l 106 dragsetMove',
                            'RaphObject is : \n',
                            RaphObject,
                           'RaphObject.attr("x") is \n ',
                           RaphObject.attr("x"),
                           '\n',
                           'RaphObject.attr("y") is \n ',
                           RaphObject.attr("y")
                    )
                    */
                }
            }

            Box.dragBoxMove = function(_dx,_dy) {

                //Debug
                /*
                console.log(
                        'l 242 dragBoxMove \n',
                        'Box.set is \n',
                        Box.set,
                        '\n',
                        'Box.ox is \n',
                        Box.ox,
                        '\n',
                        'Box.oy is \n',
                        Box.oy,
                        '\n',
                        '_dx is : \n',
                        _dx,
                        '\n',
                        '_dy is : \n',
                        _dy
                    )
                */

                //transform the local set
                Box.lx = Box.ox+_dx;
                Box.ly = Box.oy+_dy;
                Box.set.transform('T' + Box.lx + ',' + Box.ly);
                

            }

            Box.dragBoxStop = function() {

                //set
                Box.ox = Box.lx;
                Box.oy = Box.ly;

                //Debug
                /*
                console.log(
                        'l 264 dragBoxStop \n',
                        'Box.ox is \n',
                        Box.ox,
                        '\n',
                        'Box.oy is \n',
                        Box.oy,
                        '\n',
                        'Box.lx is \n',
                        Box.lx,
                        '\n',
                        'Box.ly is \n',
                        Box.ly
                    )
                */

                //update the db
                var newX=Box.AnchorRect.attr('x')+Box.lx
                var newY=Box.AnchorRect.attr('y')+Box.ly
              
                //better to not update directly the boxes to not overload the db queries
                Instances.update(
                    {_id:Box.Instance.data._id},
                    {$set:{x0:newX,y0:newY}}
                )
            }
        }   
    }
)

Template.Instance.rendered = function(){

    //Debug
    /*
    console.log(
        'l 213 Box destroyed',
        'this is : \n',
        this
    )
    */

    //init position
    CoordinateStrsList=["x","y"]
    for(var __AxisIndexInt in CoordinateStrsList)
    {

        //set
        InitAxisKeyStr=CoordinateStrsList[__AxisIndexInt]+"0"

        //Debug
        //console.log(__AxisIndexInt,InitAxisKeyStr)

        //Check
        if (this.data[InitAxisKeyStr] === undefined || this.data[InitAxisKeyStr] === null) {
            
            //init value
            this.data[InitAxisKeyStr]=200

            //update dict
            UpdateDict={}
            UpdateDict[InitAxisKeyStr]=this.data[InitAxisKeyStr]

            //Debug
            //console.log(UpdateDict)

            //update
            Instances.update(
                {_id:this.data._id},
                {$set:UpdateDict}
            )
        }
    }

    //Init the anchor Rect
    AnchorRect=PatchRaphael.rect(
            this.data.x0,
            this.data.y0,
            20,
            20
        ).attr(
            {
                fill : 'green',
                cursor : 'move'
            }
        )
    
    //Init the anchor Rect
    InfoRect=PatchRaphael.rect(
            this.data.x0,
            this.data.y0+20,
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
        'l 290 Box rendered \n',
        //'Box is \n',
        //Box
        'init a new Box'
    )
    */

    //init
    Box=new Box()
    Box.Instance=this
    Box.AnchorRect=AnchorRect

    //Debug
    /*
    console.log(
        'l 300 Box rendered \n',
        'Box is \n',
        Box
    )
    */

    //push
    Box.set.push(
        AnchorRect,
        InfoRect
    )   

    //Debug
    /*
    console.log(
        'l 228 Box \n',
        'Make it drag'
    )
    */

    //make it draggable
    Box.set.drag(
        Box.dragBoxMove, 
        Box.dragBoxStart, 
        Box.dragBoxStop
    );

    //link
    this.Box=Box

    //Give to the InstancesSet
    InstancesSet[this.data._id]=this

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

    //remove
    this.Box.set.remove()

}