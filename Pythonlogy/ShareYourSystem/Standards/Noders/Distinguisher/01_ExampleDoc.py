
#ImportModules
import ShareYourSystem as SYS
import copy

#Definition a tree of Distinguishers.
MyDistinguisher=SYS.DistinguisherClass().update(
	map(
			lambda __Int:
			(
				'<Distinguishers>'+str(__Int)+'Distinguisher',
				SYS.DistinguisherClass()
			),
			xrange(2)
	)
)

#distinguish
MyDistinguisher.distinguish(
	"Distinguishers",[
	[('MyStr',"hello")],
	[('MyInt',0)]
])

#distinguish through setting
MyDistinguisher.__setitem__(
	"Dis_<Distinguishers>",
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

