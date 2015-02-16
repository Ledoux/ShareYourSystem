
#ImportModules
import ShareYourSystem as SYS

#define and command with one get key str
MyCommander=SYS.CommanderClass(
	).command(
		#CommandingGetVariable
		'/',
		#CommandingSetVariable
		{
			'MyInt':0	
		}		
	)

#print
print('MyCommander.GettedValueVariable is ')
print(MyCommander.GettedValueVariable)

