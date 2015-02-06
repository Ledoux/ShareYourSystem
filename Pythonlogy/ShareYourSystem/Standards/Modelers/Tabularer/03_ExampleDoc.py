
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
MyController['<Tabularers>ThingsTabularer'].tabular(
		_DatabaseStr="mongo"
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
		'mongo db is : '+MyController.pymongoview().PymongoneViewStr
	]
) 

#Print

