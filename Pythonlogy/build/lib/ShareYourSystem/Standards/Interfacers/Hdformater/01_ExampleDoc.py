
#ImportModules
import ShareYourSystem as SYS

#Definition a Hdformater that writes an empty hdf file
MyHdformater=SYS.HdformaterClass(
	).hdformat(
		#HdformatingFileKeyStr
		'Hdformats.hdf5',
		**{
			'FolderingPathStr':SYS.Hdformater.LocalFolderPathStr
		}
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyHdformater.HdformatedConsoleStr is '+str(
			MyHdformater.hdfview()
		)
	]
) 

#close
MyHdformater.hdfclose()




