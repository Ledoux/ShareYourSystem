# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Vexflower

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Muziker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from music21 import vexflow
from ShareYourSystem.Objects import Noder
from ShareYourSystem.Functers import Argumenter,Hooker,Switcher
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class VexflowerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_VexflowedMusic21Str="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	@Argumenter.ArgumenterClass()
	def vexflow(self,**_KwargVariablesDict):

		#first muzik
		self.muzik()

		#vexflow now
		self.VexflowedMusic21Vexflow=vexflow.fromObject(
			self.MuzikedMusic21Converter)

		#Return self
		return self

#</DefineClass>
