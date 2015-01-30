
#ImportModules
import ShareYourSystem as SYS

#Definition an instance
MyNeurongrouper=SYS.NeurongrouperClass(
	**{
			#either set with N in the NeuronGroup Kwarg 
			#or here at the populating level
			#'PopulatingUnitsInt':100
		}
	).collect(
		'SpikeMoniters',
		'MySpikes',
		SYS.MoniterClass()
	).neurongroup(
		{
			'N':100,
			'model':
			'''
				dv/dt = (-(v+60*mV)+11*mV + 5.*mV*sqrt(20.*ms)*xi)/(20*ms) : volt
			''',
			'threshold':'v>-50*mV',
			'reset':'v=-70*mV'
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
			MyNeurongrouper.NeurongroupedSpikeMonitorsList,
			MyNeurongrouper.NeurongroupedStateMonitorsList
		]
	)
)

#plot
MyNeurongrouper.NeurongroupedBrianVariable.v=-55.*mV
MyNetwork.run(500.*ms)
M=MyNeurongrouper.NeurongroupedSpikeMonitorsList[0]
from matplotlib import pyplot
pyplot.plot(M.t/ms, M.i, '.')
pyplot.show()
