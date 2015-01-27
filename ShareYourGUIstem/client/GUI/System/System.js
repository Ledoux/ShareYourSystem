/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

System defines the svg support for displaying a collection dict instance coming
from a Python call.

*/

Template.System.created = function()
{
	/*
	//Debug
	console.log(
			'System created l 17'
		)
	*/

	//Define
	var LocalSystemBlaze=this

	//Debug
	/*
	console.log(
			'System created l 17'
		)
	*/

	//init
	init(
			this,
			{
				'ParentTemplateStr':"Patch",
				'TemplateStr':'System',
				'ChildCollectionStrsArray':['boxes'],
				'DefaultObject':{  
                            }
			}
		)
}

Template.System.rendered = function()
{
}

Template.System.destroyed = function()
{
}
