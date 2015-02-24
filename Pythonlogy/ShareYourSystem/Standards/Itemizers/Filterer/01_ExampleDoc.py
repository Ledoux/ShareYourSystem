
#ImportModules
import ShareYourSystem as SYS

#Definition a Filter instance that is grouped
MyFilterer=SYS.FiltererClass(
	)['#map@set'](
		[	
			('MyInt',1),
			('MyStr',"hello"),
			(
				'ConcludingConditionVariable',
				[
					(
						'MyInt',
						lambda _TestInt,_AttestInt:
							SYS.operator.lt(_TestInt,_AttestInt)
							if _TestInt!=None else False,
						2
					)
				]
			)
		]
	).filter(
		#FilteringGraspVariable
		'/',
		#FilteringGetVariable
		['MyStr']
	)

		
#Definition the AttestedStr
SYS._attest(
	[
		'MyFilterer is '+SYS._str(
		MyFilterer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

