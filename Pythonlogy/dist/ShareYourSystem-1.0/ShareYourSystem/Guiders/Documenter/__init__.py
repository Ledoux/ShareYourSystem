# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Documenter export in the mkdoc the readme of a Module 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Guiders.Installer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import copy

from ShareYourSystem.Interfacers import Loader,Writer
#</ImportSpecificModules>

#<DefineLocals>
DocumentingSysFolderPathStr=SYS.ShareYourSystemLocalFolderPathStr
DocumentingLibraryFolderPathStr=DocumentingSysFolderPathStr+'/docs/LibraryReference/'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class DocumenterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'DocumentedModulePathStr',
								'DocumentedMkdocsList',
								'DocumentedModulePathStr'
							]

	def default_init(self,
						_DocumentingNewIsBool=False,
						_DocumentingMkdocWriteIsBool=True,
						_DocumentedMkdocsList=None,
						_DocumentedMkdocsDict=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		
	def do_document(self):
				
		#first package
		self.package()

		#map
		self.DocumentedModulePathStr=self.PackagedModuleStr.replace('.','/')
		self.DocumentedNameStr=self.DocumentedModulePathStr.split('/')[-1]

		#debug
		'''
		self.debug(('self.',self,[
							'DocumentedModulePathStr',
							'DocumentedNameStr'
							]))
		'''

		#Load the readmes and write them into the docs Library reference folder
		self.load(
			**{
				'FolderingPathStr':DocumentingSysFolderPathStr+'/'+self.DocumentedModulePathStr,
				'FilingKeyStr':'Readme.md',
				'LoadingFormatStr':'txt'
			}
		).write(
			**{
					'FolderingPathStr':DocumentingLibraryFolderPathStr,
					'FilingKeyStr':self.DocumentedNameStr+'.md',
					'WritingLoadBool':True
				}
		) 

		#Definition in the future yaml config mkdocs 
		self.DocumentedMkdocsList=[
				'docs'.join(
					DocumentingLibraryFolderPathStr.split('docs/')[1:]
				)+self.DocumentedNameStr+'.md',
				'Library Reference',
				self.DocumentedNameStr
			]

		#debug
		'''
		self.debug(('self.',self,[
									'DocumentedMkdocsList'
								]))
		'''


		#Definition
		self.load(
			**{
				'FolderingPathStr':SYS.ShareYourSystemLocalFolderPathStr+self.__class__.__module__.replace(
					'.','/')
				if self.DocumentingNewIsBool
				else DocumentingSysFolderPathStr,
				'FilingKeyStr':'mkdocs.yml',
				'LoadingFormatStr':'yaml'
			}
		)

		#Add to the pages
		self.LoadedReadVariable['pages'].append(self.DocumentedMkdocsList)

		#Copy
		self.DocumentedMkdocsDict=copy.copy(
			self.LoadedReadVariable
		)

		#debug
		'''
		self.debug(('self.',self,[
									'DocumentedMkdocsDict'
								]))
		'''

		if self.DocumentingMkdocWriteIsBool:

			#Close and write now in the top root folder
			self.write(
				self.DocumentedMkdocsDict,
				**{
					'FolderingPathStr':DocumentingSysFolderPathStr,
				}
			).FiledFileVariable.close()

		#Return self
		#return self

#</DefineClass>
