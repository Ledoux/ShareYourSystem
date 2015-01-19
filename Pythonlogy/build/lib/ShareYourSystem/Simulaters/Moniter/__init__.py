# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

A Moniter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class MoniterClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'MoniteringVariableStr',
								'MoniteringIndexIntsList',
							]
	
	def default_init(self,
						_MoniteringVariableStr="",
						_MoniteringIndexIntsList=None,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def do_monit(self):

		pass

#</DefineClass>

