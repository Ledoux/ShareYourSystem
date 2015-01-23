
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Guider
from ShareYourSystem.Standards.Objects import Concluder

#Definition an instance
MyGuider=Guider.GuiderClass(
	).package(
		Concluder
	).guide(
		'001','Github','Doc','Markdown',
	)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyGuider is '+str(
			SYS._str(
				MyGuider,
				**{
				'RepresentingBaseKeyStrsListBool':False
				}
			)
		)
	]
) 
