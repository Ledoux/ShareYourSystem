
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Noder
from ShareYourSystem.Applyiers import Producer

#produce
MyProducer=Producer.ProducerClass().produce(
		['First','Second'],
		Noder.NoderClass,
		{'MyInt':0},
		**{'CollectingCollectionStr':'Nodome'}
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

