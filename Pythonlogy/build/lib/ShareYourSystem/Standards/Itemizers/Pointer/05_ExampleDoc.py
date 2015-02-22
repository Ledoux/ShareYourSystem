
#ImportModules
import ShareYourSystem as SYS

#Define and shortcut point without SetKeyVariable
MyPointer=SYS.PointerClass(
		).get(
			'->/ChildPointer/FirstGrandChildPointer'
		).get(
			'<->/ChildPointer/SecondGrandChildPointer'
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

#Define and shortcut point with SetKeyVariable
MyPointer=SYS.PointerClass(
		).set(
			'->/ChildPointer/FirstGrandChildPointer',
			'MySecondGrandChildPointer'
		).set(
			'->/ChildPointer/SecondGrandChildPointer',
			'/MySecondGrandChildPointer/'
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

#Define and shortcut back point with SetKeyVariable
MyPointer=SYS.PointerClass(
		).set(
			'<->/ChildPointer/FirstGrandChildPointer',
			('MyFirstGrandChildPointer','MyGrandParentPointer')
		).set(
			'<->/ChildPointer/SecondGrandChildPointer',
			('/MySecondGrandChildPointer/','/MyGrandParentPointer/')
		)

#print
print('MyPointer is')
SYS._print(MyPointer)
