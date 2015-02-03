# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Expresser

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Matrixer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ExpresserClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'ExpressingInputFloat',
		'ExpressingSymbolStr',
		'ExpressingDelayFloat',
		'ExpressingTransferFunctionStr',
		'ExpressingOutputFloat',
		'ExpressedTermStr',
	]

	def default_init(
						self,
						_ExpressingInputFloat=0.,
						_ExpressingSymbolStr='x',
						_ExpressingDelayFloat=0.,
						_ExpressingTransferFunctionStr='',
						_ExpressingOutputFloat=1.,
						_ExpressedTermStr="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_express(
				self,
				**_KwargVariablesDict
			):
		
		#Check
		if self.ExpressingInputFloat!=0.:

			#define
			self.ExpressedTermStr=(
				str(self.ExpressingInputFloat)
				if self.ExpressingInputFloat>0.
				else '('+str(self.ExpressingInputFloat)+')'
				)+'*'+self.ExpressingSymbolStr+(
					'(t-0.)'
					if self.ExpressingDelayFloat<=0.
					else '(t-'+str(self.ExpressingDelayFloat)+')'
				)

			#Check
			if self.ExpressingTransferFunctionStr:
				self.ExpressedTermStr=self.ExpressingTransferFunctionStr+'('+self.ExpressedTermStr+')'
			
#</DefineClass>
