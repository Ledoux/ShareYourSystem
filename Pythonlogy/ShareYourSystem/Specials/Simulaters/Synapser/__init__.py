# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Synapser

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Itemizers.Pointer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class SynapserClass(BaseClass):
	
	def default_init(self,
						_SynapsingKwargVariablesDict=None,
						_SynapsingProbabilityVariable=None,
						_SynapsingTagStr="",
						_SynapsingWeigthSymbolStr="",
						_SynapsingWeigthFloatsArray=None,
						_SynapsingDelayDict=0.,
						_SynapsedBrianVariable=None,
						_SynapsedWeigthFloatsArray=None,
						_SynapsedCustomOperationStr="",
						_SynapsedDelayStateStrsList="",
						**_KwargVariablesDict
					):

		#init
		self.PostModelInsertStrsList=[]
		self.PostModelAddDict={}

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def setDelay(self,_SymbolStr,_DelayVariable):

		#debug
		'''
		self.debug(
			[
				"self.SynapsingKwargVariablesDict['source'].clock is ",
				self.SynapsingKwargVariablesDict['source'].clock
			]
		)
		'''

		#define
		if type(_DelayVariable).__name__=='Quantity':

			#divide
			DelayEquationsInt=(int)(
				_DelayVariable/self.SynapsingKwargVariablesDict['source'].clock.dt
			)

		else:

			#debug
			'''
			self.debug(
				[
					"float of dt is ",
					float(
						self.SynapsingKwargVariablesDict['source'].clock.dt
					)
				]
			)
			'''

			#divide and put that in ms...(rough)
			DelayEquationsInt=(int)(
				_DelayVariable*0.001/float(
					self.SynapsingKwargVariablesDict['source'].clock.dt
				)
			)

		#join
		self.SynapsedCustomOperationStr='\n'.join(
			map(
					lambda __EquationIndexInt:
					_SymbolStr+"_delayer_"+str(
						__EquationIndexInt
					)+"="+_SymbolStr+"_delayer_"+str(
						__EquationIndexInt-1
					),
					xrange(DelayEquationsInt,1,-1)
				)+[
				_SymbolStr+"delayer_1="+_SymbolStr
			]
		)

		#debug
		self.debug(
			('self.',self,[
							'SynapsedCustomOperationStr'
						])
		)

		#custom
		self.SynapsingKwargVariablesDict['source'].custom_operation(
				self.SynapsedCustomOperationStr
			)

		#join
		self.SynapsedDelayStateStrsListsList=map(
					lambda __EquationIndexInt:
					_SymbolStr+"_delayer_ : 1",
					xrange(DelayEquationsInt)
				)

		#debug
		self.debug(
			('self.',self,[
							'SynapsedDelayStateStrsList'
						])
		)

		#add in the PreModelInsertStrsList
		if hasattr(self,'AttentionUpdateVariable')==False:
			self.AttentionUpdateVariable={
				'PreModelInsertStrsList':[]
			}
		self.AttentionUpdateVariable['PreModelInsertStrsList']+=self.SynapsedDelayStateStrsListsList


	def do_synapse(
				self
			):	

		
		#Maybe should import
		from brian2 import Synapses

		#Check
		if len(self.SynapsingDelayDict)>0.:

			#map
			map(
					lambda __ItemTuple:
					self.setDelay(*__ItemTuple),
					self.SynapsingDelayDict.items()
				)

		#debug
		'''
		self.debug(('self.',self,[
								'SynapsingKwargVariablesDict'
								]))
		'''
		
		#init
		self.SynapsedBrianVariable=Synapses(
				**self.SynapsingKwargVariablesDict
			)

		#connect
		if type(self.SynapsingProbabilityVariable)==float:

			#debug
			'''
			self.debug('we connect with a sparsity of '+str(self.SynapsingProbabilityVariable))
			'''

			self.SynapsedBrianVariable.connect(
				True,
				p=self.SynapsingProbabilityVariable
			)

		#Check
		if self.SynapsingWeigthSymbolStr!="":

			#debug
			'''
			self.debug(
				('self.',self,[
					'SynapsedBrianVariable',
					'SynapsingWeigthSymbolStr'
					])
			)
			'''

			#connect
			self.SynapsedBrianVariable.connect(True)

			#get
			self.SynapsedWeigthFloatsArray=getattr(
				self.SynapsedBrianVariable,
				self.SynapsingWeigthSymbolStr
			)
			
			#set
			self.SynapsedWeigthFloatsArray[:]=np.reshape(
					self.SynapsingWeigthFloatsArray,
					self.SynapsedBrianVariable.source.N*self.SynapsedBrianVariable.target.N
				)

			#debug
			self.debug(
				('self.',self,[
					'SynapsedWeigthFloatsArray'
					])
			)

#</DefineClass>

#</DefinePrint>
SynapserClass.PrintingClassSkipKeyStrsList.extend(
	[
		'SynapsingKwargVariablesDict',
		'SynapsingProbabilityVariable',
		'SynapsingTagStr',
		'SynapsingWeigthSymbolStr',
		'SynapsingWeigthFloatsArray',
		'SynapsingDelayDict',
		'SynapsedBrianVariable',
		'SynapsedCustomOperationStr',
		'SynapsedDelayStateStrsList'
	]
)
#<DefinePrint>