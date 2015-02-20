
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

#Define and set a dict
MySetter.set(
		{
			'#set':"MyDict"
		},
		{'MyInt':0}
	)


#print
print('MySetter is ')
SYS._print(MySetter)