# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Loader is a quick object to load from a FiledHardVariable a LoadedReadVariable

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Closer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import json
import yaml
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class LoaderClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'LoadingFormatStr',
									'LoadedReadVariable',
									'FiledHardVariable'
								]

	def default_init(self,
						_LoadingFormatStr='txt',
						_LoadedReadVariable=None,
						_FiledHardVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_load(self,**_KwargVariablesDict):

		#debug
		'''
		self.debug(('self.',self,['LoadingFormatStr']))
		'''

		#file first
		self.file(_ModeStr='r')

		#Check
		if self.LoadingFormatStr=='txt':

			#Read the FiledHardVariable
			self.LoadedReadVariable=self.FiledHardVariable.read()

		elif self.LoadingFormatStr=='json':

			#Use the json decoder
			self.LoadedReadVariable=json.load(self.FiledHardVariable)

		elif self.LoadingFormatStr=='yaml':

			#Use the json decoder
			self.LoadedReadVariable=yaml.load(self.FiledHardVariable)

		#Return self
		#return self
	
#</DefineClass>

