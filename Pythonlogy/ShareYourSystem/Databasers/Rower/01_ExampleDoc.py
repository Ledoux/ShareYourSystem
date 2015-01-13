
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Rower

#Definition of a Structurer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
	"Datome",
	"Things",
	Rower.RowerClass().update(
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
MyStructurer.update(								
[
	('MyInt',0),
	('MyStr',"hello"),
	('MyIntsList',[2,4,1])
])['<Datome>ThingsRower'].row()
		
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

