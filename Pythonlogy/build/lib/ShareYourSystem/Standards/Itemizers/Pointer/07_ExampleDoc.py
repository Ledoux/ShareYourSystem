
#ImportModules
import ShareYourSystem as SYS

#Explicit expression
MyPointer=SYS.PointerClass(
		).point(
			'/ChildPather/FirstGrandChildPather',
			'/MyGrandChildPointer/'
		)

#print
print("MyPointer['*MyGrandChildPointer'] is")
SYS._print(MyPointer['*MyGrandChildPointer'])

'''
MyPointer['*MyGrandChildPointer']=SYS.PatherClass(
	).set(
		'MyStr',
		"hello"
	)

#print
print("MyPointer is")
SYS._print(MyPointer)
'''