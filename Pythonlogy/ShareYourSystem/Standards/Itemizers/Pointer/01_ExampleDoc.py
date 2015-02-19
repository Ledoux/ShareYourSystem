
#ImportModules
import ShareYourSystem as SYS

#Define and direct point
MyPointer=SYS.PointerClass(
		).point(
			#PointingToGetVariable
			'/ChildPather/GrandChildPather'
		).point(
			#PointingToGetVariable
			'/ChildPather/GrandChildPather',
			#PointingToSetKeyVariable
			'MyGrandChildPather'
		).point(
			#PointingToGetVariable
			'/ChildPather/GrandChildPather',
			#PointingToSetKeyVariable
			SYS.PointerClass(
				).set(
					'GetKeyVariable':"MyGrandParentPointer"
				)
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

