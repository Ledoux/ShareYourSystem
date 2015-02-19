
#ImportModules
import ShareYourSystem as SYS

#Define and direct point with an automatic keystr
MyPointer=SYS.PointerClass(
		).point(
			#PointingToGetVariable
			'/ChildPointer/GrandChildPointer'
		)

#Point direct with a special Key str
MyPointer.point(
			#PointingToGetVariable
			'/ChildPointer/GrandChildPointer',
			#PointingToSetKeyVariable
			'GrandChildPointer'
		)

#print
print('MyPointer is')
SYS._print(MyPointer)


#Point with a Pointer encapsulator
MyPointer=SYS.PointerClass(
	).point(
			#PointingToGetVariable
			'/ChildPointer/GrandChildPointer',
			#PointingToSetKeyVariable
			'/GrandChildPointer/GrandChildPointer'
		)

#Point with a Pointer encapsulator and without the keystr
MyPointer.point(
			#PointingToGetVariable
			'/ChildPointer/GrandChildPointer',
			#PointingToSetKeyVariable
			'/CloneGrandChildPointer/'
		)

#print
print('MyPointer is')
SYS._print(MyPointer)

