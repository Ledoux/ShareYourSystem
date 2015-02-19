
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).point(
			#PointingToGetVariable
			'/ChildPather/GrandChildPather',
			#PointingToSetKeyVariable
			'MyGrandChildPather',
			#PointingBackBool
			_BackBool=True
		).point(
			#PointingToGetVariable
			'/ChildPather/GrandChildPather',
			#PointingToSetKeyVariable
			'MyGrandChildPather',
			#PointingBackSetKeyVariable
			'MyGrandParentPointer',
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

