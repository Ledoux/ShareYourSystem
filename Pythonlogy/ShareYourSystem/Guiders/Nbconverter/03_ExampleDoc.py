#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Nbconverter

#Definition a Nbconverter
MyNbconverter=Nbconverter.NbconverterClass().nbconvert(
			'Presentation.html',
			'Slide',
			**{
				'FolderingPathStr':
				SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Objects/Concluder',
				#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Objects',
				'GuidingBookStr':'Doc',
				'NotebookingFileKeyStr':'Presentation.ipynb'
			}
).nbconvert(
			**{
			'FolderingPathStr':
			SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Interfacers/Filer',
		}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyNbconverter is '+SYS._str(
		MyNbconverter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
			}
		)
	]
)  

#Print


