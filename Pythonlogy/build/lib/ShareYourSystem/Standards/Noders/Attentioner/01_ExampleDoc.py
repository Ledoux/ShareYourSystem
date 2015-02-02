
#ImportModules
import ShareYourSystem as SYS

#Definition of an instance
MyProducer=SYS.ProducerClass().produce(
			"Attentioners",
			['First','Second'],
			SYS.AttentionerClass,
		)

#attention
MyProducer['<Attentioners>FirstAttentioner'].grasp(
		'/NodePointDeriveNoder/<Attentioners>SecondAttentioner'
	).attention(
		#AttentioningCollectionStr
		'BackRelatome',
		#AttentioningUpdateVariable
		{'MyStr':"hello"}
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

