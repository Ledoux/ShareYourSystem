
#ImportModules
import ShareYourSystem as SYS

#Define and set a dict
MySetter=SYS.SetterClass(
	).set(
		{
			'GetVariable':"MyStr"
		},
		"hello"
	)

#Define and set a dict
MySetter=SYS.SetterClass(
	).set(
		{
			'SetKeyVariable':"MyDict"
		},
		{'MyInt':0}
	)

#set a Setter that will be updated by the dict
MySetter.set(
		SYS.SetterClass(
			)['map*set'](
				{
					'SetKeyVariable':"MySetter",
					'MyInt':0
				}
			),
		{'MyFloat':5.}
	)

#print
print('MySetter is ')
SYS._print(MySetter)