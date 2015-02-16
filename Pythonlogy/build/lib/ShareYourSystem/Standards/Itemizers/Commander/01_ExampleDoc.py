
#ImportModules
import ShareYourSystem as SYS

#define and command with one get key str
MyCommander=SYS.CommanderClass(
	).command(
		#CommandingGetVariable
		'/',
		#CommandingSetVariable
		[
			('MyStr',"hello"),
			('MyChildCommander',{}),
			('get',"MyInt")
		]
	)

#print
print('MyCommander.GettedValueVariable is ')
print(MyCommander.GettedValueVariable)

#command several objects with a list
MyCommander.command(
		#CommandingGetVariable
		['/','MyChildCommander'],
		#CommandingSetVariable
		[
			(
				'map*set',
				[
					('MyFirstBool',True),
					('MySecondBool',False),
				]
			)
		]
	)

#print
print('MyCommander is ')
SYS._print(MyCommander)	
