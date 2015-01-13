#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Writer

#Definition of an instance Writer and make it find the current dir
MyWriter=Writer.WriterClass().write("hello",**{
	'FolderingPathStr':Writer.LocalFolderPathStr,
	'FilingKeyStr':'MyFile.txt',
	'FilingModeStr':'w'
	}
)
	
#Definition the AttestedStr
SYS._attest(
	[
		'MyWriter is '+SYS._str(MyWriter)
	]
) 

#Print

