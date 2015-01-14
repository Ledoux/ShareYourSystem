
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Attentioner

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
			['First','Second'],
			Attentioner.AttentionerClass,
			**{'CollectingCollectionStr':"Pointome"}
		)

#attention
MyProducer['<Pointome>FirstAttentioner'].grasp(
		'/NodePointDeriveNoder/<Pointome>SecondAttentioner'
	).attention(
		'BackRelatome'
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

