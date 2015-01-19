
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Controllers import Controller
from ShareYourSystem.Modelers import Databaser

#Definition of a Controller instance with a noded datar
MyController=Controller.ControllerClass().collect(
	"Datome",
	"Things",
	Databaser.DatabaserClass()
)

#Definition a Databaser instance
MyController['<Datome>ThingsDatabaser'].database([
										#GetStr #ColumnStr #Col
										('MyInt','MyInt',tables.Int64Col()),
										('MyStr','MyStr',tables.StringCol(10)),
										('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
								])
							
		
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
		'MyController["<Datome>ThingsDatabaser"].DatabasedModelClass.__dict__ is '+SYS._str(
		dict(MyController['<Datome>ThingsDatabaser'].DatabasedModelClass.__dict__.items()
			) if MyController['<Datome>ThingsDatabaser'
		].DatabasedModelClass!=None else {},**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print

