
#ImportModules
import ShareYourSystem as SYS

#Definition 
MyController=SYS.ControllerClass(
		**{
			'FolderingPathStr':SYS.Tabularer.LocalFolderPathStr
		}
	).collect(
		"Tabularers",
		"Things",
		SYS.TabularerClass()
	)

#Build a structure with a database
MyController['<Tabularers>ThingsTabularer'].tabular()
MyController['<Tabularers>ThingsTabularer'].TabularedMongoLocalDatabaseVariable.TestsCollection.remove(
	{}
)
MyController['<Tabularers>ThingsTabularer'].TabularedMongoLocalDatabaseVariable.TestsCollection.insert(
	{'MyStr':"hello"}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyController is '+SYS._str(
		MyController,
			**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
			}
		),
		
	]
) 

#print
print('mongo db is : \n'+SYS._str(MyController.pymongoview()))

#Print
MyController.close()
