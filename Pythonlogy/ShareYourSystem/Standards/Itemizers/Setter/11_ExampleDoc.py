
#ImportModules
import ShareYourSystem as SYS

#Define and set a dict
MySetter=SYS.SetterClass(
	).set(
		{
			'SetKeyVariable':"MyStr"
		},
		"hello"
	)

#print
print('MySetter is ')
SYS._print(MySetter)