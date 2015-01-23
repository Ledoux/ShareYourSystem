
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

var destroyPatch = function(){
    Connectors.find({}).forEach(function(_Connector){
        Connectors.remove({_id:_Connector._id});
    });
    Boxes.find({}).forEach(function(_Box){
        Boxes.remove({_id:_Box._id});
    });
};

Template.Patch.helpers({
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



