
#ImportModules
import ShareYourSystem as SYS

#Definition of an instance
MyCollecter=SYS.CollecterClass().collect(
		'Nodome',
		'First',
		SYS.NoderClass()
	).collect(
		'Nodome',
		'Second',
		SYS.NoderClass()
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

