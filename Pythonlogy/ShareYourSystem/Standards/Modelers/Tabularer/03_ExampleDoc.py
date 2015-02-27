
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Tabularer.LocalFolderPathStr
		}
	).command(
		'/&Models/$Things','#call:tabular'
	)

#Build a structure with a database
MyController['/&Models/$Things'].TabularedMongoLocalDatabaseVariable.TestsCollection.remove(
	{}
)
MyController['/&Models/$Things'].TabularedMongoLocalDatabaseVariable.TestsCollection.insert(
	{'MyStr':"hello"}
)

#print
print('MyController is ')
SYS._print(MyController)

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#Print
MyController.close()
