/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Ghost defines an empty collection that is the last child to climb again 
the childify methods along ParentBlaze

*/

GhostAbstraction=new AbstractionClass(
   {
	    'ParentTemplateStr':"Coop",
	    'TemplateStr':'Ghost',
        'CollectionStr':'ghosts',
	}
)

Template.Ghost.created = function()
{
	//Debug
    /*
    console.log(
            'Ghost created l 29'
        )
    */
    
    //init
    /*
    var LocalInstance=new InstanceClass(
      {
        'Blaze':this,
        'Abstraction':GhostAbstraction
      }
    )
    */
}
