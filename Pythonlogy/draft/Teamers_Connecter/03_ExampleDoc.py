
#ImportModules
import ShareYourSystem as SYS

#Definition of an instance
MyProducer=SYS.ProducerClass().produce(
			"Connecters",
			['E','I'],
			SYS.ConnecterClass
		)

#connect
MyProducer.__setitem__(
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
							}
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
							}
						}
					),
					['E','I']
				)
			}
		]
	)

#
ConnectedCatchDerivePointersList=SYS.flat(
	map(
		lambda __Connecter:
		__Connecter.connect(
			_CatchCollectionStr='PostConnecters',
			_AttentionCollectionStr='PreConnecters'
		).ConnectedCatchDerivePointersList,
		MyProducer['<Connecters>']
	)
)


SYS._print(
	map(
		lambda __Pointer:
		__Pointer['SynapsingKwargVariablesDict'],
		ConnectedCatchDerivePointersList
	)
)

#Print
SYS._print(
	[
		'MyProducer["<Connecters>EConnecter"].PostConnectersCollectionOrderedDict.keys() is',
		MyProducer['<Connecters>EConnecter'].PostConnectersCollectionOrderedDict.keys()
	]
)

#Print

