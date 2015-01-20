# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Neurongrouper

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Populater"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Neuroners import Synapser
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class NeurongrouperClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'NeurongroupingKwargVariablesDict',
								'NeurongroupedBrianVariable'
							]

	def default_init(self,
						_NeurongroupingKwargVariablesDict=None,
						_NeurongroupedBrianVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#set
		self.CatchingDerivePointerClass=Synapser.SynapserClass

	def do_neurongroup(
				self
			):	

		#maybe should import
		import brian2

		#init
		self.NeurongroupedBrianVariable=brian2.NeuronGroup(
			**NeurongroupingKwargVariablesDict 
		)

#</DefineClass>
