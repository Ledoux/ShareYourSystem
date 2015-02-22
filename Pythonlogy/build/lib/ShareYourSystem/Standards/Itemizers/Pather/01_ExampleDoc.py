
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPather=SYS.PatherClass(
	).__setitem__(
		'MyStr',
		'I am the parent'
	)

MyPather.__setitem__(
	'ChildPather',
	SYS.PatherClass()
	)

#set with a deep short Str
MyPather.__setitem__(
	'/ChildPather/MyStr',
	'I am the child'
)

#print
print('MyPather[\'/ChildPather\'] is ')
SYS._print(
			MyPather['/ChildPather'],
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)

#set with a deep deep short Str
MyPather.__setitem__(
	'/ChildPather/GrandChildPather',
	SYS.PatherClass()
)

#print
print('MyPather[\'/ChildPather/GrandChildPather\'] is ')
SYS._print(
			MyPather['/ChildPather/GrandChildPather'],
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)

#set with a deep short Str
MyPather.__setitem__(
	'/OtherChildPather',
	SYS.PatherClass().__setitem__('MyInt',3)
)

#set with a deep short Str
MyPather.__setitem__(
	'/OtherChildPather',
	SYS.PatherClass().__setitem__('MyInt',4)
)

#'/' gets the self
MyPather.__setitem__(
	'/SelfPather',
	MyPather['/']
)

#print
print('MyPather is ')
SYS._print(
			MyPather,
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)

