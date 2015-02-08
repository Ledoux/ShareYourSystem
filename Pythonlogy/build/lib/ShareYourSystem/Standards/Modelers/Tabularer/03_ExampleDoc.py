
#ImportModules
import ShareYourSystem as SYS
#import tables

#Definition 
MyController=SYS.ControllerClass(
		**{
			'PymongoingDatabaseKeyStr':"Things",
			'FolderingPathStr':SYS.Tabularer.LocalFolderPathStr
		}
	).collect(
		"Tabularers",
		"Things",
		SYS.TabularerClass()
	)

#Build a structure with a database
MyController['<Tabularers>ThingsTabularer'].tabular()
MyController['<Tabularers>ThingsTabularer'].TabularedMongoTopDatabaseVariable.TestsCollection.remove(
	{}
)
MyController['<Tabularers>ThingsTabularer'].TabularedMongoTopDatabaseVariable.TestsCollection.insert(
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
print('mongo db is : \n'+MyController.pymongoview().PymongoneViewStr)

#Print
MyController.close()
