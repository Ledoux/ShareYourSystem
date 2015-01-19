
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Functers import Triggerer
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Modelers import Featurer,Joiner
import tables
import operator

MyFeaturer=Featurer.FeaturerClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MyFeaturer is '+SYS._str(
		MyFeaturer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
		'hdf5 file is : '+MyFeaturer.hdfview().hdfclose().HdformatedStr
	]
) 

#Print

