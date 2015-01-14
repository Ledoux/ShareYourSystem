
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Connecter

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
			['First','Second'],
			Connecter.ConnecterClass,
			**{'CollectingCollectionStr':"Connectome"}
		)

#connect
MyProducer['<Connectome>FirstConnecter'].connect(
	[
		'/NodePointDeriveNoder/<Connectome>SecondConnecter'
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

