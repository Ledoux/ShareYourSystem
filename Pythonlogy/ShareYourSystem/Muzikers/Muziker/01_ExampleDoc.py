
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Muzikers import Muziker

#Definition a "graph" structure
MyMuziker=Muziker.MuzikerClass()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyMuziker is '+SYS._str(
		MyMuziker,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'MyMuziker.hdfview().HdformatedStr is '+MyMuziker.hdfview().HdformatedStr
	]
) 

#Print

