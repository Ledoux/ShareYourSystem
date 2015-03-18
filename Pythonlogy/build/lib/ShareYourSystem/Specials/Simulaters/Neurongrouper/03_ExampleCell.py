#/###################/#
# Import modules
#

#ImportModules
import ShareYourSystem as SYS

#
UnitsInt=3

#/###################/#
# Build the model
#

#Definition an instance
MyNeurongrouper=SYS.NeurongrouperClass(
	).set(
		'/-States/|Run',
		{
			'MoniteringVariableStr':'r'
		}
	).neurongroup(
		{
			'N':UnitsInt,
			'model':
			''' 
				dr/dt = -r/(20*ms) : 1
			'''
		}
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
