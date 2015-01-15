#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Nbconverter

#Definition a Nbconverter
MyNbconverter=Nbconverter.NbconverterClass().nbconvert(
			'Presentation.html',
			'Slide',
			**{
				'FolderingPathStr':
				SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects/Concluder',
				#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects',
				'GuidingBookStr':'Doc',
				'NotebookingFileKeyStr':'Presentation.ipynb'
			}
).nbconvert(
			**{
			'FolderingPathStr':
			SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Interfacers/Filer',
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


