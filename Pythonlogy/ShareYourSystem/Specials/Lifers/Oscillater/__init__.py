# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import types
BaseModuleStr="ShareYourSystem.Specials.Lifers.Transferer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Oscillater','Oscillate','Oscillating','Oscillated')
#</DefineAugmentation>

#<ImportSpecificModules>
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class OscillaterClass(BaseClass):
	
	def default_init(self,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_oscillate(self):

		pass


#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=OscillaterClass
#<DefineLocals>

#</DefinePrint>
OscillaterClass.PrintingClassSkipKeyStrsList.extend(
	[
	]
)
#<DefinePrint>