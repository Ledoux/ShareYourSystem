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
BaseModuleStr="ShareYourSystem.Standards.Recorders.Simulater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Recorders import Recorder
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['brian'],
	'ClassingStructureVariable':[
			('Neurongroup','Neurongroups'),
			('Trace','Traces'),
			('Sample','Samples'),
			('Postlet','Postlets'),
			('Event','Events')
		]
})
class BrianerClass(BaseClass):
		
	def default_init(self,
			_BrianingNeurongroupDict=None,
			_BrianingSynapsesDict=None,
			_BrianingConnectVariable=None,
			_BrianingTraceDict=None,
			_BrianingMoniterTuple=None,
			_BrianingSpikesDict=None,
			_BrianingTimeDimensionVariable=None,
			_BrianedNetworkVariable=None,
			_BrianedNeurongroupVariable=None,
			_BrianedSynapsesVariable=None,
			_BrianedStateMonitorVariable=None,
			_BrianedSpikeMonitorVariable=None,
			_BrianedParentSingularStr=None,
			_BrianedRecordKeyStrsList=None,
			_BrianedTraceDeriveBrianersList=None,
			_BrianedSynapsesDeriveBrianersList=None,
			_BrianedStateDeriveBrianersList=None,
			_BrianedSpikeDeriveBrianersList=None,
			_BrianedParentNetworkDeriveBrianerVariable=None,
			_BrianedParentNeurongroupDeriveBrianerVariable=None,
			_BrianedParentDeriveRecorderVariable=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_brian(self):

		#/#################/#
		# Determine if it is an inside structure or the top
		#

		#debug
		'''
		self.debug(
			[
				'We brian here',
				'First look for deeper teams in the structure',
			]
		)
		'''

		#Check
		if self.ParentedTotalSingularListDict!=None and len(self.ParentedTotalSingularListDict)>0:

			#debug
			'''
			self.debug(
				[
					'self.ParentedTotalSingularListDict.keys() is ',
					str(self.ParentedTotalSingularListDict.keys())
				]
			)
			'''

			#get
			self.BrianedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		self.debug(
			[
				'Ok',
				('self.',self,['BrianedParentSingularStr'])
			]
		)

		#Check
		if (self.ParentDeriveTeamerVariable==None or 'Neurongroups' in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces','Samples','Events','Postlets'
		]) and self.BrianedParentSingularStr!='Neurongroup':

			#/########################/#
			# Network level
			# 

			#debug
			self.debug(
				[
					'It is a Network level',
					'We set the brian network'
				]
			)
			
			#import
			from brian2 import Network

			#structure
			self.BrianedNetworkVariable=Network()

			#/########################/#
			# Special Network-Neurongroup level
			# 

			#Check
			if 'Neurongroups' not in self.TeamDict:
		
				#set
				self.BrianedParentNetworkDeriveBrianerVariable=self

				#setNeurongroup
				self.setNeurongroup()

			#/########################/#
			# network
			# 

			#debug
			'''
			self.debug(
				[
					'We structure the Neurongroups Postlets Traces Events Samples',
				]
			)
			'''

			#structure
			self.structure(
				[
					'Neurongroups',
					'Postlets',
					'Traces',
					'Events',
					'Samples'
				],
				None,
				_DoStr="Brian"
			)

		#Check
		if self.BrianedParentSingularStr=="Neurongroup":
			
			#/########################/#
			# Neurongroup level
			#  

			#set the parent
			self.BrianedParentNetworkDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#setNeurongroup
			self.setNeurongroup()

		elif self.BrianedParentSingularStr=='Postlet':

			#/########################/#
			# Postlet level
			#  

			#debug
			'''
			self.debug(
				[
					'It is a Synapser level, we set the Synapser',
					('self.',self,[
								'BrianingSynapsesDict'
								]
					),
					'self.PointToVariable.BrianedNeurongroupVariable is ',
					str(self.PointToVariable.BrianedNeurongroupVariable)
				]
			)
			'''

			#/####################/#
			# Set the parent
			#

			#get
			self.BrianedParentNeurongroupDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#get
			self.BrianedParentNetworkDeriveBrianerVariable=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedParentNetworkDeriveBrianerVariable


			#/####################/#
			# Set the BrianedParentNeurongroupDeriveBrianerVariable
			#

			#debug
			self.debug(
				[
					'We set the synapses',
					'self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable is ',
					str(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable),
					'self.PointToVariable.BrianedNeurongroupVariable is ',
					str(self.PointToVariable.BrianedNeurongroupVariable),
					'Maybe we have to make brian the post'
				]
			)

			#Check 
			if self.PointToVariable.BrianedNeurongroupVariable==None:
				self.PointToVariable.brian()

			#import
			from brian2 import Synapses

			#init
			self.BrianedSynapsesVariable=Synapses(
				source=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable,
				target=self.PointToVariable.BrianedNeurongroupVariable,
				**self.BrianingSynapsesDict
			)

			#/####################/#
			# Connect options
			#

			#connect
			if type(self.BrianingConnectVariable)==float:

				#debug
				self.debug(
					[
						'we connect with a sparsity of ',
						('self.',self,[
							'BrianingConnectVariable'
						])
					]
				)

				#connect
				self.BrianedSynapsesVariable.connect(
					True,
					p=self.BrianingConnectVariable
				)

			#/####################/#
			# add to the structure
			#

			#add
			self.BrianedParentNetworkDeriveBrianerVariable.BrianedNetworkVariable.add(
				self.BrianedSynapsesVariable
			)

		elif self.BrianedParentSingularStr=='Trace':

			#debug
			'''
			self.debug(
				[
					'It is a Trace level, we set the Samples',
					('self.',self,[
								#'RecordingKeyVariable',
								'RecordKeyStr'
								])
				]
			)
			'''

			#/####################/#
			# we record
			#

			#record
			self.record()

			#/####################/#
			# Set the parent
			#

			#get
			self.BrianedParentNeurongroupDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#get
			self.BrianedParentNetworkDeriveBrianerVariable=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedParentNetworkDeriveBrianerVariable

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
			'''
			self.debug(
				[
					'Do we have to set a default moniter ?',
					'len(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedRecordKeyStrsList) is ',
					str(len(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedRecordKeyStrsList))
				]
			)
			'''

			#Check
			if len(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedRecordKeyStrsList)==1:

				#Check
				if len(BrianedDeriveSamples.ManagementDict)==0:

					BrianedDefaultMoniter=BrianedDeriveSamples.manage(
						'Default',

					).ManagedValueVariable
					BrianedDefaultMoniter.MoniteringLabelIndexIntsArray=[0] if self.BrianedParentNeurongroupDeriveBrianerVariable.BrianingNeurongroupDict[
					'N']>0 else []

		elif self.BrianedParentSingularStr=='Sample':

			#debug
			'''
			self.debug(
				[
					'It is a State Moniter level',
					('self.',self,[
								'MoniteringLabelIndexIntsArray',
								])
				]
			)
			'''

			#/####################/#
			# Set the parent
			#

			#get
			self.BrianedParentDeriveRecorderVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#get
			self.BrianedParentNeurongroupDeriveBrianerVariable=self.BrianedParentDeriveRecorderVariable.BrianedParentNeurongroupDeriveBrianerVariable

			#get
			self.BrianedParentNetworkDeriveBrianerVariable=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedParentNetworkDeriveBrianerVariable

			#/####################/#
			# Set the brian monitor
			#
		
			#debug
			'''
			self.debug(
				[
					'We set the state monitor',
					('self.',self,[
						#'BrianedParentNeurongroupDeriveBrianerVariable'
						]),
					#'self.BrianedParentDeriveRecorderVariable.RecordKeyStr is ',
					#str(self.BrianedParentDeriveRecorderVariable.RecordKeyStr)
					'self.ParentedTotalManagementOrderedDict.keys() is ',
					str(self.ParentedTotalManagementOrderedDict.keys())
				]
			)
			'''

			#import
			from brian2 import StateMonitor

			#init
			self.BrianedStateMonitorVariable=StateMonitor(
					self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable,
					self.BrianedParentDeriveRecorderVariable.RecordKeyStr,
					self.MoniteringLabelIndexIntsArray,
				)

			#debug
			'''
			self.debug(
				[
					'Ok we have setted the monitor',
					('self.',self,['BrianedStateMonitorVariable']),
					'Now we add to the structure',
					'self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNetworkVariable is ',
					str(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNetworkVariable)
				]
			)
			'''

			#/####################/#
			# add to the structure
			#

			#debug
			'''
			self.debug(
				[
					'We add to the structure'
				]
			)
			'''

			#add
			self.BrianedParentNetworkDeriveBrianerVariable.BrianedNetworkVariable.add(
				self.BrianedStateMonitorVariable
			)

			#/####################/#
			# maybe pyplot
			#

			#debug
			self.debug(
				[
					'We complete a view'
				]
			)

			#set
			self.PyplotingDrawVariable=[
				(
					'plot',
					{
						'#liarg:#map@get':[
							'#LocalBrianer.BrianedStateMonitorVariable.t',
							'#LocalBrianer.BrianedStateMonitorVariable.v.T'
						]
					}
				)
			]

			#debug
			self.debug(
				[
					('self.',self,['PyplotingDrawVariable'])
				]
			)

			#mapReplace
			self.PyplotingDrawVariable=SYS.replace(
				self.PyplotingDrawVariable,
				{
					'#LocalBrianer':">>SYS.IdDict["+str(self.PrintIdInt)+"]"
				},
				self
			)

			#debug
			self.debug(
				[
					('self.',self,['PyplotingDrawVariable'])
				]
			)


		elif self.BrianedParentSingularStr=='Event':

			#debug
			'''
			self.debug(
				[
					'It is a Spike Moniter level',
					('self.',self,[
								])
				]
			)
			'''

			#/####################/#
			# Set the BrianedParentNeurongroupDeriveBrianerVariable
			#

			#get
			self.BrianedParentNeurongroupDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#get
			self.BrianedParentNetworkDeriveBrianerVariable=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedParentNetworkDeriveBrianerVariable


			#/####################/#
			# Set the brian monitor
			#
		
			#debug
			'''
			self.debug(
				[
					'We set the spike monitor'
				]
			)
			'''

			#import
			from brian2 import SpikeMonitor

			#init
			self.BrianedSpikeMonitorVariable=SpikeMonitor(
					self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable,
				)

			#debug
			'''
			self.debug(
				[
					'Ok we have setted the monitor',
					('self.',self,['BrianedSpikeMonitorVariable']),
					'Now we add to the structure',
					'self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNetworkVariable is ',
					str(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNetworkVariable)
				]
			)
			'''

			#/####################/#
			# add to the structure
			#

			#add
			self.BrianedParentNetworkDeriveBrianerVariable.BrianedNetworkVariable.add(
				self.BrianedSpikeMonitorVariable
			)

	def propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable):

		#/##################/#
		# Maybe brian
		#

		#debug
		'''
		self.debug(
			[
				'We are going to parent but before',
				('self.',self,['StructuringDoStr']),
				'self.StructuringTopDeriveStructurerVariable!=self is ',
				str(self.StructuringTopDeriveStructurerVariable!=self),
				'self.ParentedTotalListDict.keys() is ',
				str(self.ParentedTotalListDict.keys()),
				'self.ParentedTotalSingularListDict.keys() is ',
				str(self.ParentedTotalSingularListDict.keys())
			]
		)
		''' 

		#Check
		if self.StructuringDoStr=='Brian' and self.StructuringTopDeriveStructurerVariable!=self:

			#record
			self.brian()

		#/##################/#
		# Call the base method
		#

		#debug
		'''
		self.debug(
			[
				'Now we call the base setParent method'
			]
		)
		'''

		#set
		BaseClass.propertize_setWatchAfterParentWithParenterBool(self,_SettingValueVariable)


	def setNeurongroup(self):

		#debug
		'''
		self.debug(
			[
				'It is a Neurongroup level, we set the Neurongroup',
				'We adapt the shape of BrianingNeurongroupDict',
				('self.',self,[
							'BrianingNeurongroupDict',
							'RecordingKeyVariable'
						])
			]
		)
		'''

		#/################/#
		# Adapt the arg
		#

		#Check
		if 'N' not in self.BrianingNeurongroupDict:
			self.BrianingNeurongroupDict['N']=self.SimulatingUnitsInt
		else:
			self.SimulatingUnitsInt=self.BrianingNeurongroupDict['N']

		#Check
		if 'model' not in self.BrianingNeurongroupDict:
			self.BrianingNeurongroupDict['model']=''

		#maybe should import
		from brian2 import NeuronGroup

		#debug
		'''
		self.debug(
			[
				('self.',self,[
							'BrianingNeurongroupDict'
							])
			]
		)
		'''

		#/################/#
		# Set the brian neurongroup
		#

		#init
		self.BrianedNeurongroupVariable=NeuronGroup(
			**dict(
				self.BrianingNeurongroupDict,
				**{
					'name':self.ParentedTotalPathStr.replace('/','_')+'_'+self.ManagementTagStr
				} 
			)
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
		# team States first all the brian variables
		#

		#get
		self.BrianedRecordKeyStrsList=self.BrianedNeurongroupVariable.equations._equations.keys()

		#Check
		if len(self.BrianedRecordKeyStrsList)>0:

			#debug
			'''
			self.debug(
					[
						'We simulate with neurongroup',
						'adapt the initial conditions of all the brian variables',
						'so first we team Traces and put Recorders inside or get it and mapSet'
					]
				)
			'''

			#Check
			if 'Traces' not in self.TeamDict:
				BrianedDeriveTraces=self.team(
					'Traces'
				).TeamedValueVariable
			else:
				BrianedDeriveTraces=self.TeamDict[
						'Traces'
					]

			#map
			self.BrianedTraceDeriveBrianersList=map(
					lambda __ManagementKeyStr,__RecordKeyStr:
					BrianedDeriveTraces.manage(
							__ManagementKeyStr,
							{
								'RecordingKeyVariable':getattr(
									self.BrianedNeurongroupVariable,
									__RecordKeyStr
								),
								'RecordKeyStr':__RecordKeyStr
							}
						).ManagedValueVariable
					if __ManagementKeyStr not in BrianedDeriveTraces.ManagementDict
					else BrianedDeriveTraces.ManagementDict[__ManagementKeyStr].mapSet(
						{
							'RecordingKeyVariable':getattr(
								self.BrianedNeurongroupVariable,
								__RecordKeyStr
							),
							'RecordKeyStr':__RecordKeyStr
						}
					),
					map(
						lambda __BrianedRecordKeyStr:
						Recorder.RecorderPrefixStr+__BrianedRecordKeyStr,
						self.BrianedRecordKeyStrsList
					),
					self.BrianedRecordKeyStrsList
				)

			#debug
			'''
			self.debug(
				[
					'Ok we know the structure ',
					('self.',self,['BrianedNetworkVariable'])
				]
			)
			'''

			#/##################/#
			# add in the net
			#

			#add
			self.BrianedParentNetworkDeriveBrianerVariable.BrianedNetworkVariable.add(
				self.BrianedNeurongroupVariable
			)

	def mimic_simulate(self):

		#parent method
		BaseClass.simulate(self)

		#debug
		'''
		self.debug('We start simulate in brian')
		'''

		#Check
		if self.BrianingTimeDimensionVariable==None:

			from brian2 import ms 
			self.BrianingTimeDimensionVariable=ms

		#run with the brian method
		self.BrianedNetworkVariable.run(
			self.SimulatingStopTimeFloat*self.BrianingTimeDimensionVariable
		)

		#debug
		'''
		self.debug('We stop running in brian')
		'''

	def mimic_record(self):

		#base method
		BaseClass.record(self)

		#debug
		'''
		self.debug(
			[
				'We have traced, alias the init in the brian object',
				('self.',self,[
					'RecordedTraceFloatsArray',
					'RecordedInitFloatsArray'
				])
			]
		)
		'''

		#alias
		self.RecordedTraceFloatsArray[:]=self.RecordedInitFloatsArray*self.RecordedTraceFloatsArray.unit

		#debug
		'''
		self.debug(
			[
				('self.',self,['RecordedTraceFloatsArray'])
			]
		)
		'''

	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Remove the brian objects that are non setted
			#

			#map
			map(
					lambda __KeyStr:
					self.PrintingCopyVariable.PrintingInstanceSkipKeyStrsList.append(
						__KeyStr
					) if getattr(self.PrintingCopyVariable,__KeyStr)==None
					else None,
					[
						'BrianedNetworkVariable',
						'BrianedNeurongroupVariable',
						'BrianedSynapsesVariable',
						'BrianedStateMonitorVariable',
						'BrianedSpikeMonitorVariable',
					]
				)


		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>

#</DefinePrint>
BrianerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'BrianingNeurongroupDict',
		'BrianingSynapsesDict',
		'BrianingConnectVariable',
		'BrianingTraceDict',
		'BrianingMoniterTuple',
		'BrianingSpikesDict',
		'BrianingTimeDimensionVariable',
		#'BrianedNetworkVariable',
		#'BrianedNeurongroupVariable',
		#'BrianedSynapsesVariable',
		#'BrianedStateMonitorVariable',
		#'BrianedSpikeMonitorVariable',
		'BrianedRecordKeyStrsList',
		'BrianedTraceDeriveBrianersList',
		'BrianedSynapsesDeriveBrianersList',
		'BrianedStateDeriveBrianersList',
		'BrianedSpikeDeriveBrianersList',
		'BrianedParentSingularStr',
		'BrianedParentNetworkDeriveBrianerVariable',
		'BrianedParentNeurongroupDeriveBrianerVariable',
		'BrianedParentDeriveRecorderVariable'
	]
)
#<DefinePrint>
