
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Tutorials import Decrementer

#Definition an instance
MyDecrementer=Decrementer.DecrementerClass().decrement()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyDecrementer is '+SYS._str(
				MyDecrementer,
				**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
				}
			)
	]
) 

