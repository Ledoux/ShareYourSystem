
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
		'/NodePointDeriveNoder/<Connecters>FirstConnecter',
		SYS.GraspDictClass(**{
				'MyInt':0,
				'HintVariable':MyProducer['<Connecters>SecondConnecter'],
				'AttentionUpdateVariable':{
					'MyStr':"hello"
				}
			}
		)
	],
	"PostConnecters",
	"PreConnecters"
)

#connect
MyProducer['<Connecters>SecondConnecter'].connect(
	[
		'/NodePointDeriveNoder/<Connecters>SecondConnecter',
		SYS.GraspDictClass(**{
				'MyInt':0,
				'HintVariable':'/NodePointDeriveNoder/<Connecters>FirstConnecter',
				'AttentionUpdateVariable':{
					'MyStr':"bonjour"
				}
			}
		)
	],
	"PostConnecters",
	"PreConnecters"
)

#Print
SYS._print(
	[
		'MyProducer["<Connecters>FirstConnecter"].PostConnectersCollectionOrderedDict.keys() is',
		MyProducer['<Connecters>FirstConnecter'].PostConnectersCollectionOrderedDict.keys()
	]
)

#Print
SYS._print(
	[
		"MyProducer['<Connecters>FirstConnecter'].PreConnectersCollectionOrderedDict.keys() is",
		MyProducer['<Connecters>FirstConnecter'].PreConnectersCollectionOrderedDict.keys()
	]
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

