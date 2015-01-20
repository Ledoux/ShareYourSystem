
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass().__setitem__(
		'ChildPather',
		SYS.PatherClass().__setitem__(
			'GrandChildPather',
			SYS.PatherClass()
			)
		).point(
			'/',
			'/ChildPather/GrandChildPather/GrandParentPointer'
		)

#Return
SYS._attest(
	[
	'MyPointer is '+SYS._str(
			MyPointer,
			**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
			}
		)
	]
)

#Print

