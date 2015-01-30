
#ImportModules
import ShareYourSystem as SYS
import operator

#Definition of a brian structure
MyPopulater=SYS.PopulaterClass().populate(
					**{
						'PopulatingUnitsInt':500
					}
				)
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyPopulater is '+SYS._str(
		MyPopulater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print

