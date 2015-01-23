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
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Populater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Brianers import Synapser
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class NeurongrouperClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'NeurongroupingKwargVariablesDict',
								'NeurongroupedBrianVariable',
								'NeurongroupedSpikeMonitorsList',
								'NeurongroupedStateMonitorsList'
							]

	def default_init(self,
						_NeurongroupingKwargVariablesDict=None,
						_NeurongroupedBrianVariable=None,
						_NeurongroupedSpikeMonitorsList=None,
						_NeurongroupedStateMonitorsList=None,
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
		from brian2 import NeuronGroup,SpikeMonitor,StateMonitor

		#debug
		self.debug(('self.',self,[
							'NeurongroupingKwargVariablesDict'
							]))
		
		#init
		self.NeurongroupedBrianVariable=NeuronGroup(
			**self.NeurongroupingKwargVariablesDict 
		)

		#debug
		self.debug(('self.',self,['NeurongroupedBrianVariable']))

		#map
		self.NeurongroupedSpikeMonitorsList=map(
						lambda __PopulatedEventDeriveMoniter:
						__PopulatedEventDeriveMoniter.__setitem__(
							'SpikeMonitor',
							SpikeMonitor(
								self.NeurongroupedBrianVariable
							)
						).SpikeMonitor,
						self.PopulatedEventDeriveMonitersList
					)

		#map
		self.NeurongroupedStateMonitorsList=map(
				lambda __PopulatedStateDeriveMoniter:
				__PopulatedStateDeriveMoniter.__setitem__(
					'StateMonitor',
					StateMonitor(
						self.NeurongroupedBrianVariable,
						__PopulatedStateDeriveMoniter.MoniteringVariableStr,
						__PopulatedStateDeriveMoniter.MoniteringIndexIntsList
					)
				).StateMonitor,
				self.PopulatedStateDeriveMonitersList
			)

#</DefineClass>
