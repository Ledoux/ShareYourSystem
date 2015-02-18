
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).get(
			'/ChildPather/GrandChildPather'
		).point(
			#PointingToGetVariable
			'/ChildPather/GrandChildPather'
		).point(
			#PointingToGetVariable
			'/ChildPather/GrandChildPather',
			#PointingToSetKeyVariable
			'MyGrandChildPather'
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

