
#ImportModules
import ShareYourSystem as SYS

#Definition a Hdformater that writes an empty hdf file
MyHdformater=SYS.HdformaterClass().hdformat(
	_FileKeyStr='Hdformats.hdf5',
	**{
	'FolderingPathStr':SYS.Hdformater.LocalFolderPathStr
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



