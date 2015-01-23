
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Specials.Simulaters import Rater

#Definition an instance
MyRater=Rater.RaterClass().populate()
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyRater is '+SYS._str(
		MyRater,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False,
			'RepresentingKeyStrsList':[
				'PopulatingEquationStr',
				'DynamizedParamStr',
				'DynamizedPreStr',
				'DynamizedPostStr'
			]
		}
		),
	]
) 

#Print

