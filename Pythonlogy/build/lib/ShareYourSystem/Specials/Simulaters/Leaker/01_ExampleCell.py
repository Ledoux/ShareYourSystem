
#ImportModules
import ShareYourSystem as SYS
import numpy as np 

#Init
MyLeaker=SYS.LeakerClass(
	).leak(
		#LeakingConstantTimeVariable
		#10.
		np.array([10.,20.]),
		**{
			'PopulatingUnitsInt':2,
			'<LateralExpressers>LateralMatrixer/MatrixingStdFloat':0.2
			}
	)

#print
SYS._print(
		[
			"MyLeaker['EquationingDifferentialDict'] is ",
			MyLeaker['EquationingDifferentialDict']
		]
	)


#Definition the AttestedStr
SYS._attest(
	[
		'MyLeaker is '+SYS._str(
		MyLeaker,
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
		'Leakers',
		'MyLeaker',
		MyLeaker
	).simulate(
		20.,
		np.array([1.,1.2])
	)

from matplotlib import pyplot
pyplot.plot(MyPydelayer['<StateMoniters>VariableMoniter'].MoniteredTotalVariablesArray.T)
pyplot.show()


#Print