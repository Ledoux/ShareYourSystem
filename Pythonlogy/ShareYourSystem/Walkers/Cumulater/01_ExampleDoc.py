
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Cumulater
import operator

#Definition a Filter instance that is grouped
MyCumulater=Cumulater.CumulaterClass().update(
		[
			(
				'<Filterome>FirstChildCumulater',
				Cumulater.CumulaterClass().update(
					[
						(
							'<Filterome>GrandChildFilter',
							Cumulater.CumulaterClass()
						)
					]
				)
			),
			(
				'<Filterome>SecondChildFilter',
				Cumulater.CumulaterClass()
			),
			(
				'<Filterome>ThirdChildFilter',
				Cumulater.CumulaterClass()
			)
		]	
	)

#Walk inside the group in order to parent
MyCumulater.walk(
			{
				'BeforeUpdateList':
				[
					(
						'ConcludingConditionTuplesList',[
							(
								'NodeIndexInt',
								lambda _TestInt,_AttestInt:
									operator.lt(_TestInt,_AttestInt) and operator.lt(-1,_TestInt)
									if _TestInt!=None else False,
								2
							)
						]
					),
					(
						'PickingGetKeyVariablesList',['NodeKeyStr']
					),
					('cumulate',{'LiargVariablesList':[]})
				],
				'GatherVariablesList':['<Filterome>']
			}
		)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyCumulater is '+SYS._str(
		MyCumulater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print


