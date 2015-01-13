
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Pather

#Explicit expression
MyPather=Pather.PatherClass().__setitem__('MyStr','I am the parent')
MyPather.__setitem__('ChildPather',Pather.PatherClass())

#set with a deep short Str
MyPather.__setitem__(
	'/ChildPather/MyStr',
	'I am the child'
)

#set with a deep deep short Str
MyPather.__setitem__(
	'/ChildPather/GrandChildPather',
	Pather.PatherClass()
)

#set with a deep short Str
MyPather.__setitem__(
	'/OtherChildPather',
	Pather.PatherClass().__setitem__('MyInt',3)
)

#set with a deep short Str
MyPather.__setitem__(
	'/OtherChildPather',
	Pather.PatherClass().__setitem__('MyInt',4)
)

#'/' gets the self
MyPather.__setitem__(
	'/SelfPather',
	MyPather['/']
)


#Definition the AttestedStr
SYS._attest(
[
	'MyPather is '+SYS._str(
			MyPather,
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		),
	'MyPather[\'/ChildPather\'] is '+SYS._str(
			MyPather['/ChildPather'],
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		),
	'MyPather[\'/ChildPather/GrandChildPather\'] is '+SYS._str(
			MyPather['/ChildPather/GrandChildPather'],
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
	]
) 
	
#Print

