# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Rater

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Recorders.Brianer"
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
	'ClassingSwitchMethodStrsList':['rate'],
})
class RaterClass(BaseClass):
		
	def default_init(self,
			_RatingUnitsInt=0,
			_RatingConstantTimeFloat=20.,
			_RatingTransferFunction=lambda _Float:_Float,
			_RatingMonitorList=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_rate(self):

		#/################/#
		# Update the NeurongroupingKwargVariablesDict
		#

		#debug
		self.debug(
			[
				'We build the rate model system if N>0',
				('self.',self,['BrianingNeurongroupDict'])
			]
		)

		#Check
		if self.RatingUnitsInt>0:

			#update
			self.BrianingNeurongroupDict.update(
				{
					'N':self.RatingUnitsInt,
					'model':
					'''
						Jr : 1
						tau : 1
						dr/dt = (-r+Jr)/(tau*ms) : 1
					'''
				}
			)

			#team traces
			RatedTracesDeriveManager=self.team(
				'Traces'
				).TeamedValueVariable

			#manage
			RatedRecordDeriveBrianer=RatedTracesDeriveManager.manage(
					'*r'
				).ManagedValueVariable

			#set
			RatedRecordDeriveBrianer.NumscipyingStdFloat=0.001
			RatedSamplesDeriveBrianer=RatedRecordDeriveBrianer.team(
					'Samples'
				).TeamedValueVariable
			RatedDefaultDeriveBrianer=RatedSamplesDeriveBrianer.manage(
					'Default'
				).ManagedValueVariable

			#Check
			if len(self.RatingMonitorList)==0:
				self.RatingMonitorList=[0]

			#set
			RatedDefaultDeriveBrianer.MoniteringLabelIndexIntsArray=self.RatingMonitorList

	def mimic_simulate(self):

		#/################/#
		# Set values
		#

		#debug
		self.debug(
			[
				'Before simulation we fix certain values',
				('self.',self,['RatingConstantTimeFloat'])
			]
		)

		#Check
		if self.BrianedNeurongroupVariable!=None:

			#set
			self.BrianedNeurongroupVariable.tau=self.RatingConstantTimeFloat

		#/################/#
		# We call the base method
		#

		#simulate
		BaseClass.simulate(self)


	"""
	def mimic_brian(self):

		#Check
		if self.

			#/#################/#
			# Neurongroup case
			#


		#/#################/#
		# Call the base method
		#

		#brian
		BaseClass.brian(self)
	"""


	#override
	def setNeurongroup(self):

		#/#################/#
		# Rhook toward rate
		#

		#rate
		self.rate()

		#/#################/#
		# Call the base method
		#

		#brian
		BaseClass.setNeurongroup(self)
		


		
#</DefineClass>

#</DefinePrint>
RaterClass.PrintingClassSkipKeyStrsList.extend(
	[
	]
)
#<DefinePrint>
