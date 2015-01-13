
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Filterer
import operator

#Definition a Filter instance that is grouped
MyFilterer=Filterer.FiltererClass().update(
	[	
		('NodeIndexInt',1),
		('NodeKeyStr','MyFilterer'),
		(
			'ConcludingConditionTuplesList',[
						(
							'NodeIndexInt',
							lambda _TestInt,_AttestInt:
								operator.lt(_TestInt,_AttestInt)
								if _TestInt!=None else False,
							2
						)
					]
				),
		(
			'PickingGetKeyVariablesList',['NodeKeyStr']
		)
	]
).filter('/')

		
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

