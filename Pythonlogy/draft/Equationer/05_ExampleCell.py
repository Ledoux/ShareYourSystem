
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyEquationer=SYS.EquationerClass(
		**{
			'PopulatingUnitsInt':2
		}
	).collect(
		'LateralExpressers',
		'Leak',
		SYS.ExpresserClass(
				**{
					'MatrixingStdFloat':0.,
					'MatrixingDiagFloatsArray':np.array([-1.,-1.])
				}
			)
	).collect(
		'LateralExpressers',
		'Interaction',
		SYS.ExpresserClass(
				**{
					'ExpressingSpecificTagVariablesArray':np.array(
						[
							[{},{'DelayFloat':5.,'TransferFunctionStr':'cos'}],
							[{'DelayFloat':5.},{}]
						]
					),
					'ExpressingRowTagVariablesArray':np.array(
						[
							{'TransferFunctionStr':'foo'},
							{}
						]
					),
					'MatrixingStdFloat':0.2,
				}
			)
	).equation(
		_CodeStr='''
			double foo(double t){
						return cos(t);
					}
		'''
	)

#print
SYS._print(
		[
			"MyEquationer['EquationingDifferentialDict'] is ",
			MyEquationer['EquationingDifferentialDict']
		]
	)

#Definition the AttestedStr
'''
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
'''

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
