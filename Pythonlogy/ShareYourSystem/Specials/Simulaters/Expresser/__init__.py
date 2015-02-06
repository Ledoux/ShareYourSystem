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
		'ExpressedPreExpressionStrsList',
		'ExpressedIndexTuplesList',
		'ExpressedTheoryParamStrsList'
	]

	def default_init(
						self,
						_ExpressingInputFloat=0.,
						_ExpressingSymbolStr='x',
						_ExpressingDelayFloat=0.,
						_ExpressingTransferFunctionStr='',
						_ExpressingOutputFloat=1.,
						_ExpressingMapBool=False,
						_ExpressingTheoryBool=False,
						_ExpressingJacSymbolStr='J',
						_ExpressingSpecificTagVariablesArray=None,
						_ExpressingRowTagVariablesArray=None,
						_ExpressingColTagVariablesArray=None,
						_ExpressedTermStr="",
						_ExpressedPreExpressionStrsList=None,
						_ExpressedIndexTuplesList=None,
						_ExpressedTheoryParamStrsList=None,
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
			if self.ExpressingTheoryBool==False:
				self.matrix()

			#debug
			'''
			self.debug(('self.',self,[
						'MatrixedRandomFloatsArray',
						'ExpressingRowTagVariablesArray',
						'ExpressingColTagVariablesArray',
						'ExpressingSpecificTagVariablesArray'
					]))
			'''
			
			#Check
			if type(self.ExpressingColTagVariablesArray)==None.__class__:
				self.ExpressingColTagVariablesArray=[]

			#Init
			self.ExpressedCountInt=0

			#Check
			if self.ExpressingTheoryBool==False:

				#map express
				self.ExpressedPreExpressionStrsList=map(
						lambda __RowJacFloatsArray,__RowSpecificTagVariablesArray:
						('+'.join(
								map(
									lambda __RowJacFloat,__ExpressingColTagVariable,__SpecificTagVariable:
									self.update(
										{
											'ExpressingInputFloat':0.,
											'ExpressingSymbolStr':'x',
											'ExpressingDelayFloat':0.,
											'ExpressingTransferFunctionStr':'',
											'ExpressingOutputFloat':1.,
											'ExpressedCountInt':self.ExpressedCountInt+1
										}
									).update(
										dict(
											__ExpressingColTagVariable,
											**__SpecificTagVariable
										)
									).express(
											__RowJacFloat,
											_MapBool=False
										).ExpressedTermStr,
									__RowJacFloatsArray,
									self.ExpressingColTagVariablesArray,
									__RowSpecificTagVariablesArray 
								)
							)
						),
						self.MatrixedRandomFloatsArray,
						self.ExpressingSpecificTagVariablesArray
						if len(np.shape(self.ExpressingSpecificTagVariablesArray))==2
						else [[]]
					)

			else:

				#get
				self.ExpressedIndexTuplesList=SYS.getIndexTuplesList(self.MatrixingSizeTuple)

				#
				self.ExpressedTheoryParamStrsList=map(
						lambda __ExpressedIndexTuple:
						self.ExpressingJacSymbolStr+''.join(map(str,__ExpressedIndexTuple)),
						self.ExpressedIndexTuplesList
					)

				#map
				map(
						lambda __ExpressedIndexTuple,__ExpressedTheoryParamStr:
						self.ExpressingSpecificTagVariablesArray[
						__ExpressedIndexTuple].__setitem__(
							'ExpressingInputFloat',
							__ExpressedTheoryParamStr
						),
						self.ExpressedIndexTuplesList,
						self.ExpressedTheoryParamStrsList
					)
				
				#debug
				self.debug(('self.',self,['ExpressingSpecificTagVariablesArray']))

				#map express
				self.ExpressedPreExpressionStrsList=map(
						lambda __RowSpecificTagVariablesArray:
						('+'.join(
								map(
									lambda __ExpressingColTagVariable,__SpecificTagVariable:
									self.update(
										{
											'ExpressingSymbolStr':'x',
											'ExpressingDelayFloat':0.,
											'ExpressingTransferFunctionStr':'',
											'ExpressingOutputFloat':1.,
											'ExpressedCountInt':self.ExpressedCountInt+1
										}
									).update(
										dict(
											__ExpressingColTagVariable,
											**__SpecificTagVariable
										)
									).express(
											_MapBool=False
										).ExpressedTermStr,
									self.ExpressingColTagVariablesArray,
									__RowSpecificTagVariablesArray 
								)
							)
						),
						self.ExpressingSpecificTagVariablesArray
						if len(np.shape(self.ExpressingSpecificTagVariablesArray))==2
						else [[]]
					)


			#debug
			self.debug('Ok we have joined')

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
			'''
			self.debug(('self.',self,[
							'ExpressedPreExpressionStrsList'
						]))
			'''

			#map
			'''
			self.ExpressedPreExpressionStrsList=map(
					lambda __ExpressedPreExpressionStr:
					__ExpressedPreExpressionStr.replace('++',''),
					self.ExpressedPreExpressionStrsList
				)

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
			'''

			#debug
			'''
			self.debug(('self.',self,['ExpressedPreExpressionStrsList']))
			'''

		#One single expression
		else:

			#debug
			'''
			self.debug(
					[
						'We express just one element',
						('self.',self,[
							'ExpressingSymbolStr',
							'ExpressingInputFloat'
						])
					]
				)
			'''


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
				if self.ExpressingTransferFunctionStr!='':
					self.ExpressedTermStr=self.ExpressingTransferFunctionStr+'('+self.ExpressedTermStr+')'
				
			#else
			else:
				self.ExpressedTermStr=''

			#debug
			'''
			self.debug(
					[
						'We express just one element now it is ',
						('self.',self,['ExpressedTermStr'])
					]
				)
			'''

			#debug
			print('Ok we have expressed, ExpressedCountInt is '+str(self.ExpressedCountInt))

#</DefineClass>
