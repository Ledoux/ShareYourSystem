/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Patch defines the svg support for displaying the views of the instances.
It calls a Raphael instance and defines a 

*/


//starup
Meteor.startup(

    function () {

        /*
            Define here the global variables for the raphael env
        */


        // require
        require('raphael')

        //build the Raphael environment
        PatchRaphael=Raphael($('#PatchSvg').get(0))

        //get
        PatchSvg=$('#PatchSvg')
        PatchSvgOffset=PatchSvg.offset()

        //Debug
        console.log(
                    'l Patch 36\n',
                    'PatchSvg is ',
                    PatchSvg,
                    '\n',
                    'PatchSvgOffset is ',
                    PatchSvgOffset,
                    '\n'
                )

        //init
        RaphObjectsDict={}
        GlobalSet=PatchRaphael.set()

        /*
            Define here a drag option for the sets
        */

        /*
        Raphael.st.draggable=function()
        {
            //set
            var LocalSet=this

            //define
            dragSetStart = function()
            {

                //Debug
                console.log(
                        'l 58 dragSetStart',
                        'LocalSet is \n',
                        LocalSet
                )

                for(var __KeyStr in LocalSet.items) {

                    //get
                    RaphObject=LocalSet.items[__KeyStr]

                    //set
                    RaphObject.ox = RaphObject.attr("x");
                    RaphObject.SetY0Int = RaphObject.attr("y");

                    //Debug
                    console.log(
                            'l 69 dragSetStart',
                            'RaphObject is : \n',
                            RaphObject
                    )
   
                }
                
            }
            dragSetMove = function(_dx,_dy)
            {

                //Debug
                console.log(
                        'l 58 dragSetMove',
                        'LocalSet is : \n',
                        LocalSet,
                        'LocalSet.items is : \n',
                        LocalSet.items
                )

                for(var __KeyStr in LocalSet.items) {

                    //get
                    RaphObject=LocalSet.items[__KeyStr]

                    //Debug
                    console.log(
                            'l 106 dragSetMove',
                            'RaphObject is : \n',
                            RaphObject,
                           'RaphObject.attr("x") is \n ',
                           RaphObject.attr("x"),
                           '\n',
                           'RaphObject.attr("y") is \n ',
                           RaphObject.attr("y")
                    )

                    //set
                    //lx=RaphObject.ox+_dx
                    //ly=RaphObject.SetY0Int+_dy
                    RaphObject.attr(
                        { 
                            x: RaphObject.ox + _dx, 
                            y: RaphObject.SetY0Int + _dy 
                        }
                    );

                    //RaphObject.transform('t'+_dx+','+_dy)

                    //Debug
                    console.log(
                            'l 125 dragSetMove',
                           'RaphObject.attr("x") is \n ',
                           RaphObject.attr("x"),
                           '\n',
                           'RaphObject.attr("y") is \n ',
                           RaphObject.attr("y")
                    )
    

                }
            }
            dragSetStop = function()
            {   
                
            }

            //set
            LocalSet.drag(dragSetMove,dragSetStart,dragSetStop)
        }
        */

        Raphael.st.draggable = function() {

            //
            var LocalSet = this
            var lx = 0
            var ly = 0
            //SetX0Int = PatchSvgOffset.left,
            //SetY0Int = PatchSvgOffset.top,
            if(LocalSet.SetX0Int == undefined || LocalSet.SetX0Int == null)
            {
                LocalSet.SetX0Int=0
            }
            if(LocalSet.SetY0Int == undefined || LocalSet.SetY0Int == null)
            {
                LocalSet.SetY0Int=0
            }

            //Debug
            console.log(
                'Raphael.st.draggable l 166',
                'LocalSet is',
                LocalSet,
                '\n',
                'LocalSet.SetX0Int is \n',
                LocalSet.SetX0Int,
                '\n',
                'LocalSet.SetY0Int is \n',
                LocalSet.SetY0Int,
                '\n',
                'lx is \n',
                lx,
                '\n',
                'ly is \n',
                ly
            )


            dragSetStart = function() {

                //Debug
                /*
                console.log(
                        'l 188 dragSetStart \n',
                        'SetX0 is \n',
                        SetX0,
                        '\n',
                        'SetY0Int is \n',
                        SetY0Int,
                        '\n',
                        'lx is \n',
                        lx,
                        '\n',
                        'ly is \n',
                        ly
                    )
                */

                //update the x and y in the elements
                for(var __KeyStr in LocalSet.items) {

                    //get
                    RaphObject=LocalSet.items[__KeyStr]

                    //Debug
                    /*
                    console.log(
                            'l 106 dragSetMove',
                            'RaphObject is : \n',
                            RaphObject,
                           'RaphObject.attr("x") is \n ',
                           RaphObject.attr("x"),
                           '\n',
                           'RaphObject.attr("y") is \n ',
                           RaphObject.attr("y")
                    )
                    */

                     //update
                    if(RaphObject.ParentBox!=undefined || RaphObject.ParentBox!=null){

                        //update x and y 
                        RaphObject.attr(
                            {
                                x:RaphObject.ParentBox.data.x0,
                                y:RaphObject.ParentBox.data.y0
                            }
                        )
                    }
                }

                //SetX0Int=0
                //SetY0Int=0
            }
            dragSetMove = function(_dx,_dy) {

                //Debug
                console.log(
                        'l 242 dragSetMove \n',
                        'LocalSet is \n',
                        LocalSet,
                        '\n',
                        'LocalSet.SetX0Int is \n',
                        LocalSet.SetX0Int,
                        '\n',
                        'LocalSet.SetY0Int is \n',
                        LocalSet.SetY0Int,
                        '\n',
                        '_dx is : \n',
                        _dx
                    )

                //transform the local set
                var scale=1
                lx = LocalSet.SetX0Int+_dx/scale;
                ly = LocalSet.SetY0Int+_dy/scale;
                LocalSet.transform('T' + lx + ',' + ly);
                
                //update the x and y in the elements
                /*
                for(var __KeyStr in LocalSet.items) {

                    //get
                    RaphObject=LocalSet.items[__KeyStr]

                    //update x and y 
                    var x=RaphObject.attr('x')
                    var y=RaphObject.attr('y')
                    RaphObject.attr(
                        {
                            x:lx,
                            y:ly
                        }
                    )

                    RaphObject.transform('...t' + lx + ',' + ly);
                }
                */

            }
            dragSetStop = function() {

                //set
                LocalSet.SetX0Int = lx;
                LocalSet.SetY0Int = ly;

                //Debug
                console.log(
                        'l 264 dragSetStop \n',
                        'LocalSet.SetX0Int is \n',
                        LocalSet.SetX0Int,
                        '\n',
                        'LocalSet.SetY0Int is \n',
                        LocalSet.SetY0Int,
                        '\n',
                        'lx is \n',
                        lx,
                        '\n',
                        'ly is \n',
                        ly
                    )

                //LocalSet.transform("");
                //LocalSet.transform('...t' + lx + ',' + ly);

                /*
                var realX = LocalSet.matrix.x(
                        LocalSet.attr("x"),LocalSet.attr("y")
                    );
                var realY = LocalSet.matrix.y(
                        LocalSet.attr("x"),LocalSet.attr("y")
                );
                LocalSet.attr(
                        {
                            x:realX,
                            y:realY
                        }
                    )
                */

                /*
                //update the x and y in the elements
                for(var __KeyStr in LocalSet.items) {

                    //get
                    RaphObject=LocalSet.items[__KeyStr]

                    //Debug
                    console.log(
                            'l 286 dragSetStop',
                            'RaphObject is : \n',
                            RaphObject,
                           'RaphObject.attr("x") is \n ',
                           RaphObject.attr("x"),
                           '\n',
                           'RaphObject.attr("y") is \n ',
                           RaphObject.attr("y")
                    )

                    //update x and y 
                    var realX = RaphObject.matrix.x(
                        RaphObject.attr("x"),RaphObject.attr("y")
                    );
                    var realY = RaphObject.matrix.y(
                        RaphObject.attr("x"),RaphObject.attr("y")
                    );
                    var x=RaphObject.attr('x')
                    var y=RaphObject.attr('y')
                    RaphObject.attr(
                        {
                            x:realX,
                            y:realY
                        }
                    )

                    //remove all trans
                    //RaphObject.transform("")

                    var newX=x+lx
                    var newY=y+ly

                    //update
                    if(RaphObject.ParentBox!=undefined || RaphObject.ParentBox!=null){

                        //set in the box
                        RaphObject.ParentBox.data.x0=x
                        RaphObject.ParentBox.data.y0=y

                        //Debug
                        console.log('We update the db')

                        //better to not update directly the boxes to not overload the db queries
                        Boxes.update(
                            {_id:RaphObject.ParentBox.data._id},
                            {$set:{x0:newX,y0:newY}}
                        )

                    }

                    //set
                    //lx=RaphObject.ox+_dx
                    //ly=RaphObject.SetY0Int+_dy
                    /*
                    RaphObject.attr(
                        { 
                            x: lx, 
                            y: ly 
                        }
                    );
                    */
                //}

            }

            //
            this.drag(dragSetMove, dragSetStart, dragSetStop);
        };

        /*
            Define here BackRect and the selection box option
        */

        //set that will receive the selected items
        SelectionSet = PatchRaphael.set();
        //SelectionSet.transform("")

        //DRAG FUNCTIONS
        //when mouse goes down over background, start drawing selection box
        function dragSelectionStart (_x, _y, _Event) {

            //Debug
            /*
            console.log(
                'l 32 dragStart \n',
                '_x _y are : \n',
                _x,_y
            )
            */

            //init
            SelectionRect = PatchRaphael.rect(
                              _x-PatchSvgOffset.left, 
                              _y-PatchSvgOffset.top, 5, 5
                            ).attr(
                              "stroke", "#9999FF"
                            );   

            //for
            for (var __KeyStr in SelectionSet.items) {

                //exclude
                //SelectionSet.exclude(RaphObject)

                //get
                var RaphObject=SelectionSet[__KeyStr]

                //get
                RaphObject.attr("opacity", 1); 
            }
        }

        // When mouse moves during drag, adjust box.
        // If the drag is to the left or above original point,
        // you have to translate the whole box and invert the dx 
        // or dy values since .rect() doesn't take negative width or height
        function dragSelectionMove (_dx, _dy, _x, _y, _Event) {

            //init
            var xoffset = 0,
                yoffset = 0;

            //Check negative values
            if (_dx < 0) {
                xoffset = _dx;
                _dx = -1 * _dx;
            }
            if (_dy < 0) {
                yoffset = _dy;
                _dy = -1 * _dy;
            }

            //Debug
            /*
            console.log(
              'l 60 GUI dragMove \n',
              'SelectionRect is : \n',
              SelectionRect
            )
            */

            //transform
            SelectionRect.transform("T" + xoffset + "," + yoffset);

            //set
            SelectionRect.attr("width", _dx);    
            SelectionRect.attr("height", _dy);    

        }

        function resetSelection(){

            //undrag
            SelectionSet.undrag()

            //for
            for (var __KeyStr in SelectionSet.items) {

                //exclude
                //SelectionSet.exclude(RaphObject)

                //get
                var RaphObject=SelectionSet[__KeyStr]

                //get
                RaphObject.attr("opacity", 1);

                //Debug
                /*
                console.log(
                    'l 220 reset \n',
                    'RaphObject is ',
                    RaphObject
                )
                */

                //Remake drag
                RaphObject.drag(dragBoxMove,dragBoxStart,dragBoxStop)
                //undrag
                //SelectionSet[c].undrag()

                //exclude
                //SelectionSet.exclude(RaphObject)

            }

            //remove the rectangle of selection
            SelectionRect.remove();

            //reinit and give the last X0 and Y0
            var SetX0Int=SelectionSet.SetX0Int
            var SetY0Int=SelectionSet.SetY0Int
            //empty selections and reset opacity;
            SelectionSet = PatchRaphael.set();
            SelectionSet.SetX0Int=SetX0Int
            SelectionSet.SetY0Int=SetY0Int
        }

        function dragSelectionStop (_Event) {

            //get the RectBounds of the selections
            var RectBounds = SelectionRect.getBBox();

            //Debug
            /*
            console.log(
            'l 144 before reset \n',
            'SelectionSet is \n',
            SelectionSet
            )
            */

            //
            resetSelection()
            
            /*
            console.log(
              'dragSelectionEnd l 100\n',
              'RectBounds is \n :',
              RectBounds,
              '\n',
              'GlobalSet is :\n',
              GlobalSet,
              'SelectionSet is \n',
                SelectionSet
            );
            */

            //for
            for (var __KeyStr in GlobalSet.items) {

                //get
                var RaphObject=GlobalSet[__KeyStr]

                // Here, we want to get the x,y vales of each object
                // regardless of what sort of shape it is.
                // But rect uses rx and ry, circle uses cx and cy, etc
                // So we'll see if the bounding boxes intercept instead
                var MyBounds = RaphObject.getBBox();

                //Debug
                /*
                console.log(
                    'l 327 dragSelectionEnd \n',
                    '__KeyStr is ',
                    __KeyStr,
                    'RaphObject is ',
                    RaphObject,
                    '\n',
                    'MyBounds is \n',
                    MyBounds,
                    '\n',
                    'RectBounds is \n',
                    RectBounds,
                    '\n'
                )
                */

                //do bounding boxes overlap?
                //is one of this object's x extremes between the selection's xe xtremes?
                if (MyBounds.x >= RectBounds.x && MyBounds.x <= RectBounds.x2 || MyBounds.x2 >= RectBounds.x && MyBounds.x2 <= RectBounds.x2) {

                    //same for y
                    if (MyBounds.y >= RectBounds.y && MyBounds.y <= RectBounds.y2 || MyBounds.y2 >= RectBounds.y && MyBounds.y2 <= RectBounds.y2) 
                    {

                        //push
                        SelectionSet.push(RaphObject);     

                        //drag
                        //RaphObject.drag(dragBoxMove,dragBoxStart,dragBoxStop)
                        RaphObject.undrag()

                        //set
                        RaphObject.attr("opacity", 0.5);
                    }
                }

                //enable the drag
                SelectionSet.draggable()
                //SelectionSet.drag(dragSetMove,dragSetStart,dragSetStop)
            }

            //Debug
            /*
            console.log(
                'dragEnd l 133 \n',
                'SelectionSet is \n',
                SelectionSet
            )
            */

            /*

                //
                var x=RaphObject.attr('x')
                var y=RaphObject.attr('y')

                
                //set in the box
                RaphObject.ParentBox.data.x0=x
                RaphObject.ParentBox.data.y0=y

                //better to not update directly the boxes to not overload the db queries
                Boxes.update(
                    {_id:RaphObject.ParentBox.data._id},
                    {$set:{x0:x,y0:y}}
                )
            }
            */

            


        }

        //init
        var BackRect = PatchRaphael.rect(
                        0, 0, PatchRaphael.width, PatchRaphael.height
                      ).attr(
                        "fill", "#FFF"
                      );
        BackRect.drag(
                dragSelectionMove, dragSelectionStart, dragSelectionStop
            );
        BackRect.click(
            function(e) 
            {
                resetSelection(); 
            }
        );

        /*
            Define here a drag option for each set
        */

        

    }
)
/*
//Init functions
var createPatch = function(){
    for(i = 0; i < 20; i++)
        Boxes.insert({
            x:Math.floor(Math.random()*800),
            y:Math.floor(Math.random()*600)
        });

    for(i = 0; i < 10; i++)
    {
        var Source = Random.choice(Boxes.find().fetch());
        var Target = Random.choice(
                        Boxes.find(
                            {_id:{$ne:Source._id}}
                         ).fetch()
                     );
        //make sure we dont connect to the source
        
        Connectors.insert(
            {
                SourceId:Source._id,
                TargetId:Target._id
            }
        );
    }

};
var destrSetY0IntPatch = function(){
    Connectors.find({}).forEach(function(_Connector){
        Connectors.remove({_id:_Connector._id});
    });

    Boxes.find({}).forEach(
        function(_Box){
            Boxes.remove({_id:_Box._id});
        }
    );
};
*/

Template.Patch.helpers(
{
    'boxes': function () {
        return Boxes.find(
            {
                PatchStr:
               {
                $in:
                Session.get('PatchStrsList')
                //Patches.find({},{name:true}).map(function(object){return object['name']})
               }
           }
       )
    },

    'connectors': function () {
        return Connectors.find();
    }
});



