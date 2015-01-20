
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
			'produce':
			{
				'LiargVariablesList':
				[
					['Spike'],
					Moniter.MoniterClass
				],
				'KwargVariablesDict':
				{
					'CollectingCollectionStr':'Spikome'
				}
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

#init
import brian2
map(
	lambda __BrianedNeuronGroup:
	__BrianedNeuronGroup.__setattr__(
		'v',
		-60*brian2.mV
	),
	MyBrianer.BrianedNeuronGroupsList
)

#run
MyBrianer.run(1000)

#plot
M=MyBrianer['<Populatome>EPopulater']['<Spikome>SpikeMoniter'].SpikeMonitor
from matplotlib import pyplot
pyplot.plot(M.t/brian2.ms, M.i, '.')
pyplot.show()

#Print


