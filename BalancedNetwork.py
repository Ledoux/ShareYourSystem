
#/##################/#
# Parameters
#

#import
import numpy as np

UnitsInt=100
SparsityFloat=0.2
NeuronTypeStrsList=["Exc","Inh"]
ExcWeightFloat=10./np.sqrt(UnitsInt)
InhScaleFloat=4.

#/##################/#
# Architecture
#

#NeuronGroups
NeuronGroupStrsList=map(
	lambda __NeuronTypeStr:
	__NeuronTypeStr+'NeuronGroup',
	NeuronTypeStrsList
)

#Synapses
import itertools
NeuronTypeStrsTuplesList=list(
	itertools.product(
		NeuronTypeStrsList,
		NeuronTypeStrsList
	)
)
SynapsesStrsList=map(
	lambda __NeuronTypeStrsTuple:
	__NeuronTypeStrsTuple[0]+'To'+__NeuronTypeStrsTuple[1]+'Synapses',
	NeuronTypeStrsTuplesList
)

#StateMonitor
StateMonitorStrsList=map(
	lambda __NeuronTypeStr:
	__NeuronTypeStr+'StateMonitor',
	NeuronTypeStrsList
)

#SpikeMonitor
SpikeMonitorStrsList=map(
	lambda __NeuronTypeStr:
	__NeuronTypeStr+'SpikeMonitor',
	NeuronTypeStrsList
)

#Debug
#print('NeuronTypeStrsList is '+str(NeuronTypeStrsList))
#print('SynapsesStrsList is '+str(SynapsesStrsList))

#/##################/#
# Brian instanciation
#

#import
import brian2,itertools

#derive
class SynapsesClass(brian2.Synapses):
	def connect(self,*_LiargVariablesList,**_KwargVariablesDict):
		brian2.Synapses.connect(self,*_LiargVariablesList,**_KwargVariablesDict)
		return self
	def setWeight(self,_WeigthFloatsArray):
		self.J[:]=_WeigthFloatsArray.reshape(
				self.source.N*self.target.N
			)
		return self

#build network
BalanceNetwork=brian2.Network()

#build neuron groups
map(
	lambda __NeuronGroupStr:
	BalanceNetwork.add(
		brian2.NeuronGroup(
			N=UnitsInt
			if __NeuronGroupStr.startswith('Exc')
			else UnitsInt/4,
			model='''
				mu : volt
				dv/dt= ( -(v-(-60.*mV)) + mu + xi*sqrt(10.*ms)*0.*mV ) /(10.*ms) : volt
			''',
			threshold="v>-50*mV",
			reset="v=-70*mV",
			name=__NeuronGroupStr
		)
	),
	NeuronGroupStrsList	
)

#Debug
#print("BalanceNetwork['ExcNeuronGroup'] is ")
#print(BalanceNetwork['ExcNeuronGroup'])

#import 
import scipy.stats

#build synapses
map(
	lambda __NeuronTypeStrsTuple,__SynapsesStr:
	BalanceNetwork.add(
		SynapsesClass(
			BalanceNetwork[__NeuronTypeStrsTuple[0]+'NeuronGroup'],
			BalanceNetwork[__NeuronTypeStrsTuple[1]+'NeuronGroup'],
			model='''
				J:1
			''',
			pre="v+=J*mV",
			name=__SynapsesStr
		).connect(
			True
		).setWeight(
			ExcWeightFloat*scipy.stats.bernoulli.rvs(
				SparsityFloat,
				size=(
					BalanceNetwork[__NeuronTypeStrsTuple[0]+'NeuronGroup'].N,
					BalanceNetwork[__NeuronTypeStrsTuple[1]+'NeuronGroup'].N
				)
			)
			if __NeuronTypeStrsTuple[0]=='Exc'
			else
			-InhScaleFloat*ExcWeightFloat*scipy.stats.bernoulli.rvs(
				SparsityFloat,
				size=(
					BalanceNetwork[__NeuronTypeStrsTuple[0]+'NeuronGroup'].N,
					BalanceNetwork[__NeuronTypeStrsTuple[1]+'NeuronGroup'].N
				)
			)
		)
	),
	NeuronTypeStrsTuplesList,
	SynapsesStrsList
)

