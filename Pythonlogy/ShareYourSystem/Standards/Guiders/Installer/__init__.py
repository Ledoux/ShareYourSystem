# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Installer collects ModuleStrs to write 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Guiders.Nbconverter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import copy
from ShareYourSystem.Standards.Interfacers import Loader,Writer
#</ImportSpecificModules>

#<DefineLocals>
InstallingSysFolderPathStr=SYS.PythonlogyLocalFolderPathStr
InstallingLibraryFolderPathStr=InstallingSysFolderPathStr+'/docs/LibraryReference/'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['install']
})
class InstallerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'InstallingModuleStrsList',
									'InstallingAllBool'
								]

	def default_init(self,
						_InstallingModuleStrsList=None,
						_InstallingAllBool=False,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		
	def do_install(self):

		#Definition
		self.load(
			**{
				'FolderingPathVariable':InstallingSysFolderPathStr,
				'FilingKeyStr':'setup.py'
			}
		)

		#chunk to set the InstalledModuleStrsList
		if len(self.InstallingModuleStrsList)==0:
			self.InstallingModuleStrsList=SYS.lib()

		#debug
		'''
		self.debug(('self.',self,['InstallingModuleStrsList']))
		'''
		
		#map
		self.InstalledModulePathStrsList=map(
			lambda __InstallingModuleStr:
			__InstallingModuleStr.replace('.','/'),
			self.InstallingModuleStrsList
		)

		#debug
		'''
		self.debug(('self.',self,['InstalledModulePathStrsList']))
		'''
		
		#set with all the NameStrs
		self.InstalledNameStrsList=map(
					lambda __InstalledModulePathStr:
					__InstalledModulePathStr.split('/')[-1],
					self.InstalledModulePathStrsList
			)
#</DefineClass>
