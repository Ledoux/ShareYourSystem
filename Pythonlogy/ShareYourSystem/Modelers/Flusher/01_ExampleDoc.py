
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Controllers import Controller
from ShareYourSystem.Modelers import Flusher

#Definition of a Controller instance with a noded datar
MyController=Controller.ControllerClass(
		**{
			'HdformatingFileKeyStr':"Datome.hdf5",
			'FolderingPathStr':Flusher.LocalFolderPathStr
		}
	).collect(
		"Datome",
		"Things",
		Flusher.FlusherClass().update(
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
	_UpdateList=[('flush',{'LiargVariablesList':[]})],
	**{'GatheringVariablesList':['<Datome>ThingsFlusher']}		
).update(
			[
				('MyInt',0),
				('MyStr',"hello"),
				('MyIntsList',[0,0,0])
			]
).command(
	_UpdateList=[('flush',{'LiargVariablesList':[]})],		
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

