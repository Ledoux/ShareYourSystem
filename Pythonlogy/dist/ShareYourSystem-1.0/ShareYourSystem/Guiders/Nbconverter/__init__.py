# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Nbconverter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Guiders.Notebooker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import json
import os
import sys
Filer=BaseModule
#</ImportSpecificModules>

#<DefineFunctions>
def getNbconvertedMarkdownCellDictsListWithCodeCellDict(_CellDict):
	return [
				{
					'source': "```python\n"+"".join(
						map(
								lambda __LineStr:
								__LineStr.replace('\t','    '),
								_CellDict['input']
							)
					)+"\n```\n", 
					'cell_type': 'markdown', 
					'metadata': {}
				}
			]+[
					{
						'source': "```console\n>>>\n"+"".join(
							_CellDict['outputs'][0]['text'])+"\n```\n", 
						'cell_type': 'markdown', 
						'metadata': {}
					} 
			] if len(_CellDict['outputs'])>0 else []

#</DefineFunctions>

#<DefineLocals>
NbconvertingFilePrefixStr=""
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class NbconverterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'NbconvertingFileKeyStr'
							]

	def default_init(self,
						_NbconvertingFileKeyStr="",
						_NbconvertingFormatStr="Markdown",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_nbconvert(self):

		#debug
		'''
		self.debug(('self.',self,['FiledFileVariable']))
		'''

		#Check
		if self.NbconvertingFormatStr=="Markdown":

			#debug
			'''
			self.debug(
						'worksheets are before the markdown '+Representer.represent(
							self.NbconvertedNotebookDict['worksheets'][0],**{'RepresentingAlineaIsBool':False})
					)
			'''

			#Transform the code cells into Nbconverted cells
			NbconvertedWorksheetsList=SYS.flat(
				map(
					lambda __CellDict:
					getNbconvertedMarkdownCellDictsListWithCodeCellDict(
						__CellDict
					) 
					if __CellDict['cell_type']=='code'
					else __CellDict,
					self.NotebookedCodeDict['worksheets'][0]['cells']
					)
			)

			#debug
			'''
			self.debug(
						'NbconvertedWorksheetsList is '+SYS._str(
							NbconvertedWorksheetsList,**{'RepresentingAlineaIsBool':False})
						)
			'''

			#set the dict
			self.NotebookedCodeDict['worksheets'][0]['cells']=NbconvertedWorksheetsList

			#debug
			'''
			self.debug(('self.',self,['FilingKeyStr']))
			'''

			#Write
			self.file(
						self.NbconvertingFileKeyStr.replace('.md','.ipynb'),
						'w'
			).write(
				self.NotebookedCodeDict,**{
					'LoadingFormatStr':'json'
				}
			).FiledFileVariable.close()

			#debug
			'''
			self.debug(('self.',self,[
										'FilingKeyStr',
										'FilingModeStr',
										'FiledPathStr'
									]))
			'''

			#Definition the NbconvertedCommandStr
			NbconvertedCommandStr=SYS.IPythonPathStr+" nbconvert --to markdown --output "+self.FiledPathStr.replace('.ipynb','')+" "+self.FiledPathStr

		elif self.NbconvertingFormatStr=='Slide':

			#Definition the NbconvertedCommandStr
			NbconvertedCommandStr=SYS.IPythonPathStr+" nbconvert --to slides --output "+self.FiledPathStr.replace('.ipynb','')+" "+self.FiledPathStr

			#debug
			'''
			self.debug(
						'NbconvertedCommandStr is '+NbconvertedCommandStr,
						('self.',self,['FiledPathStr'])
					)
			'''

		#debug
		'''
		self.debug('NbconvertedCommandStr is '+NbconvertedCommandStr)
		'''

		#Convert
		os.popen(NbconvertedCommandStr)

		#set the name
		if self.NbconvertingFormatStr=='Slide':

			#popen
			os.popen(
					'mv '+self.FiledPathStr.replace(
					'.ipynb','.slides.html'
					)+' '+self.FiledPathStr.replace(
					'.ipynb','.html'
				)
			)

			#change the reveal.js directory
			self.load(**{
					'FilingKeyStr':self.FiledPathStr.split('/')[-1].replace(
						'.ipynb',
						'.html'
					),
					'LoadingFormatStr':'txt'
				})

			self.LoadedReadVariable=self.LoadedReadVariable.replace(
				'reveal.js/','reveal/'
			).replace(
				"Reveal.initialize({",
				#"Reveal.initialize({"
				"Reveal.initialize({width: 1000,height: 400,margin: 0.,minScale: 0.5,maxScale: 1.0,"
			)	


			#chunk
			InformedOldChunkStrsList=SYS.chunk(
						['<code class="language-python">','</code>'],
						self.LoadedReadVariable,
						**{'ChunksInt':"All"}
					)
			
			#debug
			'''
			self.debug(
						[
							'self.InformedOldChunkStrsList is ',
							str(InformedOldChunkStrsList)
						]
					)
			'''
			
			#map
			InformedNewChunkStrsList=copy.deepcopy(InformedOldChunkStrsList)
			map(
					lambda __ChunkStr,__ChunkIndexInt:
					map(
							lambda __RemoveStr:
							 InformedNewChunkStrsList.__setitem__(
							 	__ChunkIndexInt,
							 	InformedNewChunkStrsList[__ChunkIndexInt].replace(
									__RemoveStr,
									''
								)
							),
							map(
									lambda __KeyStr:
									'<span class="'+__KeyStr+'">',
									[
										"built_in",
										"comment",
										"keyword",
										"params",
										"string",
										"number",
										"title",
										"function",
										"decorator",
										"class",
										#"highlight",
										#"kn",
										#"c",
										#"n",
										#"p",
										#"o"
									]
							)+['</span>']
					),
					InformedOldChunkStrsList,
					xrange(len(InformedOldChunkStrsList))
				)

			#debug
			'''
			self.debug(
						[
							'self.InformedNewChunkStrsList is ',
							str(InformedNewChunkStrsList)
						]
					)
			'''

			#replace
			map(
					lambda __InformedOldChunkStr,__InformedNewChunkStr:
					self.__setattr__(
							'LoadedReadVariable',
							self.LoadedReadVariable.replace(__InformedOldChunkStr,__InformedNewChunkStr)
						),
					InformedOldChunkStrsList,
					InformedNewChunkStrsList
				)

			#write
			self.write(self.LoadedReadVariable).close()

		#Return self
		#return self	

#</DefineClass>

