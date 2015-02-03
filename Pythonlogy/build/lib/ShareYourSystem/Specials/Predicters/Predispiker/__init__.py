# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Predispiker

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Neurongrouper"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
from ShareYourSystem.Specials.Simulaters import Neurongrouper,Synapser
import operator
#</ImportSpecificModules>

#<DefineFunctions>
#</DefineFunctions>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
})
class PredispikerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
						]

	def default_init(self,
						_PredictedDerivePredicterVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#
		self.collect(
				'Components',
				'Lifer',
				SYS.LiferClass()
			)


	def do_predispike(self):	

		
#</DefineClass>
