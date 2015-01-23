
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Specials.Simulaters import Moniter,Populater,Brianer
from brian2 import *

#P.v=-60*mV
#M=SpikeMonitor(P)

#Definition
MyBrianer=Brianer.BrianerClass(
	).produce(
		['E','I'],
		Populater.PopulaterClass,
		#Here are defined the brian classic shared arguments for each pop
		{
			'NeuronGroupKwargDict':
			{
				'model':
				'''
					dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
					dge/dt = -ge/(5*ms) : volt
					dgi/dt = -gi/(10*ms) : volt
				''',
				'threshold':'v>-50*mV',
				'reset':'v=-60*mV'
			}
		},
		**{'CollectingCollectionStr':'Populatome'}
	).__setitem__(
		'Dis_<Populatome>',
		#Here are defined the brian classic specific arguments for each pop
		[
			{
				'PopulatingUnitsInt':3200,
				'ConnectingGraspClueVariablesList':
				[
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Populatome>IPopulater',
							'SynapsePreStr':'ge+=1.62*mV',
							'SynapseProbabilityFloat':0.02,
							'BrianClassStr':"Synapse"
						}
					)
				]
			},
			{
				'PopulatingUnitsInt':800,
				'ConnectingGraspClueVariablesList':
				[
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Populatome>IPopulater',
							'SynapsePreStr':'ge+=1.62*mV',
							'SynapseProbabilityFloat':0.02,
							'BrianClassStr':"Synapse"
						}
					)
				]
			}
		]
	).brian()

#add
MyBrianer.BrianedNetworkVariable.add(M)
		
#run
#MyBrianer.BrianedNetworkVariable.run(1*second)

#Definition the AttestedStr
SYS._attest(
	[
		'MyBrianer is '+SYS._str(
		MyBrianer,
		**{
			'RepresentingBaseKeyStrsList':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#import matplotlib
#plot(M.t/ms, M.i, '.')
#show()

#Print


