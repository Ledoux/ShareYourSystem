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
		'EquationedIndexSymbolStrsList',
		'EquationedPreExpressionStrsList'
	]

	def default_init(self,
						_EquationingDifferentialDict=None,
						_EquationingParamDict=None,
						_EquationingSymbolStr='x',
						_EquationingCodeStr='',
						_EquationedIndexSymbolStrsList=None,
						_EquationedPreExpressionStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_equation(
				self,
				**_KwargVariablesDict
			):
		
		#Loop integrativ over the lateral expressers to build the equations
		for __IndexInt,__LateralExpresser in enumerate(self['<LateralExpressers>']):
				
			#debug
			'''
			self.debug(
				[
					'__LateralExpresser is \n',
					__LateralExpresser
				]
			)
			'''

			#Check
			if __IndexInt==0:

				#set
				self.EquationedIndexSymbolStrsList=map(
					lambda __IndexInt:
					self.EquationingSymbolStr+EquationingIndexStr+str(__IndexInt),
					xrange(
						self.PopulatingUnitsInt
					)
				)
				self.EquationingDifferentialDict.update(
					zip(
						self.EquationedIndexSymbolStrsList,
						['']*len(self.EquationedIndexSymbolStrsList)
					)
				)



			#debug
			'''
			self.debug(
				[
					('self.',self,[
									'EquationedIndexSymbolStrsList',
								]),
					('__LateralExpresser.',__LateralExpresser,['MatrixedRandomFloatsArray'])
				]
			)
			'''

			#map to give name variables in the cols
			__LateralExpresser.ExpressingColTagVariablesArray=map(
					lambda __EquationedIndexSymbolStr,__ExpressingColTagVariable:
					dict(
							__ExpressingColTagVariable,
							**{'SymbolStr':__EquationedIndexSymbolStr}
						)
					if type(
						__ExpressingColTagVariable
					)!=None.__class__
					else {'SymbolStr':__EquationedIndexSymbolStr},
					self.EquationedIndexSymbolStrsList,
					__LateralExpresser.ExpressingColTagVariablesArray
					if type(
						__LateralExpresser.ExpressingColTagVariablesArray
					)!=None.__class__
					else []
				)

			#debug
			'''
			self.debug(
				[
					('__LateralExpresser.',__LateralExpresser,['ExpressingColTagVariablesArray'])
				]
			)
			'''

			#map express
			self.EquationedPreExpressionStrsList=__LateralExpresser.express(
					_MapBool=True,
					**{
						'MatrixingSizeTuple':(
							self.PopulatingUnitsInt,
							self.PopulatingUnitsInt
						)
					}
				).ExpressedPreExpressionStrsList
			
			#debug
			'''
			self.debug(
				[
					'update equation for a lateral',
					('self.',self,[
								'EquationedPreExpressionStrsList',
								'EquationingDifferentialDict'
							])
				]
			)
			'''

			#update
			map(
					lambda __EquationedIndexSymbolStr,__EquationedPreExpressionStr:
					self.EquationingDifferentialDict.__setitem__
					(
						__EquationedIndexSymbolStr,
						self.EquationingDifferentialDict[__EquationedIndexSymbolStr].__add__(
							'+'+__EquationedPreExpressionStr
							if self.EquationingDifferentialDict[__EquationedIndexSymbolStr]!=''
							else __EquationedPreExpressionStr
						) 
					),
					self.EquationedIndexSymbolStrsList,
					self.EquationedPreExpressionStrsList
				)

		#Loop integrativ over the input expressers to build the equations
		for __IndexInt,__InputExpresser in enumerate(self['<InputExpressers>']):
				
			#debug
			'''
			self.debug(
				[
					'__InputExpresser is \n',
					__InputExpresser
				]
			)
			'''

			#matrix first
			if __InputExpresser.MatrixingSizeTuple==None:

				#Check
				if __InputExpresser.ExpressingSpecificTagVariablesArray!=None:
					__InputExpresser.MatrixingSizeTuple=np.shape(
							__InputExpresser.ExpressingSpecificTagVariablesArray
						)
				elif __InputExpresser.ExpressingRowTagVariablesArray!=None:
					__InputExpresser.MatrixingSizeTuple=(
						self.PopulatingUnitsInt,
						len(
						__InputExpresser.ExpressingRowTagVariablesArray
						)
					)
				else:
					__InputExpresser.MatrixingSizeTuple=(self.PopulatingUnitsInt,0)

			#express
			self.EquationedPreExpressionStrsList=__InputExpresser.express(
					_MapBool=True
				).ExpressedPreExpressionStrsList

			#debug
			'''
			self.debug(
				[
					'update equation for an input',
					('self.',self,['EquationedPreExpressionStrsList'])
				]
			)
			'''

			#update
			map(
					lambda __EquationedIndexSymbolStr,__EquationedPreExpressionStr:
					self.EquationingDifferentialDict.__setitem__
					(
						__EquationedIndexSymbolStr,
						self.EquationingDifferentialDict[__EquationedIndexSymbolStr].__add__(
							'+'+__EquationedPreExpressionStr
							if self.EquationingDifferentialDict[__EquationedIndexSymbolStr]!=''
							else __EquationedPreExpressionStr
						) 
					),
					self.EquationedIndexSymbolStrsList,
					self.EquationedPreExpressionStrsList
				)

		'''
		#check the format
		map(
			lambda __EquationTuple:
			self.EquationingDifferentialDict.__setitem__(
				__EquationTuple[0],
				__EquationTuple[1].replace('++','')
			),
			self.EquationingDifferentialDict.items()
		)

		#check the format
		map(
			lambda __EquationTuple:
			self.EquationingDifferentialDict.__setitem__(
				__EquationTuple[0],
				__EquationTuple[1][1:] 
				if __EquationTuple[1][0]=='+'
				else __EquationTuple[1]
			),
			self.EquationingDifferentialDict.items()
		)

		#check the format
		map(
			lambda __EquationTuple:
			self.EquationingDifferentialDict.__setitem__(
				__EquationTuple[0],
				__EquationTuple[1][:-1] 
				if __EquationTuple[1][-1]=='+'
				else __EquationTuple[1]
			),
			self.EquationingDifferentialDict.items()
		)
		'''

			
#</DefineClass>
