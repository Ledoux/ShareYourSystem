
#ImportModules
import ShareYourSystem as SYS

#Definition an instance
MySynapser=Synapser.SynapserClass().run()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MySynapser is '+SYS._str(
		MySynapser,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		),
	]
) 
