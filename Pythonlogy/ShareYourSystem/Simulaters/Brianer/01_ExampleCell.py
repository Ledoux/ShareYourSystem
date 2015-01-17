
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Populater,Brianer

#Definition
MyBrianer=Brianer.BrianerClass(
	).update(
		{
			'StimulatingStepTimeFloat':0.1
		}
	).produce(
		['E','I'],
		Populater.PopulaterClass,
		{
			'NeuronGroupArgumentVariable':{
				'LiargVariablesList':[
					3200,
					'''
						dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
						dge/dt = -ge/(5*ms) : volt
						dgi/dt = -gi/(10*ms) : volt
					'''
				],
				'KwargVariablesDict':
				{
					'threshold':'v>-50*mV'
					'reset':'v=-60*mV'
				}
			},
			'MonitorSpikeArgumentVariablesList':
			[
				[]
			],
			'PopulatingInitDict':
			{
				'v':-60.
			}
		},
		**{'CollectingCollectionStr':'Populatome'}
	).__setitem__(
		'Dis_<Populatome>',
		[
			{
				'PopulatingUnitsInt':3200,
				'ConnectingGraspClueVariablesList':
				[
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Populatome>IPopulater',
							'SynapseArgumentVariable':
							{
								'pre':'ge+=1.62*mV'
								'connect':{'p':0.02}
							}
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
							'HintVariable':'/NodePointDeriveNoder/<Populatome>EPopulater',
							'SynapseArgumentVariable':
							{
								'pre':'gi-=9*mV'
								'connect':{'p':0.02}
							}
						}
					)
				]
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


