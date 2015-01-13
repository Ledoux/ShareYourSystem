
#ImportModules
import ShareYourSystem as SYS,Classer
from ShareYourSystem.Storers import Storer

#Definition
MyStorer=Storer.StorerClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MyStorer is '+SYS._str(
		MyStorer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
	]
) 

#Print

