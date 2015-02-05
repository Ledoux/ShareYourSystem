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
		'ExpressingMapBool',
		'ExpressingSpecificTagVariablesArray',
		'ExpressingRowTagVariablesArray',
		'ExpressingColTagVariablesArray',
		'ExpressedTermStr',
		'ExpressedPreExpressionStrsList'
	]

	def default_init(
						self,
						_ExpressingInputFloat=0.,
						_ExpressingSymbolStr='x',
						_ExpressingDelayFloat=0.,
						_ExpressingTransferFunctionStr='',
						_ExpressingOutputFloat=1.,
						_ExpressingMapBool=False,
						_ExpressingSpecificTagVariablesArray=None,
						_ExpressingRowTagVariablesArray=None,
						_ExpressingColTagVariablesArray=None,
						_ExpressedTermStr="",
						_ExpressedPreExpressionStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_express(
				self,
				**_KwargVariablesDict
			):
		

		#Check
		if self.ExpressingMapBool:

			#Check
			if self.MatrixingSizeTuple==None:
				self.MatrixingSizeTuple=np.shape(
					self.ExpressingSpecificTagVariablesArray
				)

			#matrix first
			self.matrix()

			#debug
			self.debug(('self.',self,[
						'MatrixedRandomFloatsArray',
						'ExpressingRowTagVariablesArray',
						'ExpressingColTagVariablesArray',
						'ExpressingSpecificTagVariablesArray'
					]))

			#map express
			self.ExpressedPreExpressionStrsList=map(
					lambda __RowJacFloatsArray,__RowSpecificTagVariablesArray:
					('+'.join(
							map(
								lambda __RowJacFloat,__ExpressingColTagVariable,__SpecificTagVariable:
								self.express(
										__RowJacFloat,
										__SpecificTagVariable['SymbolStr'] 
										if __SpecificTagVariable!=None and 'SymbolStr' in __SpecificTagVariable
										else
										(
											__ExpressingColTagVariable['SymbolStr']
											if __ExpressingColTagVariable!=None and 'SymbolStr' in __ExpressingColTagVariable
											else self.ExpressingSymbolStr
										),
										__SpecificTagVariable['DelayFloat']
										if type(
												__SpecificTagVariable
											)!=None.__class__ and 'DelayFloat' in __SpecificTagVariable 
										else 0.,
										__SpecificTagVariable['TransferFunctionStr']
										if type(
											__SpecificTagVariable
											)!=None.__class__ and 'TransferFunctionStr' in __SpecificTagVariable
										else "",
										_ExpressingMapBool=False
									).ExpressedTermStr,
								__RowJacFloatsArray 
								if type(__RowJacFloatsArray)!=None.__class__ 
								else [],
								self.ExpressingColTagVariablesArray
								if type(self.ExpressingColTagVariablesArray)!=None.__class__
								else [],
								__RowSpecificTagVariablesArray 
								if type(__RowSpecificTagVariablesArray)!=None.__class__ 
								else []
							)
						)
					),
					self.MatrixedRandomFloatsArray,
					self.ExpressingSpecificTagVariablesArray
					if len(np.shape(self.ExpressingSpecificTagVariablesArray))==2
					else [[]]
				)

			#row
			self.ExpressedPreExpressionStrsList=map(
					lambda __ExpressedPreExpressionStr,__ExpressingRowTagVariable:
					__ExpressingRowTagVariable['TransferFunctionStr']+'('+__ExpressedPreExpressionStr+')'
					if __ExpressingRowTagVariable!=None and 'TransferFunctionStr' in __ExpressingRowTagVariable
					else __ExpressedPreExpressionStr,
					self.ExpressedPreExpressionStrsList,
					self.ExpressingRowTagVariablesArray
					if type(self.ExpressingRowTagVariablesArray)!=None.__class__
					else []
				)

			#debug
			self.debug(('self.',self,[
							'ExpressedPreExpressionStrsList'
						]))

			#map
			self.ExpressedPreExpressionStrsList=map(
					lambda __ExpressedPreExpressionStr:
					__ExpressedPreExpressionStr[1:]
					if __ExpressedPreExpressionStr[0]=='+'
					else __ExpressedPreExpressionStr,
					self.ExpressedPreExpressionStrsList
				)
			self.ExpressedPreExpressionStrsList=map(
					lambda __ExpressedPreExpressionStr:
					__ExpressedPreExpressionStr[:-1]
					if __ExpressedPreExpressionStr[-1]=='+'
					else __ExpressedPreExpressionStr,
					self.ExpressedPreExpressionStrsList
				)
			self.ExpressedPreExpressionStrsList=map(
					lambda __ExpressedPreExpressionStr:
					__ExpressedPreExpressionStr.replace('++',''),
					self.ExpressedPreExpressionStrsList
				)

			#debug
			self.debug(('self.',self,['ExpressedPreExpressionStrsList']))

		#One single expression
		else:

			#debug
			self.debug(
					[
						'We express just one element',
						('self.',self,[
							'ExpressingSymbolStr',
							'ExpressingInputFloat'
						])
					]
				)

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
				
			#else
			else:
				self.ExpressedTermStr=''

			#debug
			self.debug(
					[
						'We express just one element now it is ',
						('self.',self,['ExpressedTermStr'])
					]
				)




#</DefineClass>
