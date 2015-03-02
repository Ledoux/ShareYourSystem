
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Tabularer.LocalFolderPathStr,
			'ControllingModelClassVariable':SYS.TabularerClass
		}
	).get(
		'/-Models/|Things'
	)


#Build a structure with a database
MyController['/-Models/|Things'].TabularedMongoLocalDatabaseVariable.TestsCollection.remove(
	{}
)
MyController['/-Models/|Things'].TabularedMongoLocalDatabaseVariable.TestsCollection.insert(
	{'MyStr':"hello"}
)

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#print
print('MyController is ')
SYS._print(MyController)

#kill
MyController.process(_ActionStr='kill')

