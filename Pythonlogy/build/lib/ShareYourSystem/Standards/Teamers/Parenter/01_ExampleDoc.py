#ImportModules
import ShareYourSystem as SYS

#define structure
MyParenter=SYS.ParenterClass(
	).get(
		'/*Children/$Child/*Children/$GrandChild'
	).set('TeamKeyStr',3)

#parent then
MyParenter['/*Children/$Child/*Children/$GrandChild'].parent()







"""
#print(MyParenter['/*Children/$Child/*Children/$GrandChild/<Teamer'])
print(MyParenter['/*Children/$Child/*Children/$GrandChild'].ManagementPointDeriveTeamer)

#print(MyParenter['/*Children/$Child/<Teamer'])
print(MyParenter['/*Children/$Child'].ManagementPointDeriveTeamer)

print(MyParenter.ManagementPointDeriveTeamer)
"""

"""
.__setitem__(
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
"""

#print
"""
print('MyParenter is ')
SYS._print(MyParenter)
"""

"""
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
"""
#Print

