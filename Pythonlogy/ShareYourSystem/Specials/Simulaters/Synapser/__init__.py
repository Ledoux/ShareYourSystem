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
	
	#Definition
	RepresentingKeyStrsList=[
									'SynapsingKwargVariablesDict',
									'SynapsingProbabilityVariable',
									'SynapsingTagStr',
									'SynapsingWeigthSymbolStr',
									'SynapsingWeigthFloatsArray',
									'SynapsedBrianVariable',
							]

	def default_init(self,
						_SynapsingKwargVariablesDict=None,
						_SynapsingProbabilityVariable=None,
						_SynapsingTagStr="",
						_SynapsingWeigthSymbolStr="",
						_SynapsingWeigthFloatsArray=None,
						_SynapsedBrianVariable=None,
						_SynapsedWeigthFloatsArray=None,
						**_KwargVariablesDict
					):

		#init
		self.PostModelInsertStrsList=[]
		self.PostModelAddDict={}

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_synapse(
				self
			):	

		
		#Maybe should import
		import brian2

		#debug
		'''
		self.debug(('self.',self,[
								'SynapsingKwargVariablesDict'
								]))
		'''
		
		#init
		self.SynapsedBrianVariable=brian2.Synapses(
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
