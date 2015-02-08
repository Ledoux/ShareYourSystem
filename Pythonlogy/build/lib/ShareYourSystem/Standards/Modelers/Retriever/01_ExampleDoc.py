
#ImportModules
import ShareYourSystem as SYS
import tables

#Definition of a Controller instance with a noded datar
MyController=SYS.ControllerClass().collect(
	"Retrievers",
	"Things",
	SYS.RetrieverClass().update(
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

MyController.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[2,4,6])
			]
).command(
	_UpdateList=[('insert',{'LiargVariablesList':[]})],	
	**{'GatheringVariablesList':['<Retrievers>ThingsRetriever']}		
).update(
			[
				('MyInt',0),
				('MyStr',"guten tag"),
				('MyIntsList',[0,0,0])
			]
).command(
	_UpdateList=[('insert',{'LiargVariablesList':[]})],	
)


#Retrieve
MyController['<Retrievers>ThingsRetriever'].__setitem__(
	'RetrievingIndexesList',(0,1)
).retrieve()
					
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

