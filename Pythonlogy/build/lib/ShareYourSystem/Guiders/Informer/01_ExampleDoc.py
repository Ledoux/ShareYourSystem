#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Informer

#Definition an Informer instance
MyInformer=Informer.InformerClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MyInformer is '+SYS._str(
		MyInformer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

