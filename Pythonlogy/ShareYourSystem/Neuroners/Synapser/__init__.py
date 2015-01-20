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
BaseModuleStr="ShareYourSystem.Itemizer.Pointer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
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
									'SynapsingProbabilityFloat',
									'SynapsedBrianVariable'
							]

	def default_init(self,
						_SynapsingKwargVariablesDict=None,
						_SynapsingProbabilityFloat=0.,
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

		#set
		self.SynapsedBrianVariable=brian2.Synapses(**self.SynapsingKwargVariablesDict)



#</DefineClass>
