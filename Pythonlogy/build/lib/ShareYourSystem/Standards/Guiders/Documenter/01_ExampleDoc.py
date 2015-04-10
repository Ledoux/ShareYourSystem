#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Documenter

#Definition an Documenter instance
MyDocumenter=Documenter.DocumenterClass()

#Definition the AttestedStr
SYS._attest(
	[
		'MyDocumenter is '+SYS._str(
		MyDocumenter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

