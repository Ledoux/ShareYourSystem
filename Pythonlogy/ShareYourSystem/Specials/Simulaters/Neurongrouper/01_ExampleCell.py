#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#/###################/#
# Build the model
#

#Definition an instance
MyNeurongrouper=SYS.NeurongrouperClass(
	).neurongroup(
		#NeurongroupingBrianDict
		{
			'N':10,
			'model':
			'''
				dv/dt = (-(v+60*mV)+11*mV + 5.*mV*sqrt(20.*ms)*xi)/(20*ms) : volt
			''',
			'threshold':'v>-50*mV',
			'reset':'v=-70*mV'
		},
		#NeurongroupingStatesDict
		{	
			'v':[('Run',[0,1])],
		},
		#NeurongroupingSpikesDict
		{	
			'Run':{}
		},
	)
	
#/###################/#
# Print
#

#Definition the AttestedStr
print('MyNeurongrouper is ')
SYS._print(MyNeurongrouper) 

#/###################/#
# Do one simulation
#

"""
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
"""
