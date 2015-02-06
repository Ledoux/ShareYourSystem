
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Functers import Triggerer
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Featurer,Recuperater
import tables
import operator

MyRecuperater=Recuperater.RecuperaterClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MyRecuperater is '+SYS._str(
		MyRecuperater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MyRecuperater.hdfview().hdfclose().HdformatedConsoleStr
	]
) 

#Print

