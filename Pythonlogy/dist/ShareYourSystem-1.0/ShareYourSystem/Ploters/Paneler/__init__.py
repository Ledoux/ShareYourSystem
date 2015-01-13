# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Paneler

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Ploters.Figurer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Paneler","Panel","Paneling","Paneled"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class PanelerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	#@Argumenter.ArgumenterClass()
	def do_panel(
				self
			):	

		pass

		#Return self
		#return self

#</DefineClass>
