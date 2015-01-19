
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Meteorers import Meteorer

#Definition an Tree instance
MyMeteorer=Meteorer.MeteorerClass().meteor()
MyMeteorer.MeteoredConcurrentDDPClientVariable.stop()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyMeteorer is '+SYS._str(
		MyMeteorer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

