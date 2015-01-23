
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Scriptbooker

#Definition of a Scriptbooker
MyScriptbooker=Scriptbooker.ScriptbookerClass(
	).package(
		"ShareYourSystem.Standards.Objects.Object"
	).scriptbook(
		**{
			'GuidingBookStr':'Doc'
		}
	)

#Definition the AttestedStr
SYS._attest(
	[
		'MyScriptbooker is '+SYS._str(
				MyScriptbooker,
				**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
				}
		)
	]
) 

#Print

