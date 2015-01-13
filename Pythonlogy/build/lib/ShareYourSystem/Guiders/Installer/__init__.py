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
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import copy

from ShareYourSystem.Interfacers import Loader,Writer
#</ImportSpecificModules>

#<DefineLocals>
InstallingSysFolderPathStr=SYS.LocalShareYourSystemFolderPathStr
InstallingLibraryFolderPathStr=InstallingSysFolderPathStr+'/docs/LibraryReference/'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
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
				'FolderingPathStr':InstallingSysFolderPathStr,
				'FilingKeyStr':'setup.py'
			}
		)

		#chunk to set the InstalledModuleStrsList
		InstalledPackageStr=SYS.chunk(
			['packages=[','],'],self.LoadedReadVariable
		)[0]
		InstalledTextStrsList=InstalledPackageStr.split('\n')
		InstalledTextStrListsList=SYS._filter(
			lambda __InstalledChunkList:
			len(__InstalledChunkList)>0,
			map(
					lambda __InstalledTextStr:
					SYS.chunk(
						["'ShareYourSystem","',"],
						__InstalledTextStr
					),
					InstalledTextStrsList
			)
		)

		self.InstallingModuleStrsList=map(
			lambda __InstalledTextStrList:
			('ShareYourSystem'+__InstalledTextStrList[0])
			if __InstalledTextStrList[0]!="'"
			else 'ShareYourSystem',
			InstalledTextStrListsList
		)

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

		#Return self
		#return self

#</DefineClass>
