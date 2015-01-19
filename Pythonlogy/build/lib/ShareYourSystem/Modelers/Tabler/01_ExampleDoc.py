
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Controllers import Controller
from ShareYourSystem.Modelers import Tabler

#Definition of a Controller instance with a noded datar
MyController=Controller.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Datome.hdf5",
			'FolderingPathStr':Tabler.LocalFolderPathStr
		}
	).collect(
		"Datome",
		"Things",
		Tabler.TablerClass().__setitem__(
			'Attr_DatabasingSealTuplesList',
			[
				#GetStr #ColumnStr #Col
				('MyInt','MyInt',tables.Int64Col()),
				('MyStr','MyStr',tables.StringCol(10)),
				('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
			]	
		)
	)

#Tabular in it
MyController['<Datome>ThingsTabler'].table(
	**{
		'FolderingPathStr':Tabler.LocalFolderPathStr
	}
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
		'hdf5 file is : '+MyController.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

