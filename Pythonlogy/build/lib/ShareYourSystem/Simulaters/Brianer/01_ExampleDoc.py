
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Moniter,Populater,Brianer

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
			},
			'collect':
			{
				'LiargVariablesList':
				[
					'Spikome',
					'Spike',
					Moniter.MoniterClass()
				]
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
				map(
					lambda __PrefixStr:
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Populatome>'+__PrefixStr+'Populater',
							'SynapsesKwargVariablesDict':
							{
								'pre':'ge+=1.62*mV',
							},
							'ConnectProbabilityFloat':0.02
						}
					),
					['E','I']
				)
			},
			{
				'PopulatingUnitsInt':800,
				'ConnectingGraspClueVariablesList':
				map(
					lambda __PrefixStr:
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Populatome>'+__PrefixStr+'Populater',
							'SynapsesKwargVariablesDict':
							{
								'pre':'gi-=9*mV'
							},
							'ConnectProbabilityFloat':0.02
						}
					),
					['E','I']
				)
			}
		]
	).brian()
		
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


