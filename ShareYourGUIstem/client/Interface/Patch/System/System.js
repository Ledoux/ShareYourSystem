/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

System defines the svg support for displaying a collection dict instance coming
from a Python call.

*/

SystemAbstraction= new AbstractionClass(
	{
		'ParentTemplateStr':"Patch",
	    'TemplateStr':'System',
	    'CollectionStr':'systems',
	    'ChildHelpersObject':
	    {
	      'boxes':function()
	       {

	       		//Define
	       		var Find=Boxes.find(
	       			{'ParentNameStr':this.NameStr}
	       		)

	       		//Debug
	       		/*
	       		console.log(
	       			'System boxes helpers l 24 \n',
	       			'this.SystemStr is \n',
	       			this.SystemStr,
	       			'\n',
	       			'Find.fetch() is \n',
	       			Find.fetch()
	       		)
				*/

	            //return
	            return Find

	       }
	    }
	}
)

Template.System.created = function()
{	
	//Debug
	/*
	console.log(
			'System created l 17'
		)
	*/

	//init
	/*
	var LocalInstance=new InstanceClass(
	  {
	    'Blaze':this,
	    'Abstraction':SystemAbstraction
	  }
	)
	*/
}

Template.System.helpers(
	SystemAbstraction.ChildHelpersObject
)