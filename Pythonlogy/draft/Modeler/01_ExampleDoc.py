
#ImportModules
import ShareYourSystem as SYS

#Define
MyController=SYS.ControllerClass(
	).command(
		'/&Models/$Things','#call:model'
	)
		
#print
print('MyController is ')
SYS._print(MyController)

