
#ImportModules
import ShareYourSystem as SYS

#Definition of an instance
MyProducer=SYS.ProducerClass().produce(
			"Catchers",
			['First','Second'],
			SYS.CatcherClass,
		)

#point
MyProducer['<Catchers>FirstCatcher'].grasp(
			'/NodePointDeriveNoder/<Catchers>SecondCatcher'
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

