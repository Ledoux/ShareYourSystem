
#ImportModules
import ShareYourSystem as SYS

#Definition of an instance
MyProducer=SYS.ProducerClass().produce(
			"Connecters",
			['First','Second'],
			SYS.ConnecterClass
		)

#connect
MyProducer['<Connecters>FirstConnecter'].connect(
	[
		'/NodePointDeriveNoder/<Connecters>SecondConnecter',
		SYS.GraspDictClass(**{'MyInt':0,'HintVariable':MyProducer['<Connecters>FirstConnecter']})
	],
	**{
		'CatchingCollectionStr':"PostRelatome",
		'AttentioningCollectionStr':"PreRelatome",
	}
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyProducer is '+SYS._str(
		MyProducer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

#Print

