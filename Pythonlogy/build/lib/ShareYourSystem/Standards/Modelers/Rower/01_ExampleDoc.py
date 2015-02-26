
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Things.hdf5",
			'FolderingPathStr':SYS.Rower.LocalFolderPathStr
		}
	).collect(
		"Rowers",
		"Things",
		SYS.RowerClass().update(
			[
				(
					'Attr_ModelingSealTuplesList',
					[
						#GetStr #ColumnStr #Col
						('MyInt','MyInt',tables.Int64Col()),
						('MyStr','MyStr',tables.StringCol(10)),
						('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
					]
				),
				('Attr_RowingGetStrsList',['MyInt'])	
			]
		)
	)

#Tabular in it
MyController.update(								
[
	('MyInt',0),
	('MyStr',"hello"),
	('MyIntsList',[2,4,1])
])['<Rowers>ThingsRower'].row()
		
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

#close
MyController.close()
