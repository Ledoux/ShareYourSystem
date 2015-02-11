
#ImportModules
import ShareYourSystem as SYS

#define and command
MyCommander=SYS.CommanderClass(
	).command(
		'/',
		[
			('MyStr',"hello"),
			('MyInt',0),
			('apply*get',"MyInt")
		]
	)

print(MyCommander.GettedValueVariable)

#print
print('MyCommander is ')
SYS._print(MyCommander)	
