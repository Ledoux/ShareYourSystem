
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Controllers import Controller
from ShareYourSystem.Modelers import Rower

#Definition of a Controller instance with a noded datar
MyController=Controller.ControllerClass().collect(
	"Datome",
	"Things",
	Rower.RowerClass().update(
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

#Tabular in it
MyController.update(								
[
	('MyInt',0),
	('MyStr',"hello"),
	('MyIntsList',[2,4,1])
])['<Datome>ThingsRower'].row()
		
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

