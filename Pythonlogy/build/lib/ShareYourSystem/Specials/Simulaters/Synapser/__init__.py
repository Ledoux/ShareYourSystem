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
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class SynapserClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'SynapsingKwargVariablesDict',
									'SynapsingProbabilityVariable',
									'SynapsedBrianVariable'
							]

	def default_init(self,
						_SynapsingKwargVariablesDict=None,
						_SynapsingProbabilityVariable=None,
						_SynapsedBrianVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_synapse(
				self
			):	

		
		#Maybe should import
		import brian2

		#debug
		self.debug(('self.',self,[
								'SynapsingKwargVariablesDict'
								]))
		
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


#</DefineClass>
