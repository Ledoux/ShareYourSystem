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
					_.range(_.size(ScaleIntsArraysArray)),
					function(__IndexInt)
					{
						//define
						var ScaleIntsArray=ScaleIntsArraysArray[__IndexInt]

						//return
						return [
							ScaleIntsArray.toString(),
							{
								'KeyStr':ScaleIntsArray.join('').toString(),
								'IndexInt':__IndexInt,
								'NameStr':"Unnamed",
								'NotesInt':__NotesInt,
								'PoolIntsArray':ScaleIntsArray,
								'NoteSharpStrsArray':_.map(
										ScaleIntsArray,
										function(__ScaleInt)
										{
											return NoteSharpStrsArray[__ScaleInt]
										}
									),
								'NoteFlatStrsArray':_.map(
										ScaleIntsArray,
										function(__ScaleInt)
										{
											return NoteFlatStrsArray[__ScaleInt]
										}
									),
								'IntervalIntsArray':
								_.map(
										_.range(_.size(ScaleIntsArray)),
										function(__IndexInt)
										{
											if(__IndexInt<(_.size(ScaleIntsArray)-1))
											{
												return ScaleIntsArray[__IndexInt+1]-ScaleIntsArray[__IndexInt]
											}
											else{
												return 12-ScaleIntsArray[__IndexInt]
											}

										}
									),
								'MinorThirdBool':_.contains(ScaleIntsArray,3),
								'MajorThirdBool':_.contains(ScaleIntsArray,4),
								'MinorSevenBool':_.contains(ScaleIntsArray,10),
								'MajorSevenBool':_.contains(ScaleIntsArray,11),
								'PerfectFifthBool':_.contains(ScaleIntsArray,7),
								'DimFifthBool':_.contains(ScaleIntsArray,6),
							}
						]
					}
				)
			)
			//console.log(ScalesDictObject)

			_.map(
				ScalesDictObject,
				function(__ValueObject,__KeyStr)
				{
					_.extend(
						__ValueObject,
						{
							//distance compute
							'DistanceIntsArray':_.map(
										_.range(_.size(__ValueObject['IntervalIntsArray'])),
										function(__IndexInt)
										{
											if(__IndexInt<(_.size(__ValueObject[
												'IntervalIntsArray'])-1))
											{
												return __ValueObject['IntervalIntsArray'
												][__IndexInt+1]+__ValueObject['IntervalIntsArray'][
												__IndexInt]
											}
											else{
												return __ValueObject['IntervalIntsArray'][
												__IndexInt]+__ValueObject['IntervalIntsArray'][
												0]
											}

										}
									),

							//classic tetrade test
							'Major7Bool': __ValueObject['MajorThirdBool'] && __ValueObject['MajorSevenBool'
							] && __ValueObject['MinorThirdBool']==false && __ValueObject['MinorSevenBool']==false,
							'Minor7Bool':__ValueObject['MinorThirdBool'] && __ValueObject['MinorSevenBool'
							] && __ValueObject['MajorThirdBool']==false && __ValueObject['MajorSevenBool']==false,
							'Dominant7Bool': __ValueObject['MajorThirdBool'] && __ValueObject['MinorSevenBool'
							] && __ValueObject['MinorThirdBool']==false && __ValueObject['MajorSevenBool']==false,
							'MinMaj7Bool': __ValueObject['MinorThirdBool'] && __ValueObject['MajorSevenBool'
							] && __ValueObject['MajorThirdBool']==false && __ValueObject['MinorSevenBool']==false

						}
					)
				}
			)

			//map
			_.map(
					ScalesDictObject,
					function(__ValueObject,__KeyStr)
					{
						//define
						var PoolIntsArray=__ValueObject['PoolIntsArray']

						//extend
						_.extend(
							__ValueObject,
							{
		
								//classic mode test
								'Ionien7Bool':__ValueObject['PerfectFifthBool'] && __ValueObject['DimFifthBool']==false && __ValueObject['Major7Bool'
								] && _.contains(PoolIntsArray,2) && _.contains(PoolIntsArray,9),
								'Dorien7Bool':__ValueObject['PerfectFifthBool'] && __ValueObject['DimFifthBool']==false && __ValueObject['Minor7Bool'
								] && _.contains(PoolIntsArray,2) && _.contains(PoolIntsArray,9),
								'Phrygian7Bool':__ValueObject['PerfectFifthBool'] && __ValueObject['DimFifthBool']==false && __ValueObject['Minor7Bool'
								] && _.contains(PoolIntsArray,1) && _.contains(PoolIntsArray,8),
								'Lydian7Bool':__ValueObject['PerfectFifthBool'] && __ValueObject['DimFifthBool'] && __ValueObject['Major7Bool'
								] && _.contains(PoolIntsArray,2) && _.contains(PoolIntsArray,9),
								'Mixolydian7Bool':__ValueObject['PerfectFifthBool'] && __ValueObject['DimFifthBool']==false && __ValueObject['Dominant7Bool'
								] && _.contains(PoolIntsArray,2) && _.contains(PoolIntsArray,9),
								'Eolien7Bool':__ValueObject['PerfectFifthBool'] && __ValueObject['DimFifthBool']==false && __ValueObject['Minor7Bool'
								] && _.contains(PoolIntsArray,2) && _.contains(PoolIntsArray,8),
								'Locrien7Bool':__ValueObject['DimFifthBool'] && __ValueObject['PerfectFifthBool']==false && __ValueObject['Minor7Bool'
								] && _.contains(PoolIntsArray,1) && _.contains(PoolIntsArray,8)
							}
						)
	
					//name
					_.map(
						//['Major7Bool','Minor7Bool'],
						['Ionien7Bool','Dorien7Bool','Phrygian7Bool','Lydian7Bool','Mixolydian7Bool','Eolien7Bool','Locrien7Bool'],
						function(__BoolKeyStr)
						{
							if(__ValueObject[__BoolKeyStr])
							{
								__ValueObject['NameStr']=__BoolKeyStr.replace('Bool','')
							}
						}
					)

					//Jim or Barack scale test
					__ValueObject['JimScaleBool']=_.contains(
							__ValueObject['DistanceIntsArray'],2
						)==false
	
					}
				)
					
	
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


