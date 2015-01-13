
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Tabularer

#Definition of a Storer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
	"Datome",
	"Things",
	Tabularer.TabularerClass().__setitem__(
		'Attr_ModelingSealTuplesList',
		[
			#GetStr #ColumnStr #Col
			('MyInt','MyInt',tables.Int64Col()),
			('MyStr','MyStr',tables.StringCol(10)),
			('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
		]	
	)
)

#Build a structure with a database
MyStructurer['<Datome>ThingsTabularer'].tabular()
		
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

