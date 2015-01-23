#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Objects import Caller

#Definition of a Caller instance
MyCaller=Caller.CallerClass()
	
#Call the _print from the Rep
MyCaller.call(
	_FunctionStr='represent',
	**{
		'PackagingModuleVariable':'ShareYourSystem.Standards.Classors.Representer',	
	}
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyCaller is '+SYS._str(
		MyCaller,
		**{
			'RepresentingBaseKeyStrsListBool':False
		}
		)
	]
) 

#Print

