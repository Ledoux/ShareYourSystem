
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

A=np.array(
		[
			[0,4],
			[5,7],
			[9,1]
		]
	)

print(A[
			np.array([0,1]),
			np.array([0,1])
	])

print(A[
			np.array([0,1]),
			:
	][np.array([0,1])])



A[
	[0,2],
	0:2
]=np.array(
		[
			[55,78],
			[12,34]
		]
	)

print(A)


"""
#Definition an instance
MyPydelayer=SYS.PydelayerClass(
	).simulate(
		#SimulatingStopTimeFloat
		20.,
		#SimulatingInitFloatsArray
		np.array([1.,1.]),
		**{
			'PydelayingKwargVariablesDict':
			{
				'eqns':{
					'x0' : '-1. * x0(t-0.) + (-1.) * x1(t-5.) ',
					'x1' : '-1. * x1(t-0.) + (-1.) * x0(t-5.) '
					#'x' : '-x(t-0.)'
				}
			}
		}
	)
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyPydelayer is '+SYS._str(
		MyPydelayer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#plot

from matplotlib import pyplot
pyplot.plot(MyPydelayer['<StateMoniters>VariableMoniter'].MoniteredTotalVariablesArray.T)
pyplot.show()

#Print

"""
