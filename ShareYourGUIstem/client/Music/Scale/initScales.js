/*

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

subscribe

*/


NoteSharpStrsArray=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
NoteFlatStrsArray=["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]

initScales=function()
{

	//remove
	Meteor.call('mongo','scales','remove',{})

	//map	
	_.map(
		[3,4,5,6,7,8],
		function(__NotesInt){

			//pool
			var PoolIndexStrsArraysArray=pool(12,__NotesInt)
			//console.log(PoolIndexStrsArraysArray)

			//filter
			var ScaleIntsArraysArray=_.filter(
				PoolIndexStrsArraysArray,
				function(__PoolIndexStrsArray)
				{
					return __PoolIndexStrsArray[0]==0
				}
			)
			//console.log(ScaleIntsArraysArray)

			//object
			var ScalesDictObject=_.object(
				_.map(
					ScaleIntsArraysArray,
					function(__ScaleIntsArray)
					{
						return [
							__ScaleIntsArray.toString(),
							{
								'NotesInt':__NotesInt,
								'PoolIntsArray':__ScaleIntsArray,
								'NoteSharpsArray':_.map(
										__ScaleIntsArray,
										function(__ScaleInt)
										{
											return NoteSharpStrsArray[__ScaleInt]
										}
									),
								'NoteFlatsArray':_.map(
										__ScaleIntsArray,
										function(__ScaleInt)
										{
											return NoteFlatStrsArray[__ScaleInt]
										}
									)
							}
						]
					}
				)
			)
			//console.log(ScalesDictObject)

			
			//map inserts
			_.map(
				ScalesDictObject,
				function(__ScaleObject)
				{
					Meteor.call(
						'mongo',
						'scales',
						'insert',
						__ScaleObject
					)
				}
			)
		}
	)

}


