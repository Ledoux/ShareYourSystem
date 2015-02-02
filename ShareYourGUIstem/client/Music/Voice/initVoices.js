/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

subscribe

*/

initVoices=function()
{

	//remove
	Meteor.call('mongo','voices','remove',{})

	//
	var VoicesDictObject={}

	//map
	_.map(
		[1,2],
		function(__IntervalUnitsInt)
		{
			_.map(
				[3],
				function(__NotesInt)
				{

					//range
					var PoolIntsArray=_.range(__NotesInt)

					//map
					var RepeatArray=_.map(
										_.range(__IntervalUnitsInt),
										function()
										{
											return PoolIntsArray
										}
									)

					//Debug
					/*
					console.log(
						'initVoices l 45 \n',
						'RepeatArray is \n',
						RepeatArray
					)
					*/

					//cartesian product
					var VoiceCursorIntsArraysArray=cartesianproduct(
						RepeatArray
					)

					//Debug
					console.log(
						'initVoices l 45 \n',
						'VoiceCursorIntsArraysArray is \n',
						VoiceCursorIntsArraysArray
					)

					//set
					_.map(
							VoiceCursorIntsArraysArray,
							function(__VoiceCursorIntsArray)
							{
								VoicesDictObject[__VoiceCursorIntsArray.join('').toString()]={
									'VoiceCursorIntsArrays':__VoiceCursorIntsArray
								}
							}
						)
					
				}
			)
		}
	)

	//map inserts
	_.map(
		VoicesDictObject,
		function(__VoiceObject)
		{
			Meteor.call(
				'mongo',
				'voices',
				'insert',
				__VoiceObject
			)
		}
	)


}


