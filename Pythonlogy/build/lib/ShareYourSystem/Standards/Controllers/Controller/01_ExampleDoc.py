#ImportModules
import ShareYourSystem as SYS

#Short expression and set in the appended manner
MyController=SYS.ControllerClass()

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

