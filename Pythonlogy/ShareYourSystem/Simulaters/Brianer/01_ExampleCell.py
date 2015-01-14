
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Populater,Brianer

#Definition
MyBrianer=Brianer.BrianerClass(
	).produce(
		['E','I'],
		Populater.PopulaterClass,
		[
			{
				'PopulatingEquationStr':
				'''
					dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
					dge/dt = -ge/(5*ms) : volt
					dgi/dt = -gi/(10*ms) : volt
				''',
			
				'PopulatingThresholdStr':'v>-50*mV',

				'PopulatingResetStr':'v=-60*mV',
			
				'MoniteringTrackTuplesList':
				[
					('Spike')
				],
	
				'PopulatingInitDict':
				{
					'v':-60.
				}
			}
		],
		**{'CollectingCollectionStr':'Populatome'}
	).__setitem__(
		'Dis_<Populatome>',
		[
			[
				{
					'PopulatingUnitsInt':3200,
				
					'PopulatingCommunicationDictsList':
					[
						{
							'CommunicationKeyStr':'E to I',
							'CatchGetStr':'/NodePointDeriveNoder/<Populatome>IPopulater',
							'SynapsePreStr':'ge+=1.62*mV',
							'SynapseProbabilityFloat':0.02
						}
					]
				}
			],
			[
				{
					'PopulatingUnitsInt':800,
				
					'PopulatingCommunicationDictsList':
					[
						{
							'CommunicationKeyStr':'I to E',
							'CatchGetStr':'/NodePointDeriveNoder/<Populatome>EPopulater',
							'SynapsePreStr':'gi-=9*mV',
							'SynapseProbabilityFloat':0.02
						}
					]
				}
			]
		]
	).run(2.)	
		
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

SYS._print(
	MyBrianer.BrianedNeuronGroupsList[0].__dict__
)

#import matplotlib
#plot(MyBrianer['<Connectome>FirstRater'].)

#Print


