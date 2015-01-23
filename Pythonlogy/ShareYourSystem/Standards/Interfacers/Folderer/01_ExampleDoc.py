#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Interfacers import Folderer

#Definition of an instance Folderer and make it find the current dir
MyFolderer=Folderer.FoldererClass(
	).folder(
		Folderer.LocalFolderPathStr
	)
	
#If you don't have these folder, MyFolderer is going to create them for you
MyFolderer=Folderer.FoldererClass(
	).folder(
		MyFolderer.FolderingPathStr+'TestFolder1/TestFolder2/',
		True
	)	

#Definition the AttestedStr
SYS._attest(
	[
		'MyFolderer is '+SYS._str(MyFolderer,
		**{'RepresentingAlineaIsBool':False})
	]
) 

#Print
