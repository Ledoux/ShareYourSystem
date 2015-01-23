
#ImportModules
import ShareYourSystem as SYS

#Definition of a Controller instance with a noded databaser
MyController=SYS.ControllerClass().collect(
	"Modelers",
	"Things",
	SYS.ModelerClass()
)

#database
MyController['<Modelers>ThingsModeler'].model()
		
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

