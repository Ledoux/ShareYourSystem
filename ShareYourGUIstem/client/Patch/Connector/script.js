//Build collection
var Connectors = new Meteor.Collection(null);//client side only

//helpers for connectors are reactive, so any changes to Boxes redraws connectors also
Template.Connector.helpers({
    "sourceX":function(){
        var Box = Boxes.findOne({_id:this.SourceId});
        if(Box){
            return Box.x;
        }
    },
    "sourceY":function(){
        var Box = Boxes.findOne({_id:this.SourceId});
        if(Box){
            return Box.y;
        }
    },
    "targetX":function(){
        var Box = Boxes.findOne({_id:this.TargetId});
        if(Box){
            return Box.x;
        }
    },
    "targetY":function(){
        var Box = Boxes.findOne({_id:this.TargetId});
        if(Box){
            return Box.y;
        }
    }
});

//Link
Meteor.Connectors=Connectors
