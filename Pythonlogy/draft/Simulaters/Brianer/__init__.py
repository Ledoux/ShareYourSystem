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
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Simulater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Pointer,Networker
from ShareYourSystem.Standards.Recorders import Recorder,Tracer
#</ImportSpecificModules>

#<DefineLocals>
BrianNeurongroupsTeamKeyStr="Neurongroups"
BrianStatesTeamKeyStr="States"
class StatesClass(Networker.NetworkerClass):pass
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['brian']
})
class BrianerClass(BaseClass):
		
	def default_init(self,
			_BrianingNeurongroupDict=None,
			_BrianingTraceDict=None,
			_BrianingMoniterTuple=None,
			_BrianingSpikesDict=None,
			_BrianedNeurongroupVariable=None,
			_BrianedTraceKeyStrsList=None,
			_BrianedDeriveTracersList=None,
			_BrianedParentNeurongroupDeriveBrianerVariable=None,
			_BrianedStateMonitersList=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_brian(self):

		#/########################/#
		# Import brian 
		# adapt the shape of the BrianingNeurongroupDict

		#debug
		self.debug(
			[
				'We brian here',
				'We adapt the shape of BrianingNeurongroupDict',
				('self.',self,[
							'BrianingNeurongroupDict',
							'TracingKeyVariable'
						])
			]
		)

		#Check
		if 'N' not in self.BrianingNeurongroupDict:
			self.BrianingNeurongroupDict['N']=self.SimulatingUnitsInt
		else:
			self.SimulatingUnitsInt=self.BrianingNeurongroupDict['N']

		#Check
		if 'model' not in self.BrianingNeurongroupDict:
			self.BrianingNeurongroupDict['model']=''

		#/##################/#
		# Set finally the Neurongroup
		#

		#Check
		if self.BrianingNeurongroupDict['model']!="" or self.BrianingNeurongroupDict['N']>0:
		
			#maybe should import
			from brian2 import NeuronGroup

			#debug
			'''
			self.debug(
				[
					'It is a Neurongroup level, we set the Neurongroup',
					('self.',self,[
								'BrianingNeurongroupDict'
								])
				]
			)
			'''

			#init
			self.BrianedNeurongroupVariable=NeuronGroup(
				**self.BrianingNeurongroupDict 
			)

			#debug
			'''
			self.debug(
				[
					'Ok we have setted the Neurongroup',
					('self.',self,[
								'BrianedNeurongroupVariable'
								])
				]
			)
			'''

			#/##################/#
			# team Traces first all the brian variables
			#

			#get
			self.BrianedTraceKeyStrsList=self.BrianedNeurongroupVariable.equations._equations.keys()

			if len(self.BrianedTraceKeyStrsList)>0:

				#debug
				'''
				self.debug(
						[
							'We simulate with neurongroup',
							'adapt the initial conditions of all the brian variables',
							'so first we team Traces and put Tracers inside or get it and mapSet'
						]
					)
				'''

				#Check
				if 'Traces' not in self.TeamDict:
					BrianedDeriveTraces=self.team(
						BrianStatesTeamKeyStr
					).TeamedValueVariable
				else:
					BrianedDeriveTraces=self.TeamDict[
							BrianStatesTeamKeyStr
						]

				#map
				self.BrianedDeriveTracersList=map(
						lambda __ManagementKeyStr,__TraceKeyStr:
						BrianedDeriveTraces.manage(
								__ManagementKeyStr,
								{
									'TracingKeyVariable':getattr(
										self.BrianedNeurongroupVariable,
										__TraceKeyStr
									),
									'TraceKeyStr':__TraceKeyStr
								}
							).ManagedValueVariable
						if __ManagementKeyStr not in BrianedDeriveTraces.ManagementDict
						else BrianedDeriveTraces.ManagementDict[__ManagementKeyStr].mapSet(
							{
								'TracingKeyVariable':getattr(
									self.BrianedNeurongroupVariable,
									__TraceKeyStr
								),
								'TraceKeyStr':__TraceKeyStr
							}
						),
						map(
							lambda __BrianedTraceKeyStr:
							Tracer.TracerPrefixStr+__BrianedTraceKeyStr,
							self.BrianedTraceKeyStrsList
						),
						self.BrianedTraceKeyStrsList
					)

				#/##################/#
				# We make brian the Tracers
				#

				#debug
				self.debug(
						[
							'Make brian the tracers',
							('self.',self,['BrianedDeriveTracersList'])
						]
					)

				#map
				map(
					lambda __BrianedDeriveTracer:
					__BrianedDeriveTracer.brian(),
					self.BrianedDeriveTracersList
				)

				#debug
				self.debug(
						[
							'Ok the Tracers have brianed',
						]
					)


			"""
			#/##################/#
			# Now analyze the NeurongroupingStatesDict to set Moniters
			#

			#debug
			'''
			self.debug(
					[
						'We analyze the NeurongroupingStatesDict',
						('self.',self,['NeurongroupingStatesDict'])
					]
				)
			'''

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
						BrianedDeriveTraces.ManagementDict[
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
									self.BrianedNeurongroupVariable,
									#varname
									__NeurongroupedDeriveMoniter.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable.TraceKeyStr,
									#record
									__NeurongroupedDeriveMoniter.MoniteringLabelIndexIntsArray
								)
					).MonitBrianVariable,
					self.NeurongroupedDeriveMonitersList
				)
		"""

		elif self.TracingKeyVariable!=None:

			#debug
			self.debug(
				[
					'It is a Tracer level, we set the Samples',
					('self.',self,[
								'TracingKeyVariable',
								'TraceKeyStr'
								])
				]
			)

			#get
			self.BrianedParentNeurongroupDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/###################/#
			# Build the samples and maybe one default moniter
			#

			#Check
			if 'Samples' not in self.TeamDict:
				BrianedDeriveSamples=self.team(
					'Samples'
				).TeamedValueVariable
			else:
				BrianedDeriveSamples=self.TeamDict[
						'Samples'
					]

			#debug
			self.debug(
				[
					'Do we have to set a default moniter ?',
					'len(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedTraceKeyStrsList) is ',
					str(len(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedTraceKeyStrsList))
				]
			)

			#Check
			if len(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedTraceKeyStrsList)==1:

				#Check
				if len(BrianedDeriveSamples.ManagementDict)==0:

					BrianedDefaultMoniter=BrianedDeriveSamples.manage(
						'Default',

					).ManagedValueVariable
					BrianedDefaultMoniter.MoniteringLabelIndexIntsArray=[0] if self.BrianedParentNeurongroupDeriveBrianerVariable.BrianingNeurongroupDict[
					'N']>0 else []


			#/###################/#
			# We make brian the Moniters
			#

			#debug
			self.debug(
				[
					'We make brian the moniters',
					'BrianedDeriveSamples.ManagementDict.keys() is ',
					str(BrianedDeriveSamples.ManagementDict.keys())
				]
			)

			#map
			map(
				lambda __DeriveMoniter:
				__DeriveMoniter.brian(),
				BrianedDeriveSamples.ManagementDict.values()
			)

			#/###################/#
			# We trace and set to the brian value
			#

			#debug
			self.debug(
				[
					'We trace and alias the init in the brian object',
					('self.',self,['TracingKeyVariable'])
				]
			)

			#trace
			self.trace()

			#debug
			self.debug(
				[
					'We have traced, alias the init in the brian object',
					('self.',self,[
						'TracedValueFloatsArray',
						'TracedInitFloatsArray'
					])
				]
			)
			
			#alias
			self.TracedValueFloatsArray[:]=self.TracedInitFloatsArray*self.TracedValueFloatsArray.unit

			#debug
			self.debug(
				[
					('self.',self,['TracedValueFloatsArray'])
				]
			)
		

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#/##################/#
		# Call the parent method
		#

		#set
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)


		#/##################/#
		# brian
		#

		#brian
		self.brian()


#</DefineClass>

#<DefineLocals>

#set
BrianerClass.TeamingClassesDict.update(
	{
		'States':StatesClass,
		'Samples':StatesClass
	}
)
StatesClass.ManagingValueClass=BrianerClass

#</DefineLocals>


#</DefinePrint>
BrianerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'BrianingNeurongroupDict',
		'BrianingTraceDict',
		'BrianingSpikesDict',
		'BrianedNeurongroupVariable',
		'BrianedTraceKeyStrsList',
		'BrianedDeriveTracersList',
		'BrianedStateMonitersList'
	]
)
#<DefinePrint>
