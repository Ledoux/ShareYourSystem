/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Ghost defines an empty collection that is the last child to climb again 
the childify methods along ParentBlaze

*/

Template.Ghost.created = function()
{
	//Debug
	console.log(
			'Ghost created l 17'
		)

	//Define
	var LocalGhostBlaze=this

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
				'ParentTemplateStr':"Coop",
				'TemplateStr':'Ghost',
				'ChildCollectionStrsArray':[],
				'DefaultObject':{  
                            }
			}
		)

}

Template.Ghost.helpers(
)

Template.Ghost.rendered = function()
{
}

Template.Ghost.destroyed = function()
{
}
