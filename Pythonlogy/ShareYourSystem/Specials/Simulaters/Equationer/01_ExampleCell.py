
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
ParamFloat=10.+np.random.rand()

MyEquationer=SYS.EquationerClass(
	).equation(
		{
			'x' : '( foo(t) + 0.25 * x(t-5.0) )/ (1.0 + pow(x(t-5.0),'+str(ParamFloat)+'))'
		},
		_CodeStr='''
			double foo(double t){
						return cos(t);
					}
		'''
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyEquationer is '+SYS._str(
		MyEquationer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#plot
MyPydelayer=SYS.PydelayerClass(
	).collect(
		'Equationers',
		'MyEquationer',
		MyEquationer
	).simulate(
		20.,
		np.array([1.]),
		**{
			'PydelayingKwargVariablesDict':{
				#'supportcode':'''
				#	double foo(double t){
				#		return cos(t);
				#	}
				#'''
			}
		}
	)

from matplotlib import pyplot
pyplot.plot(MyPydelayer['<StateMoniters>VariableMoniter'].MoniteredTotalVariablesArray.T)
pyplot.show()

#Print
