
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Moniter,Populater,Brianer
import brian

#Set a neuron group
TotalNeuronGroup=brian.NeuronGroup(
			4000,
			'''
				dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
				dge/dt = -ge/(5*ms) : volt
				dgi/dt = -gi/(10*ms) : volt
			''',
			threshold='v>-50*mV',
			reset='v=-60*mV'
		)
TotalNeuronGroup.v=-60*brian.mV
TotalSpikeMonitor=brian.SpikeMonitor(TotalNeuronGroup)

#Definition
MyBrianer=Brianer.BrianerClass(
	).update(
		{
			#Set here the global net parameters
			'StimulatingStepTimeFloat':0.1
		}
	).produce(
		['E','I'],
		Populater.PopulaterClass,
		{
			#Here are the settig of future brian monitors
			'collect':
			{
				'LiargVariablesList':
				[
					'Spikome',
					'Spike',
					Moniter.MoniterClass()
				],
			}
		},
		**{'CollectingCollectionStr':'Populatome'}
	).__setitem__(
		'Dis_<Populatome>',
		#Here are defined the brian classic specific arguments for each pop
		[
			{
				'PopulatingUnitsInt':3200,
				'NeuronGroup':TotalNeuronGroup
			},
			{
				'PopulatingUnitsInt':800,
				'NeuronGroup':TotalNeuronGroup
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

#SYS._print(MyBrianer.BrianedMonitorsList[0].__dict__)

#SYS._print(
#	MyBrianer.BrianedNeuronGroupsList[0].__dict__
#)

#import matplotlib
#plot(MyBrianer['<Connectome>FirstRater'].)

#Print


