#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Notebooker

#Definition a Notebooker
MyNotebooker=Notebooker.NotebookerClass(
	).package(
		'ShareYourSystem.Objects.Concluder'
	).scriptbook(
		**{
			'GuidingBookStr':'Doc'
		}
	).notebook(
		'Presentation.ipynb'
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyNotebooker is '+SYS._str(
		MyNotebooker,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
)  

#Print




