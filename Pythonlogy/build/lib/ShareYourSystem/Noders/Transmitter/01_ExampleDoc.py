#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Transmitter
import operator

#Definition of a brian structure
MyTransmitter=Transmitter.TransmitterClass(
	).push(
[
	(
		'First',
		Transmitter.TransmitterClass().update(
			[
				('ConnectingCatchGetStrsList',
					[
						'/NodePointDeriveNoder/<Transmitome>SecondTransmitter'
					]
				),
				('ConnectingAttentionGetStrsList',
					[
						'/NodePointDeriveNoder/<Transmitome>SecondTransmitter'
					]
				),
				('TagStr','Networked')
			]
		)
	),
	(
		'Second',
		Transmitter.TransmitterClass().__setitem__(
			'TagStr',
			'Networked'
		)
	)
],
	**{
		'CollectingCollectionStr':'Transmitome'
	}
).network(
	**{
				'RecruitingConcludeConditionTuplesList':[
					('__class__.NameStr',operator.eq,'Transmitter')
				]
		}
)	

#transmit
MyTransmitter['<Transmitome>FirstTransmitter'].transmit(
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

