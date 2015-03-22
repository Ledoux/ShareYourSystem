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
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Runner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
from ShareYourSystem.Specials.Simulaters import Populater
import operator
#</ImportSpecificModules>

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
							'BrianedClocksList',
							'BrianedSimulationClock',
							'BrianedNeuronGroupsList',
							'BrianedStateMonitorsList',
							'BrianedSpikeMonitorsList',
							'BrianedConnectionsList',
						]

	def default_init(self,
						_BrianingTimeDimensionVariable=None,
						_BrianingPrintRunIsBool=True,
						_BrianedNetworkVariable=None,
						_BrianedClocksList=None,
						_BrianedSimulationClock=None,
						_BrianedNeuronGroupsList=None,
						_BrianedStateMonitorsList=None,
						_BrianedSpikeMonitorsList=None,
						_BrianedConnectionsList=None,
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
				'RecruitingConcludeConditionVariable':[
					(
						'__class__.__mro__',
						operator.contains,Populater.PopulaterClass
					)
				]
			}
		)

		"""
		#populate
		map(
				lambda __NetworkedDeriveConnecter:
				__NetworkedDeriveConnecter.populate(),
				self.NetworkedDeriveConnectersList
			)
		
		"""

		#set the different times
		self.BrianedStepTimeFloatsList=list(
			set(
				SYS.flat(
					map(
						lambda __BrianingDerivePopulater:
						SYS.unzip(
							__BrianingDerivePopulater.MoniteringStateTuplesList,
							[2]
						) if len(
							__BrianingDerivePopulater.MoniteringStateTuplesList
						)>0 else [],
						self.NetworkedDeriveConnectersList
					)
				)
			)
		)

		#debug
		'''
		self.debug(('self.',self,['BrianedStepTimeFloatsList']))
		'''

		#import 
		import brian

		#Check
		if self.BrianingTimeDimensionVariable==None:
			self.BrianingTimeDimensionVariable=brian.ms

		#init
		self.BrianedNetworkVariable=brian.MagicNetwork()
		
		#set the clocks
		self.BrianedSimulationClock=brian.Clock(
								dt=self.SimulatingStepTimeFloat*self.BrianingTimeDimensionVariable
							)
		self.BrianedClocksDict=dict(
			map(
				lambda __BrianedStepTimeFloat:
				(
					str(__BrianedStepTimeFloat),
					brian.Clock(
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
		self.debug(('self.',self,['BrianedClocksDict']))
		
		#set clock to the neuron groups
		self.BrianedNeuronGroupsList=map(
				lambda __BrianingDerivePopulater:
				__BrianingDerivePopulater.__setitem__(
					'NeuronGroup',
					brian.NeuronGroup(
						__BrianingDerivePopulater.PopulatingUnitsInt,
						__BrianingDerivePopulater.PopulatingEquationStr,
						clock=self.BrianedClocksDict[str(self.SimulatingStepTimeFloat)]
					)
				).NeuronGroup,
				self.NetworkedDeriveConnectersList
			)

		#set the clocks and state monitors
		self.BrianedStateMonitorsList=SYS.flat(
			map(
				lambda __BrianingDerivePopulater:
					map(
							lambda __MoniteringStateTuple:
							__BrianingDerivePopulater.__setitem__(
								str(__MoniteringStateTuple)+'StateMonitor',
								getattr(
									brian,
									'StateMonitor'
								)(
									__BrianingDerivePopulater.NeuronGroup,
									__MoniteringStateTuple[0],
									record=__MoniteringStateTuple[1],
									clock=self.BrianedClocksDict[str(__MoniteringStateTuple[2])]
								)
							).SettingValueVariable,
							__BrianingDerivePopulater.MoniteringStateTuplesList
					),
					self.NetworkedDeriveConnectersList
				)
			)

		#set the spike monitors
		self.BrianedSpikeMonitorsList=SYS.flat(
			map(
				lambda __BrianingDerivePopulater:
					map(
							lambda __MoniteringSpikeTuple:
							__BrianingDerivePopulater.__setitem__(
								str(__MoniteringSpikeTuple)+'SpikeMonitor',
								getattr(
									brian,
									'SpikeMonitor'
								)(
									__BrianingDerivePopulater.NeuronGroup,
								)
							).SettingValueVariable,
							__BrianingDerivePopulater.MoniteringSpikeTuplesList
					),
					self.NetworkedDeriveConnectersList
				)
			)

		#set the post synapses
		self.BrianedSpikeMonitorsList=SYS.flat(
				map(
					lambda __BrianingDerivePopulater:
					map(
							lambda __MoniteringSpikeTuple:
							__BrianingDerivePopulater.__setitem__(
								str(__MoniteringSpikeTuple)+'SpikeMonitor',
								getattr(
									brian,
									'SpikeMonitor'
								)(
									__BrianingDerivePopulater.NeuronGroup,
								)
							).SettingValueVariable,
							__BrianingDerivePopulater.MoniteringSpikeTuplesList
					),
					self.NetworkedDeriveConnectersList
				)
			)

		#debug
		'''
		self.debug(('self.',self,['NetworkedConnectionTuplesList']))
		'''

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

		#add
		map(
				lambda __BrianedVariable:
				BrianedNetworkVariable.add(__BrianedVariable),
				self.BrianedNeuronGroupsList+self.BrianedConnectionsList+self.BrianedMonitorsList
			)

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
