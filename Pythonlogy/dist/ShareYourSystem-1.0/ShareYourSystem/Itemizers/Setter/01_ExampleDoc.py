
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Setter

#Definition a Setter and set with the __setitem__
MySetter=Setter.SetterClass().__setitem__('MyInt',0)
		
#Definition the AttestedStr
SYS._attest(
	[
	'MySetter is '+SYS._str(
			MySetter,
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
	]
) 

#Print

