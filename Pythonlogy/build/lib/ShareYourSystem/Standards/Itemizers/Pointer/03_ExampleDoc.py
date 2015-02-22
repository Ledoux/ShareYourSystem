
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).point(
			#PointingToGetVariable
			'/FirstChildPointer/GrandChildPointer',
			#PointingToSetKeyVariable
			'FirstGrandChildPointer',
			#PointingBackBool
			_BackBool=True
		).point(
			#PointingToGetVariable
			'/SecondChildPointer/GrandChildPointer',
			#PointingToSetKeyVariable
			'SecondGrandChildPointer',
			#PointingBackSetKeyVariable
			'MyGrandParentPointer'
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

