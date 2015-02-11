
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Itemizers import Deleter

#Definition a Deleter
MyDeleter=Deleter.DeleterClass().__setitem__('MyInt',0).__delitem__('MyInt')
		
#Definition the AttestedStr
SYS._attest(
	[
	'MyDeleter is '+SYS._str(
			MyDeleter,
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
	]
) 

#Print

