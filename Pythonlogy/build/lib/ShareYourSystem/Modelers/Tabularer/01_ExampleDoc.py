
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Controllers import Controller
from ShareYourSystem.Modelers import Tabularer

#Definition 
MyController=Controller.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Datome.hdf5",
			'FolderingPathStr':Tabularer.LocalFolderPathStr
		}
	).collect(
		"Datome",
		"Things",
		Tabularer.TabularerClass().__setitem__(
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
MyController['<Datome>ThingsTabularer'].tabular()
		
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

