var Svg=function()
{
	this.SvgCenterXFloat=0.
	this.SvgCenterYFloat=0.
}

var Stave=function()
{
	Svg.apply(this,arguments)
}



/*
var StavesCollection=new Meteor.Collection(null)

Template.Stave.helpers(
{
	'lines': function(){
		return Lines.find()
	}
})
*/

MySvg=new Svg()
console.log(MySvg)
MyStave=new Stave()
console.log(MyStave)



