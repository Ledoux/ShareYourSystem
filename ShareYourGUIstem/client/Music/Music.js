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
    		/*
			console.log(
				'Template Music helpers l 25 \n',
				'Session.get("ScaleConditionsDictObject") is \n',
				Session.get('ScaleConditionsDictObject')
			)
			*/

			//find
			var Find=Scales.find(
				Session.get('ScaleConditionsDictObject')
			)

			//fetch
			var FindFetch=Find.fetch()

			//map
			_.map(
				_.range(_.size(FindFetch)),
				function(__Int)
				{
					Scales.update(
						{_id:FindFetch[__Int]._id},
						{$set:{'ScaleCountInt':__Int}}
					)
				}
			)

			//Debug
			/*
			console.log(
				'Template Music helpers l 53 \n',
				'Find.fetch() is \n',
				Find.fetch()
			)
			*/

			//return
			return Find
    	},
    	'patterns':function()
    	{
    		//Debug
    		/*
			console.log(
				'Template Music helpers l 66 \n',
				'Session.get("VoiceConditionsDictObject") is \n',
				Session.get('VoiceConditionsDictObject')
			)
			*/

			//find
			var Find=Patterns.find(
				Session.get('PatternConditionsDictObject')
			)

			//fetch
			var FindFetch=Find.fetch()

			//map
			_.map(
				_.range(_.size(FindFetch)),
				function(__Int)
				{
					Patterns.update(
						{_id:FindFetch[__Int]._id},
						{$set:{'PatternCountInt':__Int}}
					)
				}
			)

			//Debug
			/*
			console.log(
				'Template Music helpers l 96 \n',
				'Find.fetch() is \n',
				Find.fetch()
			)
			*/

			//return
			return Find
    	},
    	'voices':function()
    	{
    		//Debug
    		/*
			console.log(
				'Template Music helpers l 66 \n',
				'Session.get("VoiceConditionsDictObject") is \n',
				Session.get('VoiceConditionsDictObject')
			)
			*/

			//find
			var Find=Voices.find(
				Session.get('VoiceConditionsDictObject')
			)

			//fetch
			var FindFetch=Find.fetch()

			//map
			_.map(
				_.range(_.size(FindFetch)),
				function(__Int)
				{
					Voices.update(
						{_id:FindFetch[__Int]._id},
						{$set:{'VoiceCountInt':__Int}}
					)
				}
			)

			//Debug
			/*
			console.log(
				'Template Music helpers l 96 \n',
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

Session.set(
	'ScaleConditionsDictObject',
	{
		'NotesInt':7,
		'JimScaleBool':true,
		'NameStr':"Ionien"
	}
)

Session.set(
	'VoiceConditionsDictObject',
	{
	}
)

Session.set(
	'PatternConditionsDictObject',
	{
		'PatternCursorIntsArray':[1,0]
	}
)

Template.Music.helpers(
    MusicAbstraction.ChildHelpersObject
)
