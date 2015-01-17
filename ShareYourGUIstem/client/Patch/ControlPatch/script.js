

//Define helpers
Template.ControlPatch.helpers(
	{
		
	}
)

Template.ControlPatch.events({
    'click #AddInstance': function () {
        Boxes.insert({
            x:200,
            y:150
        });
    }
});