
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Pather,Pointer

#Explicit expression
MyPointer=Pointer.PointerClass().__setitem__(
		'ChildPather',
		Pather.PatherClass().__setitem__(
			'GrandChildPather',
			Pather.PatherClass()
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

