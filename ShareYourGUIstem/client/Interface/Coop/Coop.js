/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Coop defines the svg support for displaying a collection dict instance coming
from a Python call.

*/

CoopAbstraction=new AbstractionClass(
   {
	    'ParentTemplateStr':"Box",
	    'TemplateStr':'Coop',
	    'DefaultObject':{
	        'x':200,
	        'y':200
	    },
	    'ChildHelpersObject':
	    {
	      'ghosts':function()
	       {

	            //return
	            return Ghosts.find(
	                {
	                    'ParentCoopStr':this.CoopStr
	                }
	           )
	       }
	    }
	}
)

Template.Coop.created = function()
{
    //Debug
    /*
    console.log(
            'Box created l 17'
        )
    */

    //init
    var LocalData=new DataClass(
      {
        'Blaze':this,
        'Abstraction':CoopAbstraction
      }
    )

    //datafy
    LocalData.datafy()
}

Template.Coop.helpers(
    CoopAbstraction.ChildHelpersObject
)

