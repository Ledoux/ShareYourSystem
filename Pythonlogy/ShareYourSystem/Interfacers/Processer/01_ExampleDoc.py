#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Processer

#Definition of an instance Processer and make it print hello
MyProcesser=Processer.ProcesserClass().process('which python ',
	**{
	'FolderingPathStr':Processer.LocalFolderPathStr
	}
)
		
#Definition the AttestedStr
SYS._attest(
	[
		'MyProcesser is '+SYS._str(MyProcesser)
	]
) 

#Print

