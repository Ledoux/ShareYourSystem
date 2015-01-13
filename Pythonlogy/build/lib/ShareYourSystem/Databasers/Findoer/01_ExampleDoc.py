
#ImportModules
import tables,operator

import ShareYourSystem as SYS
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Findoer

#Definition of a Structurer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
	"Datome",
	"Things",
	Findoer.FindoerClass().update(
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

MyStructurer.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[0,0,1])
			]
)['<Datome>ThingsFindoer'].flush()

MyStructurer.update(
			[
				('MyInt',0),
				('MyStr',"guten tag"),
				('MyIntsList',[0,0,1])
			]
)['<Datome>ThingsFindoer'].flush()

MyStructurer.update(
			[
				('MyInt',1),
				('MyStr',"bonjour"),
				('MyIntsList',[0,0,0])
			]
)['<Datome>ThingsFindoer'].flush()

#Retrieve
MyStructurer['<Datome>ThingsFindoer'].find(
										[
											('MyInt',(operator.eq,1)),
											('MyIntsList',(SYS.getIsEqualBool,[0,0,1]))
										]
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


