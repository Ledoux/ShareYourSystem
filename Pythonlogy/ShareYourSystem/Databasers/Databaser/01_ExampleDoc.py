
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Storers import Storer
from ShareYourSystem.Databasers import Databaser

#Definition of a Storer instance with a noded databaser
MyStorer=Storer.StorerClass().collect(
	"Datome",
	"Things",
	Databaser.DatabaserClass()
)

#database
MyStorer['<Datome>ThingsDatabaser'].database()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyStorer is '+SYS._str(
		MyStorer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)

#Print

