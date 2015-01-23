
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Controllers import Controller
from ShareYourSystem.Standards.Modelers import Merger
import operator,tables

#Definition a structure
MyController=Controller.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Datome.hdf5",
			'FolderingPathStr':Merger.LocalFolderPathStr
		}
	).collect(
	"Datome",
	"Things",
	Merger.MergerClass().update(
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
)['<Datome>ThingsMerger'].flush()

MyController.update(
	[
		('MyInt',1),
		('MyStr',"bonjour"),
		('MyIntsList',[0,0,1])
	]
)['<Datome>ThingsMerger'].flush()

MyController.update(
	[
		('MyInt',1),
		('MyStr',"ola"),
		('MyIntsList',[0,1])
	]
)['<Datome>ThingsMerger'].flush()

#Merge
MyController['<Datome>ThingsMerger'].merge(
			[
				('UnitsInt',(operator.gt,2))
			]	
)

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

