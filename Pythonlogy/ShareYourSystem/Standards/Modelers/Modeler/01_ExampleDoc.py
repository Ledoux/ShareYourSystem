
#ImportModules
import ShareYourSystem as SYS

#A Modeler alone is not so much good
LonelyModeler=SYS.ModelerClass(
	).model(
	)

#print
print('LonelyModeler is ')
SYS._print(LonelyModeler)


#Definition of a Controller instance and the Child Modeler automatically model
MyController=SYS.ControllerClass(
		**{
			'ControllingModelClassVariable':SYS.ModelerClass
		}
	).get(
		'/-Models/|Stuff'
	)

#print
print('MyController is ')
SYS._print(MyController)

#print
print('The Modeler object has a key for getting faster the related controller')
SYS._print(MyController['/-Models/|Stuff'].ModeledDeriveControllerVariable)

