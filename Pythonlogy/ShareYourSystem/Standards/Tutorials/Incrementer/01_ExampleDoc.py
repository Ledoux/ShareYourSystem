
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Tutorials import Incrementer

#Definition an instance
MyIncrementer=Incrementer.IncrementerClass().increment()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyIncrementer is '+SYS._str(
				MyIncrementer,
				**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
				}
			)
	]
) 

