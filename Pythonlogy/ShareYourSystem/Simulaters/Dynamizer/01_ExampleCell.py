
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Simulaters import Dynamizer

#Definition an instance
MyDynamizer=Dynamizer.DynamizerClass().dynamize()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyDynamizer is '+SYS._str(
		MyDynamizer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':['PopulatingEquationStr','DynamizedPostStr']
		}
		),
	]
) 

#Print

