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
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Simulater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Specials.Simulaters import Synapser
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class NeurongrouperClass(BaseClass):
	
	def default_init(self,
						_NeurongroupingKwargVariablesDict=None,
						_NeurongroupingVariableStrToGetStrDict=None,
						_NeurongroupedPostModelInsertStrsList=None,
						_NeurongroupedPostModelAddDict=None,
						_NeurongroupedEquationStrsList=None,
						_NeurongroupedBrianVariable=None,
						_NeurongroupedSpikeMonitorsList=None,
						_NeurongroupedStateMonitorsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

		#set
		self.CatchingDerivePointerClass=Synapser.SynapserClass

		#
		self.node('PostConnecters')
		self.node('PreConnecters')

	def do_neurongroup(
				self
			):	

		#populate before
		self.populate()

		#debug
		self.debug(('self.',self,[
							'NeurongroupingKwargVariablesDict'
							]))

		#maybe should import
		from brian2 import NeuronGroup,SpikeMonitor,StateMonitor

		#Check
		if 'N' not in self.NeurongroupingKwargVariablesDict:
			self.NeurongroupingKwargVariablesDict['N']=self.SimulatingUnitsInt

		#add the synaptic model strs
		'''
		self.debug(('self.',self,['CollectionsOrderedDict']))
		'''

		#map
		self.NeurongroupedPostModelInsertStrsList=list(
			set(
				SYS.flat(
					map(
						lambda __PreConnecter:
						__PreConnecter.PostModelInsertStrsList,
						self.PreConnectersCollectionOrderedDict.values()
					)
				)
			)
		)

		#map
		'''
		self.debug(
			[
				'self.PreConnectersCollectionOrderedDict.keys() is ',
				self.PreConnectersCollectionOrderedDict.keys(),
				'self.PostConnectersCollectionOrderedDict.keys() is ',
				self.PostConnectersCollectionOrderedDict.keys(),
			]
		)
		'''

		#map
		map(
				lambda __PreConnecter:
				map(
						lambda __ItemTuple:
						self.NeurongroupedPostModelAddDict.__setitem__(
							__ItemTuple[0],
							list(
								set(
									(self.NeurongroupedPostModelAddDict[__ItemTuple[0]]
									if __ItemTuple[0] in self.NeurongroupedPostModelAddDict
									else [])+__ItemTuple[1]
								)
							)
						),
						__PreConnecter.PostModelAddDict.items()
				),
				self.PreConnectersCollectionOrderedDict.values()
			)

		#debug
		'''
		self.debug(('self.',self,[
							'NeurongroupedPostModelInsertStrsList',
							'NeurongroupedPostModelAddDict'
						]))
		'''

		#Check
		if 'model' not in self.NeurongroupingKwargVariablesDict:
			self.NeurongroupingKwargVariablesDict['model']=''
			
		#add synaptic model variables
		map(
				lambda __NeurongroupedPostModelInsertStr:
				self.NeurongroupingKwargVariablesDict.__setitem__(
					'model',
					self.NeurongroupingKwargVariablesDict['model'
					]+'\n'+__NeurongroupedPostModelInsertStr
				),
				self.NeurongroupedPostModelInsertStrsList
			)

		#map
		self.NeurongroupedEquationStrsList=map(
				lambda __KeyStr:
				SYS.chunk(
					['d'+__KeyStr+'/dt',')/'],
					self.NeurongroupingKwargVariablesDict['model'],
				)[0],
				self.NeurongroupedPostModelAddDict.keys()
			)

		#map
		map(
				lambda __NeurongroupedEquationStr,__AddStrsList:
				self.NeurongroupingKwargVariablesDict.__setitem__(
					'model',
					self.NeurongroupingKwargVariablesDict['model'].replace(
						__NeurongroupedEquationStr,
						__NeurongroupedEquationStr+'+'+'+'.join(__AddStrsList)
					)
				),
				self.NeurongroupedEquationStrsList,
				self.NeurongroupedPostModelAddDict.values()
		)

		#debug
		'''
		self.debug(('self.',self,[
							'NeurongroupedEquationStrsList',
							'NeurongroupingKwargVariablesDict'
							]))
		'''

		#init
		self.NeurongroupedBrianVariable=NeuronGroup(
			**self.NeurongroupingKwargVariablesDict 
		)

		#debug
		'''
		self.debug(('self.',self,['NeurongroupedBrianVariable']))
		'''

		#update variables
		map(
				lambda __ItemTuple:
				setattr(
					self.NeurongroupedBrianVariable,
					__ItemTuple[0],
					self[__ItemTuple[1]]
				),
				self.NeurongroupingVariableStrToGetStrDict.items()
			)

		#debug
		'''
		self.debug(('self.',self,['NeurongroupedBrianVariable']))
		'''

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
						__PopulatedStateDeriveMoniter.MoniteringRecordTimeIndexIntsArray
					)
				).StateMonitor,
				self.PopulatedStateDeriveMonitersList
			)

#</DefineClass>

#</DefinePrint>
NeurongrouperClass.PrintingClassSkipKeyStrsList.extend(
	[
		'NeurongroupingKwargVariablesDict',
		'NeurongroupingVariableStrToGetStrDict',
		'NeurongroupedPostModelInsertStrsList',
		'NeurongroupedPostModelAddDict',
		'NeurongroupedEquationStrsList',
		'NeurongroupedBrianVariable',
		'NeurongroupedSpikeMonitorsList',
		'NeurongroupedStateMonitorsList'
	]
)
#<DefinePrint>
