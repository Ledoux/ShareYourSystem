#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Filer

#Definition of an instance Filer and make it find the current dir
MyFiler=Filer.FilerClass().file('MyFile.txt','w',
	**{
	'FolderingPathStr':
	Filer.LocalFolderPathStr
	}
)

#close
MyFiler.FiledFileVariable.close()
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyFiler is '+SYS._str(MyFiler,
		**{'RepresentingAlineaIsBool':False})
	]
) 

#Print

