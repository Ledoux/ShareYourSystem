/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

subscribe

*/

initPatterns=function()
{

	//remove
	Meteor.call('mongo','patterns','remove',{})

	//
	var PatternsDictObject={}

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
						'initPatterns l 45 \n',
						'RepeatArray is \n',
						RepeatArray
					)
					*/

					//cartesian product
					var PatternCursorIntsArraysArray=cartesianproduct(
						RepeatArray
					)

					//Debug
					console.log(
						'initPatterns l 45 \n',
						'PatternCursorIntsArraysArray is \n',
						PatternCursorIntsArraysArray
					)

					//set
					_.map(
							PatternCursorIntsArraysArray,
							function(__PatternCursorIntsArray)
							{
								PatternsDictObject[__PatternCursorIntsArray.join('').toString()]={
									'PatternCursorIntsArray':__PatternCursorIntsArray
								}
							}
						)
					
				}
			)
		}
	)

	//map inserts
	_.map(
		PatternsDictObject,
		function(__PatternObject)
		{
			Meteor.call(
				'mongo',
				'patterns',
				'insert',
				__PatternObject
			)
		}
	)


}


