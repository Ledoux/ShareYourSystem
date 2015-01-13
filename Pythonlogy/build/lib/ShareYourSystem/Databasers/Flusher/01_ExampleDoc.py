
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Flusher

#Definition of a Structurer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
	"Datome",
	"Things",
	Flusher.FlusherClass().update(
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

#Definition a structure with a db
MyStructurer.update(
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
		'MyStructurer is '+SYS._str(
		MyStructurer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MyStructurer.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

