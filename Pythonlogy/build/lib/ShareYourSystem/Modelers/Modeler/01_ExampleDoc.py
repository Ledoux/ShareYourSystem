
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Controllers import Controller
from ShareYourSystem.Modelers import Modeler

#Definition of a Controller instance with a noded databaser
MyController=Controller.ControllerClass().collect(
	"Datome",
	"Things",
	Modeler.ModelerClass()
)

#database
MyController['<Datome>ThingsModeler'].model()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyController is '+SYS._str(
		MyController,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)

#Print

