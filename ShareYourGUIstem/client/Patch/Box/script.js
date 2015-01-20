//Build collections


//drag function
var BoxDrag = d3.behavior.drag().on("drag", function(d) {
    var id = $(this).data("id");
    if(id && d3.event.dx !== 0 || d3.event.dy !== 0){
        var incObject = {};
        if(d3.event.dx !== 0)//did it move in x direction?
            incObject.x = d3.event.dx;

        if(d3.event.dy !== 0)//did it move in y direction?
            incObject.y = d3.event.dy;

        if(incObject.x || incObject.y)//if moved x or y
            Boxes.update({_id:id},{$inc:incObject});//use increment to save the delta of position, positive or negative
            //save the new position to the collection, triggering a dom update by blaze/meteor
    }
});

Template.Box.rendered = function ( ) {
    d3.select("#Box_"+this.data._id).call(BoxDrag);
    //attach drag handler
};

