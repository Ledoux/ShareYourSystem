
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Interfacers import Directer
import os

#Definition an instance 
MyDirecter=Directer.DirecterClass()

#Direct for displaying folders
'''
MyDirecter.direct(
			lambda _LiargVariablesList,_FolderPathStr,_FileKeyStrsList:
			Representer._print(_LiargVariablesList[0]+_FolderPathStr),
			["_FolderPathStr is "],
			**{'FolderingPathStr':'/'.join(SYS.__file__.split('/')[:-1])}
		)
'''	

#Delete things	
def delete(_LiargVariablesList,_FolderPathStr,_FileKeyStrsList):
	#os.popen('rm -r '+_FolderPathStr+'/Attests/')
	os.popen('rm '+_FolderPathStr+'/02_ClassCell.md')
	os.popen('rm '+_FolderPathStr+'/03_ClassCell.py')
	os.popen('rm '+_FolderPathStr+'/04_InstanceCell.md')
	os.popen('rm '+_FolderPathStr+'/05_InstanceCell.py')
def move(_LiargVariablesList,_FolderPathStr,_FileKeyStrsList):
	os.popen('mv '+_FolderPathStr+'/00_ExampleCell.md '+_FolderPathStr+'/00_ExampleDoc.md')
	os.popen('mv '+_FolderPathStr+'/01_ExampleCell.py '+_FolderPathStr+'/01_ExampleDoc.py')

MyDirecter=Directer.DirecterClass().direct(
			delete,
			[],
			**{
				'FolderingPathStr':
				SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Guiders/'
			}
		)

#Definition the AttestedStr
SYS._attest(
	[
		'MyDirecter is '+SYS._str(
				MyDirecter,
				**{
				'RepresentingBaseKeyStrsListBool':False
				}
			)
	]
) 

#Print

