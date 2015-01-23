
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Itemizers import Attributer

#Definition a Attributer and set with the __setitem__
MyAttributer=Attributer.AttributerClass().__setitem__('Attr_MyInt',0)
		
#Definition the AttestedStr
SYS._attest(
	[
	'MyAttributer is '+SYS._str(
			MyAttributer,
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
		
	]
) 

#Print

