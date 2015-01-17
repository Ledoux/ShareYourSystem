
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Meteorers import Viewer

#Definition an Tree instance
MyViewer=Viewer.ViewerClass().view()
MyViewer.MeteoredConcurrentDDPClientVariable.stop()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyViewer is '+SYS._str(
		MyViewer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print

