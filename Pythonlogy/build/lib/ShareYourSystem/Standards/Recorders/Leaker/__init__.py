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
			_LeakingActivitySymbolStr="V",
			_LeakingCurrentStr="",
			_LeakingTimeConstantFloat=0.,
			_LeakingTimeDirectBool=True,
			_LeakingActivityDimensionStr='volt',
			_LeakingMonitorIndexIntsList=None,
			_LeakingTimeUnitStr='ms',
			_LeakingInteractionClampStr='Rate',
			_LeakingInteractionPrefixSymbolStr='J',
			_LeakingInputPrefixSymbolStr='I',
			_LeakingExternalVariable=None,
			_LeakedTimeSymbolStr="tau_V",
			_LeakedModelStr="",
			_LeakedInteractionSymbolStr="",
			_LeakedInputSymbolStr="",
			_LeakedParentSingularStr="",
			_LeakedParentNetworkDeriveLeakerVariable=None,
			_LeakedParentPopulationDeriveLeakerVariable=None,
			_LeakedParentInteractomeDeriveLeakerVariable=None,
			_LeakedTimedArrayVariable=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)


	def filterLeak(self):

		#/#################/#
		# Look for the StructureTopDeriveStructurerVariable
		#

		#debug
		self.debug(
			[
				'Check if we can leak',
				'self.StructureTopDeriveStructurerVariable!=None',
				str(self.StructureTopDeriveStructurerVariable!=None)
			]
		)

		#Check
		if self.StructureTopDeriveStructurerVariable!=None:

			#Check
			if self.StructureTopDeriveStructurerVariable.StructureFilterTeamTagStrsList!=None:

				#Check
				if self.ParentDeriveTeamerVariable!=None:

					#debug
					self.debug(
						[
							'Check if we can leak',
							'self.ParentDeriveTeamerVariable.TeamTagStr is ',
							str(self.ParentDeriveTeamerVariable.TeamTagStr)
						]
					)

					#Check
					if self.ParentDeriveTeamerVariable.TeamTagStr in self.StructureTopDeriveStructurerVariable.StructureFilterTeamTagStrsList:

						#return
						return

		#leak
		self.leak()

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
			self.debug(
				[
					'It is a Network level for the leak',
				]
			)
			
			#/########################/#
			# network the interactions
			# 

			#debug
			self.debug(
				[
					'We structure filterLeak all the interacting children...'
					'So we pass thrugh the populations and leak the interactomes, interactions and inputs',
				]
			)	

			#set
			self.StructureFilterTeamTagStrsList=[
				'Populations'
			]

			#structure
			self.structure(
				[
					'Populations',
					'Interactomes',
					'Interactions',
					'Inputs'
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
				self.debug(
					[
						'...But there is no population',
						'so set a leak model here '
					]
				)

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
			# network the populations
			# 

			#debug
			self.debug(
				[
					'We structure leak brian all the children...',
					'self.TeamDict.keys() is ',
					str(self.TeamDict.keys())
				]
			)

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

			#debug
			self.debug(
				[
					'Ok we check if this parentsingular has a special method ',
					('self.',self,[
						'LeakedParentSingularStr'
					])
				]
			)

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
						'Ok we have setted leak'+self.BrianedParentSingularStr
					]
				)
				'''	
		
	def leakPopulation(self):

		#/################/#
		# Look for the time constant
		#

		#debug
		self.debug(
			[
				'We set a population here',
				'look for the time constant'
			]
		)

		#Check
		if self.LeakingTimeDirectBool:

			#set
			self.LeakedTimeSymbolStr=str(self.LeakingTimeConstantFloat)

		else:

			#set
			self.LeakedTimeSymbolStr="tau_"+self.LeakingActivitySymbolStr

			#define the time constant variable
			self.LeakedModelStr+=self.LeakedTimeSymbolStr+' : 1\n'

		#/################/#
		# Define the main leak equation
		#

		#debug
		self.debug(
			[
				'We define the main leak equation but maybe it is just a direct value',
				('self.',self,['LeakingTimeConstantFloat'])
			]
		)

		#Check
		if self.LeakingTimeConstantFloat==0:

			#debug
			self.debug(
				[
					'Build just a variable definition',
					('self.',self,['LeakingTimeConstantFloat'])
				]
			)

			#set the left 
			self.LeakedModelStr+=self.LeakingActivitySymbolStr+' : '+self.LeakingActivityDimensionStr

		else:

			#debug
			self.debug(
				[
					'Build a differential equation'
				]
			)

			#set the left 
			self.LeakedModelStr+="d"+self.LeakingActivitySymbolStr+'/dt='

			#set the right
			self.LeakedModelStr+='(-'+self.LeakingActivitySymbolStr

			#Check
			if self.LeakingCurrentStr!="":
				self.LeakedModelStr+='+'+self.LeakingCurrentStr

			#set
			self.LeakedModelStr+=')'

			#set the right denominator
			self.LeakedModelStr+='/('+self.LeakedTimeSymbolStr+'*'+self.LeakingTimeUnitStr+')'

			#set the dimension
			self.LeakedModelStr+=' : '+self.LeakingActivityDimensionStr

		#debug
		self.debug(
			[
				'We have defined the leak model str',
				('self.',self,['LeakedModelStr'])
			]
		)

		#/################/#
		# Now update the brianer stuff
		#

		
		#team traces
		LeakedTracesDeriveManager=self.team(
			'Traces'
			).TeamedValueVariable

		#manage
		LeakedRecordDeriveLeaker=LeakedTracesDeriveManager.manage(
				'*'+self.LeakingActivitySymbolStr
			).ManagedValueVariable

		#set
		LeakedRecordDeriveLeaker.NumscipyingStdFloat=0.001
		LeakedSamplesDeriveLeaker=LeakedRecordDeriveLeaker.team(
				'Samples'
			).TeamedValueVariable
		LeakedDefaultDeriveLeaker=LeakedSamplesDeriveLeaker.manage(
				'Default'
			).ManagedValueVariable

		#Check
		if len(self.LeakingMonitorIndexIntsList)==0:
			self.LeakingMonitorIndexIntsList=[0]

		#set
		LeakedDefaultDeriveLeaker.MoniteringLabelIndexIntsArray=self.LeakingMonitorIndexIntsList

		#/##################/#
		# Update in the Neurongroup dict
		#

		#Check
		if self.BrianingNeurongroupDict==None:
		
			#init
			self.BrianingNeurongroupDict={
					'N':self.LeakingUnitsInt,
					'model':self.LeakedModelStr
				}

		else:

			#update
			self.BrianingNeurongroupDict.update(
				{
					'N':self.LeakingUnitsInt,
					'model':self.LeakedModelStr
				}
			)

		"""
		#/##################/#
		# Call the brian setNeurongroup
		#
	
		#call
		#self.setNeurongroup()
		"""

	def leakInteraction(self):

		#/####################/#
		# Set the parent
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



		#debug
		self.debug(
			[
				'We set Interaction here',
				'Look for the type of interaction'
			]
		)

		#Check
		if self.LeakingInteractionClampStr=='Rate':

			#set
			self.LeakedInteractionSymbolStr=self.LeakingInteractionPrefixSymbolStr+self.ParentTagStr.split(
				'Interactions'
			)[-1].replace('/','_')

			#debug
			self.debug(
				[
					'It is a rate interaction',
					'self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivitySymbolStr is ',
					self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivitySymbolStr,
					'First we set the model in the synapse',
					('self.',self,['LeakedInteractionSymbolStr'])
				]
			)

			#set
			self.LeakedModelStr+="\n"+self.LeakedInteractionSymbolStr+" : 1 \n"
			self.LeakedModelStr+=self.LeakedInteractionSymbolStr+self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivitySymbolStr+"_post="
			self.LeakedModelStr+=self.LeakedInteractionSymbolStr+self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivitySymbolStr+"_pre : 1 (summed)\n"

			#debug
			self.debug(
				[
					'We add the interaction in the population model',
					'self.LeakedParentPopulationDeriveLeakerVariable.LeakingCurrentStr is ',
					self.LeakedParentPopulationDeriveLeakerVariable.LeakingCurrentStr
				]
			)

			#set
			LeakedInteractionActivitySymbolStr=self.LeakedInteractionSymbolStr+self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivitySymbolStr

			#define in the model
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=LeakedInteractionActivitySymbolStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivityDimensionStr+'\n'

			#add in the current
			self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(LeakedInteractionActivitySymbolStr)

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


	def brianPopulation(self):

		#/##################/#
		# Call the base method
		#

		#debug
		self.debug(
			[
				'We call first the base method'
			]
		)

		#call
		BaseClass.brianPopulation(self)

		#/###################/#
		# Special input current case
		#

		#Check
		if 'Inputs' in self.TeamDict:

			#debug
			self.debug(
				[
					'We are going to set brianInput like in all the input variables',
				]
			)

			#map
			map(
				lambda __DeriveLeaker:
				__DeriveLeaker.brianInput(),
				self.TeamDict['Inputs'].ManagementDict.values()
			)

	def leakInput(self):

		#/################/#
		# Input level
		#

		#debug
		self.debug(
			[
				'It is an Input level',
			]
		)

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
		self.LeakedInputSymbolStr=self.LeakingInputPrefixSymbolStr+self.ParentTagStr.split(
			'Inputs'
		)[-1].replace(
			'/','_'
		)

		#debug
		self.debug(
			[
				'we add in the model of the parent population',
				('self.',self,['LeakedInputSymbolStr'])
			]
		)

		#debug
		self.debug(
			[
				'We add the interaction in the population model',
				'self.LeakedParentPopulationDeriveLeakerVariable.LeakingCurrentStr is ',
				self.LeakedParentPopulationDeriveLeakerVariable.LeakingCurrentStr
			]
		)

		#Check
		if type(self.LeakingExternalVariable)==float:

			#debug
			self.debug(
				[
					'It is a constant external so just define a variable'
				]
			)

			#define in the model
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedInputSymbolStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivityDimensionStr+'\n'

			#add in the current
			self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(
				self.LeakedInputSymbolStr
			)

		elif type(self.LeakingExternalVariable)==str:

			#debug
			self.debug(
				[
					'It is an external str so direct add'
				]
			)

			#define in the model
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedInputSymbolStr+'='+self.LeakingExternalVariable+'\n'

		else:

			#debug
			self.debug(
				[
					'It is an external array so direct add plus a (t)'
				]
			)

			#define in the model
			self.LeakedParentPopulationDeriveLeakerVariable.LeakedModelStr+=self.LeakedInputSymbolStr+' : '+self.LeakedParentPopulationDeriveLeakerVariable.LeakingActivityDimensionStr+'\n'

			#add in the current
			self.LeakedParentPopulationDeriveLeakerVariable.addCurrentStr(
				#self.LeakedInputSymbolStr+'(t)'
				self.LeakedInputSymbolStr
			)

	def brianInput(self):

		#debug
		self.debug(
			[
				'We set input brian here',
			]
		)	

		#import
		from brian2 import TimedArray

		#Check
		if type(self.LeakingExternalVariable)==float:

			#get
			Variable=getattr(
				self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
				self.LeakedInputSymbolStr
			)

			#debug
			self.debug(
				[
					'This input is just a constant value'
				]
			)

			#set
			setattr(
				self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
				self.LeakedInputSymbolStr,
				self.LeakingExternalVariable*Variable.unit
			)

		else:	

			#debug
			self.debug(
				[
					'This input is time varying',
					'self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable.clock.dt is ',
					self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable.clock.dt,
					('self.',self,['LeakedInputSymbolStr'])
				]
			)

			#init
			self.LeakedTimedArrayVariable=TimedArray(
				self.LeakingExternalVariable,
				dt=self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable.clock.dt
			)


			#import sys
			#set in the population
			'''
			setattr(
				#self.LeakedParentPopulationDeriveLeakerVariable,
				#sys.modules['__main__'],
				self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
				self.LeakedInputSymbolStr,
				self.LeakedTimedArrayVariable
			)
			#globals()[self.LeakedInputSymbolStr]=self.LeakedTimedArrayVariable
			'''
			setattr(
				self.LeakedParentPopulationDeriveLeakerVariable.BrianedNeurongroupVariable,
				self.LeakedInputSymbolStr,
				self.LeakedTimedArrayVariable
			)


		#debug
		'''
		self.debug(
			[
				'Yeah we have timed arrayed ',
				('self.',self,[
					'LeakedTimedArrayVariable'
					])
			]
		)	
		'''
			
	def addCurrentStr(self,_CurrentStr):

		#Check
		if self.LeakingCurrentStr=="":
			self.LeakingCurrentStr=_CurrentStr
		else:
			self.LeakingCurrentStr+='+ '+_CurrentStr



#</DefineClass>

#</DefinePrint>
LeakerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'LeakingUnitsInt',
		'LeakingActivitySymbolStr',
		'LeakingCurrentStr',
		'LeakingTimeConstantFloat',
		'LeakingTimeDirectBool',
		'LeakingActivityDimensionStr',
		'LeakingMonitorIndexIntsList',
		'LeakingTimeUnitStr',
		'LeakingInteractionClampStr',
		'LeakingInteractionPrefixSymbolStr',
		'LeakingInputPrefixSymbolStr',
		'LeakingExternalVariable',
		'LeakedTimeSymbolStr',
		'LeakedModelStr',
		'LeakedInteractionSymbolStr',
		'LeakedInputSymbolStr',
		'LeakedParentSingularStr',
		'LeakedParentNetworkDeriveLeakerVariable',
		'LeakedParentPopulationDeriveLeakerVariable',
		'LeakedParentInteractomeDeriveLeakerVariable',
		'LeakedTimedArrayVariable'
	]
)
#<DefinePrint>
