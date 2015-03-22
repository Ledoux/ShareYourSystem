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
SYS.addDo('Neurongrouper','Neurongroup','Neurongrouping','Neurongrouped')
#</DefineAugmentation>

#<ImportSpecificModules>
Classer=DecorationModule
from ShareYourSystem.Standards.Itemizers import Networker
from ShareYourSystem.Standards.Recorders import Tracer,Moniter
#</ImportSpecificModules>

#<DefineLocals>
class PostletsClass(Networker.NetworkerClass):pass
class PreletsClass(Networker.NetworkerClass):pass
NeurongroupPostTeamKeyStr="Postlets"
NeurongroupPreTeamKeyStr="Prelets"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class NeurongrouperClass(BaseClass):
	
	def default_init(self,
						_NeurongroupingBrianDict=None,
						_NeurongroupingStatesDict=None,
						_NeurongroupingSpikesDict=None,
						_NeurongroupedBrianVariable=None,
						_NeurongroupedDeriveTracersList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_neurongroup(
				self
			):	

		#/########################/#
		# Import brian 
		# adapt the shape of the NeurongroupingBrianDict

		#debug
		'''
		self.debug(
			[
				'We adapt the shape of NeurongroupingBrianDict',
				('self.',self,[
							'NeurongroupingBrianDict'
							])
			]
		)
		'''

		#Check
		if 'N' not in self.NeurongroupingBrianDict:
			self.NeurongroupingBrianDict['N']=self.SimulatingUnitsInt
		else:
			self.SimulatingUnitsInt=self.NeurongroupingBrianDict['N']

		#Check
		if 'model' not in self.NeurongroupingBrianDict:
			self.NeurongroupingBrianDict['model']=''

		#/##################/#
		# Set finally the Neurongroup
		#

		#Check
		if self.NeurongroupingBrianDict['model']!="" or  self.NeurongroupingBrianDict['N']>0:
		
			#maybe should import
			from brian2 import NeuronGroup

			#debug
			self.debug(
				[
					'We set the Neurongroup',
					('self.',self,[
								'NeurongroupingBrianDict'
								])
				]
			)

			#init
			self.NeurongroupedBrianVariable=NeuronGroup(
				**self.NeurongroupingBrianDict 
			)

		else:

			#return
			return

		#/##################/#
		# team Traces first all the brian variables
		#

		#debug
		self.debug(
				[
					'We simulate with neurongroup',
					'adapt the initial conditions of all the brian variables',
					'so first we team Traces and put Tracers inside'
				]
			)

		#Check
		if 'Traces' not in self.TeamDict:
			NeurongroupedTracesDeriveTeamer=self.team(
				'Traces'
			).TeamedValueVariable
		else:
			NeurongroupedTracesDeriveTeamer=self.TeamDict[
					'Traces'
				]

		#map
		self.NeurongroupedDeriveTracersList=map(
				lambda __TraceStr:
				NeurongroupedTracesDeriveTeamer.manage(
					Tracer.TracerPrefixStr+__TraceStr,
					{
						'TracingKeyVariable':getattr(
							self.NeurongroupedBrianVariable,
							__TraceStr
						),
						'TraceKeyStr':__TraceStr
					}
				).ManagedValueVariable,
				self.NeurongroupedBrianVariable.equations._equations.keys()
			)

		#/##################/#
		# Now analyze the NeurongroupingStatesDict to set Moniters
		#

		#debug
		self.debug(
				[
					'We analyze the NeurongroupingStatesDict',
					('self.',self,['NeurongroupingStatesDict'])
				]
			)

		#get
		NeurongroupedTracesMoniterKeyStrsList=Moniter.MoniterClass.DoingAttributeVariablesOrderedDict.keys()

		#map
		self.NeurongroupedDeriveMonitersList=SYS.flat(
			map(
				lambda __DeriveMoniter,__SampleTuplesList:
				map(
					lambda __SampleTuple:
					__DeriveMoniter.manage(
							__SampleTuple[0],
							SYS.match(
								NeurongroupedTracesMoniterKeyStrsList,
								__SampleTuple[1:]
							)
					).ManagedValueVariable,
					__SampleTuplesList
				),
				map(
					lambda __KeyStr:
					NeurongroupedTracesDeriveTeamer.ManagementDict[
						Tracer.TracerPrefixStr+__KeyStr
					].team('Samples').TeamedValueVariable,
					self.NeurongroupingStatesDict.keys()
				),
				self.NeurongroupingStatesDict.values()
			)
		)

		#/##################/#
		# Set Monitors inside
		#

		#Check
		if len(NeurongroupedTracesMoniterKeyStrsList)>0:

			#debug
			self.debug(
				[
					'We set the brian monitor inside'
				]
			)

			#import
			from brian2 import StateMonitor

			#map
			self.NeurongroupedDeriveStateMonitorsList=map(
				lambda __NeurongroupedDeriveMoniter:
				__NeurongroupedDeriveMoniter.set(
					'MonitBrianVariable',
					StateMonitor(
								#NeuronGroup
								self.NeurongroupedBrianVariable,
								#varname
								__NeurongroupedDeriveMoniter.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable.TraceKeyStr,
								#record
								__NeurongroupedDeriveMoniter.MoniteringLabelIndexIntsArray
							)
				).MonitBrianVariable,
				self.NeurongroupedDeriveMonitersList
			)

		#/##################/#
		# team Events 
		#

		

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

	def mimic_simulate(
				self
			):

		#/##################/#
		# Team States first all the brian variables
		#

		#debug
		self.debug(
				[
					'We simulate with neurongroup'
					'adapt the initial conditions of all the brian variables',
					'so first we team in States'
				]
			)

		#Check
		if Tracer.TracerTracesTeamKeyStr not in self.TeamDict:
			self.team(Tracer.TracerTracesTeamKeyStr)

		#map
		map(
				lambda __TraceStr:
				self.TeamDict[
					Tracer.TracerTracesTeamKeyStr
				].manage(
					Tracer.TracerPrefixStr+__TraceStr,
					{
						'TracingKeyVariable':getattr(
							self.NeurongroupedBrianVariable,
							__TraceStr
						)
					}
				),
				self.NeurongroupedBrianVariable.equations._equations.keys()
			)
		
		#/##################/#
		# Call the base method
		#

		#simulate
		BaseClass.simulate(self)




#</DefineClass>

#<DefineLocals>

#set
#SpikesClass.ManagingValueClass=Moniter.MoniterClass
#StatesClass.ManagingValueClass=Moniter.MoniterClass

#update
#NeurongrouperClass.TeamingClassesDict.update(
#	{
#		'Spikes':SpikesClass,
#		'States':StatesClass
#	}
#)

#</DefineLocals>


#</DefinePrint>
NeurongrouperClass.PrintingClassSkipKeyStrsList.extend(
	[
		'NeurongroupingBrianDict',
		'NeurongroupingStatesDict',
		'NeurongroupingSpikesDict',
		'NeurongroupedBrianVariable',
		'NeurongroupedDeriveTracersList',
		'NeurongroupedDeriveMonitersList'
	]
)
#<DefinePrint>
