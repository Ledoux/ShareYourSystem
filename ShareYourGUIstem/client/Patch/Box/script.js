
//drag function
var BoxDrag = d3.behavior.drag(
    ).on(
        "drag", 
        function(d)
        {
            var id = $(this).data("id");
            if(id && d3.event.dx !== 0 || d3.event.dy !== 0){
                var incObject = {};
                if(d3.event.dx !== 0)//did it move in x direction?
                    incObject.x = d3.event.dx;

                if(d3.event.dy !== 0)//did it move in y direction?
                    incObject.y = d3.event.dy;

                if(incObject.x || incObject.y)//if moved x or y
                    Boxes.update({_id:id},{$inc:incObject});
                    //use increment to save the delta of position, positive or negative
                    //save the new position to the collection, triggering a dom update by blaze/meteor
            }
        }
    );

dragBoxStart = function(_x,_y){

    //get the raph box
    //Box=$("#Box_"+this.data._id)

    //Debug
    /*
    console.log(
        'dragBoxStart l 31 \n',
        'this is : \n',
        this,
        'this.ParentBox is : \n',
        this.ParentBox,
        'this.ParentBox.data.x0 is : \n',
        this.ParentBox.data.x0,
        '\n',
        'this.ParentBox.data.y0 is : \n',
        this.ParentBox.data.y0,
        '\n',
        '_x is : \n',
        _x,
        '\n',
        '_y is : \n',
        _y
    )   
    */

    //RaphRect=Box.RaphRect
    this.ox=this.ParentBox.data.x0
    this.oy=this.ParentBox.data.y0

}
dragBoxMove=function(_dx,_dy)
{


    //Debug
    console.log(
        'dragBoxMove l 45 \n',
        'this is : \n',
        this,
        'this.ox is : \n',
        this.ox
    )

    //
    var x=this.ox + _dx
    var y=this.oy + _dy

    //Move ... 
    this.attr({ x:x , y:y });

    //better to not update directly the boxes to not overload the db queries
    //Boxes.update(
    //    {_id:this.ParentBox.data._id},
    //    {$set:{x0:x,y0:y}}
    //)
    
}
dragBoxStop=function(){

    //Debug
    /*
    console.log(
        'dragEnd l 57 \n',
        'this.attr("x") is : \n',
        this.attr("x"),
    )
    */

    //
    var x=this.attr('x')
    var y=this.attr('y')

    //set in the box
    this.ParentBox.data.x0=x
    this.ParentBox.data.y0=y

    //delete
    delete(this.ox)
    delete(this.oy)

    //Debug
    /*
    console.log(
        'dragEnd l 100 \n',
        'x is ',
        x,
        'y is ',
        y
    )
    */

    //better to not update directly the boxes to not overload the db queries
    Boxes.update(
        {_id:this.ParentBox.data._id},
        {$set:{x0:x,y0:y}}
    )
}



Template.Box.rendered = function ( ) {

    //d3.select("#Box_"+this.data._id).call(BoxDrag);
    //attach drag handler

    //Debug
    /*
    console.log(
        'Box rendered l 57\n',
        'this.data is : \n',
        this.data
    )
    */

    //init position
    if (this.data.x0 === undefined || this.data.x0 === null) {
        this.data.x0=200
    }
    if (this.data.y0 === undefined || this.data.y0 === null) {
        this.data.y0=100
    }
    
    //Debug
    /*
    console.log(
        'Box rendered l 67\n',
        'PatchRaphael is : \n',
        PatchRaphael
        //'dragBoxStart is : \n',
        //dragBoxStart
    )
    */

    //
    Rect=PatchRaphael.rect(
            this.data.x0,
            this.data.y0,
            20,
            20
        ).attr('fill', 'green')
    

    //link with the parent box
    Rect.ParentBox=this

    //Make it drag
    Rect.drag(dragBoxMove,dragBoxStart,dragBoxStop)

    //add in the dict
    RaphObjectsDict[Rect.ParentBox.data._id]=Rect
    GlobalSet.push(Rect)

    /*
    //init a Raphael rect
    var Set=PatchRaphael.set()
    Set.push(
        //PatchRaphael.circle(this.data.x0,this.data.y0, 10).attr('fill', 'red')

        PatchRaphael.rect(
            this.data.x0,
            this.data.y0,
            20,
            20
        ).attr('fill', 'red')
    )
    //link parent box
    Set.ParentBox=this
    //Make them drag
    Set.draggable()
    //Debug
    console.log(
        'Box rendered l 87\n',
        'Set is : \n',
        Set
    )
    */
    
};

