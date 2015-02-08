
#ImportModules
import ShareYourSystem as SYS
import numpy as np

#
UnitsInt=3

#Definition an instance
MyNeurongrouper=SYS.NeurongrouperClass(
	**{
			#either set with N in the NeuronGroup Kwarg 
			#or here at the populating level
			#'PopulatingUnitsInt':100
		}
	).collect(
		'StateMoniters',
		'MyRates',
		SYS.MoniterClass(
			**{

				'MoniteringRecordTimeIndexIntsArray':[0,1],
				'MoniteringVariableStr':'r'
			}
		)
	).neurongroup(
		{
			'N':UnitsInt,
			'model':
			''' 
				dr/dt = -r/(20*ms) : 1
			'''
		}
	)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyNeurongrouper is '+SYS._str(
		MyNeurongrouper,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print
from brian2 import Network,ms,mV
MyNetwork=Network()
map(
	MyNetwork.add,
	SYS.flat(
		[
			MyNeurongrouper.NeurongroupedBrianVariable,
			MyNeurongrouper.NeurongroupedStateMonitorsList
		]
	)
)

#plot
MyNeurongrouper.NeurongroupedBrianVariable.r=1.+np.array(map(float,xrange(UnitsInt)))
MyNetwork.run(500.*ms)
M=MyNeurongrouper.NeurongroupedStateMonitorsList[0]
from matplotlib import pyplot
pyplot.plot(M.t/ms, M.r.T)
pyplot.show()
