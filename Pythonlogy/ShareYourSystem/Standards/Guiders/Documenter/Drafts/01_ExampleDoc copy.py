#ImportModules
import os
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Documenter


from ShareYourSystem import Interfacers

print(dir(Interfacers))
print(type(Interfacers))


"""
#Definition an Documenter instance
MyDocumenter=Documenter.DocumenterClass(**{
	'GuidingBookStr':'Doc',
	'DirectingFilterFunctionPointer':
		lambda _InstanceVariable,_FolderKeyStr:_FolderKeyStr.startswith('_'
		)==False
	}
)

#map
map(
	MyDocumenter.inform,
	[
		#os.getcwd()
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects/Object',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects/Caller'
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Objects',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Classors',
		SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Interfacers',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Guiders',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Itemizers',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Applyiers',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Walkers',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Noders',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Savers',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Databasers',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Ploters',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Tutorials',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Simulaters',
		#SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Muzikers',
	]
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyDocumenter is '+SYS._str(
		MyDocumenter,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

"""