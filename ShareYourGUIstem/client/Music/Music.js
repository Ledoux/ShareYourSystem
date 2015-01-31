/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Interface client

*/

MusicAbstraction=new AbstractionClass(
  {
    'TemplateStr':'Music',
    'CollectionStr':"musics",
    'DefaultInstanceObject':{},
    'ChildHelpersObject':
    {
    	'scales':function()
    	{
    		//Debug
			console.log(
				'Template Patch helpers l 25 \n',
				'Session.get("ScaleConditionsDictObject") is \n',
				Session.get('ScaleConditionsDictObject')
			)

			//find
			var Find=Scales.find(
			Session.get('ScaleConditionsDictObject')
			)

			//Debug
			console.log(
				'Template Patch helpers l 45 \n',
				'Find.fetch() is \n',
				Find.fetch()
			)

			//return
			return Find
    	}
    }
  }
)


Session.set(
	'ScaleConditionsDictObject',
	{
		'NotesInt':7
	}
)

Template.Music.helpers(
    MusicAbstraction.ChildHelpersObject
)
