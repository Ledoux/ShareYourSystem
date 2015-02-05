# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Leaker

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Equationer"
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
class LeakerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'LeakingConstantTimeVariable'
	]

	def default_init(self,
						_LeakingConstantTimeVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#collect some Expressers
		self.collect(
			'LateralExpressers',
			'Leak',
			SYS.ExpresserClass(**{
				'MatrixingStdFloat':0.
			})
		).collect(
			'LateralExpressers',
			'Interaction',
			SYS.ExpresserClass()
		)

	def do_leak(
				self,
				**_KwargVariablesDict
			):

		#matrix the Leak
		self['<LateralExpressers>LeakExpresser'].matrix(
						_SizeTuple=(self.PopulatingUnitsInt,self.PopulatingUnitsInt),
						_DiagFloatsArray=-np.ones(self.PopulatingUnitsInt,dtype=float),
						_DivideVariable=self.LeakingConstantTimeVariable
					)

		#matrix the Lateral
		self['<LateralExpressers>InteractionExpresser'].matrix(
				_SizeTuple=(self.PopulatingUnitsInt,self.PopulatingUnitsInt),
				_DivideVariable=self.LeakingConstantTimeVariable
			)
		
		#equation
		self.equation()
		
#</DefineClass>
