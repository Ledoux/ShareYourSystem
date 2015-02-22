
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPather=SYS.PatherClass(
	).set(
		'/ChildPather/GrandChildPather/MyInt',
		0
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

