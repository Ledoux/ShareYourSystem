# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Leaker

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Recorders.Brianer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Leaker','Leak','Leaking','Leaked')
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Interfacers import Printer
from ShareYourSystem.Standards.Recorders import Recorder
#</ImportSpecificModules>

#<DefineLocals>
LeakScalarPrefixStr='#scalar:'
LeakEquationPrefixStr='#equation:'
LeakCustomPrefixStr='#custom:'
LeakClockPrefixStr='#clock:'
LeakNetworkPrefixStr='#network:'
LeakActivityPrefixStr="U"
LeakInputPrefixStr="I"
LeakInteractionPrefixStr="J"

#define
def detectThreshold(_VariablesList,_PopulationDeriveLeaker):

	#set
	SpikeArray = _VariablesList['_spikespace']
	ActivityArray = _VariablesList[
				_PopulationDeriveLeaker.LeakedSymbolStr
			]
	
	#Choose
	AboveArray=(ActivityArray > _PopulationDeriveLeaker.LeakingThresholdVariable).nonzero()[0]

	#Debug
	print('l 52 detectThreshold')
	print('SpikeArray is ')
	print(SpikeArray)
	print('AboveArray is')
	print(AboveArray)
	print('')

"""
def filterSpike(_VariablesList,_ActivityStr,_ThresholdVariable):

	#set
	SpikeArray = _VariablesList['_spikespace']
	ActivityArray = _VariablesList[
				_ActivityStr
			]
	
	#Choose
	AboveArray=(ActivityArray > _ThresholdVariable).nonzero()[0]

	#Check
	if len(AboveArray):
		# only let one neuron spike
		SpikeArray[0] = AboveArray[0]
		SpikeArray[-1] = 1
	else:
		SpikeArray[-1] = 0
"""


