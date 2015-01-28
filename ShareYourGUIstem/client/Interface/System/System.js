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
	    'ChildHelpersObject':
	    {
	      'boxes':function()
	       {

	       		//Define
	       		var FindObject=Boxes.find(
	       			{'ParentSystemStr':this.SystemStr}
	       		)

	       		//Debug
	       		/*
	       		console.log(
	       			'System boxes helpers l 24 \n',
	       			'this.SystemStr is \n',
	       			this.SystemStr,
	       			'\n',
	       			'FindObject.fetch() is \n',
	       			FindObject.fetch()
	       		)
				*/

	            //return
	            return FindObject

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
	var LocalData=new DataClass(
	  {
	    'Blaze':this,
	    'Abstraction':SystemAbstraction
	  }
	)

	//datafy
	LocalData.datafy()
}

Template.System.helpers(
	SystemAbstraction.ChildHelpersObject
)