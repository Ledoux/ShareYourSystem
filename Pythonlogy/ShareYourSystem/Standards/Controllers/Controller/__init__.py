# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Controller

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ControllerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								]

	def default_init(self,
				**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_control(self):
		pass

#</DefineClass>

