
#ImportModules
import ShareYourSystem as SYS
import operator

#Definition a Filter instance that is grouped
MyCumulater=SYS.CumulaterClass().update(
		[
			(
				'<Cumulaters>FirstChildCumulater',
				SYS.CumulaterClass().update(
					[
						(
							'<Cumulaters>GrandChildCumulater',
							SYS.CumulaterClass()
						)
					]
				)
			),
			(
				'<Cumulaters>SecondChildCumulater',
				SYS.CumulaterClass()
			),
			(
				'<Cumulaters>ThirdChildCumulater',
				SYS.CumulaterClass()
			)
		]	
	)

#Walk inside the group in order to parent
MyCumulater.walk(
	{
		'BeforeUpdateList':
		[
			(
				'ConcludingConditionVariable',[
					(
						'NodeIndexInt',
						lambda _TestInt,_AttestInt:
							operator.lt(_TestInt,_AttestInt
								) and operator.gt(_TestInt,-1)
							if _TestInt!=None else False,
						2
					)
				]
			),
			(
				'PickingKeyVariablesList',['NodeKeyStr']
			),
			('cumulate',{'LiargVariablesList':[]})
		],
		'GatherVariablesList':['<Cumulaters>']
	}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyCumulater is '+SYS._str(
		MyCumulater.CumulatedVariablesList,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print


