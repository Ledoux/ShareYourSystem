
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Celler

#Definition an instance
MyCeller=Celler.CellerClass().load(
	**{
		'FolderingPathStr':
		SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects/Rebooter',
		'FilingKeyStr':'01_ExampleDoc.py'
	}
)
MyCeller.cell(MyCeller.LoadedReadVariable,'Python')
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyCeller is '+SYS._str(
				MyCeller,
				**{
				'RepresentingBaseKeyStrsListBool':False,
				'RepresentingAlineaIsBool':False
				}
			)
	]
) 

