
#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Collecter
from ShareYourSystem.Databasers import Modeler

#Definition of a Collecter instance with a noded datar
MyCollecter=Collecter.CollecterClass().collect(
	"Datome",
	"Things",
	Modeler.ModelerClass()
)

#Definition a Modeler instance
MyCollecter['<Datome>ThingsModeler'].model([
										#GetStr #ColumnStr #Col
										('MyInt','MyInt',tables.Int64Col()),
										('MyStr','MyStr',tables.StringCol(10)),
										('MyIntsList','MyIntsList',tables.Int64Col(shape=3))
								])
							
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyCollecter is '+SYS._str(
		MyCollecter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'MyCollecter["<Datome>ThingsModeler"].ModeledClass.__dict__ is '+SYS._str(
		dict(MyCollecter['<Datome>ThingsModeler'].ModeledClass.__dict__.items()
			) if MyCollecter['<Datome>ThingsModeler'
		].ModeledClass!=None else {},**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print

