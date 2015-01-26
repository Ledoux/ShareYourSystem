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
        //define
        SelectionProto = function() {

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
            var LocalSelection=this

            //
            LocalSelection.set=PatchRaphael.set()
            LocalSelection.set.Selection=LocalSelection
            LocalSelection.lx = 0
            LocalSelection.ly = 0
            LocalSelection.dx = 0
            LocalSelection.dy = 0
            if(LocalSelection.ox == undefined || LocalSelection.ox == null)
            {
                LocalSelection.ox=0
            }
            if(LocalSelection.oy == undefined || LocalSelection.oy == null)
            {
                LocalSelection.oy=0
            } 

            //Debug
            /*
            console.log(
                'LocalSelection l 39',
                'LocalSelection.set is',
                LocalSelection.set,
                '\n',
                'LocalSelection.ox is \n',
                LocalSelection.ox,
                '\n',
                'LocalSelection.oy is \n',
                LocalSelection.oy,
                '\n',
                'LocalSelection.lx is \n',
                LocalSelection.lx,
                '\n',
                'LocalSelection.ly is \n',
                LocalSelection.ly
            )
            */

            LocalSelection.dragSetStart = function() {

                //Debug
                /*
                console.log(
                        'l 188 dragSetStart \n',
                        'LocalSelection.ox is \n',
                        LocalSelection.ox,
                        '\n',
                        'LocalSelection.oy is \n',
                        LocalSelection.oy,
                        '\n',
                        'lx is \n',
                        LocalSelection.lx,
                        '\n',
                        'LocalSelection.ly is \n',
                        LocalSelection.ly
                    )
                */

            }

            LocalSelection.dragSetMove = function(_dx,_dy) {

                //Debug
                /*
                console.log(
                        'l 242 dragSetMove \n',
                        'LocalSelection.set is \n',
                        LocalSelection.set,
                        '\n',
                        'LocalSelection.ox is \n',
                        LocalSelection.ox,
                        '\n',
                        'LocalSelection.oy is \n',
                        LocalSelection.oy,
                        '\n',
                        '_dx is : \n',
                        _dx,
                        '\n',
                        '_dy is : \n',
                        _dy
                    )
                */

                //transform the local set
                LocalSelection.lx = LocalSelection.ox + _dx;
                LocalSelection.ly = LocalSelection.oy + _dy;
                LocalSelection.dx = _dx
                LocalSelection.dy = _dy
                LocalSelection.set.transform(
                    'T' + LocalSelection.lx + ',' + LocalSelection.ly);
                
            }

            LocalSelection.dragSetStop = function() {

                //set
                LocalSelection.ox = LocalSelection.lx;
                LocalSelection.oy = LocalSelection.ly;

                //Debug
                /*
                console.log(
                        'l 264 dragSetStop \n',
                        'LocalSelection.ox is \n',
                        LocalSelection.ox,
                        '\n',
                        'LocalSelection.oy is \n',
                        LocalSelection.oy,
                        '\n',
                        'LocalSelection.lx is \n',
                        LocalSelection.lx,
                        '\n',
                        'LocalSelection.ly is \n',
                        LocalSelection.ly
                    )
                */
            }

            //when mouse goes down over background, start drawing selection box
            LocalSelection.dragRectStart = function(_x, _y, _Event) {

                //Debug
                console.log(
                    'l 20 dragRectStart \n',
                    '_x _y are : \n',
                    _x,_y
                )

                LocalSelection.rect=PatchRaphael.rect(
                              _x-PatchSvgOffset.left, 
                              _y-PatchSvgOffset.top, 5, 5
                            ).attr(
                              "stroke", "#9999FF"
                            ); 

                //for
                for (var __KeyStr in LocalSelection.set.items) {

                    //get
                    var BoxSet=LocalSelection.set[__KeyStr]

                    //set opacity
                    BoxSet.attr("opacity", 1); 
                }
            }

            // When mouse moves during drag, adjust box.
            // If the drag is to the left or above original point,
            // you have to translate the whole box and invert the dx 
            // or dy values since .rect() doesn't take negative width or height
            LocalSelection.dragRectMove = function (_dx, _dy, _x, _y, _Event) {

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
                  'LocalSelection.rect. is : \n',
                  LocalSelection.rect.
                )
                */

                //transform
                LocalSelection.rect.transform("T" + xoffset + "," + yoffset);

                //set
                LocalSelection.rect.attr("width", _dx);    
                LocalSelection.rect.attr("height", _dy);    

            }

            LocalSelection.resetSet = function(){

                //undrag
                LocalSelection.set.undrag()

                //reinit and give the last X0 and Y0
                var ox=LocalSelection.ox
                var oy=LocalSelection.oy
                var lx=LocalSelection.lx
                var ly=LocalSelection.ly

                //for
                for (var __KeyStr in LocalSelection.set.items) {

                    //exclude
                    //SelectionSet.exclude(BoxSet)

                    //get
                    var BoxSet=LocalSelection.set[__KeyStr]

                    //get
                    BoxSet.attr("opacity", 1);

                    //Debug
                    console.log(
                        'l 235 resetSet \n',
                        'BoxSet is ',
                        BoxSet
                    )

                    //Remake drag for rect ellipse...
                    BoxSet.drag(
                        BoxSet.Box.dragBoxSetMove,
                        BoxSet.Box.dragBoxSetStart,
                        BoxSet.Box.dragBoxSetStop
                    )
                    BoxSet.Box.ox=ox
                    BoxSet.Box.oy=oy
                    BoxSet.Box.dragBoxSetStart()
                    BoxSet.Box.dragBoxSetMove(0,0)
                    BoxSet.Box.dragBoxSetStop()

                    //exclude
                    LocalSelection.set.exclude(BoxSet)

                }

                //remove the rectangle of selection
                LocalSelection.rect.remove();

                //empty selections and reset opacity;
                //LocalSelection.ox=ox
                //LocalSelection.oy=oy
            }

            LocalSelection.dragRectStop = function (_Event) {

                //get the RectBounds of the selections
                var RectBounds = LocalSelection.rect.getBBox();

                //Debug
                /*
                console.log(
                'l 144 dragSelectionStop before reset \n',
                'SelectionSet is \n',
                SelectionSet
                )
                */

                //
                LocalSelection.resetSet()
                    
                console.log(
                    'dragRectStop l 100\n',
                    'RectBounds is \n :',
                    RectBounds,
                    '\n',
                    'PatchRaphael.BoxSetsSet is :\n',
                    PatchRaphael.BoxSetsSet,
                    '\n',
                    'PatchRaphael.InstancesDict is : \n',
                    PatchRaphael.InstancesDict
                );

                //for
                //for (var __KeyStr in PatchRaphael.BoxSetsSet.items) {
                for (var __KeyStr in PatchRaphael.InstancesDict) {

                    //get
                    //var BoxSet=PatchRaphael.BoxSetsSet[__KeyStr]
                    var Instance=PatchRaphael.InstancesDict[__KeyStr]
                    var BoxSet=Instance.Box.set

                    // Here, we want to get the x,y vales of each object
                    // regardless of what sort of shape it is.
                    // But rect uses rx and ry, circle uses cx and cy, etc
                    // So we'll see if the bounding boxes intercept instead
                    BoxSet.MyBounds=BoxSet.Box.AnchorRect.getBBox()
                    //Instance.MyBounds=BoxSet.Box.AnchorRect.Bbox

                    //Debug
                    console.log(
                        'l 327 dragRectStop \n',
                        'Instance.data._id is \n',
                        Instance.data._id,
                        '\n',
                        '__KeyStr is ',
                        __KeyStr,
                        '\n',
                        'BoxSet.Box is ',
                        BoxSet.Box,
                        '\n',
                        'BoxSet.Box.AnchorRect is ',
                        BoxSet.Box.AnchorRect,
                        '\n',
                        'BoxSet is ',
                        BoxSet,
                        '\n',
                        'BoxSet.Box.AnchorRect.getBBox() is ',
                        BoxSet.Box.AnchorRect.getBBox(),
                        '\n',
                        'BoxSet.Box.AnchorRect.BBox is ',
                        BoxSet.Box.AnchorRect.BBox,
                        '\n',
                        'BoxSet.MyBounds is \n',
                        BoxSet.MyBounds,
                        '\n',
                        'LocalSelection.rect is ',
                        LocalSelection.rect,
                        '\n',
                        'RectBounds is \n',
                        RectBounds,
                        '\n'
                    )

                    //do bounding boxes overlap?
                    //is one of this object's x extremes between the selection's xe xtremes?
                    if (BoxSet.MyBounds.x >= RectBounds.x && BoxSet.MyBounds.x <= RectBounds.x2 || BoxSet.MyBounds.x2 >= RectBounds.x && BoxSet.MyBounds.x2 <= RectBounds.x2) {

                        //same for y
                        if (BoxSet.MyBounds.y >= RectBounds.y && BoxSet.MyBounds.y <= RectBounds.y2 || BoxSet.MyBounds.y2 >= RectBounds.y && BoxSet.MyBounds.y2 <= RectBounds.y2) 
                        {

                            //push
                            LocalSelection.set.push(BoxSet);     

                            //drag
                            BoxSet.undrag()

                            //set
                            BoxSet.attr("opacity", 0.5);
                        }
                    }

                    //enable the drag
                    LocalSelection.set.drag(
                        LocalSelection.dragSetMove,
                        LocalSelection.dragSetStart,
                        LocalSelection.dragSetStop
                    )
                }

            }

            //Debug
            /*
            console.log(
                'l155 SelectionProto',
                'End of the SelectionProto definition'
                )
            */

        } 


        //set that will receive the selected items
        PatchSelection=new SelectionProto()

        //init
        var BackRect = PatchRaphael.rect(
                        0, 0, PatchRaphael.width, PatchRaphael.height
                      ).attr(
                        "fill", "#FFF"
                      );
        BackRect.drag(
                PatchSelection.dragRectMove, 
                PatchSelection.dragRectStart, 
                PatchSelection.dragRectStop
            );
    }
)

