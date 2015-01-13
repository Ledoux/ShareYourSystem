
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Storer
from ShareYourSystem.Applyiers import Producer

#produce
MyProducer=Producer.ProducerClass().produce(
		['First','Second'],
		Storer.StorerClass,
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

