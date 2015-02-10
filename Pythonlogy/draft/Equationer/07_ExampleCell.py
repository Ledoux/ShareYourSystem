
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
						[{},{'DelayFloat':5.}],
						[{'DelayFloat':5.},{}]
					]
				),
				'MatrixingStdFloat':0.2,
			}
		)
	).collect(
		'InputExpressers',
		'Constant',
		SYS.ExpresserClass(
			**{
				'ExpressingSymbolStr':'id',
				'ExpressingSpecificTagVariablesArray':np.array(
					[
						[{},{'DelayFloat':1.},{}],
						[{},{},{}]
					]
				),
				#'ExpressingColTagVariablesArray':np.array(
				#		[
				#			{'SymbolStr':'1'},
				#			{'SymbolStr':'1'}
				#		]
				#	)
			}
		)
	).equation(
		_CodeStr='''
			double id(double t){
						return 1.;
					}
		'''
	)

'''
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
'''

#print
SYS._print(
		[
			"MyEquationer['EquationingDifferentialDict'] is ",
			MyEquationer['EquationingDifferentialDict']
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
