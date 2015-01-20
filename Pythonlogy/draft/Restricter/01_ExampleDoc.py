
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Restricter

#Explicit expression
MyRestricter=Restricter.RestricterClass(**{'RestrictingIsBool':True})
MyRestricter.ResettedStr="Hello"
MyRestricter.__setitem__('ResettedStr',"Bonjour")
MyRestricter.__setitem__('NotsettedFloat',1.)

#Return
SYS._attest(
	[
	'MyRestricter is '+SYS._str(
			MyRestricter,
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
	]
)

#Print

