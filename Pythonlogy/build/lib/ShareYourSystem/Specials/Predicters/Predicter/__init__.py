# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Predicter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Controllers.Systemer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineFunctions>
#</DefineFunctions>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
})
class PredicterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
						]

	def default_init(self,
						_PredictingDaleBool=False,
						_PredictingOnAndOffBool=False,
						_PredictingPrincAndAuxBool=False,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_predict(self):	

		pass
		
#</DefineClass>
