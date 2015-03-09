#ImportModules
import ShareYourSystem as SYS

#Define
MyController=SYS.ControllerClass(
	).get(
		'/-Children/|Loup/'
	)

#print
print('MyController is ')
SYS._print(MyController)
