
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#set a special jac method
SYS.EulererClass.euler_leak=lambda _InstanceVariable:-_InstanceVariable.EuleringPreFloatsArray

#Definition an instance
MyEulerer=SYS.EulererClass(
	).euler(
		np.array([0.,0.1]),
		'euler_leak'
	)


#Definition the AttestedStr
SYS._attest(
	[
		'MyEulerer is '+SYS._str(
		MyEulerer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print


