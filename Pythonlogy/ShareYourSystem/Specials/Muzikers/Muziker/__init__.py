# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Muziker

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Controller"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from music21 import converter
from ShareYourSystem.Functers import Argumenter
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class VexflowerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									"MuzikingScoreStr"
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_MuzikingScoreStr="",
						_MuzikedMusic21Converter=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	@Argumenter.ArgumenterClass()
	def muzik(self,_ScoreStr=None,**_KwargVariablesDict):

		#debug
		'''
		self.debug(('self.',self,['MuzikingScoreStr']))
		'''

		#Convert
		if self.FileKeyStr!='' and self.FileKeyStr.endswith('.xml'):

			self.MuzikedMusic21Converter=converter.parse(
				self.FilePathStr)

		else:

			self.MuzikedMusic21Converter=converter.parse(
				self.MuzikingScoreStr)

		#Return self
		return self

#</DefineClass>
