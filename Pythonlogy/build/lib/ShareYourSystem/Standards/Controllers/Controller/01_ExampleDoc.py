#ImportModules
import ShareYourSystem as SYS

#Define
MyController=SYS.ControllerClass(
	).get(
		'/-Children/|Loup/'
	).parent(
		_DownBool=True
	)

#print
print('MyController is ')
SYS._print(MyController)
