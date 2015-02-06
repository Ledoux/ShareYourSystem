
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Structurer
from ShareYourSystem.Databasers import Scanner

#Definition a structure with a db
ThingsStructurer=Structurer.StructurerClass(
).update(								
			[
				('MyIntsList',[0,0,0]),
				('HdformatingFileKeyStr',"Things.hdf5"),
				(
					'<Database>ThingsScanner',
					Scanner.ScannerClass().update(
						[
							('Attr_ModelingSealTuplesList',
								[
									#GetStr #ColumnStr #Col
									('MyInt','MyInt',tables.Int64Col()),
									('MyStr','MyStr',tables.StrCol(10)),
									('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
								]
							),
							('Attr_RowingGetStrsList',['MyInt','MyStr'])
						]
					)
				)
			]
)

#Update and store
ThingsStructurer['<Database>ThingsScanner'].scan(
	[
		('MyInt',[0,1,2]),
		('MyStr',["hello","bonjour"])
	]
)

#Definition the AttestedStr
SYS._attest(
	[
		'ThingsStructurer is '+SYS._str(
		ThingsStructurer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+ThingsStructurer.hdfview().hdfclose().HdformatedConsoleStr
	]
) 

#Print


