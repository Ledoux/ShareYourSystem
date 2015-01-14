
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Catcher

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
	['First','Second','Third','Four'],
	Catcher.CatcherClass,
	**{'CollectingCollectionStr':"Pointome"}
)

#Catch with a relative path 
MyProducer['<Pointome>FirstCatcher'].grasp(
		'/NodePointDeriveNoder/<Pointome>SecondCatcher'
	).catch(
		'Relatome',
		{'MyStr':"hello"}
	)

#Catch with a direct catch
MyProducer['<Pointome>FirstCatcher'].grasp(
		MyProducer['<Pointome>ThirdCatcher']
	).catch(
		'Relatome',
		{'MyInt':3}
)

#Catch with a CatchDict
MyProducer['<Pointome>FirstCatcher'].grasp(
	SYS.GraspDictClass(
		**{
		'HintVariable':'/NodePointDeriveNoder/<Pointome>FourCatcher',
		'MyFloat':5.5
		}
	)
	).catch(
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

