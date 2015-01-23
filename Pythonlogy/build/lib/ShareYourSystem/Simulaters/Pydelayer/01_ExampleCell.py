
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyPydelayer=SYS.PydelayerClass(
	).update(
		{
			'SimulatingInitFloatsArray':np.array([1.]),
			'SimulatingStopTimeFloat':50.,
			'EuleringStepTimeFloat':0.1,
		}
	).collect(
		"StateMoniters",
		"Variable",
		SYS.MoniterClass().update(
				{
					'MoniteringVariableStr':'x',
					'MoniteringIndexIntsList':[0]
				}
			),
	).pydelay(
		{
			'eqns':{
				'x' : '0.25 * x(t-tau) / (1.0 + pow(x(t-tau),p)) -0.1*x'
				},
			'params':{
					'tau' : 15,
			    	'p'   : 10
				}
		}
	).run()

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
"""
from matplotlib import pyplot
pyplot.plot(MyPydelayer['<StateMoniters>VariableMoniter'].MoniteredTotalVariablesArray.T)
pyplot.show()
"""

#Print

#Print


"""
# Make a plot of x(t) vs x(t-tau):
# Sample the solution twice with a stepsize of dt=0.1:

# once in the interval [515, 1000]
sol1 = dde.sample(515, 1000, 0.1)
x1 = sol1['x']

# and once between [500, 1000-15]
sol2 = dde.sample(500, 1000-15, 0.1)
x2 = sol2['x']

pl.plot(x1, x2)
pl.xlabel('$x(t)$')
pl.ylabel('$x(t - 15)$')
pl.show()
"""