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

#<DefineLocals>
NeurongroupPreTeamKeyStr='Pres'
NeurongroupPostTeamKeyStr='Posts'
NeurongroupSpikeTeamKeyStr='Spikes'
NeurongroupStateTeamKeyStr='States'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class NeurongrouperClass(BaseClass):
	
	def default_init(self,
						_NeurongroupDeriveBrianerVariable=None,
						_NeurongroupingBrianKwargDict=None,
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

		#team
		map(
				lambda __KeyStr:
				self.team(__KeyStr),
				[
					NeurongroupPreTeamKeyStr,
					NeurongroupPostTeamKeyStr,
					NeurongroupSpikeTeamKeyStr,
					NeurongroupStateTeamKeyStr
				]

			)

	def do_neurongroup(
				self
			):	

		#debug
		'''
		self.debug(('self.',self,[
							'NeurongroupingBrianKwargDict'
							]))
		'''

		#maybe should import
		from brian2 import NeuronGroup,SpikeMonitor,StateMonitor

		#Check
		if 'N' not in self.NeurongroupingBrianKwargDict:
			self.NeurongroupingBrianKwargDict['N']=self.SimulatingUnitsInt

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
						self.TeamDict[NeurongroupPostTeamKeyStr].ManagementDict.values()
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
				self.TeamDict[NeurongroupPreTeamKeyStr].ManagementDict.values()
			)

		#debug
		'''
		self.debug(('self.',self,[
							'NeurongroupedPostModelInsertStrsList',
							'NeurongroupedPostModelAddDict'
						]))
		'''

		#Check
		if 'model' not in self.NeurongroupingBrianKwargDict:
			self.NeurongroupingBrianKwargDict['model']=''
			
		#add synaptic model variables
		map(
				lambda __NeurongroupedPostModelInsertStr:
				self.NeurongroupingBrianKwargDict.__setitem__(
					'model',
					self.NeurongroupingBrianKwargDict['model'
					]+'\n'+__NeurongroupedPostModelInsertStr
				),
				self.NeurongroupedPostModelInsertStrsList
			)

		#map
		self.NeurongroupedEquationStrsList=map(
				lambda __KeyStr:
				SYS.chunk(
					['d'+__KeyStr+'/dt',')/'],
					self.NeurongroupingBrianKwargDict['model'],
				)[0],
				self.NeurongroupedPostModelAddDict.keys()
			)

		#map
		map(
				lambda __NeurongroupedEquationStr,__AddStrsList:
				self.NeurongroupingBrianKwargDict.__setitem__(
					'model',
					self.NeurongroupingBrianKwargDict['model'].replace(
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
							'NeurongroupingBrianKwargDict'
							]))
		'''

		#init
		self.NeurongroupedBrianVariable=NeuronGroup(
			**self.NeurongroupingBrianKwargDict 
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
						lambda __DeriveMoniter:
						__DeriveMoniter.__setitem__(
							'SpikeMonitor',
							SpikeMonitor(
								self.NeurongroupedBrianVariable
							)
						).SpikeMonitor,
						self.TeamDict[NeurongroupSpikeTeamKeyStr].ManagementDict.values()
					)

		#debug
		'''
		self.debug(
			[
				('self.',self,[
					'NeurongroupedSpikeMonitorsList'
					])
			]
		)
		'''

		#map
		self.NeurongroupedStateMonitorsList=map(
				lambda __DeriveMoniter:
				__DeriveMoniter.__setitem__(
					'StateMonitor',
					StateMonitor(
						self.NeurongroupedBrianVariable,
						__DeriveMoniter.MoniteringVariableStr,
						__DeriveMoniter.MoniteringRecordTimeIndexIntsArray
					)
				).StateMonitor,
				self.TeamDict[NeurongroupStateTeamKeyStr].ManagementDict.values()
			)

		#debug
		'''
		self.debug(('self.',self,['NeurongroupedStateMonitorsList']))
		'''

	"""
	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#debug
		self.debug(
			[
				'We have grand parents',
				'map(type,self.ParentedDeriveTeamersList) is '+str(
					map(type,self.ParentedDeriveTeamersList))
			]	
		)

		#Check
		if type(self.ParentTopDeriveTeamerVariable)==SYS.BrianerClass:

			#alias
			self.NeurongroupDeriveBrianerVariable=self.ParentTopDeriveTeamerVariable
		else:

			#index
			self.NeurongroupDeriveBrianerVariable=self.ParentedDeriveTeamersList[
				map(
					type,
					self.ParentedDeriveTeamersList
				).index(SYS.BrianerClass)
			]

		#manage self
		self.NeurongroupDeriveBrianerVariable.TeamDict[
			self.ParentTopDeriveTeamerVariable.Module.BrianPopulationTeamKeyStr
		].manage(self)

		#call the base method
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)
	"""

#</DefineClass>

#</DefinePrint>
NeurongrouperClass.PrintingClassSkipKeyStrsList.extend(
	[
		'NeurongroupingBrianKwargDict',
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
