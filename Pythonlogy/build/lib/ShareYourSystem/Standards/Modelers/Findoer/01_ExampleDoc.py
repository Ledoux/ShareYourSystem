
#ImportModules
import ShareYourSystem as SYS
import tables,operator

#Definition
MyController=SYS.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Things.hdf5",
			'FolderingPathStr':SYS.Findoer.LocalFolderPathStr
		}
	).collect(
	"Findoers",
	"Things",
	SYS.FindoerClass().update(
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
)['<Findoers>ThingsFindoer'].insert()

MyController.update(
			[
				('MyInt',0),
				('MyStr',"guten tag"),
				('MyIntsList',[0,0,1])
			]
)['<Findoers>ThingsFindoer'].insert()

MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[0,0,0])
			]
)['<Findoers>ThingsFindoer'].insert()

#Retrieve
MyController['<Findoers>ThingsFindoer'].find(
	[
		('MyInt',(operator.eq,1)),
		('MyIntsList',(SYS.getIsEqualBool,[0,0,1]))
	]
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

#Print
MyController.close()

