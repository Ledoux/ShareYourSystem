
#FrozenIsBool True

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Object

#Definition a Getter
MyObject=Object.ObjectClass()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyObject is '+SYS._str(
			MyObject,
		**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print

