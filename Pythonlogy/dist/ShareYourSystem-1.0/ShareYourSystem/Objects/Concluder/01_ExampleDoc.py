
#ImportModules
import ShareYourSystem as SYS
import operator

#Definition of an instance Concluder and make it print hello
MyConcluder=SYS.ConcluderClass().conclude(
	{'MyColorStr':'Black','MySuperInt':6},
	[
		('MyColorStr',operator.eq,"Black"),
		('MySuperInt',operator.gt,3),
		(1,operator.eq,1)
	]
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyConcluder is '+SYS._str(
		MyConcluder,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		),
	]
) 

#Print


	

