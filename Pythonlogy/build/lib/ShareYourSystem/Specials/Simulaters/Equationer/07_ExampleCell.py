
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Definition an instance
MyEquationer=SYS.EquationerClass(
	).collect(
		'LateralExpressers',
		'Leak',
		SYS.MatrixerClass(
			).matrix(
				_SizeTuple=(2,2),
				_StdFloat=0.,
				_DiagFloatsArray=np.array([-1.,-1.])
			)
	).collect(
		'LateralExpressers',
		'Interaction',
		SYS.MatrixerClass(
			).matrix(
				_SizeTuple=(2,2),
				_SpecificTagVariablesArray=np.array(
					[
						[{},{'DelayFloat':5.}],
						[{'DelayFloat':5.},{}]
					]
				)
			)
	).collect(
		'InputMatrixers',
		'Constant',
		SYS.MatrixerClass(
			).matrix(
				_SizeTuple=(3,2),
				_SpecificTagVariablesArray=np.array(
					[
						[{},{'DelayFloat':5.}],
						[{'DelayFloat':5.},{}]
					]
				)
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
