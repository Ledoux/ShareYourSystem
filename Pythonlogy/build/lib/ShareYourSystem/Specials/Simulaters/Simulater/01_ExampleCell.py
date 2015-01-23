
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Specials.Simulaters import Simulater

#Definition an instance
MySimulater=Simulater.SimulaterClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MySimulater is '+SYS._str(
		MySimulater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print


