var addVexflowContext=function(Event,Template)
{
	//var svg = $("svg#Staves")[0];
	console.log(Template)
	//var renderer = new Vex.Flow.Renderer(
		//svg,
		//Vex.Flow.Renderer.Backends.RAPHAEL
	//);
	//Template.ctx = renderer.getContext();

}


Template.Score.helpers(
{
	'staves': function(){
		return []
		//return Staves.find()
	}
})

Template.Score.events(
{
	'click #AddContext':function(event,tmpl)
	{
		addVexflowContext(Event,Template)
	}
})





