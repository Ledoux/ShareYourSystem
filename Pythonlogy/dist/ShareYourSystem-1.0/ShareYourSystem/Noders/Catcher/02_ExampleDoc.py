
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Catcher

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
	['First','Second','Third'],
	Catcher.CatcherClass,
	**{'CollectingCollectionStr':"Pointome"}
)

#Catch with a relative path 
MyProducer['<Pointome>FirstCatcher'].catch(
	'/NodePointDeriveNoder/<Pointome>SecondCatcher',
	'Relatome'	
)

#Catch with an absolute path 
MyProducer['<Pointome>FirstCatcher'].catch(
	MyProducer['<Pointome>ThirdCatcher'],
	'Relatome'	
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

