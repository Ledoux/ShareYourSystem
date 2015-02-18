
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).get(
			'>/ChildPather/FirstGrandChildPather'
		).set(
			'>/ChildPather/SecondGrandChildPather',
			'MySecondGrandChildPather'
		)

#print
print('MyPointer is')
SYS._print(MyPointer)
