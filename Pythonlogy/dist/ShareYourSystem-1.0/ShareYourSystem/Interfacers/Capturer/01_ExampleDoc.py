#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Capturer

#Definition a Capturer
MyCapturer=Capturer.CapturerClass().capture()
print('Hello !')
print('Bonjour !')
MyCapturer.CapturingStopBool=True
print('Y a quelqu un?')

#Definition the AttestedStr
SYS._attest(
	[
		'MyCapturer is '+SYS._str(
		MyCapturer,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
)  

#Print