#Debug
#print("BalanceNetwork['ExcToExcSynapses'] is ")
#print(BalanceNetwork['ExcToExcSynapses'])
#print("BalanceNetwork['ExcToExcSynapses'].J is ")
#print(BalanceNetwork['ExcToExcSynapses'].J)

#build state monitor for v
map(
	lambda __NeuronGroupStr,__StateMonitorStr:
	BalanceNetwork.add(
		brian2.StateMonitor(
			BalanceNetwork[__NeuronGroupStr],
			'v',
			[0,1],
			name=__StateMonitorStr,
		)
	),
	NeuronGroupStrsList,
	StateMonitorStrsList
)

#build spike monitor
map(
	lambda __NeuronGroupStr,__SpikeMonitorStr:
	BalanceNetwork.add(
		brian2.SpikeMonitor(
			BalanceNetwork[__NeuronGroupStr],
			name=__SpikeMonitorStr
		)
	),
	NeuronGroupStrsList,
	SpikeMonitorStrsList
)

#/##################/#
# Define inputs
#

#map
map(
	lambda __NeuronGroupStr:
	BalanceNetwork.add(
		BalanceNetwork[__NeuronGroupStr].custom_operation(
			'''
				mu=15.*mV*(t>10.*ms)*(t<30.*ms)*(i>-1)*(i<50)
			'''
		)
	),
	NeuronGroupStrsList
)

#/##################/#
# Random initial values 
#

#map
map(
	lambda __NeuronGroupStr:
	setattr(
		BalanceNetwork[__NeuronGroupStr],
		'v',
		(
			-60.+scipy.stats.uniform.rvs(
				size=BalanceNetwork[__NeuronGroupStr].N
			)
		)*brian2.mV
	),
	NeuronGroupStrsList
)

#Debug
#print("BalanceNetwork['ExcNeuronGroup'].v")
#print(BalanceNetwork['ExcNeuronGroup'].v)

#/##################/#
# Run 
#

#run
BalanceNetwork.run(100.*brian2.ms)

#Debug
#print("BalanceNetwork['ExcStateMonitor'].v")
#print(BalanceNetwork['ExcStateMonitor'].v)
#print("BalanceNetwork['ExcSpikeMonitor'].i")
#print(BalanceNetwork['ExcSpikeMonitor'].i)

#/##################/#
# Plot
#

#dict
ColorDict={
	"Exc":"blue",
	"Inh":"red"
}

#import 
from matplotlib import pyplot

#init
Figure=pyplot.figure()

#init
StateAxes=Figure.add_subplot(211) 

#map
map(
	lambda __NeuronTypeStr,__StateMonitorStr:
	StateAxes.plot(
			BalanceNetwork[__StateMonitorStr].t,
			BalanceNetwork[__StateMonitorStr].v.T,
			color=ColorDict[__NeuronTypeStr],
			linewidth=3
		),
	NeuronTypeStrsList,
	StateMonitorStrsList
)
#init
SpikeAxes=Figure.add_subplot(212) 

#map
map(
	lambda __IndexInt,__NeuronTypeStr,__SpikeMonitorStr:
	SpikeAxes.plot(
			BalanceNetwork[__SpikeMonitorStr].t,
			BalanceNetwork[__SpikeMonitorStr].i+(
				BalanceNetwork[
					NeuronTypeStrsList[
						__IndexInt-1
					]+'NeuronGroup'
				].N
				if __IndexInt>0 else 0.
			),
			linestyle='',
			marker='o',
			color=ColorDict[__NeuronTypeStr],
			label='$'+__NeuronTypeStr+'$'
		),
	xrange(len(NeuronTypeStrsList)),
	NeuronTypeStrsList,
	SpikeMonitorStrsList
)
SpikeAxes.set_xlim(
	[
		BalanceNetwork['ExcStateMonitor'].t[0],
		BalanceNetwork['ExcStateMonitor'].t[-1]
	]
)
SpikeAxes.legend()

#show
pyplot.show()

