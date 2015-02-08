import ShareYourSystem as SYS
from brian2 import *
import numpy as np
import operator

#Definition
MyBrianer=SYS.BrianerClass(
	).collect(
		"Neurongroupers",
		'P',
		SYS.NeurongrouperClass(
			#Here are defined the brian classic shared arguments for each pop
			**{
				'NeurongroupingKwargVariablesDict':
				{
					'N':2,
					'model':
					'''
						Jr : 1
						dr/dt = (-r+Jr)/(20*ms) : 1
					'''
				},
				'ConnectingGraspClueVariablesList':
				[
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Neurongroupers>PNeurongrouper',
							'SynapsingKwargVariablesDict':
							{
								'model':
								'''
									J : 1
									Jr_post=J*r_pre : 1 (summed)
								'''
							},
							'SynapsingWeigthSymbolStr':'J',
							'SynapsingWeigthFloatsArray':np.array(
								[
									[0.,-2.],
									[4.,0.]
								]
							)
						}
					)
				]		
			}
		).collect(
			"StateMoniters",
			'Rate',
			SYS.MoniterClass(
				**{
					'MoniteringVariableStr':'r',
					'MoniteringRecordTimeIndexIntsArray':[0,1]
					}
				)
		)
	).network(
			**{
				'RecruitingConcludeConditionTuplesList':[
					(
						'MroClassesList',
						operator.contains,
						SYS.NeurongrouperClass
					)
				]
			}
	).brian()


import brian2
map(
	lambda __BrianedNeuronGroup:
	__BrianedNeuronGroup.__setattr__(
		'r',
		1.+np.array(map(float,xrange(__BrianedNeuronGroup.N)))
	),
	MyBrianer.BrianedNeuronGroupsList
)

#run
MyBrianer.run(100)

#plot
M=MyBrianer['<Neurongroupers>PNeurongrouper']['<StateMoniters>RateMoniter'].StateMonitor
from matplotlib import pyplot
pyplot.plot(M.t/brian2.ms, M.r.T)
pyplot.show()


