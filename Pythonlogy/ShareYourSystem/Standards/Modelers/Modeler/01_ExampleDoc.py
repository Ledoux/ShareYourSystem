
#ImportModules
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
	).get(
		'/&Models/$Things'
	)


#print
print('MyController is ')
SYS._print(MyController)


