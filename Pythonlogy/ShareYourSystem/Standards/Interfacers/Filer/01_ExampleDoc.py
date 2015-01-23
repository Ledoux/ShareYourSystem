#ImportModules
import ShareYourSystem as SYS

#Definition of an instance Filer and make it find the current dir
MyFiler=SYS.FilerClass().file('MyFile.txt','w',
	**{
	'FolderingPathStr':
	SYS.Filer.LocalFolderPathStr
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

