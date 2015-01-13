
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Applyier

#Definition an applyier instance
MyApplyier=Applyier.ApplyierClass()

#Apply just a set... (even if we can do shorter !)
MyApplyier.apply(
	'__setitem__',
	{'LiargVariablesList':['MyStr','Hello']}
)

#Apply an apply is possible
MyApplyier.apply(
	'__setitem__',
	{'LiargVariablesList':[
			'__setitem__',
			{
				'LiargVariablesList':
				['MyNotLostStr','ben he']
			}
		]
	}
)
		
#Definition the AttestedStr
SYS._attest(
	[
	'MyApplyier is '+SYS._str(
			MyApplyier,
			**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
	]
) 

#Print

