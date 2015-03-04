
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Rower.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.RowerClass
		}
	).set(
		'/-Models/|Things',
		{
			'ModelingKeyStrsList':['MyInt','MyStr','MyIntsList']	
		}
	)['#map@set'](
		{
			'MyInt':0,
			'MyStr':"hello",
			'MyIntsList':[2,4,1]
		}
	).command(
		'/-Models/|Things',
		'#call:row'
	)
	
#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#print
print('MyController is ')
SYS._print(MyController)

#Print
MyController.process(_ActionStr='kill')



