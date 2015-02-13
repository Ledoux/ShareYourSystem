
#ImportModules
import ShareYourSystem as SYS

#define and command
MyCommander=SYS.CommanderClass(
	).command(
		'/',
		[
			('MyStr',"hello"),
			('MyInt',0),
			(
				'map*set',
				[
					('MyFirstBool',True),
					('MySecondBool',False),
				]
			),
			('get',"MyInt")
		]
	)

#print
print('MyCommander.GettedValueVariable is ')
print(MyCommander.GettedValueVariable)

#print
print('MyCommander is ')
SYS._print(MyCommander)	
