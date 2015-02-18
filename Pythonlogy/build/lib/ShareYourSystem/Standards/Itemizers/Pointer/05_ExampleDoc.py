
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).get(
			'/ChildPather/GrandChildPather'
		).point(
			#PointingGetVariable
			'/',
			#PointingSetPathStr
			'/ChildPather/GrandChildPather/GrandParentPointer',
			#PointingBackSetStr
			
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

