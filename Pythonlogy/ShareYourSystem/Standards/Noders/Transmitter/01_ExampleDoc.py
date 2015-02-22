#ImportModules
import ShareYourSystem as SYS
import operator

#Definition of a brian structure
MyTransmitter=SYS.TransmitterClass(
	).collect(
		"Transmiters",
		'First',
		SYS.TransmitterClass().update(
			[
				('ConnectingCatchGetStrsList',
					[
						'/NodePointDeriveNoder/<Transmiters>SecondTransmitter'
					]
				),
				('ConnectingGraspClueVariablesList',
					[
						'/NodePointDeriveNoder/<Transmiters>SecondTransmitter'
					]
				),
				('TagStr','Networked')
			]
		)
	).collect(
		"Transmiters",
		'Second',
		SYS.TransmitterClass().__setitem__(
			'TagStr',
			'Networked'
		)
	).network(
	**{
				'RecruitingConcludeConditionVariable':[
					('__class__.NameStr',operator.eq,'Transmitter')
				]
		}
)	

#transmit
MyTransmitter['<Transmiters>FirstTransmitter'].transmit(
	[('MyInt',0)],
	['PostConnectome']
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyTransmitter is '+SYS._str(
		MyTransmitter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

