#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Modeler.LocalFolderPathStr
		}
	).set(
		'/-Models/|Things',
	).get('?v')

#Build a structure with a database
SYS.mapSet(
		MyController['/-Models/|Things'].ModeledMongoCollection,
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

#kill
MyController.process(_ActionStr='kill')
