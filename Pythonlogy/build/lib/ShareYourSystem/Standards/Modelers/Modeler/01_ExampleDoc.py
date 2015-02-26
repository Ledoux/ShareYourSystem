
#ImportModules
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
	).get(
		'/&Models/$Things'
	)


#print
SYS._print('MyController is ')
print(MyController)


