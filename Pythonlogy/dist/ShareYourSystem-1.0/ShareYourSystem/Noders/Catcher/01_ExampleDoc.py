
#ImportModules
import ShareYourSystem as SYS

#Definition of an instance
MyProducer=SYS.ProducerClass().produce(
	"Catchers",
	['First','Second','Third','Four'],
	SYS.CatcherClass,
)

#Catch with a relative path 
MyProducer['<Catchers>FirstCatcher'].grasp(
		'/NodePointDeriveNoder/<Catchers>SecondCatcher'
	).catch(
		'Relatome',
		{'MyStr':"hello"}
	)

#Catch with a direct catch
MyProducer['<Catchers>FirstCatcher'].grasp(
		MyProducer['<Catchers>ThirdCatcher']
	).catch(
		'Relatome',
		{'MyInt':3}
)

#Catch with a CatchDict
MyProducer['<Catchers>FirstCatcher'].grasp(
	SYS.GraspDictClass(
		**{
		'HintVariable':'/NodePointDeriveNoder/<Catchers>FourCatcher',
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

