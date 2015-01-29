/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Selection defines the option to select several instances
to make it drag together

*/

//define
SelectionClass = function() {

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

    //Debug
    /*
    console.log(
        'LocalSelection l 39',
        'LocalSelection.set is',
        LocalSelection.set
    )
    */

    LocalSelection.dragSelectionSetStart = function() {

        //Debug
        /*
        console.log(
                'l 188 dragSelectionSetStart \n',
                'LocalSelection.set is \n',
                LocalSelection.set,
                '\n'
            )
        */

        //map
        LocalSelection.set.items.map(
                function(__StickerSet){

                    //Debug
                    /*
                    console.log(
                        'dragSelectionSetStart l 64',
                        '\n'
                    )
                    */

                    //set
                    __StickerSet.Sticker.dragStickerSetStart()
                }
            )

    }

    LocalSelection.dragSelectionSetMove = function(_dx,_dy) {

        //Debug
        /*
        console.log(
                'l 87 dragSelectionSetMove \n',
                '\n',
                '_dx is : \n',
                _dx,
                '\n',
                '_dy is : \n',
                _dy
            )
        */

        //map
        LocalSelection.set.items.map(
                function(__StickerSet){

                    //Debug
                    /*
                    console.log(
                        'dragSelectionSetMove l 105',
                        '__StickerSet.ox is \n',
                        __StickerSet.ox,
                        '\n',
                        '__StickerSet.oy is \n',
                        __StickerSet.oy,
                        '\n'
                    )
                    */

                    //set
                    __StickerSet.Sticker.dragStickerSetMove(_dx,_dy)
                }

            )

    }

    LocalSelection.dragSelectionSetStop = function() {

        //Debug
        /*
        console.log(
                'l 264 dragSelectionSetStop \n',
            )
        */

        //map
        LocalSelection.set.items.map(
                function(__StickerSet){

                    //Debug
                    /*
                    console.log(
                        'dragSelectionSetStrop l 138',
                        '\n'
                    )
                    */

                    //set
                    __StickerSet.Sticker.dragStickerSetStop()
                }

            )

    }

    //when mouse goes down over background, start drawing selection box
    LocalSelection.dragSelectionRectStart = function(_x, _y, _Event) {

        //Debug
        /*
        console.log(
            'l 178 dragSelectionRectStart \n',
            '_x is : \n',
            _x,
            '\n',
            '_y is : \n',
            _y,
            '\n',
           ' _x-PatchSvgOffset.left is : \n',
            _x-PatchSvgOffset.left,
            '\n',
            '_y-PatchSvgOffset.top is : \n',
            _y-PatchSvgOffset.top,
            '\n'
        )
        */

        //init
        LocalSelection.rect=PatchRaphael.rect(
                      _x-PatchSvgOffset.left, 
                      _y-PatchSvgOffset.top, 5, 5
                    ).attr(
                      "stroke", "#9999FF"
                    ); 

        //for
        LocalSelection.set.items.map(
                function(__StickerSet)
                {
                    __StickerSet.attr("opacity", 1)
                }
            )
    }

    // When mouse moves during drag, adjust box.
    // If the drag is to the left or above original point,
    // you have to translate the whole box and invert the dx 
    // or dy values since .rect() doesn't take negative width or height
    LocalSelection.dragSelectionRectMove = function (_dx, _dy, _x, _y, _Event) {

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

    LocalSelection.resetSelectionSet = function(){

        //undrag
        LocalSelection.set.undrag()

        //Debug
        /*
        console.log(
            'resetSet l 229 \n',
            'LocalSelection.set.items is \n',
            LocalSelection.set.items
        )
        */
        
        //map remake them drag
        LocalSelection.set.items.map(
                function(__StickerSet)
                {

                    //change opacity
                    __StickerSet.attr("opacity", 1);

                    //make it drag
                    __StickerSet.drag(
                        __StickerSet.Sticker.dragStickerSetMove,
                        __StickerSet.Sticker.dragStickerSetStart,
                        __StickerSet.Sticker.dragStickerSetStop
                    )

                    //exclude
                    LocalSelection.set.exclude(__StickerSet)
                }
            )

        //remove the rectangle of selection
        LocalSelection.rect.remove();

    }

    LocalSelection.dragSelectionRectStop = function (_Event) {

        //get the SelectionRectBounds of the selections
        var SelectionRectBounds = LocalSelection.rect.getBBox();

        //Debug
        /*
        console.log(
            'l 267 dragSelectionStop before reset \n',
            'SelectionRectBounds is \n',
            SelectionRectBounds
        )
        */
        
        //reset
        LocalSelection.resetSelectionSet()
        
        //Debug
        /*
        console.log(
            'dragRectStop l 100\n',
            'SelectionRectBounds is \n :',
            SelectionRectBounds,
            '\n',
            'StickerSetsSet is :\n',
            StickerSetsSet,
            '\n',
            'PatchRaphael.StickeresDict is : \n',
            PatchRaphael.StickeresDict
        );
        */

        StickerSetsSet.items.map(
                function(__StickerSet)
                {
                    //get the BBox
                    __StickerSet.MyBounds=__StickerSet.Sticker.AnchorRect.getBBox()

                    //do bounding boxes overlap?
                    //is one of this object's x extremes between the selection's xe xtremes?
                    if (
                        __StickerSet.MyBounds.x >= SelectionRectBounds.x && __StickerSet.MyBounds.x <= SelectionRectBounds.x2 || __StickerSet.MyBounds.x2 >= SelectionRectBounds.x && __StickerSet.MyBounds.x2 <= SelectionRectBounds.x2) 
                        {

                            //same for y
                            if (__StickerSet.MyBounds.y >= SelectionRectBounds.y && __StickerSet.MyBounds.y <= SelectionRectBounds.y2 || __StickerSet.MyBounds.y2 >= SelectionRectBounds.y && __StickerSet.MyBounds.y2 <= SelectionRectBounds.y2) 
                            {

                                //push
                                LocalSelection.set.push(__StickerSet);     

                                //drag
                                __StickerSet.undrag()

                                //set
                                __StickerSet.attr("opacity", 0.5);
                            }
                    }
                }
            )

        //enable the drag
        LocalSelection.set.drag(
            LocalSelection.dragSelectionSetMove,
            LocalSelection.dragSelectionSetStart,
            LocalSelection.dragSelectionSetStop
        )
    }
}

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
        StickerSetsSet=PatchRaphael.set()

        //set that will receive the selected items
        PatchSelection=new SelectionClass()

        //init
        var BackRect = PatchRaphael.rect(
                        0, 0, PatchRaphael.width, PatchRaphael.height
                      ).attr(
                        "fill", "#FDFDFD"
                      );
        BackRect.drag(
                PatchSelection.dragSelectionRectMove, 
                PatchSelection.dragSelectionRectStart, 
                PatchSelection.dragSelectionRectStop
            );
    }
)

