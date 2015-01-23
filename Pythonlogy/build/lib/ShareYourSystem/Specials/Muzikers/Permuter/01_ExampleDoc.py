
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Muzikers import Permuter

#Definition a permuter
MyPermuter=Permuter.PermuterClass().permute(3,7)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPermuter is '+SYS._str(
		MyPermuter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'MyPermuter.hdfview().HdformatedStr is '+MyPermuter.hdfview().HdformatedStr
	]
) 

#Print

