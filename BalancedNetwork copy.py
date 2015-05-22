
#/##################/#
# Neurongroup Model
#

NeuronGroupModelStr='''
	tau : 1
	dv/dt= ( <LeakCurrent> + <SynapticCurrent> + <NoiseCurrent> ) /(tau*ms) : volt
'''


NeuronGroupModelStr=NeuronGroupModelStr.replace(
	'<LeakCurrent>',
	
)

NeuronGroupModelStr=NeuronGroupModelStr.replace(
	'<SynapticCurrent>',
	#"0*mV"
	'J*mV'

)

NeuronGroupModelStr=NeuronGroupModelStr.replace(
	'<NoiseCurrent>',
	"0*mV"
	#'xi*sqrt(tau*ms)*0.*mV'
)

#print
print('Our model of NeuronGroup is ')
print(NeuronGroupModelStr)

#/##################/#
# Synapses Model
#

SynapsesModelStr='''
	J : 1
	v_post += J*mV : volt
'''

#print
print('Our model of Synapses is ')
print(SynapsesModelStr)


#/##################/#
# Brian instanciation
#

#import
import brian2

#init
BalanceNetwork=brian2.Network()

#init
ExcNeuronGroup=brian2.NeuronGroup(
		10,
		NeuronGroupModelStr
	)
InhNeuronGroup=brian2.NeuronGroup(
		10,
		NeuronGroupModelStr
	)

#init
ExcToExcNeuronGroup=brian2.Synapses(
		ExcNeuronGroup,
		ExcNeuronGroup,
		SynapsesModelStr
	)







"""
#add
map(
	lambda __Variable:
		BalanceNetwork.add(
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
BalanceNetwork.run(5.*brian2.ms)

#/##################/#
# Plot
#

Figure=pyplot.figure()

"""



