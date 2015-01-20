#ImportModules
import ShareYourSystem as SYS


#Short expression and set in the appended manner
MyParenter=SYS.ParenterClass(
	).__setitem__(
		'<Parenters>ChildParenter',
		SYS.ParenterClass(
			).__setitem__(
				'<Parenters>GrandChildParenter',
				SYS.ParenterClass(
				)
			)
		)

#Parent for the children
MyParenter[
	'<Parenters>ChildParenter'
	][
	'<Parenters>GrandChildParenter'
	].parent(
		['IdInt']
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyParenter is '+SYS._str(
		MyParenter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

