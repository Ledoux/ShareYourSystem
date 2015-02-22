#ImportModules
import ShareYourSystem as SYS
import operator

#Definition
MyBrianer=SYS.BrianerClass(
	).produce(
		"Neurongroupers",
		['E','I'],
		SYS.NeurongrouperClass,
		#Here are defined the brian classic shared arguments for each pop
		{
			'NeurongroupingKwargVariablesDict':
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
					"SpikeMoniters",
					['Spike'],
					SYS.MoniterClass
				]
			}		
		}
	).__setitem__(
		'Dis_<Neurongroupers>',
		#Here are defined the brian classic specific arguments for each pop
		[
			{
				'PopulatingUnitsInt':3200,
				'ConnectingGraspClueVariablesList':
				map(
					lambda __PrefixStr:
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Neurongroupers>'+__PrefixStr+'Neurongrouper',
							'SynapsingKwargVariablesDict':
							{
								'pre':'ge+=1.62*mV',
							},
							'SynapsingProbabilityVariable':0.02
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
							'HintVariable':'/NodePointDeriveNoder/<Neurongroupers>'+__PrefixStr+'Neurongrouper',
							'SynapsingKwargVariablesDict':
							{
								'pre':'gi-=9*mV'
							},
							'SynapsingProbabilityVariable':0.02
						}
					),
					['E','I']
				)
			}
		]
	).network(
			**{
				'RecruitingConcludeConditionVariable':[
					(
						'MroClassesList',
						operator.contains,
						SYS.NeurongrouperClass
					)
				]
			}
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
MyBrianer.run(300)

#plot
ME=MyBrianer['<Neurongroupers>ENeurongrouper']['<SpikeMoniters>SpikeMoniter'].SpikeMonitor
MI=MyBrianer['<Neurongroupers>INeurongrouper']['<SpikeMoniters>SpikeMoniter'].SpikeMonitor
from matplotlib import pyplot
pyplot.plot(ME.t/brian2.ms, ME.i, 'r.')
pyplot.plot(MI.t/brian2.ms, ME.source.N+MI.i, 'b.')
pyplot.show()

#Print

