/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Selection defines the option to select several instances
to make it drag together

*/

Meteor.startup(
    function()
    {

       //set that will receive the selected items
        SelectionSet = PatchRaphael.set();

        //when mouse goes down over background, start drawing selection box
        function dragSelectionStart (_x, _y, _Event) {

            //Debug
            /*
            console.log(
                'l 20 dragSelectionStart \n',
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

                //get
                var RaphObject=SelectionSet[__KeyStr]

                //set opacity
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
              'l 60 GUI dragSelectionMove \n',
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

             //reinit and give the last X0 and Y0
            var ox=SelectionSet.ox
            var oy=SelectionSet.oy

            //for
            for (var __KeyStr in SelectionSet.items) {

                //exclude
                //SelectionSet.exclude(RaphObject)

                //get
                var RaphObject=SelectionSet[__KeyStr]

                //get
                RaphObject.attr("opacity", 1);

                //Debug
                console.log(
                    'l 220 reset \n',
                    'RaphObject is ',
                    RaphObject
                )

                if(RaphObject.AnchorRect == undefined || RaphObject.AnchorRect== null)
                {

                    //Remake drag for rect ellipse...
                    RaphObject.drag(dragBoxMove,dragBoxStart,dragBoxStop)
                }
                else
                {
                    //Debug
                    /*
                    console.log(
                        'resetSelection l 558 \n',
                        'We make redrag the set \n',
                        'RaphObject is \n',
                        RaphObject
                    )
                    */

                    //Remake drag for set...
                    RaphObject.drag(dragSetMove,dragSetStart,dragSetStop)

                    //
                    RaphObject.ox=0
                    RaphObject.oy=0

                }
                
                //undrag
                //SelectionSet[c].undrag()

                //exclude
                //SelectionSet.exclude(RaphObject)

            }

            //remove the rectangle of selection
            SelectionRect.remove();

           
            //empty selections and reset opacity;
            SelectionSet = PatchRaphael.set();
            SelectionSet.ox=ox
            SelectionSet.oy=oy
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
              'InstancesSet is :\n',
              InstancesSet,
              'SelectionSet is \n',
                SelectionSet
            );
            */

            //for
            for (var __KeyStr in InstancesSet.items) {

                //get
                var RaphObject=InstancesSet[__KeyStr]

                // Here, we want to get the x,y vales of each object
                // regardless of what sort of shape it is.
                // But rect uses rx and ry, circle uses cx and cy, etc
                // So we'll see if the bounding boxes intercept instead

                var MyBounds={}
                if(RaphObject.AnchorRect != undefined || RaphObject.AnchorRect!= null)
                {
                    MyBounds = RaphObject.getBBox();
                }
                else
                {
                    MyBounds = RaphObject.AnchorRect.getBBox();
                }

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
            }

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
            function(_Event) 
            {
                resetSelection(); 
            }
        );
    }
)

