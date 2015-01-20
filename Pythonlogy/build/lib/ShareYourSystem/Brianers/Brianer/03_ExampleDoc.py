
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Moniter,Populater,Brianer
import numpy as np

#Definition
MyBrianer=Brianer.BrianerClass(
	).collect(
		'Ratome',
		'P',
		Populater.PopulaterClass().update(
			{
				'NeuronGroupKwargDict':
				{
					'model':
					'''
						Jv : mV
						dv/dt = -r + np.atanh(Jv) : volt
					'''
				},

				'produce':
				{
					'LiargVariablesList':
					[
						['Rate'],
						Moniter.MoniterClass,
						{
							'MoniteringVariableStr':'v',
							'MoniteringIndexIntsList':[0,1]
						}
					],
					'KwargVariablesDict':
					{
						'CollectingCollectionStr':'Variablome'
					}
				},

				'PopulatingUnitsInt':2,

				'ConnectingGraspClueVariablesList':
				[
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Populatome>PPopulater',
							'SynapsesKwargVariablesDict':
							{
								'model':
								'''
									J : 1
									Jv : mV
									Jv = J*v_pre : mV
								'''
							},
							'PostVariableStrsList':['Jv']
						}
					)
				]
			}
		)
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
		0*brian2.mV
	),
	MyBrianer.BrianedNeuronGroupsList
)

#run
MyBrianer.run(1000)

#plot
M=MyBrianer['<Ratome>EPopulater']['<Variablome>RateMoniter'].StateMonitor
from matplotlib import pyplot
pyplot.plot(M.t/brian2.ms, M.i, '.')
pyplot.show()

#Print

