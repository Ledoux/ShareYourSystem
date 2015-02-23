
#ImportModules
import ShareYourSystem as SYS

#define and command with one get key str
MyCommander=SYS.CommanderClass(
	).command(
		#CommandingGetVariable
		'/',
		#CommandingSetVariable
		[
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
				'#map:set',
				[
					('MyFirstBool',True),
				]
			)
		]
	)

#command several objects with get that returns each a list
MyCommander.MyCommandersList=[SYS.CommanderClass(),SYS.CommanderClass()]
MyCommander.command(
		#CommandingGetVariable
		['/','MyCommandersList'],
		#CommandingSetVariable
		[
			(
				'#map:set',
				[
					('MySecondBool',False),
				]
			)
		]
	)

#Commanding by an implicit self set
MyCommander.command(
		[],('MyStr',"hello"),_BeforeSelfBool=True
	)


#print
print('MyCommander is ')
SYS._print(MyCommander)	
