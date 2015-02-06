
#ImportModules
import ShareYourSystem as SYS

#Definition a Pymongoer 
MyPymongoer=SYS.PymongoerClass().pymongo(
	**{
		'FolderingPathStr':SYS.Pymongoer.LocalFolderPathStr
	}
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyPymongoer.PymongoneClientVariable is '+str(
			MyPymongoer.PymongoneClientVariable)
	]
) 

#kill
MyPymongoer.PymongonePopenVariable.kill()




