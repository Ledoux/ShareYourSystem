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
import brian

from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class BrianerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'BrianedNetworkVariable',
									'BrianedClocksList',
									'BrianedNeuronGroupsList',
									'BrianedConnectionsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_BrianingTimeDimensionVariable=brian.ms,
						_BrianedNetworkVariable=None,
						_BrianedClocksList=None,
						_BrianedNeuronGroupsList=None,
						_BrianedConnectionsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Imitater.ImitaterClass()
	def mimic_run(self):

		#brian first
		self.brian()

		#parent method
		BaseClass.run(self)

		#run with the brian method
		self.BrianedNetworkVariable.run(
			self.RunningTimeFloat*self.BrianingTimeDimensionVariable
		)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	#@Argumenter.ArgumenterClass()
	def do_brian(self):	

		#network first
		self.network()

		#import 
		import brian

		#init
		self.BrianedNetworkVariable=brian.MagicNetwork()

		#set the different times
		self.BrianedStepTimeFloatsList=list(
			set(
				SYS.flat(
					map(
						lambda __BrianingDerivePopulater:
						SYS.unzip(
							__BrianingDerivePopulater.MoniteringTrackTuplesList,
							[3]
						) if len(
							__BrianingDerivePopulater.populate().MoniteringTrackTuplesList
						)>0 else [],
						self.NetworkedDeriveConnectersList
					)
				)
			)
		)

		#set the clocks
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
				str(self.SimulatingStepTimeFloat):brian.Clock(
							dt=self.SimulatingStepTimeFloat*self.BrianingTimeDimensionVariable
						)
			}
		)

		#set neuron groups
		self.BrianedNeuronGroupsList=map(
				lambda __BrianingDerivePopulater:
				__BrianingDerivePopulater.point(
					brian.NeuronGroup(
							__BrianingDerivePopulater.PopulatingUnitsInt,
							__BrianingDerivePopulater.PopulatingEquationStr,
							clock=self.BrianedClocksDict[str(self.SimulatingStepTimeFloat)]
					),
					'NeuronGroupVariable',
					False
				).NeuronGroupVariable,
				self.NetworkedDeriveConnectersList
			)


		

		#debug
		'''
		self.debug(('self.',self,['BrianedStepTimeFloatsList']))
		'''

		

		#debug
		'''
		self.debug(('self.',self,['BrianedClocksDict']))
		'''

		#set the clocks and monitors
		self.BrianedMonitorsList=SYS.flat(
			map(
				lambda __BrianingDerivePopulater:
					map(
							lambda __MoniteringTrackTuple:
							__BrianingDerivePopulater.populate().point(
								getattr(
									brian,
									__MoniteringTrackTuple[0]+'Monitor'
								)(
									__BrianingDerivePopulater.NeuronGroupVariable,
									__MoniteringTrackTuple[1],
									record=__MoniteringTrackTuple[2],
									clock=self.BrianedClocksDict[str(__MoniteringTrackTuple[3])]
								),
								'MonitorVariable',
								False
							).MonitorVariable,
							__BrianingDerivePopulater.MoniteringTrackTuplesList
					),
					self.NetworkedDeriveConnectersList
				)
			)

		#debug
		'''
		self.debug(('self.',self,['NetworkedConnectionTuplesList']))
		'''

		#set connections
		self.BrianedConnectionsList=map(
				lambda __ConnectionTuple:
				map(
						lambda __ListedVariable:
						__ConnectionTuple[0].point(
							brian.Connection(
								__ConnectionTuple[0].NeuronGroupVariable,
								__ListedVariable.NeuronGroupVariable
							),
							'ConnectionVariable'
						).ConnectionVariable,
						__ConnectionTuple[1][0]
					)+map(
						lambda __ListedVariable:
						__ListedVariable.point(
							brian.Connection(
								__ListedVariable.NeuronGroupVariable,
								__ConnectionTuple[0].NeuronGroupVariable
							),
							'ConnectionVariable'
						).ConnectionVariable,
						__ConnectionTuple[1][1]
					),
				self.NetworkedConnectionTuplesList	
			)
		
		#debug
		'''
		self.debug(('self.',self,['BrianedNeuronGroupsList']))
		'''

		#alias
		BrianedNetworkVariable=self.BrianedNetworkVariable

		#add
		map(
				lambda __BrianingVariable:
				BrianedNetworkVariable.add(__BrianingVariable),
				self.BrianedNeuronGroupsList+self.BrianedConnectionsList+self.BrianedMonitorsList
			)

		#Return self
		#return self

#</DefineClass>
