# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Grider instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Storer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<DefineDoStrsList>
DoStrsList=["Grider","grid","griding","grided"]
#<DefineDoStrsList>

#<ImportSpecificModules>
import collections
import tables
from ShareYourSystem.Classors import Doer
from ShareYourSystem.Functers import Argumenter,Hooker,Switcher
from ShareYourSystem.Databasers import Featurer,Hierarchizer
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class GriderClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':Joiner.JoinerClass.model}]})
	#@Argumenter.ArgumenterClass()
	def do_grid(self):
	
		pass

		#Return self
		#return self

#</DefineClass>

