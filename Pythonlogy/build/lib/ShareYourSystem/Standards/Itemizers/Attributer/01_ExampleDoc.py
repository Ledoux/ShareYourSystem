
#ImportModules
import ShareYourSystem as SYS

#define and set with attr
MyAttributer=SYS.AttributerClass(
	).__setitem__(
		'Attr_MyInt',
		0
	)
		
#Definition the AttestedStr
print('MyAttributer is ')
SYS._print(MyAttributer)

