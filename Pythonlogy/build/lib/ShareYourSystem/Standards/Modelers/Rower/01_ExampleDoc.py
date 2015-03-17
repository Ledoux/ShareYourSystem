
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Rower.LocalFolderPathStr
		}
	).set(
		'/-Models/|Thing',
		{
			'ModelKeyStrsList':['MyInt','MyStr','MyIntsList']	
		}
	).get('?v'
	)['#map@set'](
		{
			'MyInt':0,
			'MyStr':"hello",
			'MyIntsList':[2,4,1]
		}
	).command(
		'/-Models/|Thing',
		'#call:row'
	)
	
#Build a structure with a database
SYS.mapSet(
		MyController['/-Models/|Thing'].ModeledMongoCollection,
		[
			('remove',{}),
			('insert',{'MyStr':"hello"})
		]
)

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#print
print('MyController is ')
SYS._print(MyController)

#Print
MyController.process(_ActionStr='kill')



