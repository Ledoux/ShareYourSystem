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
	/*
	console.log(
		'Coop created l 17'
	)
	*/

	//Define
	var LocalCoopBlaze=this

	//init
	init(
	   	this,
	    {
	        'ParentTemplateStr':"Box",
	        'TemplateStr':'Coop',
	        'ChildCollectionStrsArray':['ghosts'],
	        'DefaultObject':{
	                        'x0':200,
	                        'y0':220    
	                    }
	    }
	)

	//Debug
	console.log(
		'Coop created l 38 \n',
		'LocalCoopBlaze.ParentBlaze.ChildBlazesArraysObject is \n',
		LocalCoopBlaze.ParentBlaze.ChildBlazesArraysObject,
		'LocalCoopBlaze.ParentBlaze.ChildBlazesArraysObject["coops"] is \n',
		LocalCoopBlaze.ParentBlaze.ChildBlazesArraysObject['coops']
	)

	//get the index
	LocalCoopBlaze.ParentInt=_.size(
		LocalCoopBlaze.ParentBlaze.data.CoopStrsObject
	)

	//Debug
	/*
	console.log(
		'Coop created l 50 \n',
		'LocalCoopBlaze.ParentInt is \n',
		LocalCoopBlaze.ParentInt
	)
	*/

	//push
	//LocalCoopBlaze.ParentBlaze.data.CoopStrsArray.push(
	//	LocalCoopBlaze.data.CoopStr
	//)
	/*
	LocalCoopBlaze.ParentCollection.update(
		{
			_id:LocalCoopBlaze.ParentBlaze.data._id
		},
		{
			$set:
			{
				'CoopStrsObject.0':LocalCoopBlaze.data.CoopStr
			}
		}
	)
	*/

	//put in the 
	/*
	console.log(
		'Coop created l 38',
		'LocalCoopBlaze.ParentBlaze.BoxStr is \n',
		LocalCoopBlaze.ParentBlaze.BoxStr,
		//'LocalCoopBlaze.ParentBlaze.data.CoopStrsArray is \n',
		//LocalCoopBlaze.ParentBlaze.data.CoopStrsArray
		'LocalCoopBlaze.ParentBlaze.data.CoopStrsObject is \n',
		LocalCoopBlaze.ParentBlaze.data.CoopStrsObject
	)
	*/
}

Template.Coop.rendered = function()
{

	//Define
	var LocalCoopBlaze=this

	//Debug
	/*
	console.log(
		'Coop rendered l 107'
	)
	*/

}

Template.Coop.destroyed = function()
{
}
