
#ImportModules
import ShareYourSystem as SYS

#Define and set
MySetter=SYS.SetterClass(
	).__setitem__(
		'MyInt',
		0
	)
		
#print
print('MySetter is ')
SYS._print(MySetter)