#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['leak'],
	'ClassingStructureVariable':[
			('Population','Populations'),
			('Trace','Traces'),
			('Sample','Samples'),
			('Event','Events'),
			('Interactome','Interactomes'),
			('Interaction','Interactions'),
			('Input','Inputs')
		]
})
class LeakerClass(BaseClass):
		
	def default_init(self,
			_LeakingUnitsInt=0,
			_LeakingTimeVariable='#scalar:10.*ms',
			_LeakingWeigthVariable=None,
			_LeakingQuantityStr='mV',
			_LeakingMonitorIndexIntsList=None,
			_LeakingSymbolPrefixStr="",
			_LeakingInteractionStr='Rate',
			_LeakingTransferVariable=None,
			_LeakingThresholdVariable=None,
			_LeakingResetVariable=None,
			_LeakedRecordSkipStrsList=None,
			_LeakedQuantityVariable=None,
			_LeakedDimensionStr="",
			_LeakedModelStr="",
			_LeakedCurrentStr="",
			_LeakedClampStr="",
			_LeakedSymbolStr="",
			_LeakedOperationStr="",
			_LeakedEquationStr="",
			_LeakedClockStr="",
			_LeakedTimeSymbolStr="",
			_LeakedInteractionWeigthFloat=0.,
			_LeakedParentSingularStr="",
			_LeakedParentNetworkDeriveLeakerVariable=None,
			_LeakedParentPopulationDeriveLeakerVariable=None,
			_LeakedParentInteractomeDeriveLeakerVariable=None,
			_LeakedTimedArrayVariable=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_leak(self):

		#/#################/#
		# Determine if it is an inside structure or the top
		#

		#debug
		'''
		self.debug(
			[
				'We leak here',
				'First look for deeper teams in the structure',
			]
		)
		'''

		#Check
		if self.ParentedTotalSingularListDict!=None and len(
			self.ParentedTotalSingularListDict
		)>0:

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
			self.LeakedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['LeakedParentSingularStr'])
			]
		)
		'''

		#Check
		if (self.ParentDeriveTeamerVariable==None or 'Populations' in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces',
			'Samples',
			'Events',
			'Interactomes',
			'Interactions',
			'Inputs'
		]) and self.LeakedParentSingularStr!='Population':

			#/########################/#
			# Network level
			# 

			#debug
			'''
			self.debug(
				[
					'It is a Network level for the leak',
				]
			)
			'''

			#/########################/#
			# structure leak the interactions
			# 

			#debug
			'''
			self.debug(
				[
					'We structure filterLeak all the interacting children...'
					'So we pass thrugh the populations and leak the interactomes, interactions and inputs',
				]
			)	
			'''

			#/########################/#
			# leakNetwork
			#

			#leakNetwork
			self.leakNetwork()

			#set
			self.StructureFilterTeamTagStrsList=[
				'Populations'
			]

			#structure
			self.structure(
				[
					'Populations',
					'Inputs',
					'Interactomes',
					'Interactions',
				],
				'#all',
				_ManagerCommandSetList=[
					'filterLeak'
				]
			)

			#debug
			'''
			self.debug(
				[
					'Ok we have structured the interacting children',
					'Now we brian Network'
				]
			)
			'''

			#/########################/#
			# brianNetwork
			#

			#brian
			self.brianNetwork()

			#/########################/#
			# Special Network-Neurongroup level
			# 

			#Check
			if 'Populations' not in self.TeamDict:
		
				#debug
				'''
				self.debug(
					[
						'...But there is no population',
						'so set a leak model here '
					]
				)
				'''

				#leakPopulation
				self.leakPopulation()

				#debug
				'''
				self.debug(
					[
						'Ok we have leak setted the population',
						'Now we also brianPopulation'
					]
				)
				'''

				#brianPopulation
				self.brianPopulation()

				#debug
				'''
				self.debug(
					[
						'Ok we have brian setted the population'
					]
				)
				'''

			#/########################/#
			# structure leak
			# 

			#debug
			'''
			self.debug(
				[
					'We structure leak brian all the children...',
					'self.TeamDict.keys() is ',
					str(self.TeamDict.keys())
				]
			)
			'''

			#set
			self.StructureFilterTeamTagStrsList=None

			#structure
			self.structure(
				[
					'Populations',
					'Traces',
					'Samples',
					'Events',
					'Interactomes',
					'Interactions',
				],
				'#all',
				_ManagerCommandSetList=['leak','brian']
			)

			#debug
			'''
			self.debug(
				[
					'Ok we have structured leak brian all the children',
				]
			)
			'''

		else:

			#/########################/#
			# Inside structure
			#

			#debug
			'''
			self.debug(
				[
					'Ok we check if this parentsingular has a special method ',
					('self.',self,[
						'LeakedParentSingularStr'
					])
				]
			)
			'''

			#set
			LeakedMethodKeyStr='leak'+self.LeakedParentSingularStr

			#Check
			if hasattr(self,LeakedMethodKeyStr):

				#/########################/#
				# call the special leak<LeakedParentSingularStr> method
				#

				#debug
				'''
				self.debug(
					[
						'It is a '+self.LeakedParentSingularStr+' level',
						'We leak<LeakedParentSingularStr>'
					]
				)
				'''

				#call
				getattr(
					self,
					LeakedMethodKeyStr
				)()

				#debug
				'''
				self.debug(
					[
						'Ok we have setted leak'+self.LeakedParentSingularStr
					]
				)
				'''	
		
	def leakNetwork(self):

		#/################/#
		# nothing here it is just a derive possible hook for derived classes
		#

		#debug
		'''
		self.debug(
			[
				'I a m just a possible hook for later derived classes'
			]
		)
		'''

		#pass
		pass

	def leakPopulation(self):

		#/################/#
		# Check the SymbolStr DimensionStr
		#

		#Check
		if self.LeakingSymbolPrefixStr=="":
			self.LeakingSymbolPrefixStr=LeakActivityPrefixStr

		#set direct
		self.LeakedSymbolStr=self.LeakingSymbolPrefixStr

		#Check
		if self.LeakedQuantityVariable==None:
			self.setDimension()

		#debug
		'''
		self.debug(
			[
				'We leak population here',
				('self.',self,[
					'LeakingQuantityStr',
					'LeakedQuantityVariable',
					'LeakedDimensionStr'
				])
			]
		)
		'''

		#/################/#
		# Look for the time constant
		#

		#debug
		'''
		self.debug(
			[
				'We set a population here',
				'look for the time constant'
			]
		)
		'''

		#Check
		if type(
			self.LeakingTimeVariable
		)==str:

			#Check
			if self.LeakingTimeVariable.startswith(LeakScalarPrefixStr):

				#set
				self.LeakedClampStr='Scalar'

				#debug
				'''
				self.debug(
					[
						'We direct write the time constant as a scalar in the equation'
					]
				)
				'''

				#set
				self.LeakedTimeSymbolStr=SYS.deprefix(
					self.LeakingTimeVariable,
					LeakScalarPrefixStr
				)

		else:

			#set
			self.LeakedClampStr='Variable'

			#debug
			'''
			self.debug(
				[
					'The time constant is seen as a variable with a specific name'
				]
			)
			'''

			#set
			self.LeakedTimeSymbolStr="tau_"+self.LeakingSymbolPrefixStr

			#append
			self.LeakedRecordSkipStrsList.append(self.LeakedTimeSymbolStr)

			#define the time constant variable
			self.LeakedModelStr+=self.LeakedTimeSymbolStr+' : second\n'

		#/################/#
		# Define the main leak equation
		#

		#debug
		'''
		self.debug(
			[
				'We define the main leak equation but maybe it is just a direct value',
				('self.',self,[
					'LeakingTimeVariable'
				])
			]
		)
		'''

		#Check
		LeakedDirectVariableBool=False
		if self.LeakedClampStr=='Scalar':
			if float(self.LeakedTimeSymbolStr.split('*')[0])==0.:
				LeakedDirectVariableBool=True

		#Check
		if self.LeakingTimeVariable==0 or LeakedDirectVariableBool:

			#debug
			'''
			self.debug(
				[
					'Time constant is null',
					'Build just a variable definition',
					('self.',self,['LeakingTimeVariable'])
				]
			)
			'''

			#set the left 
			self.LeakedModelStr+=self.LeakingSymbolPrefixStr+' : '+self.LeakedDimensionStr+"\n"

		else:

			#debug
			'''
			self.debug(
				[
					'Build a differential equation',
					('self.',self,[
							'LeakedModelStr'
						])
				]	
			)
			'''

			#set the left 
			self.LeakedModelStr+="d"+self.LeakedSymbolStr+'/dt='

			#debug
			'''
			self.debug(
				[
					'Check if we add a weigth',
					('self.',self,[
							'LeakingWeigthVariable'
						])
				]
			)
			'''

			#Check
			if type(self.LeakingWeigthVariable)==str:

				#Check
				if self.LeakingWeigthVariable=='0':

					#set the right
					self.LeakedModelStr+='('

				else:

					#set the right
					self.LeakedModelStr+='(-'+self.LeakingWeigthVariable+self.LeakedSymbolStr

			else:

				#set the right
				self.LeakedModelStr+='(-'+self.LeakedSymbolStr

			#debug
			'''
			self.debug(
				[
					'We maybe add a current',
					('self.',self,[
							'LeakedCurrentStr'
						])
				]
			)
			'''

			#Check
			if self.LeakedCurrentStr!="":

				#debug
				'''
				self.debug(
					[
						'We maybe transfer',
						('self.',self,[
								'LeakingTransferVariable',
								'LeakedModelStr'
							])
					]
				)
				'''

				#Check
				if self.LeakedModelStr[-1]!='(':
					self.LeakedModelStr+='+'

				#Check
				if self.LeakingTransferVariable!=None:

					#Check
					if type(
						self.LeakingTransferVariable
					)==str:

						#debug
						'''
						self.debug(
							[
								'It is a str transfer',
								'We put it in the model and replace the #CurrentStr by self.LeakedCurrentStr',
								('self.',self,[
									'LeakedCurrentStr'
								])
							]
						)
						'''

						#add
						self.LeakedModelStr+=self.LeakingTransferVariable.replace(
								'#CurrentStr',
								self.LeakedCurrentStr
							)

					else:

						#debug
						'''
						self.debug(
							[
								'It is a function transfer'
							]
						)
						'''

						#add
						self.LeakedModelStr+='F('+self.LeakedCurrentStr+')'

				else:

					#debug
					'''
					self.debug(
						[
							'We add directly the leaked current'
						]
					)
					'''

					#Check
					self.LeakedModelStr+=self.LeakedCurrentStr

			#debug
			'''
			self.debug(
				[
					'We divide by the time',
					('self.',self,[
						'LeakedClampStr'
					])
				]
			)
			'''

			#set
			self.LeakedModelStr+=')'

			#set the right denominator
			if self.LeakedClampStr=='Scalar':

				#add
				self.LeakedModelStr+='/('+self.LeakedTimeSymbolStr+')'

			elif self.LeakedClampStr=='Variable':

				#add
				self.LeakedModelStr+='/('+self.LeakedTimeSymbolStr+')'

			#set the dimension
			self.LeakedModelStr+=' : '+self.LeakedDimensionStr+"\n"

		'''
		self.debug(
			[
				'We have defined the leak model str',
				('self.',self,['LeakedModelStr'])
			]
		)
		'''

		#/################/#
		# Now update the Traces
		#

		#team traces
		LeakedTracesDeriveManager=self.team(
			'Traces'
			).TeamedValueVariable

		#manage
		LeakedRecordDeriveLeaker=LeakedTracesDeriveManager.manage(
				'*'+self.LeakedSymbolStr
			).ManagedValueVariable

		#set
		LeakedRecordDeriveLeaker.NumscipyingStdFloat=0.001
		LeakedSamplesDeriveLeaker=LeakedRecordDeriveLeaker.team(
				'Samples'
			).TeamedValueVariable
		LeakedDefaultDeriveLeaker=LeakedSamplesDeriveLeaker.manage(
				'Default'
			).ManagedValueVariable

		#/##################/#
		# Look for what to monitor
		#

		#Check
		if self.RecordingLabelVariable!=None:

			#alias
			LeakedDefaultDeriveLeaker.RecordingLabelVariable=self.RecordingLabelVariable
		else:

			#Check
			if len(self.LeakingMonitorIndexIntsList)==0:
				self.LeakingMonitorIndexIntsList=[0]

			#set
			LeakedDefaultDeriveLeaker.RecordingLabelVariable=self.LeakingMonitorIndexIntsList

		#/##################/#
		# Init the Neurongroup dict
		#

		#init
		BrianingNeurongroupDict={
				}

		#/##################/#
		# Look for a Threshold 
		#

		#debug
		self.debug(
			[
				'Look for a threshold',
				('self.',self,[
					'LeakingThresholdVariable'
				])
			]
		)

		#Check
		if self.LeakingThresholdVariable!=None:

			#type
			LeakedType=type(self.LeakingThresholdVariable)

			#Check
			if LeakedType==str:

				#Check
				if self.LeakingThresholdVariable.startswith(LeakScalarPrefixStr):

					#debug
					self.debug(
						[
							'It is a scalar threshod'
						]
					)

					#set
					BrianingNeurongroupDict['threshold']=SYS.deprefix(
						self.LeakingThresholdVariable,
						LeakScalarPrefixStr
					)

			else:

				#import 
				import numpy

				#Check
				if LeakedType in [list,numpy.ndarray]:

					#debug
					self.debug(
						[
							'It is a variable threshod',
							'add in the model'
						]
					)

					#Define
					self.LeakedModelStr+='Threshold : '+self.LeakedDimensionStr+"\n"

					#set
					BrianingNeurongroupDict['threshold']=self.LeakedSymbolStr+'>Threshold'
					
				else:
	
					#debug
					self.debug(
						[
							'It is a CodeObject threshod',
							'add in the model'
						]
					)

					#import
					from brian2 import CodeObject

					#define
					def ThresholdFunction(_VariablesList):

						#map
						map(
							lambda __Method:
							__Method(
								_VariablesList,
								self
							),
							self.LeakingThresholdVariable['MethodsList']
						)


					#Init
					ThresholdCodeObject = CodeObject()(
							ThresholdFunction,
					    	uses_variables=[
					    		'_spikespace',
					    		self.LeakedSymbolStr
					    	]
					    )
				
		#/##################/#
		# Look for a Reset
		#

		#debug
		self.debug(
			[
				'Look for a threshold',
				('self.',self,[
					'LeakingResetVariable'
				])
			]
		)

		#Check
		if self.LeakingResetVariable!=None:

			#Check
			if type(self.LeakingResetVariable)==str:

				#Check
				if self.LeakingResetVariable.startswith(LeakScalarPrefixStr):

					#debug
					self.debug(
						[
							'It is a scalar reset'
						]
					)

					#set
					BrianingNeurongroupDict['reset']=SYS.deprefix(
						self.LeakingResetVariable,
						LeakScalarPrefixStr
					)
					


		#/##################/#
		# Set
		#

		#set
		BrianingNeurongroupDict['N']=self.LeakingUnitsInt
		BrianingNeurongroupDict['model']=self.LeakedModelStr

		#Check
		if self.BrianingNeurongroupDict==None:
		
			#init
			self.BrianingNeurongroupDict=BrianingNeurongroupDict

		else:

			#update
			self.BrianingNeurongroupDict.update(
				BrianingNeurongroupDict
			)

		#debug
		self.debug(
			[
				'We have aliased the BrianingNeurongroupDict',
				('self.',self,[
						'BrianingNeurongroupDict'
					])
			]
		)

	def leakTrace(self):

		#/#################/#
		# Determine the parent
		#

		#set
		self.LeakedParentPopulationDeriveLeakerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

	def leakInput(self):

		#/################/#
		# Input level
		#

		#debug
		'''
		self.debug(
			[
				'It is an Input level',
			]
		)
		'''

		#Check
		if self.LeakingSymbolPrefixStr=="":
			self.LeakingSymbolPrefixStr=LeakInputPrefixStr

		#/################/#
		# Determine the parent
		#

		#set
		self.LeakedParentPopulationDeriveLeakerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		#Check
		if self.LeakedParentPopulationDeriveLeakerVariable.ParentDeriveTeamerVariable!=None:

			#get
			self.LeakedParentNetworkDeriveLeakerVariable=self.LeakedParentPopulationDeriveLeakerVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		else:

			#get
			self.LeakedParentNetworkDeriveLeakerVariable=self.LeakedParentPopulationDeriveLeakerVariable


		#/################/#
		# Add in the model
		#

		#set
		self.LeakedSymbolStr=self.LeakingSymbolPrefixStr+self.ParentTagStr.split(
			'Inputs'
		)[-1].replace(
			'/','_'
		)

		#debug
		'''
		self.debug(
			[
				'we add in the model of the parent population',
				('self.',self,['LeakedSymbolStr']),
				'self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr is ',
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr
			]
		)
		'''

		#Check
		if self.LeakingWeigthVariable!=None:

			#Check
			if type(self.LeakingWeigthVariable)==str:

				#Check
				if self.LeakingWeigthVariable.startswith(LeakScalarPrefixStr):

					#set
					self.LeakedClampStr='Scalar'

					#set
					self.LeakedSymbolStr=SYS.deprefix(
						self.LeakingWeigthVariable,
						LeakScalarPrefixStr
					)

					#debug
					self.debug(
						[
							'It is an external scalar so just add Current',
							"self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr is ",
							self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr
						]
					)

					#add in the current
					self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(
						self.LeakedSymbolStr
					)

				elif self.LeakingWeigthVariable.startswith(LeakEquationPrefixStr):

					#set
					self.LeakedClampStr='Equation'

					#set
					self.LeakedOperationStr=SYS.deprefix(
						self.LeakingWeigthVariable,
						LeakEquationPrefixStr
					)

					#setOperation
					self.setOperation()

				elif self.LeakingWeigthVariable.startswith(LeakCustomPrefixStr):

					#set
					self.LeakedClampStr='Custom'

					#set
					self.LeakedOperationStr=SYS.deprefix(
						self.LeakingWeigthVariable,
						LeakCustomPrefixStr
					)

					#setOperation
					self.setOperation()
		

				"""
				else:

					#debug
					'''
					self.debug(
						[
							'It is an external array so direct add plus a (t)'
						]
					)
					'''

					#Check
					if self.LeakedParentPopulationDeriveLeakerVariable.LeakedQuantityVariable==None:
						self.LeakedParentPopulationDeriveLeakerVariable.setDimension()

					#define in the model
					self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedSymbolStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr+"\n"
					
					#add in the current
					self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(
						#self.LeakedSymbolStr+'(t)'
						self.LeakedSymbolStr
					)
				"""

			#Check
			elif type(self.LeakingWeigthVariable) in [list,tuple]:

				#Check
				if self.LeakingWeigthVariable[0].startswith(LeakNetworkPrefixStr):

					#debug
					'''
					self.debug(
						[
							'It is a network operation',
							('self.',self,[
									'LeakingWeigthVariable'
								])
						]
					)
					'''

					#set
					self.LeakedClampStr='Network'

					#set
					self.LeakedOperationStr=SYS.deprefix(
						self.LeakingWeigthVariable[0],
						LeakNetworkPrefixStr
					)

					#setOperation
					self.setOperation()

			else:

				#set
				self.LeakedClampStr='Variable'

				#debug
				'''
				self.debug(
					[
						'It is a variable',
						('self.',self,[
								'LeakedSymbolStr'
							]),
						'We append in the parent pop record skip',
						'We define and add in the LeakedCurrentStr'
					]
				)
				'''

				#append
				if self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList==None:
					self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList=[self.LeakedSymbolStr]
				else:
					self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList.append(
						self.LeakedSymbolStr
					)

				#Check
				if self.LeakedParentPopulationDeriveLeakerVariable.LeakedQuantityVariable==None:
					self.LeakedParentPopulationDeriveLeakerVariable.setDimension()

				#define in the model
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedSymbolStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr+"\n"
				
				#add in the current
				self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(
					self.LeakedSymbolStr
				)

			#debug
			'''
			self.debug(
				[
					'In the end',
					"self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr is ",
					self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr,
					"self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr is ",
					self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr,
					('self.',self,[
							'LeakedSymbolStr'
						])
				]
			)
			'''

	def leakInteraction(self):

		#/################/#
		# Interaction level
		#

		#debug
		'''
		self.debug(
			[
				'It is an Interaction level',
			]
		)
		'''

		#/####################/#
		# Determine the parent
		#

		#Check
		if self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable.LeakedParentSingularStr=='Projectome':

			#debug
			'''
			self.debug(
				[
					'We are in a projectome structure'
				]
			)
			'''

			#set
			self.LeakedParentProjectomeDeriveLeakerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#get
			self.LeakedParentPopulationDeriveLeakerVariable=self.LeakedParentProjectomeDeriveLeakerVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

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
			self.LeakedParentPopulationDeriveLeakerVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		#Check
		if self.LeakedParentPopulationDeriveLeakerVariable.ParentDeriveTeamerVariable!=None:

			#get
			self.LeakedParentNetworkDeriveLeakerVariable=self.LeakedParentPopulationDeriveLeakerVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		else:

			#get
			self.LeakedParentNetworkDeriveLeakerVariable=self.LeakedParentPopulationDeriveLeakerVariable


		#/####################/#
		# Check the clamp of the interaction
		#

		#Check
		if type(self.LeakingWeigthVariable)!=None.__class__:

			#debug
			'''
			self.debug(
				[
					'We check the clamp of the interaction',
					('self.',self,[
						'LeakingWeigthVariable'
					])
				]
			)
			'''

			#Check
			if self.LeakingSymbolPrefixStr=="":
				self.LeakingSymbolPrefixStr=LeakInteractionPrefixStr

			#Check
			if self.LeakedParentPopulationDeriveLeakerVariable.LeakingSymbolPrefixStr=="":
				self.LeakedParentPopulationDeriveLeakerVariable.LeakingSymbolPrefixStr=LeakActivityPrefixStr
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedSymbolStr=LeakActivityPrefixStr

			#init
			self.LeakedClampStr='Variable'

			#Check
			if type(self.LeakingWeigthVariable)==str:

				#Check
				if self.LeakingWeigthVariable.startswith(LeakScalarPrefixStr):

					#debug
					'''
					self.debug(
						[
							'It is a scalar constant connection'
						]
					)
					'''

					#set
					self.LeakedClampStr='Scalar'

		
		#/####################/#
		# Write the LeakedSymbolStr
		#

		#debug
		'''
		self.debug(
			[
				'We set the leakedsymbolstr',
				('self.',self,[
					'LeakedClampStr'
				])
			]
		)
		'''

		#set
		self.LeakedSymbolStr=self.LeakingSymbolPrefixStr+self.ParentTagStr.split(
			'Interactions'
		)[-1].replace('/','_')+self.LeakedParentPopulationDeriveLeakerVariable.LeakedSymbolStr

		#Check
		if self.LeakedClampStr=='Variable':

			#debug
			'''
			self.debug(
				[
					'It is a variable',
					('self.',self,[
							'LeakedSymbolStr'
						]),
					'We append in the parent pop record skip',
				]
			)
			'''

			#append
			if self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList==None:
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList=[self.LeakedSymbolStr]
			else:
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList.append(
					self.LeakedSymbolStr
				)

			#Check
			if self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr=="":
				self.LeakedParentPopulationDeriveLeakerVariable.setDimension()

			#debug
			'''
			self.debug(
				[
					'in the end',
					('self.',self,[
						'LeakedSymbolStr'
					])
				]
			)
			'''

			#/####################/#
			# Build the interaction model
			#

			#debug
			'''
			self.debug(
				[
					'We set Interaction here',
					'Look for the type of interaction'
				]
			)
			'''

			#Check
			if self.LeakingInteractionStr=='Rate':

				
				#debug
				'''
				self.debug(
					[
						'It is a rate interaction',
						'self.LeakedParentPopulationDeriveLeakerVariable.LeakingSymbolStr is ',
						self.LeakedParentPopulationDeriveLeakerVariable.LeakingSymbolStr,
						'First we set the model in the synapse',
						('self.',self,['LeakedSymbolStr'])
					]
				)
				'''

				#set
				if self.LeakedClampStr=='Scalar':

					#debug
					'''
					self.debug(
						[
							'The interaction is a scalar, so just define the post pre relation'
						]
					)
					'''

					#do the operation
					self.LeakedModelStr+=self.LeakedSymbolStr+"_post="

					#deprefix
					LeakedInteractionWeigthStr=SYS.deprefix(
						self.LeakingWeigthVariable,
						LeakScalarPrefixStr
					)

					#set
					self.LeakedInteractionWeigthFloat=float(LeakedInteractionWeigthStr)

					#add
					self.LeakedModelStr+=LeakedInteractionWeigthStr+'*'+self.LeakedParentPopulationDeriveLeakerVariable.LeakedSymbolStr+"_pre : "
					self.LeakedModelStr+=self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr+" (summed)\n"

				elif self.LeakedClampStr=='Variable':

					#debug
					'''
					self.debug(
						[
							'The interaction is a variable, so define the variable and the post pre relation'
						]
					)
					'''

					#define
					#self.LeakedModelStr+="\n"+self.LeakedSymbolStr+" : 1 \n"
					self.LeakedModelStr+="\n"+self.LeakingSymbolPrefixStr+" : 1 \n"
				
					#do the operation
					self.LeakedModelStr+=self.LeakedSymbolStr+"_post="
					#self.LeakedModelStr+=self.LeakedSymbolStr+'*'+self.LeakedParentPopulationDeriveLeakerVariable.LeakedSymbolStr+"_pre : "
					self.LeakedModelStr+=self.LeakingSymbolPrefixStr+'*'+self.LeakedParentPopulationDeriveLeakerVariable.LeakedSymbolStr+"_pre : "
					self.LeakedModelStr+=self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr+" (summed)\n"

				#debug
				'''
				self.debug(
					[
						'Ok',
						('self.',self,[
							'LeakedModelStr'
						]),
						'We add the interaction in the population model',
						'self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr is ',
						self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr
					]
				)
				'''

				#define in the model
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedSymbolStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr+"\n"
				
				#add in the current
				self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(self.LeakedSymbolStr)

				#debug
				'''
				self.debug(
					[
						'In the end',
						'self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr is ',
						self.LeakedParentPopulationDeriveLeakerVariable.LeakedCurrentStr,
						'self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr is ',
						self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr
					]
				)
				'''

			#/##################/#
			# Update in the Synapses dict
			#

			#Check
			if self.BrianingSynapsesDict==None:
			
				#init
				self.BrianingSynapsesDict={
						'model':self.LeakedModelStr
					}

			else:

				#update
				self.BrianingSynapsesDict['model']=self.LeakedModelStr


	def brianPopulation(self):

		#/##################/#
		# Call the base method
		#

		#debug
		'''
		self.debug(
			[
				'We brianPopulation leak here',
				'We call first the base method',
				('self.',self,[
						'BrianingNeurongroupDict'
					])
			]
		)
		'''

		#call
		BaseClass.brianPopulation(self)

		#/###################/#
		# Set maybe the time constant
		#

		#debug
		'''
		self.debug(
			[
				'Maybe we have to set the time variable'
			]
		)
		'''

		#Check
		if self.LeakedClampStr=='Variable':

			#debug
			'''
			self.debug(
				[
					'We set the time variable',
					('self.',self,[
							'LeakingTimeVariable',
							'LeakedTimeSymbolStr',
							'BrianedTimeQuantityVariable'
						]),
					'getattr(self.BrianedNeurongroupVariable,self.LeakedTimeSymbolStr) is ',
					str(getattr(self.BrianedNeurongroupVariable,self.LeakedTimeSymbolStr))
				]
			)
			'''

			#set
			getattr(
				self.BrianedNeurongroupVariable,
				self.LeakedTimeSymbolStr
			)[:]=self.LeakingTimeVariable*self.BrianedParentNetworkDeriveBrianerVariable.BrianedTimeQuantityVariable
			
		#debug
		'''
		self.debug(
			[
				'In the end',
				'getattr(self.BrianedNeurongroupVariable,self.LeakedTimeSymbolStr) is ',
				str(getattr(self.BrianedNeurongroupVariable,self.LeakedTimeSymbolStr))
			]
		)
		'''

		#/###################/#
		# Set maybe the threshold
		#

		#Check
		if hasattr(
				self.BrianedNeurongroupVariable,
				'Threshold'
			):

			#debug
			self.debug(
				[
					'We set the thresholds in the brian Neurongroup',
					('self.',self,[
							'LeakingThresholdVariable',
							'LeakedQuantityVariable'
						])
				]
			)

			#import 
			import numpy

			#set
			self.BrianedNeurongroupVariable.Threshold[:]=numpy.array(
				self.LeakingThresholdVariable
			)*self.LeakedQuantityVariable

			#debug
			self.debug(
				[
					'self.BrianedNeurongroupVariable.Threshold is ',
					str(self.BrianedNeurongroupVariable.Threshold)
				]
			)

			#set in the Threshold Trace to not record
			self.TeamDict[
				'Traces'
			].ManagementDict[
				'*Threshold'
			].BrianingRecordBool=False





		#/###################/#
		# Reference the transfer function
		#

		#debug
		'''
		self.debug(
			[
				'Maybe we have to refer the transfer function'
			]
		)
		'''

		#Check
		if self.LeakingTransferVariable!=None:

			#Check
			if type(self.LeakingTransferVariable)==str:

				#pass
				pass

			else:

				#
				#self.
				
				#import
				import numpy

				#set
				setattr(
					numpy,
					'F',
					self.LeakingTransferVariable
				)
				#self.F=self.LeakingTransferVariable

				pass

		#/###################/#
		# Special input current case
		#

		#Check
		if 'Inputs' in self.TeamDict:

			#debug
			'''
			self.debug(
				[
					'We are going to set brianInput like in all the input _VariablesList',
				]
			)
			'''

			#map
			map(
				lambda __DeriveLeaker:
				__DeriveLeaker.brianInput(),
				self.TeamDict['Inputs'].ManagementDict.values()
			)


			#/###################/#
			# Resort input traces
			#

			#get
			BrianedTracesManager=self.TeamDict['Traces']

			#debug
			self.debug(
				[
					'We resort the inputs traces',
					'self.TeamDict["Inputs"].ManagementDict.keys() is ',
					str(self.TeamDict["Inputs"].ManagementDict.keys()),
					'BrianedTracesManager.ManagementDict.keys() is ',
					str(BrianedTracesManager.ManagementDict.keys())

				]	
			)

			#map
			map(
				lambda __IndexIntAndDeriveLeaker:
				setattr(
					BrianedTracesManager.ManagementDict[
						Recorder.RecordPrefixStr+__IndexIntAndDeriveLeaker[
							1
						].LeakedSymbolStr
					],
					'GetSortInt',
					__IndexIntAndDeriveLeaker[0]
				),
				enumerate(
					SYS._filter(
						lambda __DeriveLeaker:
						__DeriveLeaker.LeakedClampStr not in ["",'Scalar'],
						self.TeamDict['Inputs'].ManagementDict.values()
					)
				)
			)


	def brianTrace(self):

		#/#################/#
		# Check if we have to record the tiime constant
		#

		#debug
		'''
		self.debug(
			[
				'We are in brian trace',
				'Check if it is not the trace of the variable time constant',
				('self.',self,[
					'ManagementTagStr',
				]),
				'self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList is ',
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList,
			]
		)
		'''

		#Check
		if self.ManagementTagStr.split(
			Recorder.RecordPrefixStr
		)[1] in self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList:

			#debug
			'''
			self.debug(
				[
					'We are not recording this variable'
				]
			)
			'''

			#set to false
			self.BrianingRecordBool=False

		#/#################/#
		#  Call the base method
		#

		#call the base method
		BaseClass.brianTrace(self)

	def brianInput(self):

		#debug
		'''
		self.debug(
			[
				'We set input brian here',
			]
		)	
		'''

		#Check
		if self.LeakingWeigthVariable!=None:

			#Check
			if self.LeakedClampStr=='Variable':

				#get
				Variable=getattr(
					self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
					self.LeakedSymbolStr
				)

				#debug
				'''
				self.debug(
					[
						'This input is just a constant value'
					]
				)
				'''

				#set
				setattr(
					self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
					self.LeakedSymbolStr,
					self.LeakingWeigthVariable*Variable.unit
				)

			elif self.LeakedClampStr=='Equation':

				#debug
				'''
				self.debug(
					[
						'This input is time varying and it is an equation',
						('self.',self,[
							'LeakedSymbolStr'
						])
					]
				)
				'''

			elif self.LeakedClampStr=='TimedArray':

				#import
				from brian2 import TimedArray

				#init
				self.LeakedTimedArrayVariable=TimedArray(
					self.LeakingWeigthVariable,
					dt=self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable.clock.dt
				)

				#import sys
				#set in the population
				'''
				setattr(
					#self.LeakedParentPopulationDeriveLeakerVariable,
					#sys.modules['__main__'],
					self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
					self.LeakedSymbolStr,
					self.LeakedTimedArrayVariable
				)
				#globals()[self.LeakedSymbolStr]=self.LeakedTimedArrayVariable
				'''
				setattr(
					self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
					self.LeakedSymbolStr,
					self.LeakedTimedArrayVariable
				)

			elif self.LeakedClampStr=='Custom':

				#debug
				'''
				self.debug(
					[
						'We are going to do a custom operation',
						('self.',self,[
							'LeakedEquationStr',
							'LeakedSymbolStr'
						])
					]
				)
				'''

				#Check
				if '#SymbolStr' in self.LeakedEquationStr:

					#replace
					LeakedEquationStr=self.LeakedEquationStr.replace(
						'#SymbolStr',
						self.LeakedSymbolStr
					)
				else:

					#set
					LeakedEquationStr=self.LeakedSymbolStr+"="+self.LeakedEquationStr

				#debug
				'''
				self.debug(
					[
						'In the end',
						('self.',self,[
							'LeakedEquationStr',
							'LeakedClockStr'
						]),
						'LeakedEquationStr is '+LeakedEquationStr
					]
				)
				'''

				#Check
				if self.LeakedClockStr=="":

					#custom
					LeakedCustomoperation=self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable.custom_operation(
						LeakedEquationStr
					)

				else:

					#split
					LeakedStrsList=self.LeakedClockStr.split('*')

					#import
					import brian2

					#debug
					'''
					self.debug(
						[
							'LeakedStrsList is '+str(LeakedStrsList)
						]
					)
					'''

					#custom
					LeakedCustomoperation=self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable.custom_operation(
						LeakedEquationStr,
						dt=int(LeakedStrsList[0])*getattr(
							brian2,
							LeakedStrsList[1]
						)
					)

				#add
				self.LeakedParentNetworkDeriveLeakerVariable.BrianedNetworkVariable.add(
					LeakedCustomoperation
				)

				#debug
				'''
				self.debug(
					[
						'In the end',
						'self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable is ',
						str(self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable)
					]
				)
				'''

			elif self.LeakedClampStr=='Network':

				#debug
				'''
				self.debug(
					[
						'We are going to do a network operation',
						('self.',self,[
							'LeakedEquationStr',
							'LeakedSymbolStr'
						])
					]
				)
				'''

				#import
				from brian2 import network_operation

				#alias
				BrianedNeurongroupVariable=self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable

				BrianedInputQuantity=getattr(
						BrianedNeurongroupVariable,
						self.LeakedSymbolStr
					)

				if self.LeakedClockStr=="":

					@network_operation
					def updateInput():

						#get set
						BrianedInputQuantity[:]=self.LeakingWeigthVariable[1](
							BrianedInputQuantity,
							BrianedNeurongroupVariable.clock.t
						)

				else:

					#split
					LeakedStrsList=self.LeakedClockStr.split('*')

					#import
					import brian2

					#debug
					'''
					self.debug(
						[
							'LeakedStrsList is '+str(LeakedStrsList)
						]
					)
					'''

					@network_operation(
						dt=int(LeakedStrsList[0])*getattr(
							brian2,
							LeakedStrsList[1]
						)
					)
					def updateInput():

						#get set
						BrianedInputQuantity[:]=self.LeakingWeigthVariable[1](
							BrianedInputQuantity,
							BrianedNeurongroupVariable.clock.t
						)

				#add
				self.LeakedParentNetworkDeriveLeakerVariable.BrianedNetworkVariable.add(
					updateInput
				)
	
	def brianInteraction(self):

		#/##################/#
		# Call the base method
		#

		#debug
		'''
		self.debug(
			[
				'We brianInteraction leak here',
				'We call first the base method',
			]
		)
		'''

		#call
		BaseClass.brianInteraction(self)

		#/##################/#
		# Maybe we specify the connection
		#

		#debug
		'''
		self.debug(
			[
				'We set interaction brian here',
				('self.',self,[
						'LeakedClampStr'
					])
			]
		)
		'''

		#Check
		if self.LeakedClampStr=='Scalar':

			#debug
			'''
			self.debug(
				[
					'Look for a non nul connection',
					('self.',self,['LeakedInteractionWeigthFloat'])
				]
			)
			'''

			#Check
			if self.LeakedInteractionWeigthFloat!=0.:

				#debug
				'''
				self.debug(
					[
						'It is a non nul constant connection',
						'we connect True'
					]
				)
				'''

				#connect
				self.BrianedSynapsesVariable.connect(
					True
				)

		elif self.LeakedClampStr=='Variable':

			#debug
			'''
			self.debug(
				[
					'We have to set the connect variable',
					('self.',self,['LeakingWeigthVariable'])
				]
			)
			'''

			#Check
			if type(self.LeakingWeigthVariable)==float:

				#debug
				'''
				self.debug(
					[
						'It is just one value',
						'We set in the synapses if it is not null',
						('self.',self,[
								'LeakingWeigthVariable'
							])
					]
				)
				'''

				#Check
				if self.LeakingWeigthVariable!=0.:

					#connect
					self.BrianedSynapsesVariable.connect(
						True
					)

					#get and set
					getattr(
						self.BrianedSynapsesVariable,
						self.LeakingSymbolPrefixStr
					)[:]=self.LeakingWeigthVariable
					

				#debug
				'''
				self.debug(
					[
						'In the end ',
						'getattr(self.BrianedSynapsesVariable,self.LeakingSymbolPrefixStr) is ',
						str(getattr(self.BrianedSynapsesVariable,self.LeakingSymbolPrefixStr))
					]
				)
				'''

			else:

				#import
				import numpy

				#Check
				if type(self.LeakingWeigthVariable) in [list,tuple,numpy.ndarray]:

					#debug
					'''
					self.debug(
						[
							'It is an already defined array',
							('self.',self,[
									'LeakingWeigthVariable'
								]),
							'self.BrianedSynapsesVariable.source.N is '+str(self.BrianedSynapsesVariable.source.N),
							'self.BrianedSynapsesVariable.target.N is '+str(self.BrianedSynapsesVariable.target.N),
						]
					)
					'''

					#connect
					self.BrianedSynapsesVariable.connect(
						True
					)

					#get and set
					getattr(
						self.BrianedSynapsesVariable,
						self.LeakingSymbolPrefixStr
					)[:]=numpy.reshape(
						numpy.array(
							self.LeakingWeigthVariable
						),
						self.BrianedSynapsesVariable.source.N*self.BrianedSynapsesVariable.target.N
					)

				else:

					#debug
					'''
					self.debug(
						[
							'It is an array that we have to build before'
						]
					)
					'''

					#numscipy
					self.NumscipyingRowsInt=self.BrianedSynapsesVariable.source.N
					self.NumscipyingColsInt=self.BrianedSynapsesVariable.target.N
					self.numscipy()

					#debug
					'''
					self.debug(
						[
							'We are going to set with',
							('self.',self,['NumscipiedRandomFloatsArray'])
						]
					)
					'''

					#connect
					self.BrianedSynapsesVariable.connect(
						True
					)

					#get and set
					getattr(
						self.BrianedSynapsesVariable,
						self.LeakingSymbolPrefixStr
					)[:]=numpy.reshape(
						self.NumscipiedRandomFloatsArray,
						self.NumscipyingRowsInt*self.NumscipyingColsInt
					)

	def brianTrace(self):

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass.brianTrace(self)

		#debug
		'''
		self.debug(
			[
				'We are going to  brian leak a Trace'
			]
		)
		'''

		#/##################/#
		# Case of an input variable
		#

		BrianedInputStr=SYS.deprefix(
			self.ManagementTagStr,
			Recorder.RecordPrefixStr
		)

		#Check
		if BrianedInputStr.startswith(
			LeakInputPrefixStr
		):

			#join
			BrianedManagementStr='_'.join(BrianedInputStr.split('_')[1:])

			#debug
			'''
			self.debug(
				[
					'It is an input trace',
					'BrianedManagementStr is '+str(BrianedManagementStr),
				]
			)
			'''

			#get
			BrianedInputDeriveLeaker=self.LeakedParentPopulationDeriveLeakerVariable.TeamDict[
				'Inputs'
			].ManagementDict[
				BrianedManagementStr
			]

			#debug
			'''
			self.debug(
				[
					'BrianedInputDeriveLeaker.LeakedClampStr is '+BrianedInputDeriveLeaker.LeakedClampStr,
					'BrianedInputDeriveLeaker.LeakedOperationStr is '+BrianedInputDeriveLeaker.LeakedOperationStr
				]
			)
			'''

			#Check
			if BrianedInputDeriveLeaker.LeakedClampStr not in ['Scalar','Variable']:

				#debug
				'''
				self.debug(
					[
						'It is not a scalar neither a variable so we have to plot it'
					]
				)
				'''

				#manage
				BrianedDefaultDeriveLeaker=self.TeamDict['Samples'].manage(
					'Default'
				).ManagedValueVariable

				#Check
				if BrianedDefaultDeriveLeaker.RecordingLabelVariable==None:

					#debug
					'''
					self.debug(
						[
							'This input has no special recording label variable so take the one of the parent population'
						]
					)	
					'''

					#alias
					BrianedDefaultDeriveLeaker.RecordingLabelVariable=self.LeakedParentPopulationDeriveLeakerVariable.LeakingMonitorIndexIntsList


	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Print the leaked Model str if it is defined
			#

			#Check
			if self.LeakedModelStr!='':

				#Check
				if 'PrintDeepInt' in _KwargVariablesDict:
					PrintedDeepInt=_KwargVariablesDict['PrintDeepInt']
				else:
					PrintedDeepInt=0

				#join
				PrintedAlineaStr="".join([Printer.PrintIndentStr]*(PrintedDeepInt+3))

				#debug
				'''
				print('Leaker l 409')
				print('PrintedDeepInt is ')
				print(PrintedDeepInt)
				print('PrintedAlineaStr is ')
				print(PrintedAlineaStr)
				print('')
				'''

				#replace
				self.PrintingCopyVariable.LeakedModelStr=self.LeakedModelStr.replace(
					'\n','\n'+PrintedAlineaStr
				)

				#add
				self.forcePrint(
					['LeakedModelStr'],
					'LeakerClass'
				)

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)
		
	def addCurrentStr(self,_CurrentStr):

		#debug
		'''
		self.debug(
			[
				'We add current here',
				('self.',self,[
					'LeakedCurrentStr'
				]),
				'_CurrentStr is '+_CurrentStr
			]
		)
		'''

		#Check
		if self.LeakedCurrentStr=="":
			self.LeakedCurrentStr=_CurrentStr
		else:
			self.LeakedCurrentStr+='+'+_CurrentStr

	def filterLeak(self):

		#/#################/#
		# Look for the StructureTopDeriveStructurerRigidVariable
		#

		#debug
		'''
		self.debug(
			[
				'Check if we can leak',
				'self.StructureTopDeriveStructurerRigidVariable!=None',
				str(self.StructureTopDeriveStructurerRigidVariable!=None)
			]
		)
		'''

		#Check
		if self.StructureTopDeriveStructurerRigidVariable!=None:

			#Check
			if self.StructureTopDeriveStructurerRigidVariable.StructureFilterTeamTagStrsList!=None:

				#Check
				if self.ParentDeriveTeamerVariable!=None:

					#debug
					'''
					self.debug(
						[
							'Check if we can leak',
							'self.ParentDeriveTeamerVariable.TeamTagStr is ',
							str(self.ParentDeriveTeamerVariable.TeamTagStr)
						]
					)
					'''
					
					#Check
					if self.ParentDeriveTeamerVariable.TeamTagStr in self.StructureTopDeriveStructurerRigidVariable.StructureFilterTeamTagStrsList:

						#return
						return

		#leak
		self.leak()

	def setDimension(self):

		#import 
		import brian2

		#get
		self.LeakedQuantityVariable=getattr(
			brian2,
			self.LeakingQuantityStr
		)

		#repr
		LeakedQuantityReprStr=repr(self.LeakedQuantityVariable)

		#loop
		for __DimensionStr in ['volt']:

			#Check
			if LeakedQuantityReprStr.endswith(__DimensionStr):
				
				#set
				self.LeakedDimensionStr=__DimensionStr

				#return
				return

		#str
		self.LeakedDimensionStr=repr(
			self.LeakedQuantityVariable.dim
		)

	def setOperation(self):

		#debug
		'''
		self.debug(
			[
				'We set the operation',
				"self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr is ",
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr,
				('self.',self,[
					'LeakedOperationStr'
				])
			]
		)
		'''

		#Check
		if LeakClockPrefixStr in self.LeakedOperationStr:

			#split
			LeakedStrsList=self.LeakedOperationStr.split(':')

			#debug
			'''
			self.debug(
				[
					'There is a specification of the clock',
					'LeakedStrsList is '+str(LeakedStrsList)
				]
			)
			'''

			#deprefix
			self.LeakedClockStr=LeakedStrsList[1]

			#Check
			if self.LeakedClampStr!='Network':

				#join
				self.LeakedEquationStr=':'.join(
					LeakedStrsList[2:]
				)

		else:

			#Check
			if self.LeakedClampStr!='Network':

				#set direct
				self.LeakedEquationStr=self.LeakedOperationStr

		#debug
		'''
		self.debug(
			[
				(
					'self.',self,[
						'LeakedSymbolStr',
						'LeakedClockStr',
						'LeakedEquationStr'
					]
				)
			]
		)
		'''

		#append
		if self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList==None:

			#init
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList=[
				self.LeakedSymbolStr
			]

		else:

			#append
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList.append(
				self.LeakedSymbolStr
			)

		#Check
		if self.LeakedParentPopulationDeriveLeakerVariable.LeakedQuantityVariable==None:
			self.LeakedParentPopulationDeriveLeakerVariable.setDimension()

		#define in the model
		if self.LeakedClampStr=='Equation':
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedSymbolStr+'='+self.LeakedEquationStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr+"\n"
		elif self.LeakedClampStr in ['Custom','Network']:
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedSymbolStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakedDimensionStr+"\n"

		#add in the current
		self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(
			self.LeakedSymbolStr
		)

#</DefineClass>

#</DefinePrint>
LeakerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'LeakingUnitsInt',
		'LeakingSymbolStr',
		'LeakingTimeVariable',
		'LeakingQuantityStr',
		'LeakingMonitorIndexIntsList',
		'LeakingTimeUnitStr',
		'LeakingInteractionStr',
		'LeakingSymbolPrefixStr',
		'LeakingWeigthVariable',
		'LeakingTransferVariable',
		'LeakingThresholdVariable',
		'LeakingResetVariable',
		'LeakedRecordSkipStrsList',
		'LeakedQuantityVariable',
		'LeakedDimensionStr',
		'LeakedClampStr',
		'LeakedSymbolStr',
		'LeakedOperationStr',
		'LeakedEquationStr',
		'LeakedClockStr',
		'LeakedModelStr',
		'LeakedCurrentStr',
		'LeakedTimeSymbolStr',
		'LeakedInteractionWeigthFloat',
		'LeakedParentSingularStr',
		'LeakedParentNetworkDeriveLeakerVariable',
		'LeakedParentPopulationDeriveLeakerVariable',
		'LeakedParentInteractomeDeriveLeakerVariable',
		'LeakedTimedArrayVariable'
	]
)
#<DefinePrint>
