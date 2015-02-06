
#ImportModules
import ShareYourSystem as SYS
#import tables


from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')











"""
#Definition 
MyController=SYS.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Things.hdf5",
			'FolderingPathStr':SYS.Tabularer.LocalFolderPathStr
		}
	).collect(
		"Tabularers",
		"Things",
		SYS.TabularerClass().__setitem__(
			'Attr_DatabasingSealTuplesList',
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',tables.Int64Col()),
				('MyStr','MyStr',tables.StringCol(10)),
				('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
			]	
		)
	)

#Build a structure with a database
MyController['<Tabularers>ThingsTabularer'].tabular()
		
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
		'hdf5 file is : '+MyController.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

"""