/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

subscribe

*/


initProgressions=function()
{

	//remove
	Meteor.call('mongo','progressions','remove',{})

	//init a join
	var ProgressionsJoin=new JoinClass(
			{
				'Abstraction':ProgressionAbstraction
			}
		)

	//join
	ProgressionsJoin.join(
		{
			'OrderArray':['*scales','*patterns*Note','*patterns*Rhythm'],
			'*scales':{
				'NotesInt':7,
				'ModeBool':true
			},
			'*patterns*Note':
			{
				'CursorsInt':2
			},
			'*patterns*Rhythm':
			{
				'CursorsInt':2
			}
		},
		{
			'KeyStr':1,
			//'scales':{
			//	'MajorThirdBool':1
			//}
		}
	)

	//insert
	ProgressionsJoin.insert()

	
}


test=function()
{

	/*
	//init a join
	var ProgressionsJoin=new JoinClass(
			{
				'Abstraction':ProgressionAbstraction
			}
		)

	var Find=ProgressionsJoin.find(
			{
				'OrderArray':['*scales','*patterns*Note','*patterns*Rhythm'],
				'*scales':{
					'NotesInt':7,
					'ModeBool':true,
					'Major7Bool':true
				},
				'*patterns*Note':
				{
					'CursorsInt':2
				},
				'*patterns*Rhythm':
				{
					'CursorsInt':2
				}
			}
		)

	console.log(Find.fetch())
	*/

	return Progressions.findJoin(
		{
			'OrderArray':['*scales','*patterns*Note','*patterns*Rhythm'],
			'*scales':{
				'NotesInt':7,
				'ModeBool':true,
				'Major7Bool':true
			},
			'*patterns*Note':
			{
				'CursorsInt':2
			},
			'*patterns*Rhythm':
			{
				'CursorsInt':2
			}
		}
	)



}




