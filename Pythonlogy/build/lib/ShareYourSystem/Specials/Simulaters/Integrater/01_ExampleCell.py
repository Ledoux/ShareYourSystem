
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Define a leaker
SYS.IntegraterClass.euler_leak=lambda _InstanceVariable:-_InstanceVariable.EuleringPreFloatsArray

#Definition an instance
MyIntegrater=SYS.IntegraterClass(
	).integrate(
		#IntegratingStepsInt
		20,
		#IntegratingInitFloatsArray
		np.array([0.,0.1]),
		#IntegratingMoniterVariableIndexIntsArray
		np.array([0,1]),
		#IntegratingTimeDelayVariable
		10,
		**{'EuleringJacMethodStr':"euler_leak"}
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyIntegrater is '+SYS._str(
		MyIntegrater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#plot
from matplotlib import pyplot
pyplot.plot(MyIntegrater['<StateMoniters>VariableMoniter'].MoniteredTotalVariablesArray.T)
pyplot.show()

#Print
