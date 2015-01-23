
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition a structure
MyController=SYS.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Things.hdf5",
			'FolderingPathStr':SYS.Shaper.LocalFolderPathStr
		}
	).collect(
		"Shapers",
		"Things",
		SYS.ShaperClass().update(
			[
				('Attr_DatabasingSealTuplesList',
					[
						('MyInt','MyInt',tables.Int64Col()),
						('MyStr','MyStr',tables.StringCol(10)),
						('MyIntsList','MyIntsList',tables.Int64Col(shape=[3]))
					]
				),
				('Attr_RowingGetStrsList',
					['MyInt','MyStr']
				),
				('ShapingDimensionTuplesList',
					[
						('MyIntsList',['UnitsInt'])
					]
				)
			]
		)
	)

MyController.update(
	[
		('MyInt',0),
		('MyStr',"hello"),
		('UnitsInt',3),
		('MyIntsList',[0,0,1])
	]
)['<Shapers>ThingsShaper'].flush()

MyController.update(
	[
		('MyInt',1),
		('MyStr',"bonjour"),
		('MyIntsList',[0,0,1])
	]
)['<Shapers>ThingsShaper'].flush()


MyController.update(
	[
		('MyInt',1),
		('MyStr',"ola"),
		('MyIntsList',[0,1])
	]
)['<Shapers>ThingsShaper'].flush()

#Definition the AttestedStr
SYS._attest(
	[
		'MyController is '+SYS._str(
		MyController,
		**{
			'RepresentingAlineaIsBool':False,
			'RepresentingBaseKeyStrsListBool':False
		}
		),
		'hdf5 file is : '+MyController.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

