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
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
import copy
import sys

from ShareYourSystem.Classors import Doer
from ShareYourSystem.Guiders import Celler
Readmer=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
InformingOntologyFolderPathStr=SYS.ShareYourSystemLocalFolderPathStr+'/reveal/'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class InformerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'InformingConceptFolderPathStr',
								'InformingReadmeIsBool',
								'InformingConceptIsBool',
								'InformedConceptModule',
								'InformedNameStrsList',
								'InformedModulePathStrsList',
								'InformedModulesList',
								#'InformedPresentationsDictsList',
								#'InformedConceptNotebookDict'
							]

	def default_init(self,
						_InformingConceptFolderPathStr="",
						_InformingReadmeIsBool=True,
						_InformingConceptIsBool=True,
						_InformedConceptModule=None,
						_InformedNameStrsList=None,
						_InformedModulePathStrsList=None,
						_InformedModulesList=None,
						_InformedPresentationsDictsList=None,
						_InformedConceptNotebookDict=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_inform(self):
		
		#debug
		self.debug(('self.',self,['InformingReadmeIsBool','InformingConceptIsBool']))

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
						**{'FolderingPathStr':self.InformingConceptFolderPathStr}
					)
		"""

		#debug
		self.folder(self.InformingConceptFolderPathStr)

		#debug
		'''
		self.debug(('self.',self,['FolderedDirKeyStrsList']))
		'''

		#filter
		self.InformedNameStrsList=SYS._filter(
			lambda __FolderedDirKeyStr:
			os.path.isdir(
				self.FolderingPathStr+__FolderedDirKeyStr
			) and __FolderedDirKeyStr in Doer.DoerStrToDoStrOrderedDict.keys(),
			self.FolderedDirKeyStrsList
		)	

		#debug
		'''
		self.debug(('self.',self,['InformedNameStrsList','InstalledNameStrsList']))
		'''
		
		#sort
		self.InformedNameStrsList=SYS._filter(
				lambda __InstalledNameStr:
				__InstalledNameStr in self.InformedNameStrsList,
				self.InstalledNameStrsList
			)
		#map
		self.InformedModulePathStrsList=map(
			lambda __InformedNameStr:
			self.FolderingPathStr+__InformedNameStr+'/',
			self.InformedNameStrsList
		)	

		#debug
		'''
		self.debug(('self.',self,[
									'InformedNameStrsList',
									'InformedModulePathStrsList'
								]))
		'''

		#Check
		self.InformedConceptStr=self.FolderingPathStr.split('/')[-1] if self.FolderingPathStr[-1]!='/' else self.FolderingPathStr.split('/')[-2]
		if self.InformedConceptStr in PluralStrToSingularStrOrderedDict.keys():
			self.InformedConceptModule=self.package(self.FolderedModuleStr).PackagingModuleVariable

		#debug
		'''
		self.debug(('self.',self,['InformedConceptModule']))
		'''

		#filter
		self.InformedModulesList=SYS._filter(
				lambda __AttributeValueVariable:
				type(__AttributeValueVariable).__name__=='module',
				self.InformedConceptModule.__dict__.values()
			)

		#debug
		'''
		self.debug(('self.',self,['InformedModulesList']))
		'''

		#map
		self.InformedPresentationsDictsList=map(
				lambda __InformedModulePathStr:
				self.readme(
					**{
						'FolderingPathStr':__InformedModulePathStr
					}
				).load(
					**{
						'FilingKeyStr':'Presentation.ipynb',
						'LoadingFormatStr':'json'
					}
				).close().LoadedReadVariable
				if self.InformingReadmeIsBool
				else
				self.load(
					**{
						'FolderingPathStr':__InformedModulePathStr,
						'FilingKeyStr':'Presentation.ipynb',
						'LoadingFormatStr':'json'
					}
				).close().LoadedReadVariable,
				self.InformedModulePathStrsList
			)

		#debug
		'''
		self.debug(
					'self.InformedPresentationsDictsList is '+SYS._str(self.InformedPresentationsDictsList)
				)
		'''

		#Check
		if self.InformingConceptIsBool:

			#Copy
			self.InformedConceptNotebookDict=copy.copy(Celler.CellingInitDict)

			#SYS._print(self.InformedPresentationsDictsList[0]['worksheets'][0]['cells'][0])
			#print(self.InformedConceptNotebookDict)

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
						dict(__InformedFlatPresentationsDict,**{'prompt_number':__IndexInt}),
						InformedFlatPresentationsDictsList,
						xrange(len(InformedFlatPresentationsDictsList))
					)
				}
			]

			#debug
			self.debug(('self.',self,['InformedConceptNotebookDict']))

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
			os.popen('mv '+self.FiledPathStr.replace('.ipynb','.slides.html')+' '+InformingOntologyFolderPathStr+self.__class__.NameStr+self.GuidingBookStr+'.html')

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