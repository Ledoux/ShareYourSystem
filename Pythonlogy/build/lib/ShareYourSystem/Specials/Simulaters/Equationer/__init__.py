# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Equationer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Populater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
EquationingIndexStr=''
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class EquationerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'EquationingDifferentialDict',
		'EquationingParamDict',
		'EquationingSymbolStr',
		'EquationedVariableStrsList',
		'EquationedPreExpressionStrsList'
	]

	def default_init(self,
						_EquationingDifferentialDict=None,
						_EquationingParamDict=None,
						_EquationingSymbolStr='x',
						_EquationingCodeStr='',
						_EquationedVariableStrsList=None,
						_EquationedPreExpressionStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_equation(
				self,
				**_KwargVariablesDict
			):
		
		#Loop integrativ over the matrixers to build the equations
		for __IndexInt,__LateralMatrixer in enumerate(self['<LateralExpressers>']):
				
			#debug
			'''
			self.debug(
				[
					'__LateralMatrixer is \n',
					__LateralMatrixer
				]
			)
			'''

			#matrix first 
			__LateralMatrixer.matrix(
					_SizeTuple=(self.PopulatingUnitsInt,self.PopulatingUnitsInt)
				)

			#Check
			if __IndexInt==0:

				#set
				self.EquationedVariableStrsList=map(
					lambda __IndexInt:
					self.EquationingSymbolStr+EquationingIndexStr+str(__IndexInt),
					xrange(
						len(__LateralMatrixer.MatrixedRandomFloatsArray)
					)
				)
				self.EquationingDifferentialDict.update(
					zip(
						self.EquationedVariableStrsList,
						['']*len(self.EquationedVariableStrsList)
					)
				)


			#debug
			'''
			self.debug(
				[
					('self.',self,[
									'EquationedVariableStrsList',
								]),
					('__LateralMatrixer.',__LateralMatrixer,['MatrixedRandomFloatsArray'])
				]
			)
			'''

			#map express
			self.EquationedPreExpressionStrsList=map(
					lambda __RowJacFloatsArray,__RowSpecificTagVariablesArray:
					('+'.join(
							map(
								lambda __RowJacFloat,__EquationedVariableStr,__RowSpecificTagVariable:
								__LateralMatrixer.express(
										__RowJacFloat,
										__EquationedVariableStr,
										__RowSpecificTagVariable['DelayFloat']
										if type(
											__RowSpecificTagVariable
											)!=None.__class__ and 'DelayFloat' in __RowSpecificTagVariable 
										else 0.,
										__RowSpecificTagVariable['TransferFunctionStr']
										if type(
											__RowSpecificTagVariable
											)!=None.__class__ and 'TransferFunctionStr' in __RowSpecificTagVariable
										else ""
									).ExpressedTermStr,
								__RowJacFloatsArray,
								self.EquationedVariableStrsList,
								__RowSpecificTagVariablesArray if type(
									__RowSpecificTagVariablesArray
								)!=None.__class__ else []
							)
						)
					),
					__LateralMatrixer.MatrixedRandomFloatsArray,
					__LateralMatrixer.MatrixingSpecificTagVariablesArray
					if len(np.shape(__LateralMatrixer.MatrixingSpecificTagVariablesArray))==2
					else [[]]
				)

			#map
			self.EquationedPreExpressionStrsList=map(
					lambda __EquationedPreExpressionStr:
					__EquationedPreExpressionStr[1:]
					if __EquationedPreExpressionStr[0]=='+'
					else __EquationedPreExpressionStr,
					self.EquationedPreExpressionStrsList
				)
			self.EquationedPreExpressionStrsList=map(
					lambda __EquationedPreExpressionStr:
					__EquationedPreExpressionStr[:-1]
					if __EquationedPreExpressionStr[-1]=='+'
					else __EquationedPreExpressionStr,
					self.EquationedPreExpressionStrsList
				)
			self.EquationedPreExpressionStrsList=map(
					lambda __EquationedPreExpressionStr:
					__EquationedPreExpressionStr.replace('++',''),
					self.EquationedPreExpressionStrsList
				)

			#debug
			'''
			self.debug(
				[
					('self.',self,['EquationedPreExpressionStrsList'])
				]
			)
			'''

			#update
			map(
					lambda __EquationedVariableStr,__EquationedPreExpressionStr:
					self.EquationingDifferentialDict.__setitem__
					(
						__EquationedVariableStr,
						self.EquationingDifferentialDict[__EquationedVariableStr].__add__(
							'+'+__EquationedPreExpressionStr
							if self.EquationingDifferentialDict[__EquationedVariableStr]!=''
							else __EquationedPreExpressionStr
						) 
					),
					self.EquationedVariableStrsList,
					self.EquationedPreExpressionStrsList
				)
			
#</DefineClass>
