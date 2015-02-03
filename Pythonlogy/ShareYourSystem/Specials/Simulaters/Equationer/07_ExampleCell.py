
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyEquationer=SYS.EquationerClass(
	).collect(
		'LateralExpressers',
		'Leak',
		SYS.Expresser(
			**{
				'MatrixingStdFloat':0.,
				'MatrixingDiagFloatsArray':np.array([-1.,-1.])
			}
		)
	).collect(
		'LateralExpressers',
		'Interaction',
		SYS.Expresser(
			**{
				'ExpressingSpecificTagVariablesArray':np.array(
					[
						[{},{'DelayFloat':5.}],
						[{'DelayFloat':5.},{}]
					]
				)
			}
		)
	).collect(
		'InputExpressers',
		'Constant',
		SYS.Expresser(
			**{
				'MatrixingSizeTuple':(3,2),
				'ExpressingSpecificTagVariablesArray'=np.array(
					[
						[{},{'DelayFloat':5.}],
						[{'DelayFloat':5.},{}]
					]
				)
			}
		)
	).equation(
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
		np.array([1.,1.2])
	)

from matplotlib import pyplot
pyplot.plot(MyPydelayer['<StateMoniters>VariableMoniter'].MoniteredTotalVariablesArray.T)
pyplot.show()

#Print
