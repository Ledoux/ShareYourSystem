#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Controllers import Controller

#Short expression and set in the appended manner
MyController=Controller.ControllerClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MyController is '+SYS._str(
		MyController,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
) 

#Print

