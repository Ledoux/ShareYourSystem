# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Installer directs a readme call in a ShareYourSystem directory. 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Guiders.Installer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import copy
import sys

from ShareYourSystem.Standards.Classors import Doer
from ShareYourSystem.Guiders import Celler
Readmer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
DocumentingOntologyFolderPathStr=SYS.ShareYourSystemLocalFolderPathStr+'/reveal/'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class DocumenterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'DocumentingConceptFolderPathStr',
								'DocumentingReadmeIsBool',
								'DocumentingConceptIsBool',
								'DocumentedConceptModule',
								'DocumentedNameStrsList',
								'DocumentedModulePathStrsList',
								'DocumentedModulesList',
								#'DocumentedPresentationsDictsList',
								#'DocumentedConceptNotebookDict'
							]

	def default_init(self,
						_DocumentingConceptFolderPathStr="",
						_DocumentingReadmeIsBool=True,
						_DocumentingConceptIsBool=True,
						_DocumentedConceptModule=None,
						_DocumentedNameStrsList=None,
						_DocumentedModulePathStrsList=None,
						_DocumentedModulesList=None,
						_DocumentedPresentationsDictsList=None,
						_DocumentedConceptNotebookDict=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_inform(self):
		
		#debug
		self.debug(('self.',self,['DocumentingReadmeIsBool','DocumentingConceptIsBool']))

		#install first
		self.install()

		#Check
		if self.DocumentingConceptFolderPathStr=="":
			self.DocumentingConceptFolderPathStr='ShareYourSystem'.join(
				os.getcwd().split('ShareYourSystem')[:-1]
			)+'ShareYourSystem/'

		#debug
		'''
		self.debug(('self.',self,['DocumentingConceptFolderPathStr']))
		'''

		"""
		#direct the Install command
		self.direct(
						lambda _LiargVariablesList,_FolderPathStr,_FileKeyStrsList:
						self.readme(
							**{
								'FolderingPathStr':_FolderPathStr
							}
						) if '__init__.py' in _FileKeyStrsList and _FolderPathStr.startswith('_'
						)==False else None
						,[],
						**{'FolderingPathStr':self.DocumentingConceptFolderPathStr}
					)
		"""

		#debug
		self.folder(self.DocumentingConceptFolderPathStr)

		#debug
		'''
		self.debug(('self.',self,['FolderedDirKeyStrsList']))
		'''

		#filter
		self.DocumentedNameStrsList=SYS._filter(
			lambda __FolderedDirKeyStr:
			os.path.isdir(
				self.FolderingPathStr+__FolderedDirKeyStr
			) and __FolderedDirKeyStr in Doer.DoerStrToDoStrOrderedDict.keys(),
			self.FolderedDirKeyStrsList
		)	

		#debug
		'''
		self.debug(('self.',self,['DocumentedNameStrsList','InstalledNameStrsList']))
		'''
		
		#sort
		self.DocumentedNameStrsList=SYS._filter(
				lambda __InstalledNameStr:
				__InstalledNameStr in self.DocumentedNameStrsList,
				self.InstalledNameStrsList
			)
		#map
		self.DocumentedModulePathStrsList=map(
			lambda __DocumentedNameStr:
			self.FolderingPathStr+__DocumentedNameStr+'/',
			self.DocumentedNameStrsList
		)	

		#debug
		'''
		self.debug(('self.',self,[
									'DocumentedNameStrsList',
									'DocumentedModulePathStrsList'
								]))
		'''

		#Check
		self.DocumentedConceptStr=self.FolderingPathStr.split('/')[-1] if self.FolderingPathStr[-1]!='/' else self.FolderingPathStr.split('/')[-2]
		if self.DocumentedConceptStr in PluralStrToSingularStrOrderedDict.keys():
			self.DocumentedConceptModule=self.package(self.FolderedModuleStr).PackagingModuleVariable

		#debug
		'''
		self.debug(('self.',self,['DocumentedConceptModule']))
		'''

		#filter
		self.DocumentedModulesList=SYS._filter(
				lambda __AttributeValueVariable:
				type(__AttributeValueVariable).__name__=='module',
				self.DocumentedConceptModule.__dict__.values()
			)

		#debug
		'''
		self.debug(('self.',self,['DocumentedModulesList']))
		'''

		#map
		self.DocumentedPresentationsDictsList=map(
				lambda __DocumentedModulePathStr:
				self.readme(
					**{
						'FolderingPathStr':__DocumentedModulePathStr
					}
				).load(
					**{
						'FilingKeyStr':'Presentation.ipynb',
						'LoadingFormatStr':'json'
					}
				).close().LoadedReadVariable
				if self.DocumentingReadmeIsBool
				else
				self.load(
					**{
						'FolderingPathStr':__DocumentedModulePathStr,
						'FilingKeyStr':'Presentation.ipynb',
						'LoadingFormatStr':'json'
					}
				).close().LoadedReadVariable,
				self.DocumentedModulePathStrsList
			)

		#debug
		'''
		self.debug(
					'self.DocumentedPresentationsDictsList is '+SYS._str(self.DocumentedPresentationsDictsList)
				)
		'''

		#Check
		if self.DocumentingConceptIsBool:

			#Copy
			self.DocumentedConceptNotebookDict=copy.copy(Celler.CellingInitDict)

			#SYS._print(self.DocumentedPresentationsDictsList[0]['worksheets'][0]['cells'][0])
			#print(self.DocumentedConceptNotebookDict)

			DocumentedFlatPresentationsDictsList=SYS.flat(
					map(
							lambda __DocumentedPresentationsDict:
							copy.deepcopy(
								__DocumentedPresentationsDict['worksheets'][0]['cells']
								),
							self.DocumentedPresentationsDictsList
						)
					)

			#Flat all the presentations
			self.DocumentedConceptNotebookDict['worksheets']=[
				{
					'cells':map(
						lambda __DocumentedFlatPresentationsDict,__IndexInt:
						dict(__DocumentedFlatPresentationsDict,**{'prompt_number':__IndexInt}),
						DocumentedFlatPresentationsDictsList,
						xrange(len(DocumentedFlatPresentationsDictsList))
					)
				}
			]

			#debug
			self.debug(('self.',self,['DocumentedConceptNotebookDict']))

			#Write
			self.write(
				self.DocumentedConceptNotebookDict,
				**{
					'FolderingPathStr':self.DocumentingConceptFolderPathStr,
					'FilingKeyStr':'Concept'+self.GuidingBookStr+'.ipynb',
					'LoadingFormatStr':'json'
				}
			).close()

			#nbconvert
			self.NotebookedCodeDict=self.DocumentedConceptNotebookDict
			self.nbconvert(
				_FormatStr='Slide',
				**{
					'FolderingPathStr':self.DocumentingConceptFolderPathStr,
					'NotebookingFileKeyStr':'Concept'+self.GuidingBookStr+'.ipynb'
				}
			)

			#Check
			if self.NbconvertingFormatStr=='Slide':
				#change the reveal.js directory
				self.load(**{
						'FilingKeyStr':self.FilingKeyStr.replace('.ipynb','.slides.html'),
						'LoadingFormatStr':'txt'
					})
				self.LoadedReadVariable=self.LoadedReadVariable.replace('reveal.js/','')
				self.write(self.LoadedReadVariable)

			#mv
			os.popen('mv '+self.FiledPathStr.replace('.ipynb','.slides.html')+' '+DocumentingOntologyFolderPathStr+self.__class__.NameStr+self.GuidingBookStr+'.html')

			#Return self
			#return self
	
#</DefineClass>

ConceptStrsTuplesList=[
	('Classor','Classors'),
	('Interfacer','Interfacers'),
	('Guider','Guiders'),
	('Itemizer','Itemizers'),
	('Applyier','Applyiers'),
	('Walker','Walkers'),
	('Noder','Noders'),
	('Saver','Savers'),
	('Databaser','Databasers'),
	('Ploter','Ploters'),
	('Tutorials','Tutorials'),
	('Simulater','Simulaters'),
	('Muziker','Muzikers')
]
SingularStrToPluralStrOrderedDict=SYS.dictify(ConceptStrsTuplesList,0,1)
PluralStrToSingularStrOrderedDict=SYS.dictify(ConceptStrsTuplesList,1,0)