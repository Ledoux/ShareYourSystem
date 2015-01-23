
#ImportModules
import ShareYourSystem as SYS

#produce
MyProducer=SYS.ProducerClass().produce(
		'Nodome',
		['First','Second'],
		SYS.NoderClass,
		{'MyInt':0},
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

