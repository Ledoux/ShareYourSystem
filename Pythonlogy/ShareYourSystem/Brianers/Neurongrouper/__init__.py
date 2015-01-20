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
from ShareYourSystem.Brianers import Synapser
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class NeurongrouperClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'NeurongroupingKwargVariablesDict',
								'NeurongroupedNeuronGroupVariable',
								'NeurongroupedSpikeMonitorsList',
								'NeurongroupedStateMonitorsList'
							]

	def default_init(self,
						_NeurongroupingKwargVariablesDict=None,
						_NeurongroupedNeuronGroupVariable=None,
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

		#init
		self.NeurongroupedNeuronGroupVariable=NeuronGroup(
			**NeurongroupingKwargVariablesDict 
		)

		#map
		self.NeurongroupedSpikeMonitorsList=map(
				lambda __BrianedDerivePopulater:
				map(
						lambda __PopulatedEventDeriveMoniter:
						__PopulatedEventDeriveMoniter.__setitem__(
							'SpikeMonitor',
							SpikeMonitor(
								self.NeurongroupedNeuronGroupVariable.NeuronGroup
							)
						).SpikeMonitor,
						self.PopulatedEventDeriveMonitersList
					)
			)

		#map
		self.NeurongroupedStateMonitorsList=map(
				lambda __PopulatedStateDeriveMoniter:
				__PopulatedStateDeriveMoniter.__setitem__(
					'StateMonitor',
					StateMonitor(
						self.NeurongroupedNeuronGroupVariable,
						__PopulatedStateDeriveMoniter.MoniteringVariableStr,
						__PopulatedStateDeriveMoniter.MoniteringIndexIntsList
					)
				).StateMonitor,
				self.PopulatedStateDeriveMonitersList
			)

#</DefineClass>
