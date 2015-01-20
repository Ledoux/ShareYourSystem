# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Meteorer maps an append
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Controllers.Meteorer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Viewers import Boxer
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PatcherClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
							]

	def default_init(self,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
		#collect
		self.collect(
						'Representome',
						'Instance',
						Boxer.BoxerClass()
					);

	def do_patch(self):

		#box
		self['<Representome>InstanceBoxer'].box()

#</DefineClass>
