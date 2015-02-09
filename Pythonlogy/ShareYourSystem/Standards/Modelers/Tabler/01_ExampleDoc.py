
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Things.hdf5",
			'FolderingPathStr':SYS.Tabler.LocalFolderPathStr
		}
	).collect(
		"Tablers",
		"Things",
		SYS.TablerClass().__setitem__(
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
MyController['<Tablers>ThingsTabler'].table(
	**{
		'FolderingPathStr':SYS.Tabler.LocalFolderPathStr
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
		'hdf5 file is : '+MyController.hdfview()
	]
) 

#Close
MyController.close()
