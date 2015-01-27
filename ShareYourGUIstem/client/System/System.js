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

}

Template.System.helpers(
	{
		'boxes': function () 
	    {

	        //Debug
	        /*
	        console.log(
	          'Template Patch helpers l 21',
	          'this is \n',
	          this,
	          'Boxes found are \n',
	          Boxes.find(
	            	{
	                	SystemStr:this.SystemStr
	           		}
	        	).fetch()
	        )  
	        */
	        
	        //return
	        return Boxes.find(
	            	{
	                	SystemStr:this.SystemStr
	           		}
	        	)
	    }
	}
)

Template.System.rendered = function()
{
}

Template.System.destroyed = function()
{
}
