#ImportModules
import os
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Informer


from ShareYourSystem import Interfacers

print(dir(Interfacers))
print(type(Interfacers))


"""
#Definition an Informer instance
MyInformer=Informer.InformerClass(**{
	'GuidingBookStr':'Doc',
	'DirectingFilterFunctionPointer':
		lambda _InstanceVariable,_FolderKeyStr:_FolderKeyStr.startswith('_'
		)==False
	}
)

#map
map(
	MyInformer.inform,
	[
		#os.getcwd()
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Objects/Object',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Objects/Caller'
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Objects',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Classors',
		SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Interfacers',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Guiders',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Itemizers',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Applyiers',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Walkers',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Noders',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Savers',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Databasers',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Ploters',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Tutorials',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Simulaters',
		#SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Muzikers',
	]
)

#Definition the AttestedStr
SYS._attest(
	[
		'MyInformer is '+SYS._str(
		MyInformer,
		**{
			'RepresentingBaseKeyStrsListBool':False,
			'RepresentingAlineaIsBool':False
		}
		)
	]
) 

"""