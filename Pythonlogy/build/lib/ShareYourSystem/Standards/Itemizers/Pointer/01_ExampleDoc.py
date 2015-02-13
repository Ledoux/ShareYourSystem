
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).get(
			'/ChildPather/GrandChildPather'
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

