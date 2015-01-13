# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Informer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Guiders.Documenter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import os
import copy
import sys
from ShareYourSystem.Classors import Doer
from ShareYourSystem.Guiders import Celler
Readmer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
InformingOntologyLocalFolderPathStr=SYS.LocalShareYourSystemFolderPathStr+'Ouvaton/'
InformingNbviewerLocalFolderPathStr=SYS.LocalShareYourSystemFolderPathStr+'Ouvaton/'
InformingDocumentLocalFolderPathStr=SYS.LocalShareYourSystemFolderPathStr+'docs/LibraryReference/'
InformingOntologyOuvatonFolderPathStr='/httpdocs/reveal/'
InformingNbviewerOuvatonFolderPathStr='/httpdocs/ipython/'
#</DefineLocals>

#<DefineFunctions>
def getInformedReadmeInstanceVariableWithFolderPathStr(
		_InstanceVariable,_FolderPathStr
	):

	#file first
	return _InstanceVariable.notebook(
			**{
				'FolderingPathStr':_FolderPathStr,
				'GuidingBookStr':"Doc",
				'NotebookingFileKeyStr':"Presentation.ipynb"
			}
	).nbconvert("Readme.md")
#</DefineFunctions>


#<DefineClass>
@DecorationClass()
class InformerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'InformingConceptFolderPathStr',
								'InformingSubReadmeIsBool',
								'InformingConceptReadmeIsBool',
								'InformingConceptDocumentIsBool',
								'InformingConceptSlideIsBool',
								'InformedConceptModule',
								'InformedConceptModuleStr',
								'InformedConceptModuleFolderPathStr',
								'InformedSubNameStrsList',
								'InformedSubModulesList',
								'InformedSubModuleStrsList',
								'InformedSubModuleLocalFolderPathStrsList',
								#'InformedPresentationsDictsList',
								#'InformedConceptNotebookDict'
							]

	def default_init(self,
						_InformingConceptFolderPathStr="",
						_InformingSubReadmeIsBool=True,
						_InformingConceptReadmeIsBool=True,
						_InformingConceptDocumentIsBool=True,
						_InformingConceptSlideIsBool=True,
						_InformedConceptModule=None,
						_InformedConceptModuleStr="",
						_InformedConceptModuleFolderPathStr="",
						_InformedSubNameStrsList=None,
						_InformedSubModulesList=None,
						_InformedSubModuleStrsList=None,
						_InformedSubModuleLocalFolderPathStrsList=None,
						_InformedPresentationsDictsList=None,
						_InformedConceptNotebookDict=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_inform(self):
		
		#debug
		'''
		self.debug(('self.',self,['InformingSubReadmeIsBool','InformingConceptDocumentIsBool']))
		'''

		#install first
		self.install()

		#Check
		if self.InformingConceptFolderPathStr=="":
			self.InformingConceptFolderPathStr='ShareYourSystem'.join(
				os.getcwd().split('ShareYourSystem')[:-1]
			)+'ShareYourSystem/'

		#debug
		'''
		self.debug(('self.',self,['InformingConceptFolderPathStr']))
		'''

		#debug
		self.folder(self.InformingConceptFolderPathStr)
		self.InformedConceptModuleStr=self.FolderedModuleStr

		#debug
		'''
		self.debug(('self.',self,['FolderedDirKeyStrsList']))
		'''

		#filter
		self.InformedSubNameStrsList=SYS._filter(
			lambda __FolderedDirKeyStr:
			os.path.isdir(
				self.FolderingPathStr+__FolderedDirKeyStr
			) and __FolderedDirKeyStr in Doer.DoerStrToDoStrOrderedDict.keys(),
			self.FolderedDirKeyStrsList
		)	

		#debug
		'''
		self.debug(('self.',self,['InformedSubNameStrsList','InstalledNameStrsList']))
		'''
		
		#sort
		self.InformedSubNameStrsList=SYS._filter(
				lambda __InstalledNameStr:
				__InstalledNameStr in self.InformedSubNameStrsList,
				self.InstalledNameStrsList
			)
		#map
		self.InformedSubModuleStrsList=map(
			lambda __InformedSubNameStr:
			self.InformedConceptModuleStr+'.'+__InformedSubNameStr,
			self.InformedSubNameStrsList
		)	

		#Check
		self.InformedConceptNameStr=self.FolderingPathStr.split(
					'/'
			)[-1] if self.FolderingPathStr[-1]!='/' else self.FolderingPathStr.split('/'
			)[-2]

		#debug
		'''
		self.debug(('self.',self,[
									'InformedSubNameStrsList',
									'InformedSubModuleStrsList',
									'InformedConceptNameStr'
								]))
		'''

		#check
		if self.InformedConceptNameStr in SYS.PluralStrToSingularStrOrderedDict.keys():
			self.InformedConceptModule=self.package(
				self.FolderedModuleStr
			).PackagedModuleVariable
		self.InformedConceptModuleFolderPathStr='/'.join(
			self.InformedConceptModule.__file__.split(
			'/'
			)[:-1]
		)+'/'

		#debug
		'''
		self.debug(('self.',self,['InformedConceptModule']))
		'''

		#filter
		self.InformedSubModulesList=SYS._filter(
				lambda __AttributeValueVariable:
				type(__AttributeValueVariable).__name__=='module',
				self.InformedConceptModule.__dict__.values()
			)

		#debug
		'''
		self.debug((
					'self.',self,[
							'InformedSubModulesList'
						]
					))
		'''

		#Check
		if self.InformingSubReadmeIsBool:

			#debug
			'''
			self.debug(
						[
							'we build sub modules readmes here',
							('self.',self,['InformedSubModuleStrsList'])
						]
					)
			'''

			#map
			map(
					lambda __InformedSubModuleStr:
					self.package(
							__InformedSubModuleStr
						).scriptbook(
						_GuideTuplesList=[
								('001','Document','Markdown'),
							],
							**{
								'GuidingBookStr':"Doc",
							}
						).notebook(
							"PreReadme.ipynb"
						).nbconvert(
							"Readme.md"
						),
					self.InformedSubModuleStrsList
				)
			
		#Check
		if self.InformingConceptSlideIsBool:
			
			#debug
			'''
			self.debug(
						[
							'we slide here',
							('self.',self,['InformedSubModuleStrsList'])
						]
						)
			'''

			#map
			map(
					lambda __InformedSubModuleStr:
					self.package(
							__InformedSubModuleStr
						).scriptbook(
						_GuideTuplesList=[
								('001','Document','Markdown'),
								('002','Github','Markdown'),
							],
							**{
								'GuidingBookStr':"Doc",
							}
						).notebook(
							"Presentation.ipynb",
							**{'WritingLoadBool':False}
						).nbconvert(
							"Presentation.html",
							'Slide'
						),
					self.InformedSubModuleStrsList
				)
			
			#mv for Nbviewer ipython notebooks
			map(
					lambda __InformedSubModuleStr:
					os.popen(
						'cp '+sys.modules[
							__InformedSubModuleStr
						].LocalFolderPathStr+'Presentation.ipynb '+InformingNbviewerLocalFolderPathStr+__InformedSubModuleStr.split(
								'.'
							)[-1]+'.ipynb'
					),
					self.InformedSubModuleStrsList
				)

			#mv for Ouvaton slide in html
			map(
					lambda __InformedSubModuleStr:
					os.popen(
						'cp '+sys.modules[
							__InformedSubModuleStr
						].LocalFolderPathStr+'Presentation.html '+InformingOntologyLocalFolderPathStr+__InformedSubModuleStr.split(
								'.'
							)[-1]+'.html'
					),
					self.InformedSubModuleStrsList
				)

			#mv for Ouvaton slide in php
			map(
					lambda __InformedSubModuleStr:
					os.popen(
						'cp '+sys.modules[
							__InformedSubModuleStr
						].LocalFolderPathStr+'Presentation.html '+InformingOntologyLocalFolderPathStr+__InformedSubModuleStr.split(
								'.'
							)[-1]+'.php'
					),
					self.InformedSubModuleStrsList
				)

			#map
			self.InformedSubModuleLocalFolderPathStrsList=map(
					lambda __InformedSubModuleStr:
					SYS.LocalShareYourSystemFolderPathStr+__InformedSubModuleStr.replace(
						'.','/'
					),
					self.InformedSubModuleStrsList
				)

			#map
			self.InformedPresentationsDictsList=map(
					lambda __InformedSubModuleFolderPathStr:
					self.load(
						**{
							'FolderingPathStr':__InformedSubModuleFolderPathStr,
							'FilingKeyStr':'Presentation.ipynb',
							'LoadingFormatStr':'json'
						}
					).close(
					).LoadedReadVariable,
					self.InformedSubModuleLocalFolderPathStrsList
				)					

			#debug
			'''
			self.debug(
						'self.InformedPresentationsDictsList is '+SYS._str(self.InformedPresentationsDictsList)
					)
			'''

			#copy
			self.InformedConceptNotebookDict=copy.copy(Celler.CellingInitDict)

			#flat
			InformedFlatPresentationsDictsList=SYS.flat(
					map(
							lambda __InformedPresentationsDict:
							copy.deepcopy(
								__InformedPresentationsDict['worksheets'][0]['cells']
								),
							self.InformedPresentationsDictsList
						)
					)

			#Flat all the presentations
			self.InformedConceptNotebookDict['worksheets']=[
				{
					'cells':map(
						lambda __InformedFlatPresentationsDict,__IndexInt:
						dict(__InformedFlatPresentationsDict,**{
							'prompt_number':__IndexInt}),
						InformedFlatPresentationsDictsList,
						xrange(len(InformedFlatPresentationsDictsList))
					)
				}
			]

			#debug
			'''
			self.debug(('self.',self,['InformedConceptNotebookDict']))
			'''

			#Write
			self.write(
				self.InformedConceptNotebookDict,
				**{
					'FolderingPathStr':self.InformingConceptFolderPathStr,
					'FilingKeyStr':'Concept'+self.GuidingBookStr+'.ipynb',
					'LoadingFormatStr':'json'
				}
			).close()


			#nbconvert
			self.NotebookedCodeDict=self.InformedConceptNotebookDict
			self.nbconvert(
				_FormatStr='Slide',
				**{
					'FolderingPathStr':self.InformingConceptFolderPathStr,
					'NotebookingFileKeyStr':'Concept'+self.GuidingBookStr+'.ipynb'
				}
			)

			#set
			self.InformedSlideLocalFilePathStr=InformingOntologyLocalFolderPathStr+self.InformedConceptModule.__name__.split('.')[-1]+'.html'

			#cp
			os.popen('cp '+self.FiledPathStr+' '+self.InformedSlideLocalFilePathStr+self.InformedConceptModule.__name__.split('.')[-1]+'.ipynb')

			#mv with .html extension
			os.popen(
					'cp '+self.FiledPathStr.replace(
					'.ipynb',
					'.html'
					)+' '+self.InformedSlideLocalFilePathStr
				)

			#mv with .php extension
			os.popen(
					'mv '+self.FiledPathStr.replace(
					'.ipynb',
					'.html'
					)+' '+self.InformedSlideLocalFilePathStr.replace('.html','.php')
				)

			#deploy
			self.deploy(
				_ClientFilePathStrToServerFilePathStrOrderedDict=collections.OrderedDict(
					[
						(
							self.InformedSlideLocalFilePathStr,
							InformingOntologyOuvatonFolderPathStr+self.InformedConceptModule.__name__.split('.'
								)[-1]+'.php'
						)
					]
				)
			)

		#Check
		if self.InformingConceptReadmeIsBool:

			#debug
			'''
			self.debug('we build the concept readme here')
			'''

			#import submodules
			'''
			map(
					lambda __InformedSubModuleStr:
					importlib.import_modules(__InformedSubModuleStr),
					self.InformedSubModuleStrsList
				)
			'''

			#readme
			self.package(
					self.InformedConceptModuleStr
				).scriptbook(
					_GuideTuplesList=[
						('001','Document','Markdown'),
						('002','Ouvaton','Markdown'),
						('1','Github','Markdown'),
					],
					**{'GuidingBookStr':"Doc"}
				)

			#notebook
			self.scriptbook(
					_GuideTuplesList=[]
				).notebook(
					"PreReadme.ipynb"
				).nbconvert(
					"Readme.md",
					'Markdown',
			)

		#Check
		if self.InformingConceptDocumentIsBool:

			#debug
			'''
			self.debug(
						[
							'we document here',
							('self.',self,['InformedConceptModuleFolderPathStr'])
						]
					)
			'''

			'''
			#document
			self.document(
				**{'PackagingModuleVariable':self.InformedConceptModuleStr}
			)	
			'''

			#package
			self.package(self.InformedConceptModuleStr)

			#mv with .php extension
			os.popen(
					'cp '+self.PackagedLocalFolderPathStr+'Readme.md  '+InformingDocumentLocalFolderPathStr+self.InformedConceptModuleStr.split('.')[-1]+'.md'
				)

			#Return self
			#return self

#</DefineClass>