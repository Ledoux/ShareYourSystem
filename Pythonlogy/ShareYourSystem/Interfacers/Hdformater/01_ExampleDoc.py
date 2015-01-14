
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Hdformater

#Definition a Hdformater that writes an empty hdf file
MyHdformater=Hdformater.HdformaterClass().hdformat(
	_FileKeyStr='Hdformats.hdf5',
	**{
	'FolderingPathStr':Hdformater.LocalFolderPathStr
}
).hdfview().hdfclose()

#Definition the AttestedStr
SYS._attest(
	[
		'MyHdformater.HdformatedStr is '+str(
			MyHdformater.HdformatedStr)
	]
) 

#Print



