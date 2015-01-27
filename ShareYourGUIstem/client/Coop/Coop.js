/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Coop defines the svg support for displaying a collection dict instance coming
from a Python call.

*/

Template.Coop.created = function()
{
	//Debug
	console.log(
			'Coop created l 17'
		)

	//Define
	var LocalCoopBlaze=this

	//Get
	LocalCoopBlaze.Box=Boxes.findOne({BoxStr:LocalCoopBlaze.data.BoxStr})

	//Debug
	console.log(
			'Coop created l 17',
			'LocalCoopBlaze.Box is \n',
			LocalCoopBlaze.Box
		)

}
Template.Coop.helpers(
)
Template.Coop.rendered = function()
{
}

Template.Coop.destroyed = function()
{
}
