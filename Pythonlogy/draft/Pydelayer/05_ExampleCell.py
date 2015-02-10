
#ImportModules
import ShareYourSystem as SYS
import numpy as np 


#Definition an instance
MyPydelayer=SYS.PydelayerClass(
	).simulate(
		#SimulatingStopTimeFloat
		20.,
		#SimulatingInitFloatsArray
		np.array([1.,1.3]),
		**{
			'PydelayingKwargVariablesDict':
			{
				'eqns':{
					'x0' : 'g(-x0(t-0.),x1(t-0.)) ',
					'x1' : '-1. * x1(t-0.) + (1.) * x0(t-5.) '
					#'x' : '-x(t-0.)'
				},
				'supportcode':'''
					double g(double xa,double xb){
						return xa+xb;
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

