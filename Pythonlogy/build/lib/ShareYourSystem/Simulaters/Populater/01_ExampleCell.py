
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Populater

#Definition an instance
MyPopulater=Populater.PopulaterClass()
		
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

