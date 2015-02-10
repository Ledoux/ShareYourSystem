
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyPydelayer=SYS.PydelayerClass(
	).simulate(
		#SimulatingStopTimeFloat
		20.,
		#SimulatingInitFloatsArray
		np.array([1.]),
		**{
			'PydelayingKwargVariablesDict':
			{
				'eqns':{
					'x' : '(foo(t) + 0.25 * x(t-tau)) / (1.0 + pow(x(t-tau),p)) -0.1*x'
				},
				'params':{
					'tau' : 5,
			    	'p'   : 10
				},
				'supportcode':'''
				double foo(double t){
					return cos(t);
				}
				'''
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



