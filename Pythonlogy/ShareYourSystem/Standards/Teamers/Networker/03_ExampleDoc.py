#ImportModules
import ShareYourSystem as SYS
import operator

#Definition of a brian structure
MyNetworker=SYS.NetworkerClass(
	).produce(
		'Connecters',
		["E","I"],
		SYS.ConnecterClass
	).__setitem__(
		'Dis_<Connecters>',
		#Here are defined the brian classic specific arguments for each pop
		[
			{
				'PopulatingUnitsInt':3200,
				'ConnectingGraspClueVariablesList':
				map(
					lambda __PrefixStr:
					SYS.GraspDictClass(
						{
							'HintVariable':'/NodePointDeriveNoder/<Connecters>'+__PrefixStr+'Connecter',
							'SynapsingKwargVariablesDict':
							{
								'pre':'ge+=1.62*mV',
							},
							'SynapsingProbabilityVariable':0.02,
							'PostModelInsertStrsList':['dge/dt = -ge/(5*ms) : volt'],
							'PostModelAddDict':{'v':['ge']}
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
							'HintVariable':'/NodePointDeriveNoder/<Connecters>'+__PrefixStr+'Connecter',
							'SynapsingKwargVariablesDict':
							{
								'pre':'gi-=9*mV'
							},
							'SynapsingProbabilityVariable':0.02,
							'PostModelInsertStrsList':['dgi/dt = -gi/(10*ms) : volt'],
							'PostModelAddDict':{'v':['gi']}
						}
					),
					['E','I']
					#[]
				)
			}
		]
		).network(
		**{
			'VisitingCollectionStrsList':["Networkers","Connecters"],
			'RecruitingConcludeConditionVariable':[
				('NameStr',operator.eq,'Connecter')
			]
		}
	)	

#Definition the AttestedStr
SYS._attest(
	[
		'MyNetworker is '+SYS._str(
		MyNetworker,
		**{
			'RepresentingBaseKeyStrsList':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 

#Print
