# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Brianer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Runner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Noders import Noder
from ShareYourSystem.Simulaters import Populater
import operator
#</ImportSpecificModules>

#<DefineFunctions>
'''
def getStateMonitorWithArgumentVariable(_ArgumentVariable):

	import brian 

	if hasattr(_ArgumentVariable,'items'):
		brian.SpikeMonitor(

			)
'''


#</DefineFunctions>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['brian']
})
class BrianerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
							'BrianingTimeDimensionVariable',
							'BrianingPrintRunIsBool',
							'BrianedNetworkVariable',
							'BrianedDerivePopulatersList',
							'BrianedStepTimeFloatsList',
							'BrianedClocksList',
							'BrianedSimulationClock',
							'BrianedNeuronGroupsList',
							'BrianedStateMonitorsList',
							'BrianedSpikeMonitorsList',
							'BrianedSynapsesList'
						]

	def default_init(self,
						_BrianingTimeDimensionVariable=None,
						_BrianingPrintRunIsBool=True,
						_BrianedNetworkVariable=None,
						_BrianedDerivePopulatersList=None,
						_BrianedStepTimeFloatsList=None,
						_BrianedClocksList=None,
						_BrianedSimulationClock=None,
						_BrianedNeuronGroupsList=None,
						_BrianedStateMonitorsList=None,
						_BrianedSpikeMonitorsList=None,
						_BrianedSynapsesList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_run(self):

		#brian first
		self.brian()

		#parent method
		BaseClass.run(self)

		#debug
		self.debug('We start running in brian')

		#run with the brian method
		self.BrianedNetworkVariable.run(
			self.RunningTimeFloat*self.BrianingTimeDimensionVariable
		)

		#debug
		self.debug('We stop running in brian')

	def do_brian(self):	

		#network first
		self.network(
			**{
				'RecruitingConcludeConditionTuplesList':[
					('__class__.__mro__',operator.contains,Populater.PopulaterClass)
				]
			}
		)

		#link
		self.BrianedDerivePopulatersList=self.NetworkedDeriveConnectersList

		"""
		#populate
		map(
				lambda __NetworkedDeriveConnecter:
				__NetworkedDeriveConnecter.populate(),
				self.NetworkedDeriveConnectersList
			)
		
		"""

		"""
		#set the different times
		self.BrianedStepTimeFloatsList=list(
			set(
				SYS.flat(
					map(
						lambda __BrianingDerivePopulater:
						SYS.unzip(
							__BrianingDerivePopulater.MoniteringStateArgumentVariablesList,
							[2]
						) if len(
							__BrianingDerivePopulater.MoniteringStateArgumentVariablesList
						)>0 else [],
						self.NetworkedDeriveConnectersList
					)
				)
			)
		)
		"""

		#debug
		'''
		self.debug(('self.',self,['BrianedStepTimeFloatsList']))
		'''

		#import 
		import brian2

		#Check
		if self.BrianingTimeDimensionVariable==None:
			self.BrianingTimeDimensionVariable=brian2.ms

		#init
		self.BrianedNetworkVariable=brian2.Network()
		
		#set the clocks
		self.BrianedSimulationClock=brian2.Clock(
								dt=self.SimulatingStepTimeFloat*self.BrianingTimeDimensionVariable
							)
		self.BrianedClocksDict=dict(
			map(
				lambda __BrianedStepTimeFloat:
				(
					str(__BrianedStepTimeFloat),
					brian2.Clock(
							dt=__BrianedStepTimeFloat*self.BrianingTimeDimensionVariable
						)
				),
				self.BrianedStepTimeFloatsList
			)
			,**{
					str(
						self.SimulatingStepTimeFloat
						):self.BrianedSimulationClock
				}
		)

		#debug
		'''
		self.debug(('self.',self,['BrianedClocksDict']))
		'''

		#map
		self.BrianedNeuronGroupsList=map(
			lambda __BrianedDerivePopulater:
			__BrianedDerivePopulater.populate(),
			self.BrianedDerivePopulatersList
			)

		#map
		self.BrianedNeuronGroupsList=map(
			lambda __BrianedDerivePopulater:
			__BrianedDerivePopulater.NeuronGroup
			if hasattr(__BrianedDerivePopulater,'NeuronGroup')
			else __BrianedDerivePopulater.__setitem__(
				'NeuronGroup',
				brian2.NeuronGroup(
					**dict(
						__BrianedDerivePopulater.NeuronGroupKwargDict,
						**{
							'clock':self.BrianedSimulationClock,
							'N':__BrianedDerivePopulater.PopulatingUnitsInt
						}
					)
				)
			).NeuronGroup,
			self.BrianedDerivePopulatersList
		)

		#map
		map(
				lambda __BrianedNeuronGroup:
				__BrianedNeuronGroup.clock.__setattr__(
					'dt',
					self.BrianedSimulationClock.dt
				),
				self.BrianedNeuronGroupsList
			)

		#flat the spike monitors
		self.BrianedSpikeMonitorsList=SYS.flat(
			map(
				lambda __BrianedDerivePopulater:
				map(
						lambda __PopulatedEventDeriveMoniter:
						__PopulatedEventDeriveMoniter.__setitem__(
							'SpikeMonitor',
							brian2.SpikeMonitor(__BrianedDerivePopulater.NeuronGroup)
						).SpikeMonitor,
						__BrianedDerivePopulater.PopulatedEventDeriveMonitersList
					),
				self.BrianedDerivePopulatersList
			)
		)

		#debug
		'''
		self.debug(('self.',self,['BrianedSpikeMonitorsList']))
		'''

		#flat the state monitors
		self.BrianedStateMonitorsList=SYS.flat(
			map(
				lambda __BrianedDerivePopulater:
				map(
						lambda __PopulatedStateDeriveMoniter:
						__PopulatedStateDeriveMoniter.__setitem__(
							'StateMonitor',
							brian2.StateMonitor(
								__BrianedDerivePopulater.NeuronGroup,
								__PopulatedStateDeriveMoniter.MoniteringVariableStr,
								__PopulatedStateDeriveMoniter.MoniteringIndexIntsList
							)
						).StateMonitor,
						__BrianedDerivePopulater.PopulatedStateDeriveMonitersList
					),
				self.BrianedDerivePopulatersList
			)
		)	
		
		#debug
		'''
		self.debug(('self.',self,['BrianedStateMonitorsList']))
		'''

		"""

		#debug
		self.debug(('self.',self,['NetworkedGraphTuplesList']))
		"""

		self.BrianedSynapsesList=map(
				lambda __NetworkedDerivePointer:
				__NetworkedDerivePointer.__setitem__(
					'Synapses',
					brian2.Synapses(
						__NetworkedDerivePointer.CatchFromPointVariable.NeuronGroup,
						__NetworkedDerivePointer.CatchToPointVariable.NeuronGroup,
						**__NetworkedDerivePointer.SynapsesKwargVariablesDict
					)
				).Synapses,
				self.NetworkedDerivePointersList
			)




		'''
		#set connections
		self.BrianedConnectionsList=map(
				lambda __ConnectionTuple:
				map(
						lambda __ListedVariable:
						__ConnectionTuple[0].__setitem__(
							str(
								(
									__ConnectionTuple[0].NodeKeyStr,
									__ListedVariable.NodeKeyStr
								)
							)+'Connection',
							brian.Connection(
								__ConnectionTuple[0].NeuronGroup,
								__ListedVariable.NeuronGroup
							)
						).SettingValueVariable,
						__ConnectionTuple[1][0]
					)+map(
						lambda __ListedVariable:
						__ListedVariable.__setitem__(
							str(
								(
									__ListedVariable.NodeKeyStr,
									__ConnectionTuple[0].NodeKeyStr
								)
							)+'Connection',
							brian.Connection(
								__ListedVariable.NeuronGroup,
								__ConnectionTuple[0].NeuronGroup
							)
						).SettingValueVariable,
						__ConnectionTuple[1][1]
					),
				self.NetworkedConnectionTuplesList	
			)
		'''

		"""
		#debug
		'''
		self.debug(('self.',self,['BrianedNeuronGroupsList']))
		'''

		#alias
		BrianedNetworkVariable=self.BrianedNetworkVariable

		"""

		#add
		map(
				lambda __BrianedVariable:
				self.BrianedNetworkVariable.add(__BrianedVariable),
				self.BrianedNeuronGroupsList+self.BrianedSynapsesList+self.BrianedStateMonitorsList+self.BrianedSpikeMonitorsList
			)

		"""
		#Check
		if self.BrianingPrintRunIsBool:

			#debug
			self.debug(('self.',self,[
								'BrianedSimulationClock'
								]))


			#define
			@brian.network_operation(
				self.BrianedSimulationClock
			)
			def printControl():

				#Print Time
				print(
					"time is "+str(
						self.BrianedSimulationClock.t*self.BrianingTimeDimensionVariable
					)
				)

				'''
				#Print NeuronGroup
				print(
					"variables are"+str(
					self.BrianedNeuronGroupsList[0]
					)
				)
				'''
				
			self.BrianedNetworkVariable.add(printControl);
		"""
#</DefineClass>
