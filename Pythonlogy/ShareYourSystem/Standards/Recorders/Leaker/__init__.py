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
from ShareYourSystem.Standards.Recorders import Recorder
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
	'ClassingSwitchMethodStrsList':['leak'],
})
class LeakerClass(BaseClass):
		
	def default_init(self,
			_LeakLevelStr="",
			_LeakingUnitsInt=0,
			_LeakingActivitySymbolStr="V",
			_LeakingCurrentStr="",
			_LeakingTimeConstantFloat=20.,
			_LeakingTimeDirectBool=True,
			_LeakingActivityDimensionStr='volt',
			_LeakingMonitorIndexIntsList=None,
			_LeakingTimeUnitStr='ms',
			_LeakedTimeSymbolStr="tau_V",
			_LeakedModelStr="",
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_leak(self):

		#Check
		if self.LeakLevelStr=='Neurongroup':

			#/################/#
			# Look how to define the time constant
			#

			#debug
			self.debug(
				[
					'Check if we direct define the time constant or not'
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

			#update
			self.BrianingNeurongroupDict.update(
				{
					'N':self.LeakingUnitsInt,
					'model':self.LeakedModelStr
				}
			)

			#team traces
			LeakedTracesDeriveManager=self.team(
				'Traces'
				).TeamedValueVariable

			#manage
			LeakedRecordDeriveBrianer=LeakedTracesDeriveManager.manage(
					'*'+self.LeakingActivitySymbolStr
				).ManagedValueVariable

			#set
			LeakedRecordDeriveBrianer.NumscipyingStdFloat=0.001
			LeakedSamplesDeriveBrianer=LeakedRecordDeriveBrianer.team(
					'Samples'
				).TeamedValueVariable
			LeakedDefaultDeriveBrianer=LeakedSamplesDeriveBrianer.manage(
					'Default'
				).ManagedValueVariable

			#Check
			if len(self.LeakingMonitorIndexIntsList)==0:
				self.LeakingMonitorIndexIntsList=[0]

			#set
			LeakedDefaultDeriveBrianer.MoniteringLabelIndexIntsArray=self.LeakingMonitorIndexIntsList

		elif self.LeakLevelStr=='Synapses':

			#/################/#
			# Look how to define the time constant
			#

			#debug
			self.debug(
				[
					'We leak synapses here',
					'self.BrianedParentNeurongroupDeriveBrianerVariable.LeakedModelStr is ',
					self.BrianedParentNeurongroupDeriveBrianerVariable.LeakedModelStr 
				]
			)







	#override
	def setNeurongroup(self):

		#/#################/#
		# hook toward leak
		#

		#leak
		self.LeakLevelStr="Neurongroup"
		self.leak()

		#/#################/#
		# Call the base method
		#

		#brian
		BaseClass.setNeurongroup(self)

	def setSynapses(self):

		#/#################/#
		# hook toward leak
		#

		#leak
		self.LeakLevelStr="Synapses"
		self.leak()

		#/#################/#
		# Call the base method
		#

		#brian
		BaseClass.setSynapses(self)
			
#</DefineClass>

#</DefinePrint>
LeakerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'LeakingUnitsInt',
		'LeakingActivitySymbolStr',
		'LeakingCurrentStr',
		'LeakingTimeConstantFloat',
		'LeakingTimeDirectBool',
		'LeakingActivityDimensionStr=',
		'LeakingTimeUnitStr',
		'LeakedTimeSymbolStr',
		'LeakedModelStr'
	]
)
#<DefinePrint>
