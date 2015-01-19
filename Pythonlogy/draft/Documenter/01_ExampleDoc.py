
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Documenter

#Definition a Documenter instance
MyDocumenter=Documenter.DocumenterClass().document(
	True,
	**{
		'PackagingModuleVariable':'ShareYourSystem.Objects'
	}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyDocumenter is '+SYS._str(
		MyDocumenter,
		**{
			'RepresentingBaseKeyStrsListBool':False
			}
		)
	]
)  

#Print






