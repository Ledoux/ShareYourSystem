
#/##################/#
# Import
#

#import
import brian2
from matplotlib import pyplot

#/##################/#
# Model
#

#init
BalanceNetowrk=brian2.Network()

#init
ExcNeuronGroup=brian2.NeuronGroup(
		10,
		'''
			dv/dt=-(v-(-60.*mV))/(10.*ms) : volt
		'''
	)

#add
map(
	lambda __Variable:
		BalanceNetowrk.add(
				__Variable
			),
		[
			ExcNeuronGroup
		]
	)

#/##################/#
# Simulate
#

#run
BalanceNetowrk.run(5.*brian2.ms)

#/##################/#
# Plot
#

Figure=pyplot.figure()





