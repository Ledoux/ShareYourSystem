
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Commander
import copy

#Definition a structure of Commanders.
MyFirstCommander=Commander.CommanderClass().__add__(
	[
		Commander.CommanderClass().update(
			[
				('NodeCollectionStr','Commandome'),
				('NodeKeyStr',str(Int1))
			]) for Int1 in xrange(2)
	]
)

#Definition a structure of Commanders.
MySecondCommander=Commander.CommanderClass().__add__(
	[
		Commander.CommanderClass().update(
			[
				('NodeCollectionStr','Commandome'),
				('NodeKeyStr',str(Int1))
			]) for Int1 in xrange(2)
	]
)


#Definition an CommandingUpdateList to be commanded
CommandingUpdateList=[
	(
		'MyCountingInt',
		';'.join([
					'Exec_self.SettingValueVariable=self.__class__.MyCountingInt',
					'self.__class__.MyCountingInt+=1'
				])
	),
	(
		'MyCountingInt',
		';'.join([
					'Exec_self.SettingValueVariable=self.__class__.MyCountingInt',
					'self.__class__.MyCountingInt+=1'
				])
	)
]

#Definition GatheringVariablesList
GatheringVariablesList=[
		['/'],
		'<Commandome>'
]

#Now command with a AllSetsForEach protocol
MyFirstCommander.execute('self.__class__.MyCountingInt=0').command(
		_UpdateList=CommandingUpdateList,
		**{
			'GatheringVariablesList': GatheringVariablesList
			}
		)

#Command with a EachSetForAll protocol
MySecondCommander.execute('self.__class__.MyCountingInt=0').command(
		CommandingUpdateList,
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

