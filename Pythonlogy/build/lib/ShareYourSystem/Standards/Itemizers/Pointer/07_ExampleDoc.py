
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).get(
			'*FirstLinkPointer>/ChildPather/FirstGrandChildPather'
		)
		.set(
			'*SecondLinkPointer>/ChildPather/SecondGrandChildPather',
			'MySecondGrandChildPather'
		).set(
			'*<Pointer>/ChildPather/SecondGrandChildPather',
			'MySecondGrandChildPather'
		)


#print
print('MyPointer is')
SYS._print(MyPointer)
