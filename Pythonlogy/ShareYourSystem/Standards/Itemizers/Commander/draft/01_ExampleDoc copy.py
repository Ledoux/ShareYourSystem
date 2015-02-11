
#ImportModules
import ShareYourSystem as SYS

#Definition a structure of Commanders.
MyFirstCommander=SYS.CommanderClass()
map(
		lambda __Int:
		MyFirstCommander.__setitem__
		(
			'<Commanders>'+str(__Int),
			SYS.CommanderClass()
		),
		xrange(2)
	)

MySecondCommander=SYS.CommanderClass()
map(
		lambda __Int:
		MySecondCommander.__setitem__
		(
			'<Commanders>'+str(__Int),
			SYS.CommanderClass()
		),
		xrange(2)
	)

#Definition an CommandingUpdateList to be commanded
CommandingUpdateList=[
	(
		'SpecificCountInt',
		';'.join([
					'Exec_self.SettingValueVariable=self.__class__.ShareCountInt',
					'self.__class__.ShareCountInt+=1'
				])
	),
	(
		'SpecificCountInt',
		';'.join([
					'Exec_self.SettingValueVariable=self.__class__.ShareCountInt',
					'self.__class__.ShareCountInt+=1'
				])
	)
]

#Definition GatheringVariablesList
GatheringVariablesList=[
		['/'],
		'<Commanders>'
]

#Now command with a AllSetsForEach protocol
MyFirstCommander.execute(
	'self.__class__.ShareCountInt=0'
	).command(
		_UpdateList=CommandingUpdateList,
		**{
			'GatheringVariablesList': GatheringVariablesList
		}
	)

#Command with a EachSetForAll protocol
MySecondCommander.execute(
	'self.__class__.ShareCountInt=0'
	).command(
		_UpdateList=CommandingUpdateList,
		_OrderStr='EachSetForAll',
		**{
			'GatheringVariablesList': GatheringVariablesList
		}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyFirstCommander is '+SYS._str(
		MyFirstCommander,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'MySecondCommander is '+SYS._str(
		MySecondCommander,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

