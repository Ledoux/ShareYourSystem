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
BrianConnectPrefixStr='Synaps'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['brian'],
	'ClassingStructureVariable':[
			('Population','Populations'),
			('Trace','Traces'),
			('Sample','Samples'),
			('Event','Events'),
			('Interactome','Interactomes'),
			('Interaction','Interactions')
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
			_BrianingPyplotDict=None,
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
			_BrianedParentInteractomeDeriveBrianerVariable=None,
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
		if (self.ParentDeriveTeamerVariable==None or 'Populations' in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces',
			'Samples',
			'Events',
			'Interactomes',
			'Interactions'
		]) and self.BrianedParentSingularStr!='Population':

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
			
			#set
			self.setNetwork()

			#/########################/#
			# Special Network-Neurongroup level
			# 

			#Check
			if 'Populations' not in self.TeamDict:
		
				#debug
				self.debug(
					[
						'It is a network with a one level pop',
						'So set the neurongroup'
					]
				)

				#set
				self.BrianedParentNetworkDeriveBrianerVariable=self

				#setNeurongroup
				self.setNeurongroup()

				#debug
				self.debug(
					[
						'We end to set the neuron group here'
					]
				)

			#/########################/#
			# network
			# 

			#debug
			self.debug(
				[
					'We structure in all the brian children...',
				]
			)

			#structure
			self.structure(
				[
					'Populations',
					'Traces',
					'Events',
					'Samples',
					'Interactomes',
					'Interactions'
				],
				None,
				_DoStr="Brian"
			)

			#debug
			self.debug(
				[
					'Ok we have structured all the brian children...',
				]
			)

		#Check
		if self.BrianedParentSingularStr=='Population':
			
			#/########################/#
			# Neurongroup level
			#  

			#debug
			self.debug(
				[
					'It is a Neurongroup level',
					'We set the brian neurongroup'
				]
			)

			#set the parent
			self.BrianedParentNetworkDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#setNeurongroup
			self.setNeurongroup()

			#debug
			self.debug(
				[
					'Ok we have setted setNeurongroup'
				]
			)

		elif self.BrianedParentSingularStr=='Interactome':

			#/########################/#
			# call the  method
			#  

			#debug
			self.debug(
				[
					'It is a Interactome level'
				]
			)

			return

		elif self.BrianedParentSingularStr=='Interaction':
		
			#/########################/#
			# call the setSynapses method
			#  
		
			#debug
			self.debug(
				[
					'It is a Interaction level',
					'We set the synapses'
				]
			)

			#set Synapses
			self.setSynapses()
		
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
					'self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable is ',
					str(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable)
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
			# maybe pyplot a draw plot
			#

			#debug
			'''
			self.debug(
				[
					'We complete a view so first fill the draw'
				]
			)
			'''

			#set
			LabelStr='$'+self.BrianedParentDeriveRecorderVariable.RecordKeyStr+'_{'+str(
									self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable.name
								).replace('_','/')+'}'


			#set
			self.PyplotingDrawVariable=map(
				lambda __IndexInt:
				(
					'plot',
					{
						'#liarg:#map@get':[
							'#IdGetStr.BrianedStateMonitorVariable.t',
							'>>SYS.IdDict[#IdStr].BrianedStateMonitorVariable.'+self.BrianedParentDeriveRecorderVariable.RecordKeyStr+'['+str(
								__IndexInt)+',:]'
						],
						'#kwarg':dict(
							{
								'label':LabelStr+'^{'+str(__IndexInt)+'}$',
								'linestyle':'-',
								'color':'b'
							},
							**self.BrianingPyplotDict
						)
					}
				),
				self.MoniteringLabelIndexIntsArray
			)


			#/####################/#
			# maybe set for the Chart
			#

			#init
			self.PyplotingChartVariable=[]

			#/####################/#
			# maybe set the X Chart also
			#

			#Check
			if self.BrianedParentNeurongroupDeriveBrianerVariable.BrianingTimeDimensionVariable==None:
				from brian2 import ms
				self.BrianedParentNeurongroupDeriveBrianerVariable.BrianingTimeDimensionVariable=ms

			#set
			XLabelStr='$t\ ('+str(
				self.BrianedParentNeurongroupDeriveBrianerVariable.BrianingTimeDimensionVariable
			)+')$'

			#set
			SampleTagStr=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable.name+'t'

			#join
			XlimLiargStr="".join([
							">>SYS.set(SYS,'"+SampleTagStr+"LimFloatsArray',",
							"[SYS.IdDict[#IdStr].BrianedStateMonitorVariable.t[:].min(),",
							"SYS.IdDict[#IdStr].BrianedStateMonitorVariable.t[:].max()]",
							').'+SampleTagStr+"LimFloatsArray"
							])

			#join
			XticksLiargStr="".join([
							">>SYS.set(SYS,'"+SampleTagStr+"TickFloatsArray',",
							"map(lambda __Float:float('%.2f'%__Float),",
							"SYS.getTickFloatsArray(",
							'SYS.'+SampleTagStr+"LimFloatsArray,3",
							")))."+SampleTagStr+"TickFloatsArray"
							])

			XtickLabelLiargStr="".join([
							">>SYS.set(SYS,'"+SampleTagStr+"TickStrsArray',",
							"map(lambda __Float:'$'+str(__Float)+'$',",
							"SYS."+SampleTagStr+"TickFloatsArray))."+SampleTagStr+"TickStrsArray"
							])
					
			#debug
			'''
			self.debug(
				[
					'XLabelStr is ',
					XLabelStr,
					'XlimLiargStr is',
					XlimLiargStr,
					'XticksLiargStr is ',
					XticksLiargStr,
					'XtickLabelLiargStr is ',
					XtickLabelLiargStr
				]
			)
			'''

			#set
			self.PyplotingChartVariable+=[
				(
					'set_xlabel',XLabelStr
				),
				(
					'set_xlim',{
						'#liarg:#map@get':[XlimLiargStr]
					}
				),
				(
					'set_xticks',{
						'#liarg:#map@get':[XticksLiargStr]
					}
				),
				(
					'set_xticklabels',{
						'#liarg:#map@get':[XtickLabelLiargStr]
					}
				)
			]

			#/####################/#
			# maybe set the Y Chart also
			#

			#set
			YLabelStr='$'+self.BrianedParentDeriveRecorderVariable.RecordKeyStr+'_{'+str(
				self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable.name
					).replace('_','/')+'}(t)\ ('+str(
						self.BrianedParentDeriveRecorderVariable.RecordedTraceFloatsArray.unit
					)+')$'

			#set
			SampleTagStr=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable.name+self.BrianedParentDeriveRecorderVariable.RecordKeyStr

			#join
			YlimLiargStr="".join([
							">>SYS.set(SYS,'"+SampleTagStr+"LimFloatsArray',",
							"[SYS.IdDict[#IdStr].BrianedStateMonitorVariable."+self.BrianedParentDeriveRecorderVariable.RecordKeyStr+".min(),",
							"SYS.IdDict[#IdStr].BrianedStateMonitorVariable."+self.BrianedParentDeriveRecorderVariable.RecordKeyStr+".max()]",
							').'+SampleTagStr+"LimFloatsArray"
							])

			#join
			YticksLiargStr="".join([
							">>SYS.set(SYS,'"+SampleTagStr+"TickFloatsArray',",
							"map(lambda __Float:float('%.2f'%__Float),",
							"SYS.getTickFloatsArray(",
							'SYS.'+SampleTagStr+"LimFloatsArray,3",
							")))."+SampleTagStr+"TickFloatsArray"
							])

			YtickLabelLiargStr="".join([
							">>SYS.set(SYS,'"+SampleTagStr+"TickStrsArray',",
							"map(lambda __Float:'$'+str(__Float)+'$',",
							"SYS."+SampleTagStr+"TickFloatsArray))."+SampleTagStr+"TickStrsArray"
							])
					
			#debug
			'''
			self.debug(
				[
					'YLabelStr is ',
					YLabelStr,
					'YlimLiargStr is',
					YlimLiargStr,
					'YticksLiargStr is ',
					YticksLiargStr,
					'YtickLabelLiargStr is ',
					YtickLabelLiargStr
				]
			)
			'''

			#set
			self.PyplotingChartVariable+=[
				(
					'set_ylabel',YLabelStr
				),
				(
					'set_ylim',{
						'#liarg:#map@get':[YlimLiargStr]
					}
				),
				(
					'set_yticks',{
						'#liarg:#map@get':[YticksLiargStr]
					}
				),
				(
					'set_yticklabels',{
						'#liarg:#map@get':[YtickLabelLiargStr]
					}
				)
			]

			#/####################/#
			# maybe set global Chart also
			#

			self.PyplotingChartVariable+=[
				(
					'tick_params',{
						'#kwarg':{
							'length':10,
							'width':5,
							'which':'major'
						}
					}
				),
				(
					'tick_params',{
						'#kwarg':{
							'length':5,
							'width':2,
							'which':'minor'
						}
					}
				),
				('xaxis.set_ticks_position',
					{
						'#liarg':['bottom']
					}
				),
				('yaxis.set_ticks_position',
					{
						'#liarg':['left']
					}
				),
				('legend',{
					'#liarg':[],
					'#kwarg':{
						'fontsize':10,
						'shadow':True,
						'fancybox':True,
						'ncol':max(1,len(
							getattr(
								self.BrianedStateMonitorVariable,
								self.BrianedParentDeriveRecorderVariable.RecordKeyStr
							)
						)/2),
						'loc':2,
						'bbox_to_anchor':(1.05, 1)
					}
				})
			]

			#/####################/#
			# maybe replace Chart also
			#

			#debug
			'''
			self.debug(
				[
					'Before replace',
					('self.',self,[
						'PyplotingDrawVariable',
						'PyplotingChartVariable'
					])
				]
			)
			'''

			#mapReplace
			[
				self.PyplotingDrawVariable,
				self.PyplotingChartVariable
			]=map(
				lambda __Variable:
				SYS.replace(
					__Variable,
					{
						'#IdStr':str(self.PrintIdInt),
						'#IdGetStr':"#id:"+str(self.PrintIdInt)
					},
					self
				)
				if __Variable!=None
				else None,
				map(
					lambda __KeyStr:
					getattr(
						self,
						__KeyStr
					),
					[
						'PyplotingDrawVariable',
						'PyplotingChartVariable'
					]
				)
			)

			#debug
			'''
			self.debug(
				[
					'After replace',
					('self.',self,[
						#'PyplotingDrawVariable',
						'PyplotingChartVariable'
					])
				]
			)
			'''

			#/####################/#
			# Update maybe the 
			# parent neuron group

			BrianedChartNeurongroupDerivePyploter=self.BrianedParentNeurongroupDeriveBrianerVariable.TeamDict[
				'Charts'
			].ManagementDict[
				self.BrianedParentDeriveRecorderVariable.ManagementTagStr
			]

			#debug
			'''
			self.debug(
				[
					'We update in the parent neurongroup chart',
					'BrianedChartNeurongroupDerivePyploter is ',
					SYS._str(BrianedChartNeurongroupDerivePyploter),
					('self.',self,[])
				]
			)
			'''

			#manage
			BrianedChartNeurongroupDerivePyploter.TeamDict['Draws'].manage(
				str(self.ManagementIndexInt),
				{
					'PyplotingDrawVariable':self.PyplotingDrawVariable
				}
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

			#/####################/#
			# maybe pyplot a draw plot
			#

			#debug
			'''
			self.debug(
				[
					'We complete a view so first fill the draw'
				]
			)
			'''

			#set
			LabelStr='$'+self.ManagementTagStr+'_{'+str(
				self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable.name
								).replace('_','/')+'}'

			#set
			self.PyplotingDrawVariable=[
				(
					'plot',
					{
						'#liarg:#map@get':[
							'#IdGetStr.BrianedSpikeMonitorVariable.t',
							'>>SYS.IdDict[#IdStr].BrianedSpikeMonitorVariable.i'
						],
						'#kwarg':dict(
							{
								'label':LabelStr,
								'linestyle':'',
								'marker':'.',
								'color':'b'
							},
							**self.BrianingPyplotDict
						)
					}
				)
			]

			#/####################/#
			# maybe replace Chart also
			#

			#debug
			'''
			self.debug(
				[
					'Before replace',
					('self.',self,[
						'PyplotingDrawVariable',
						'PyplotingChartVariable'
					])
				]
			)
			'''

			#mapReplace
			[
				self.PyplotingDrawVariable,
				self.PyplotingChartVariable
			]=map(
				lambda __Variable:
				SYS.replace(
					__Variable,
					{
						'#IdStr':str(self.PrintIdInt),
						'#IdGetStr':"#id:"+str(self.PrintIdInt)
					},
					self
				)
				if __Variable!=None
				else None,
				map(
					lambda __KeyStr:
					getattr(
						self,
						__KeyStr
					),
					[
						'PyplotingDrawVariable',
						'PyplotingChartVariable'
					]
				)
			)

			#debug
			'''
			self.debug(
				[
					'After replace',
					('self.',self,[
						#'PyplotingDrawVariable',
						'PyplotingChartVariable'
					])
				]
			)
			'''

			#/####################/#
			# Update maybe the 
			# parent neuron group

			BrianedChartNeurongroupDerivePyploter=self.BrianedParentNeurongroupDeriveBrianerVariable.TeamDict[
				'Charts'
			].ManagementDict[
				self.ManagementTagStr
			]

			#debug
			'''
			self.debug(
				[
					'We update in the parent neurongroup chart',
					'BrianedChartNeurongroupDerivePyploter is ',
					SYS._str(BrianedChartNeurongroupDerivePyploter),
					('self.',self,[])
				]
			)
			'''

			#manage
			BrianedChartNeurongroupDerivePyploter.TeamDict['Draws'].manage(
				str(self.ManagementIndexInt),
				{
					'PyplotingDrawVariable':self.PyplotingDrawVariable
				}
			)

		#debug
		'''
		self.debug(
			[
				'end of brian here'
			]
		)
		'''

	def mimic_structure(self):

		#/##################/#
		# Maybe brian
		#

		#debug
		'''
		self.debug(
			[
				'We are going to parent but before',
				('self.',self,['StructuringDoStr']),
				'self.StructureTopDeriveStructurerVariable!=self is ',
				str(self.StructureTopDeriveStructurerVariable!=self),
				'self.ParentedTotalListDict.keys() is ',
				str(self.ParentedTotalListDict.keys()),
				'self.ParentedTotalSingularListDict.keys() is ',
				str(self.ParentedTotalSingularListDict.keys())
			]
		)
		''' 

		#Check
		if self.StructuringDoStr=='Brian' and self.StructureTopDeriveStructurerVariable!=self:

			#record
			self.brian()
			
		else:

			#/##################/#
			# Call the base method
			#

			#debug
			'''
			self.debug(
				[
					'Now we call the base method'
				]
			)
			'''

			#set
			BaseClass.structure(self)

	def setNetwork(self):

		#maybe should import
		from brian2 import Network

		#set
		self.BrianedNetworkVariable=Network()

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
			self.BrianingNeurongroupDict['N']=0

		#Check
		if 'model' not in self.BrianingNeurongroupDict:
			self.BrianingNeurongroupDict['model']=''

		#maybe should import
		from brian2 import NeuronGroup

		#debug
		self.debug(
			[
				('self.',self,[
							'BrianingNeurongroupDict'
							]),
				'We now set the model system Neurongroup if N>0 and model!=""'
			]
		)

		#/################/#
		# Set the brian neurongroup
		#

		#Check
		if self.BrianingNeurongroupDict['N']>0 and self.BrianingNeurongroupDict['model']!="":

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
			self.debug(
				[
					'Ok we have setted the Neurongroup',
					('self.',self,[
								'BrianedNeurongroupVariable'
								])
				]
			)

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

				#debug
				self.debug(
					[
						'We set the tracers',
						('self.',self,['BrianedRecordKeyStrsList'])
					]
				)

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


				#/####################/#
				# maybe pyplot a draw plot
				#

				#debug
				'''
				self.debug(
					[
						'We complete a view so first fill the draw'
					]
				)
				'''

				#Check
				if 'Charts' not in self.TeamDict:
					BrianedChartsDeriveTeamer=self.team(
						'Charts'
					).TeamedValueVariable
				else:
					BrianedChartsDeriveTeamer=self.TeamDict['Charts']

				#Check
				if 'Traces' in self.TeamDict:

					#debug
					'''
					self.debug(
						[
							'First we add the traces'
						]
					)
					'''

					#set
					map(
						lambda __KeyStr:
						BrianedChartsDeriveTeamer.manage(
							__KeyStr,
							{
								'-Draws':
								{

								}
							}
						),
						self.TeamDict['Traces'].ManagementDict.keys()
					)

					#debug
					'''
					self.debug(
						[
							'self.TeamDict["Traces"] is ',
							str(self.TeamDict["Traces"])
						]
					)
					'''

				#Check
				if 'Events' in self.TeamDict:

					#debug
					'''
					self.debug(
						[
							'Then we add the events'
						]
					)
					'''

					#set
					BrianedChartsDeriveTeamer.mapSet(
						map(
							lambda __KeyStr:
							(
								'|'+__KeyStr,
								{
									'-Draws':
									{

									}
								}
							),
							self.TeamDict['Events'].ManagementDict.keys()
						)
					)

					#debug
					'''
					self.debug(
						[
							'self.TeamDict["Events"] is ',
							str(self.TeamDict["Events"])
						]
					)
					'''

		#debug
		'''
		self.debug(
			[
				'End of setNeurongroup'
			]
		)
		'''

	def setSynapses(self):

		#/########################/#
		# Postlet level
		#  

		#debug
		self.debug(
			[
				'It is a Synapser level, we set the Synapser',
				('self.',self,[
							#'BrianingSynapsesDict'
							]
				)
			]
		)

		#/####################/#
		# Set the parent
		#

		#Check
		if self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable.BrianedParentSingularStr=='Interactome':

			#debug
			'''
			self.debug(
				[
					'We are in a projectome structure'
				]
			)
			'''

			#set
			self.BrianedParentInteractomeDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#get
			self.BrianedParentNeurongroupDeriveBrianerVariable=self.BrianedParentInteractomeDeriveBrianerVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		else:

			#debug
			'''
			self.debug(
				[
					'There is no projectome structure'
				]
			)
			'''

			#get
			self.BrianedParentNeurongroupDeriveBrianerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		#get
		self.BrianedParentNetworkDeriveBrianerVariable=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedParentNetworkDeriveBrianerVariable


		#/####################/#
		# Set the ConnectedTo Variable
		#

		#debug
		self.debug(
			[
				'Check if we have to get the connected to variable',
				('self.',self,['ConnectedToVariable'])
			]
		)

		#Check
		if self.ConnectedToVariable==None:

			#debug
			self.debug(
				[
					'We setConnection here'
				]
			)

			#setConnection
			self.setConnection(
				self.ManagementTagStr,
				self,
				self.BrianedParentNeurongroupDeriveBrianerVariable
			)

		#/####################/#
		# Set the BrianedParentNeurongroupDeriveBrianerVariable
		#

		#Check 
		if self.ConnectedToVariable.BrianedNeurongroupVariable==None:
			self.ConnectedToVariable.brian()

		#set
		BrianedNameStr=self.BrianedParentNeurongroupDeriveBrianerVariable.ParentTagStr+'_To_'+self.ConnectedToVariable.ParentTagStr

		#debug
		self.debug(
			[
				'We set the synapses',
				'self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable is ',
				str(self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable),
				'self.ConnectedToVariable.BrianedNeurongroupVariable is ',
				str(self.ConnectedToVariable.BrianedNeurongroupVariable),
				'Maybe we have to make brian the post',
				'BrianedNameStr is '+BrianedNameStr
			]
		)

		#import
		from brian2 import Synapses

		#init
		self.BrianedSynapsesVariable=Synapses(
			source=self.BrianedParentNeurongroupDeriveBrianerVariable.BrianedNeurongroupVariable,
			target=self.ConnectedToVariable.BrianedNeurongroupVariable,
			name=BrianedNameStr.replace('/','_'),
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
					else (
						self.PrintingCopyVariable.PrintingInstanceForceKeyStrsList.append(
							__KeyStr
						)
						if self.__class__.__name__=='BrianerClass'
						else self.PrintingCopyVariable.PrintingInstanceForceBaseKeyStrsList.append(
							__KeyStr
						)
					),
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
		'BrianingPyplotDict',
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
		'BrianedParentInteractomeDeriveBrianerVariable',
		'BrianedParentDeriveRecorderVariable'
	]
)
#<DefinePrint>
