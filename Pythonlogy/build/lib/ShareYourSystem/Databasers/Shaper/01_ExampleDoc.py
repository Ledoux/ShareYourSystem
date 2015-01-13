
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Shaper

#Definition a structure
MyStructurer=Structurer.StructurerClass().collect(
	"Datome",
	"Things",
	Shaper.ShaperClass().update(
		[
			('Attr_ModelingSealTuplesList',
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

MyStructurer.update(
	[
		('MyInt',0),
		('MyStr',"hello"),
		('UnitsInt',3),
		('MyIntsList',[0,0,1])
	]
)['<Datome>ThingsShaper'].flush()

MyStructurer.update(
	[
		('MyInt',1),
		('MyStr',"bonjour"),
		('MyIntsList',[0,0,1])
	]
)['<Datome>ThingsShaper'].flush()


MyStructurer.update(
	[
		('MyInt',1),
		('MyStr',"ola"),
		('MyIntsList',[0,1])
	]
)['<Datome>ThingsShaper'].flush()

#Definition the AttestedStr
SYS._attest(
	[
		'MyStructurer is '+SYS._str(
		MyStructurer,
		**{
			'RepresentingAlineaIsBool':False,
			'RepresentingBaseKeyStrsListBool':False
		}
		),
		'hdf5 file is : '+MyStructurer.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

