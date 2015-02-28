# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Processer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Filer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineLocals>
ProcessingFileStr="ProcessTemp"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ProcesserClass(BaseClass):
	
	def default_init(self,
						_ProcessingBashStr="",
						_ProcessedBashStr="",
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
			
	def do_process(self):

		#file
		self.file(ProcessingFileStr+'.sh','w')

		#Define
		ProcessedBashPathStr=self.FolderingPathStr+ProcessingFileStr+'.txt'

		#set
		self.ProcessedBashStr='OUTPUT="$('+self.ProcessingBashStr+')"\n'
		self.ProcessedBashStr+='echo "${OUTPUT}" > '+ProcessedBashPathStr

		#write
		self.file(
			_ModeStr='w',
			_WriteVariable=self.ProcessedBashStr
		)
		self.FiledHardVariable.close()

		#debug
		'''
		self.debug(('self.',self,[
									'FiledPathStr',
								]))
		'''
		
		#popen
		os.popen('sh '+self.FiledPathStr)

		#load
		self.ProcessedBashStr=self.file(
					ProcessingFileStr+'.txt',
					'r'
				).FiledReadVariable

#</DefineClass>

#</DefinePrint>
ProcesserClass.PrintingClassSkipKeyStrsList.extend(
	[
		'ProcessingBashStr',
		'ProcessedBashStr'
	]
)
#<DefinePrint>

