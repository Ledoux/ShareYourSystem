
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Noder,Collecter

#Definition of an instance
MyCollecter=Collecter.CollecterClass().collect(
	'Nodome',
	'First',
	Noder.NoderClass()
).collect(
	'Nodome',
	'Second',
	Noder.NoderClass()
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyCollecter is '+SYS._str(
		MyCollecter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

