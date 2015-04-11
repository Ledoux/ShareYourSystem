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
BaseModuleStr="ShareYourSystem.Standards.Guiders.Nbconverter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import copy
from ShareYourSystem.Standards.Interfacers import Filer
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
	
	def default_init(self,
						_InstallingModuleStrsList=None,
						_InstallingAllBool=False,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def do_install(self):

		#/##################/#
		# First analyze all the modules
		#

		"""
		#folder
		self.folder(
				InstallingSysFolderPathStr
			)

		#Definition
		self.file(
			'setup.py',
			_ModeStr='r'
		)
		"""
		
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

#</DefinePrint>
InstallerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'InstallingModuleStrsList',
		'InstallingAllBool'
	]
)
#<DefinePrint>
