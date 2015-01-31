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
		for __Int,__Matrixer in enumerate(self['<JacobianMatrixers>']):
				
			#debug
			self.debug(
				[
					'__Matrixer is \n',
					__Matrixer
				]
			)

			#Check
			if __Int==0:

				#set
				self.EquationedVariableStrsList=map(
					lambda __Int:
					self.EquationingSymbolStr+EquationingIndexStr+str(__Int),
					xrange(
						len(__Matrixer.MatrixedRandomFloatsArray)
					)
				)
				self.EquationingDifferentialDict.update(
					zip(
						self.EquationedVariableStrsList,
						['']*len(self.EquationedVariableStrsList)
					)
				)


			#debug
			self.debug(
				[
					('self.',self,[
									'EquationedVariableStrsList',
								]),
					('__Matrixer.',__Matrixer,['MatrixedRandomFloatsArray'])
				]
			)

			#map
			self.EquationedPreExpressionStrsList=map(
					lambda __RowJacFloatsArray,__RowTagVariablesArray:
					('+'.join(
							map(
								lambda __RowJacFloat,__RowTagVariable,__EquationedVariableStr:
								(
									(
									str(__RowJacFloat)
									if __RowJacFloat>0.
									else '('+str(__RowJacFloat)+')'
									)+'*'+__EquationedVariableStr+(
									'(t-0.)'
									if hasattr(
										__RowTagVariable,
										'items'
									)==False or 'DelayFloat' not in __RowTagVariable or __RowTagVariable['DelayFloat'
									]<=0.
									else '(t-'+str(__RowTagVariable['DelayFloat'])+')'
									)
								) 
								if __RowJacFloat!=0.
								else '',
								__RowJacFloatsArray,
								__RowTagVariablesArray if __RowTagVariablesArray!=None else [],
								self.EquationedVariableStrsList
							)
						)
					),
					__Matrixer.MatrixedRandomFloatsArray,
					__Matrixer.MatrixingTagVariablesArray
					if len(np.shape(__Matrixer.MatrixingTagVariablesArray))==2
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
			self.debug(
				[
					('self.',self,['EquationedPreExpressionStrsList'])
				]
			)

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
