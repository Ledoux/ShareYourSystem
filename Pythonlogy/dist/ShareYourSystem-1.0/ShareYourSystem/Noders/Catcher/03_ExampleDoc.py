
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Catcher

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
			['First','Second'],
			Catcher.CatcherClass,
			**{'CollectingCollectionStr':"Pointome"}
		)

#point
MyProducer['<Pointome>FirstCatcher'].grasp(
			'/NodePointDeriveNoder/<Pointome>SecondCatcher'
		).catch(
			_PointBackSetStr='MyBackVariable',
			**{
				'CollectingCollectionStr':'Relatome',
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

