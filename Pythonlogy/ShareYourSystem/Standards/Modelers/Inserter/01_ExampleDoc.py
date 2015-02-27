
#ImportModules
import tables
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Things.hdf5",
			'FolderingPathStr':SYS.Inserter.LocalFolderPathStr
		}
	).collect(
		"Inserters",
		"Things",
		SYS.InserterClass().update(
		[
			(
				'Attr_ModelingDescriptionTuplesList',
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

#Definition a structure with a db
MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[2,4,6])
			]
).command(
	_UpdateList=[('insert',SYS.ApplyDictClass({'LiargVariablesList':[]}))],
	**{'GatheringVariablesList':['<Inserters>ThingsInserter']}		
).update(
			[
				('MyInt',0),
				('MyStr',"hello"),
				('MyIntsList',[0,0,0])
			]
).command(
	_UpdateList=[('insert',SYS.ApplyDictClass({'LiargVariablesList':[]}))],		
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

#close
MyController.close()

