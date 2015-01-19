
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Distinguisher
import copy

#Definition a tree of Distinguishers.
MyDistinguisher=Distinguisher.DistinguisherClass().update(
	map(
			lambda __Int:
			(
				'<Tree>'+str(__Int)+'Distinguisher',
				Distinguisher.DistinguisherClass()
			),
			xrange(2)
	)
)

#distinguish
MyDistinguisher.distinguish("Tree",[
										[('MyStr',"hello")],
										[('MyInt',0)]
									])

#distinguish through setting
MyDistinguisher.__setitem__(
	"Dis_<Tree>",
	[
		[('MyOtherStr',"bonjour")],
		[('MyOtherInt',1)]
	]
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyDistinguisher is '+SYS._str(
		MyDistinguisher,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

