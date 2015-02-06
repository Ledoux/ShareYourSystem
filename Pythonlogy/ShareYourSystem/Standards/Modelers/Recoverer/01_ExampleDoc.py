
#ImportModules
import ShareYourSystem as SYS
import operator,tables

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass(
	**{
		'FolderingPathStr':SYS.Recoverer.LocalFolderPathStr,
		'HdformatingFileKeyStr':"Recoverers.hdf5"
		}
	).collect(
	"Recoverers",
	"Things",
	SYS.RecovererClass().update(
		[
			(
				'Attr_DatabasingSealTuplesList',
				[
					#GetStr #ColumnStr #Col
					('MyInt','MyInt',tables.Int64Col()),
					('MyStr','MyStr',tables.StringCol(10)),
					('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
				]
			),
			('Attr_RowingGetStrsList',['MyInt','MyStr','MyIntsList'])	
		]
	)
)

MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[0,0,1])
			]
	)['<Recoverers>ThingsRecoverer'].flush(
	)

MyController.update(
			[
				('MyInt',0),
				('MyStr',"guten tag"),
				('MyIntsList',[0,0,1])
			]
)['<Recoverers>ThingsRecoverer'].flush()

MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[0,0,0])
			]
)['<Recoverers>ThingsRecoverer'].flush()

#Retrieve
MyController['<Recoverers>ThingsRecoverer'].recover(
												**{
														'FindingConditionTuplesList':
														[
															('MyInt',(operator.eq,1)),
															('MyIntsList',(SYS.getIsEqualBool,[0,0,1]))
														]
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
		'hdf5 file is : '+MyController.hdfview().hdfclose().HdformatedConsoleStr
	]
) 

#Print


