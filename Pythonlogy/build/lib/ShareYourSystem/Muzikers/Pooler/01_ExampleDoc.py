
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Muzikers import Pooler

#Definition a Pooler
MyPooler=Pooler.PoolerClass().pool(8,12)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPooler is '+SYS._str(
		MyPooler,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'MyPooler.hdfview().HdformatedStr is '+MyPooler.hdfview().HdformatedStr
	]
) 

#Print
