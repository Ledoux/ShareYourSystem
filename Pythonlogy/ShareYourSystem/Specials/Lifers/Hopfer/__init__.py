# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import types
BaseModuleStr="ShareYourSystem.Specials.Lifers.Lifer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Hopfer','Hopf','Hopfing','Hopfed')
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Recorders import Leaker
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class HopferClass(BaseClass):
	
	def default_init(self,
			_HopfingUnitsInt = 1,
			_HopfingLateralWeightVariable = None,
			_HopfingConstantTimeVariable = 0.02, 
			_HopfingDelayTimeVariable = 0.002,
			_HopfingMeanWeightFloat = 0.0,
			_HopfingStdWeightFloat = 1.0,
			_HopfingSparseWeightFloat=0.,
			_HopfingSwitchWeightFloat=0.5,
			_HopfingNormalisationInt= 0.5,
			_HopfingSymmetryFloat = 0.0,
			_HopfingPerturbationEnvelopBool=True,
			_HopfingContourSamplesInt=50,
			_HopfingInteractionStr="Rate",
			_HopfingRestVariable=-48.,
			_HopfedLateralWeightFloatsArray=None,
			_HopfedMeanfieldWeightFloat=0.,
			_HopfedRealLateralEigenFloatsArray = None,
			_HopfedImagLateralEigenFloatsArray = None,
			_HopfedHalfHeightFloat=0.,
			_HopfedLateralHalfWidthFloat=0., 
			_HopfedLateralContourComplexesArray=None,
			_HopfedEigenComplex=None,
			_HopfedEigenvalueComplexesArray=None,
			_HopfedPerturbationContourRealFloatsArray = None,
			_HopfedPerturbationContourImagFloatsArray = None,
			_HopfedInstabilityIndexInt=-1,
			_HopfedInstabilityComplex=None,
			_HopfedInstabilityLambdaFloatsTuple=None,
			_HopfedInstabilityFrequencyFloat=0.,
			_HopfedIsStableBool=True,
			_HopfedInstablesInt=0,
			_HopfedInstabilityStr="",
			_HopfedStdSparseFloat=0.,
			_HopfedParentSingularStr="",
			_HopfedIndexIntsTuplesList=None,
			_HopfedPerturbationNullVariable=None,
			_HopfedPerturbationWeightFloatsArray=None,
			_HopfedConstantTimeVariable=None,
			_HopfedStabilityScanFrequencyFloatsArray=None,
			_HopfedOptimizeRoot=None,
			_HopfedAgentDeriveHopferVariable=None,
			_HopfedNetworkDeriveHopferVariable=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_hopf(self):

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
			self.HopfedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['HopfedParentSingularStr'])
			]
		)
		'''

		#Check
		if (self.ParentDeriveTeamerVariable==None or "Populations" in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces',
			'Samples',
			'Events',
			'Interactomes',
			"Interactions",
			'Inputs'
		]) and self.HopfedParentSingularStr!='Population':

			#/########################/#
			# Network level
			# 

			#debug
			'''
			self.debug(
				[
					'It is a Network level for the hopf',
				]
			)
			'''

			#/########################/#
			# Determine parent level
			# 

			#alias
			self.HopfedNetworkDeriveHopferVariable=self

			#/########################/#
			# hopfNetwork
			# 

			#hopf
			self.hopfNetwork()

			#/########################/#
			# structure hopf 
			# 

			#debug
			'''
			self.debug(
				[
					'We structure all the hopfing children...'
				]
			)	
			'''

			#structure
			self.structure(
				[
					"Populations",
					'Inputs',
					'Interactomes',
					"Interactions",
				],
				'#all',
				_ManagerCommandSetList=[
						'hopf'
					]
			)
			
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
						'HopfedParentSingularStr'
					])
				]
			)
			'''

			#set
			HopfedMethodKeyStr='hopf'+self.HopfedParentSingularStr

			#Check
			if hasattr(self,HopfedMethodKeyStr):

				#/########################/#
				# call the special hopf<HopfedParentSingularStr> method
				#

				#debug
				'''
				self.debug(
					[
						'It is a '+self.HopfedParentSingularStr+' level',
						'We hopf<HopfedParentSingularStr>'
					]
				)
				'''

				#call
				getattr(
					self,
					HopfedMethodKeyStr
				)()

				#debug
				'''
				self.debug(
					[
						'Ok we have setted hopf'+self.HopfedParentSingularStr
					]
				)
				'''	
	
	def hopfNetwork(self):

		#/###############/#
		# Build the laterals
		#

		#type
		HopfedLateralType=type(self.HopfingLateralWeightVariable)

		#Check
		if HopfedLateralType==None.__class__:

			#debug
			'''
			self.debug(
				[
					'Ok we build the laterals'
				]
			)
			'''

			#numscipy
			self.NumscipyingRowsInt=self.HopfingUnitsInt
			self.NumscipyingColsInt=self.HopfingUnitsInt
			self.NumscipyingStdFloat=self.HopfingStdWeightFloat
			self.NumscipyingMeanFloat=self.HopfingMeanWeightFloat
			self.NumscipyingSymmetryFloat=self.HopfingSymmetryFloat
			if self.HopfingInteractionStr=="Rate":
				self.NumscipyingEigenvalueBool=self.HopfingPerturbationEnvelopBool or self.HopfingDoStabilityBool
			else:
				self.NumscipyingEigenvalueBool=False
			self.NumscipyingNormalisationFunction=lambda __ColsInt:__ColsInt**0.5
			self.NumscipyingMeanForceStr="rows"

			#Check
			self.NumscipyingSparseFloat=self.HopfingSparseWeightFloat
			self.NumscipyingSwitchFloat=self.HopfingSwitchWeightFloat

			#numscipy
			self.numscipy(
				)

			#Check
			if self.HopfingInteractionStr=="Spike":

				#debug
				self.debug(
					[
						"We have to modify the matrix G",
						"First we compute the stationary solution"
					]
				)

				self.LifingConstantTimeFloat = self.HopfingConstantTimeVariable
				self.LifingResetFloat = -60.
				self.LifingThresholdFloat = -50.
				self.LifingRestFloat = -70.
				

				#self.LifingNoiseFloat = self.HopfingStdWeightFloat
				#self.LifingStationaryCurrentFloat = self.HopfingRestVariable-self.LifingVoltageRestFloat


				#debug
				self.debug(
					[
						"We compute then the perturbations ",
					]
				)

				
				#lif
				self.lif(
					_PerturbationLambdaVariable=0.,
					_ComputeNoisePerturbationBool=True
				)

				#debug
				self.debug(
					[
						"We have lifed"
					]
				)

				#set
				self.HopfedTotalPerturbationComplexesArray=self.LifedPerturbationMeanComplexVariable*self.NumscipiedValueFloatsArray
				self.HopfedTotalPerturbationComplexesArray+=(
					self.LifedPerturbationNoiseComplexVariable/(2.*self.LifingNoiseFloat)
				)*(self.NumscipiedValueFloatsArray**2)
				self.HopfedTotalPerturbationComplexesArray*=self.HopfingConstantTimeVariable
		
				#import
				import numpy as np

				#eigenvalues
				self.HopfedEigenvalueComplexesArray = np.linalg.eigvals(
					self.HopfedTotalPerturbationComplexesArray
				)

			else:

				#alias
				self.HopfedEigenvalueComplexesArray = self.NumscipiedEigenvalueComplexesArray

			#alias
			self.HopfedLateralWeightFloatsArray=self.NumscipiedValueFloatsArray

			#set
			self.HopfedMeanfieldWeightFloat=self.HopfingStdWeightFloat if self.HopfingStdWeightFloat>0. else self.HopfingMeanWeightFloat

			#debug
			'''
			self.debug(
				[
					'We have setted the laterals',
					('self.',self,[
						'HopfedLateralWeightFloatsArray',
						'HopfedMeanfieldWeightFloat'
					])
				]
			)
			'''

			

			#Check
			if self.HopfedMeanfieldWeightFloat==0.:

				#return
				self.HopfedIsStableBool=True

				#return 
				return self

			#/###################/#
			# Determine the stationary solutions
			# 

			#Check
			if self.HopfingInteractionStr=="Spike":

				#debug
				"""
				self.debug(
					[
						'We compute the stationary solutions'
					]
				)
				"""

			#/###############/#
			# Determine the contour properties
			#



			#debug
			'''
			self.debug(
				[
					'We set the contour of the ellipse',
					('self.',self,[
							'NumscipiedVarianceFloat',
							'NumscipiedStdFloat',
							'NumscipiedCovarianceFloat',
							'NumscipiedSommersFloat'
						])
				]
			)
			'''

			#/###############/#
			# Build the eigen values real and imag
			#

			#import 
			import numpy as np

			#real and imag
			self.HopfedRealLateralEigenFloatsArray=np.real(
				self.HopfedEigenvalueComplexesArray
			)
			self.HopfedImagLateralEigenFloatsArray=np.imag(
				self.HopfedEigenvalueComplexesArray
			)

			#debug
			'''
			self.debug(
				[
					'We have built the real and imag',
					('self.',self,[
							'HopfedRealLateralEigenFloatsArray',
							'HopfedImagLateralEigenFloatsArray'
						])
				]
			)
			'''

			#/###############/#
			# Compute for each eigenvalues a possible solution
			#

			#Check
			if self.HopfingPerturbationEnvelopBool:

				#debug
				"""
				self.debug(
					[
						('self.',self,[
								'NumscipiedEigenvalueComplexesArray'
							])
					]
				)
				"""

				#map
				HopfedPerturbationFloatsTuplesList=map(
					lambda __NumscipiedEigenvalueComplex:
					self.setAttr(
						'HopfedEigenComplex',
						__NumscipiedEigenvalueComplex
					).getPerturbationSolutionFloatsTuple(),
					self.HopfedEigenvalueComplexesArray
				)
			
			else:

				"""
				#Check
				if self.HopfingDoStabilityBool:

					#for
					for __NumscipiedEigenvalueComplex in self.NumscipiedEigenvalueComplexesArray:

						#set
						self.HopfedInstabilityPerturbationComplex=self.setAttr(
							'HopfedEigenComplex',
							__NumscipiedEigenvalueComplex
						).getPerturbationSolutionFloatsTuple(
						)
				"""
				pass


			#unpack
			[
				HopfedPerturbationRealFloatsTuple,
				HopfedPerturbationImagFloatsTuple
			]=SYS.unzip(
				HopfedPerturbationFloatsTuplesList,
				[0,1]
			)
			self.HopfedPerturbationRealFloatsArray=np.array(HopfedPerturbationRealFloatsTuple)
			self.HopfedPerturbationImagFloatsArray=np.array(HopfedPerturbationImagFloatsTuple)
			
			#/###############/#
			# Build the contour of the eigen values real and ima
			#

			#list
			self.HopfedLateralContourComplexesArray=[
				__Float + (
					1.-self.NumscipiedSommersFloat
				)*np.sqrt(
					1-(__Float/(1+self.NumscipiedSommersFloat))**2
				)*1j for __Float in np.linspace(
					-1.-self.NumscipiedSommersFloat,
					1.+self.NumscipiedSommersFloat,
					self.HopfingContourSamplesInt
				)
			]

			#list
			self.HopfedLateralContourComplexesArray+=list(
				np.array(
				self.HopfedLateralContourComplexesArray
				).conjugate()[::-1]  
			)

			#array
			self.HopfedLateralContourComplexesArray=np.array(
				self.HopfedLateralContourComplexesArray
			)

			#Check
			if self.HopfingStdWeightFloat>0.:

				#set
				self.HopfedLateralContourComplexesArray*=self.HopfingStdWeightFloat

			else:

				#sqrt
				self.HopfedStdSparseFloat=np.sqrt(
					self.NumscipyingSparseFloat*(1.-self.NumscipyingSparseFloat)
				)
				
				#set
				self.HopfedLateralContourComplexesArray*=self.HopfedStdSparseFloat
	          	      
			#/###############/#
			# Compute for each eigen of the contour a possible solution
			#

			#debug
			"""
			self.debug(
				[
					('self.',self,[
							'HopfingPerturbationEnvelopBool'
						])
				]
			)
			"""

			#Check
			if self.HopfingPerturbationEnvelopBool:

				#map
				HopfedPerturbationContourFloatsTuplesList=map(
					lambda __HopfedContourComplex:
					self.setAttr(
						'HopfedEigenComplex',
						__HopfedContourComplex
					).getPerturbationSolutionFloatsTuple(),
					self.HopfedLateralContourComplexesArray
				)

				#unpack
				[
					HopfedPerturbationContourRealFloatsTuple,
					HopfedPerturbationContourImagFloatsTuple
				]=SYS.unzip(
					HopfedPerturbationContourFloatsTuplesList,
					[0,1]
				)
				self.HopfedPerturbationContourRealFloatsArray=np.array(HopfedPerturbationContourRealFloatsTuple)
				self.HopfedPerturbationContourImagFloatsArray=np.array(HopfedPerturbationContourImagFloatsTuple)
				
				#debug
				"""
				self.debug(
					[
						('self.',self,[
								'HopfingDoStabilityBool',
								'HopfedPerturbationRealFloatsArray',
							])
					]
				)
				"""

				#get
				self.HopfedInstabilityIndexInt = np.argmax(
					self.HopfedPerturbationRealFloatsArray
				)

				#find
				InstableEigenIndexIntsArray=np.where(self.HopfedPerturbationRealFloatsArray>0.)[0]
			
				#debug
				'''
				self.debug(
					[
						"InstableEigenIndexIntsArray is ",str(InstableEigenIndexIntsArray)
					]
				)
				'''

				#len
				self.HopfedInstablesInt=len(InstableEigenIndexIntsArray)

				#get	
				self.HopfedInstabilityComplex=self.HopfedPerturbationRealFloatsArray[
					self.HopfedInstabilityIndexInt
				]

				#set
				self.HopfedIsStableBool=self.HopfedPerturbationRealFloatsArray[
					self.HopfedInstabilityIndexInt
				]<0.

				#Check
				if self.HopfedIsStableBool==False:

					#set
					self.HopfedInstabilityStr='Rate' if self.HopfedPerturbationImagFloatsArray[
						self.HopfedInstabilityIndexInt
					]==0. else 'Hopf'

				#debug
				'''
				self.debug(
					[
						('self.',self,[
								'HopfedInstabilityIndexInt',
								'HopfedInstabilityComplex',
								'HopfedIsStableBool',
								'HopfedInstabilityStr'
							])
					]
				)
				'''

			else:

				#for
				for __HopfedContourComplex in self.HopfedLateralContourComplexesArray:

					#set
					self.setAttr(
						'HopfedEigenComplex',
						__HopfedContourComplex
					).getPerturbationSolutionFloatsTuple(
					)

			#debug
			'''
			self.debug(
				[
					('self.',self,[
						'HopfedPerturbationContourRealFloatsArray',
						'HopfedPerturbationContourImagFloatsArray'

					])
				]
			)
			'''

			#/###################/#
			# Check for Populations
			# 

			#get
			HopfedPopulationsDeriveManager=self.getTeamer(
				"Populations"
			)

			#debug
			'''
			self.debug(
				[
					'We predict network here',
					'Check for a sensor population'
				]
			)
			'''

			#/###################/#
			# Check for Agent
			# 

			#get
			LeakedAgentDeriveHopfer=HopfedPopulationsDeriveManager.getManager(
				"Agent"
			)
				
	def hopfPopulation(self):

		#Check
		if self.ManagementTagStr=='Agent':

			#/####################/#
			# Determine the relations
			#

			#set
			self.HopfedNetworkDeriveHopferVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Set properties
			#

			#set
			self.LeakingUnitsInt=self.HopfedNetworkDeriveHopferVariable.HopfingUnitsInt

			#set
			#self.LeakingGlobalBool=True

			#Check
			if self.RecordingLabelVariable==None:
				self.RecordingLabelVariable=[0,1,2]

			#set in ms
			self.LeakingTimeVariable=1000.*self.HopfedNetworkDeriveHopferVariable.HopfingConstantTimeVariable
			
			#set
			self.LeakingInteractionStr=self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'LeakingInteractionStr',
							'LeakingTimeVariable'
						])
				]
			)
			'''

			#/####################/#
			# Rate case
			#

			#Check
			if self.LeakingInteractionStr=="Rate":

				#Check
				if self.LeakingTransferVariable==None:
					
					#set
					self.LeakingTransferVariable='mV*tanh((#CurrentStr)/mV)'

			else:

				#/###############/#
				# Set the special spikes properties
				#

				#/####################/#
				# Check for Inputs
				#

				#get
				HopfedInputsDeriveHopfer=self.getTeamer(
					"Inputs"
				)

				#get
				HopfedInputsDeriveHopfer.getManager(
					"Rest"
				)

				#get
				HopfedInputsDeriveHopfer.getManager(
					"Stimulation"
				)

				#/####################/#
				# Neuron properties
				#

				#debug
				self.debug(
					[
						"We set the spikes attributes"
					]
				)

				#set
				self.LeakingThresholdVariable="#scalar:U>-50*mV"
				self.LeakingResetVariable="#scalar:U=-60*mV"
				self.LeakingRefractoryVariable=0.5
				#self.LeakingNoiseStdVariable="0.1*mV"
				#self.LeakingNoiseStdVariable=5.	

			#/####################/#
			# Check for Interactions
			#

			#Check
			if self.HopfedNetworkDeriveHopferVariable.HopfedMeanfieldWeightFloat!=0.:

				#get
				HopfedInteractionsDeriveHopfer=self.getTeamer(
					"Interactions"
				)

				#get
				HopfedInteractionsDeriveHopfer.getManager(
					"Autapse"
				)

	def hopfInteraction(self):

		#Check
		if self.ManagementTagStr=="Autapse":

			#/####################/#
			# Determine the relations
			#

			#set
			self.HopfedAgentDeriveHopferVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.HopfedNetworkDeriveHopferVariable=self.HopfedAgentDeriveHopferVariable.HopfedNetworkDeriveHopferVariable

			#/####################/#
			# Set properties
			#

			#alias
			self.LeakingWeightVariable=self.HopfedNetworkDeriveHopferVariable.HopfedLateralWeightFloatsArray

			#Check
			if self.HopfedNetworkDeriveHopferVariable.HopfingDelayTimeVariable!=0.:

				#set
				self.LeakingDelayVariable=self.HopfedNetworkDeriveHopferVariable.HopfingDelayTimeVariable

				#set in ms
				if self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr=='Rate':

					#set
					self.LeakingDelayVariable*=1000.
				
			#set
			self.LeakingInteractionStr=self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr

			#set the connect target
			self.ConnectingKeyVariable=self.HopfedAgentDeriveHopferVariable

	def hopfInput(self):

		#debug
		"""
		self.debug(
			[
				'We hopfInput here'
			]
		)
		"""

		#Check
		if self.ManagementTagStr=="Rest":

			#debug
			"""
			self.debug(
				[
					'We hopf Input Rest here'
				]
			)
			"""

			#/####################/#
			# Determine the relations
			#

			#set
			self.HopfedAgentDeriveHopferVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.HopfedNetworkDeriveHopferVariable=self.HopfedAgentDeriveHopferVariable.HopfedNetworkDeriveHopferVariable

			#/####################/#
			# Set properties
			#

			#Check
			if self.LeakingWeightVariable==None:

				#get
				#self.LeakingWeightVariable='#scalar:-70*mV'
				self.LeakingWeightVariable='#scalar:'+str(self.HopfingRestVariable)+'*mV'
				

		elif self.ManagementTagStr=="Stimulation":

			#debug
			"""
			self.debug(
				[
					'We hopf Input Stimulation here'
				]
			)
			"""

			#/####################/#
			# Determine the relations
			#

			#set
			self.HopfedAgentDeriveHopferVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.HopfedNetworkDeriveHopferVariable=self.HopfedAgentDeriveHopferVariable.HopfedNetworkDeriveHopferVariable

			#/####################/#
			# Set properties
			#

			#Check
			if self.LeakingWeightVariable==None:

				#get
				self.LeakingWeightVariable='#custom:#clock:100*ms:(0.*mV)*(t==100*ms)'
				#self.LeakingWeightVariable=0.

	def leakInteraction(self):

		#debug
		"""
		self.debug(
			[
				"We brian hopf here ",
				('self.',self,['ManagementTagStr'])
			]
		)
		"""
		
		#Check
		if self.ManagementTagStr=="Autapse" and self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr=="Rate":

			#debug
			"""
			self.debug(
				[
					"We brian hopf here "
				]
			)
			"""

			#self.Recorded
			self.LeakingRecordBool=True


		#call the base method
		BaseClass.leakInteraction(self)	


	#/######################/#
	# Augment view
	#
	
	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Print things if they are computed
			#

			#Check
			if self.HopfingDoStabilityBool:

				#map
				map(
						lambda __KeyStr:
						self.forcePrint(
							[__KeyStr],
							'HopferClass'
						)
						if getattr(
							self.PrintingCopyVariable,
							__KeyStr
						) not in [None,0.,""]
						else None,
						[
							'HopfingConstantTimeVariable',
							'HopfingDelayTimeVariable',
							'HopfingDecayTimeVariable',
							'HopfingRiseTimeVariable',
							'HopfedInstabilityStr',
							'HopfedInstabilityFrequencyFloat',
							'HopfedIsStableBool'
						]
					)

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)
	
	def mimic_view(self):

		#Check
		if self.HopfedNetworkDeriveHopferVariable==self:

			#get the Panels
			ViewedPanelsDerivePyploter=self.getTeamer(
				'Panels'
			)

			#debug
			'''
			self.debug(
				[
					'ViewedPanelsDerivePyploter is '+str(ViewedPanelsDerivePyploter)
				]
			)
			'''

			#Check
			if self.HopfedMeanfieldWeightFloat==0.:

				#del
				del ViewedPanelsDerivePyploter.ManagementDict['Eigen']

				#view
				BaseClass.view(self)

				#return
				return

			#/################/#
			# Build an Eigen Panel with Charts
			#

			#get
			ViewedChartsDerivePyploter=ViewedPanelsDerivePyploter.getManager(
				'Eigen'
			).getTeamer(
				'Charts'
			)

			#/################/#
			# Build an Eigen J Chart
			#

			#get
			ViewedConnectivityChartDerivePyploter=ViewedChartsDerivePyploter.getManager(
				'Connectivity',
				_IndexInt=0
			)

			#get
			ViewedConnectivityDrawDerivePyploter=ViewedConnectivityChartDerivePyploter.getTeamer(
				'Draws'
			).getManager(
				'Default'
			)

			#debug
			'''
			self.debug(
				[
					'self.TeamDict.keys() is ',
					str(self.TeamDict.keys())
				]
			)
			'''

			#/##################/#
			# Build the theoritical ellipse
			#

			#import
			import matplotlib.patches

			#Add the matrix contour Ellipse
			PyplotedBifurcationEllipse=matplotlib.patches.Ellipse(
								xy=(self.NumscipiedCenterFloat,0.), 
							 	width=self.NumscipiedWidthFloat,
							 	height=self.NumscipiedHeightFloat,
							 	color='r',
						)
			PyplotedBifurcationEllipse.set_alpha(0.2)

			#Add the Wiener Circle
			PyplotedBifurcationCircle=matplotlib.patches.Ellipse(
								xy=(self.NumscipiedCenterFloat,0.), 
							 	width=2.,
							 	height=2.,
							 	linewidth=2,
							 	color='black',
							 	fill=False
						)
			PyplotedBifurcationCircle.set_alpha(0.4)

			#/##################/#
			# draw
			#

			#list
			ViewedConnectivityDrawDerivePyploter.PyplotingDrawVariable=[
				(
					'plot',
					{
						'#liarg':[
							[-2.,2.],
							[0.,0.]
						],
						'#kwarg':dict(
							{
								'linestyle':"--",
								'linewidth':1,
								'color':'black'
							}
						)
					}
				),
				(
					'plot',
					{
						'#liarg':[
							[-0.,0.],
							[-2.,2.]
						],
						'#kwarg':dict(
							{
								'linestyle':"--",
								'linewidth':1,
								'color':'black'
							}
						)
					}
				),
				(
					'plot',
					{
						'#liarg':[
							[1.,1.],
							[-2.,2.]
						],
						'#kwarg':dict(
							{
								'linestyle':"-",
								'linewidth':2,
								'color':'black',
								'alpha':0.5
							}
						)
					}
				),
				(
					'add_artist',
					PyplotedBifurcationEllipse
				),
				(
					'add_artist',
					PyplotedBifurcationCircle
				),
				(
					'plot',
					{
						'#liarg':[
							np.real(self.HopfedLateralContourComplexesArray),
							np.imag(self.HopfedLateralContourComplexesArray)
						],
						'#kwarg':dict(
							{
								'linestyle':"-",
								'color':'red',
								'linewidth':5
							}
						)
					}
				),
				(
					'plot',
					{
						'#liarg':[
							self.HopfedRealLateralEigenFloatsArray,
							self.HopfedImagLateralEigenFloatsArray
						],
						'#kwarg':dict(
							{
								'linestyle':"",
								'marker':'o',
								'color':'black'
							}
						)
					}
				)
			]
			
			#/##################/#
			# View chart
			#

			#concatenate
			ViewedVariablesArray=np.concatenate(
				[
					self.HopfedRealLateralEigenFloatsArray,
					self.HopfedImagLateralEigenFloatsArray
				]
			)
			ViewedMinFloat=ViewedVariablesArray.min()
			ViewedMaxFloat=max(ViewedVariablesArray.max(),1.)
			ViewedLimFloatsArray=[ViewedMinFloat,ViewedMaxFloat]

			#view
			ViewedConnectivityChartDerivePyploter.view(
				_XLabelStr="$Re(\lambda_{J})$",
				_YLabelStr="$Im(\lambda_{J})$",
				_XVariable=ViewedLimFloatsArray,
				_YVariable=ViewedLimFloatsArray
			)

			#/################/#
			# Build an Eigen Perturb Chart
			#

			#get
			ViewedPerturbationChartDerivePyploter=ViewedChartsDerivePyploter.getManager(
				'Perturbation'
			)

			#get
			ViewedPerturbationDrawDerivePyploter=ViewedPerturbationChartDerivePyploter.getTeamer(
				'Draws'
			).getManager(
				'Default'
			)


			#/##################/#
			# Think already on the max
			#

			#concatenate
			ViewedVariablesArray=np.concatenate(
				[
					self.HopfedPerturbationContourRealFloatsArray,
					self.HopfedPerturbationContourImagFloatsArray
				]
			)
			ViewedMinFloat=ViewedVariablesArray.min()
			ViewedMaxFloat=ViewedVariablesArray.max()
			ViewedLimFloatsArray=[ViewedMinFloat,ViewedMaxFloat]

			#/##################/#
			# draw
			#

			#list
			ViewedPerturbationDrawDerivePyploter.PyplotingDrawVariable=[
				(
					'plot',
					{
						'#liarg':[
							ViewedLimFloatsArray,
							[0.,0.]
						],
						'#kwarg':dict(
							{
								'linestyle':"--",
								'linewidth':1,
								'color':'black'
							}
						)
					}
				),
				(
					'plot',
					{
						'#liarg':[
							[-0.,0.],
							ViewedLimFloatsArray
						],
						'#kwarg':dict(
							{
								'linestyle':"--",
								'linewidth':1,
								'color':'black'
							}
						)
					}
				),
				(
					'plot',
					{
						'#liarg':[
							self.HopfedPerturbationContourRealFloatsArray,
							self.HopfedPerturbationContourImagFloatsArray
						],
						'#kwarg':dict(
							{
								'linestyle':"-",
								'linewidth':3,
								'color':'red'
							}
						)
					}
				),
				(
					'plot',
					{
						'#liarg':[
							self.HopfedPerturbationRealFloatsArray,
							self.HopfedPerturbationImagFloatsArray
						],
						'#kwarg':dict(
							{
								'linestyle':"",
								'marker':"o",
								'color':'black'
							}
						)
					}
				)
			]

			#/##################/#
			# view chart
			#

			

			#view
			ViewedPerturbationChartDerivePyploter.view(
				_XLabelStr="$Re(\lambda_{P})$",
				_YLabelStr="$Im(\lambda_{P})$",
				_XVariable=ViewedLimFloatsArray,
				_YVariable=ViewedLimFloatsArray
			)
			
			#/################/#
			# Prepare a Run Panel
			#

			#Check
			if 'Populations' in self.TeamDict:

				#debug
				'''
				self.debug(
					[
						'We put the Run on the right'
					]
				)
				'''

				#get
				ViewedRunDerivePyploter=ViewedPanelsDerivePyploter.getManager(
						'Run'
					)
				#ViewedRunDerivePyploter.PyplotingShiftVariable=[0,3]

		#/###############/#
		# Call the base method
		#

		#debug
		'''
		self.debug(
			[
				'self.TeamDict.keys() is ',
				str(self.TeamDict.keys()),
				'BaseClass.view is ',
				str(BaseClass.view)
			]
		)
		'''

		#view
		BaseClass.view(self)

		#debug
		'''
		self.debug(
			[
				'self.TeamDict.keys() is ',
				str(self.TeamDict.keys())
			]
		)
		'''

	#/#################/#
	# Other functions
	#

	def getUniqueDelayPerturbationRootFloatsTuple(self,_PerturbationFloatsTuple):
			
		#set
		ConstantTimeVariable=1000.*self.HopfingConstantTimeVariable
		DelayTimeVariable=1000.*self.HopfingDelayTimeVariable

		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationFloatsTuple

		#compute
		#PrefixComplex=(1./self.HopfedMeanfieldWeightFloat)*np.exp(
		#		PerturbationRealFloat*DelayTimeVariable
		#	)
		PrefixComplex=np.exp(
				PerturbationRealFloat*DelayTimeVariable
			)

		#compute
		CosFloat=np.cos(PerturbationImagFloat*DelayTimeVariable)
		SinFloat=np.sin(PerturbationImagFloat*DelayTimeVariable)

		#compute
		NeuralFloat=(1.+ConstantTimeVariable*PerturbationRealFloat)

		#compute
		FirstRootFloat = PrefixComplex*(
			NeuralFloat*CosFloat-ConstantTimeVariable*PerturbationImagFloat*SinFloat
		)-self.HopfedEigenComplex.real

		#compute
		SecondRootFloat = PrefixComplex*(
			ConstantTimeVariable*PerturbationImagFloat*CosFloat+NeuralFloat*SinFloat
		)-self.HopfedEigenComplex.imag
		
		#return
		return (FirstRootFloat,SecondRootFloat)

	def getPerturbationSolutionFloatsTuple(self):

		#import
		import scipy.optimize

		#return
		return scipy.optimize.fsolve(
			self.getUniqueDelayPerturbationRootFloatsTuple, 
			(0,0)
		)


#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=HopferClass
#<DefineLocals>

#</DefinePrint>
HopferClass.PrintingClassSkipKeyStrsList.extend(
	[
		'HopfingUnitsInt',
		'HopfingLateralWeightVariable',
		'HopfingConstantTimeVariable',
		'HopfingMeanWeightFloat',
		'HopfingStdWeightFloat',
		'HopfingSparseWeightFloat',
		'HopfingSwitchWeightFloat',
		'HopfingNormalisationInt',
		'HopfingSymmetryFloat',
		'HopfingPerturbationEnvelopBool',
		'HopfingDoStationaryBool',
		'HopfingDoStabilityBool',
		'HopfingDoTransferBool',
		'HopfingContourSamplesInt',
		'HopfingInteractionStr',
		'HopfingRestVariable',
		'HopfedLateralWeightFloatsArray',
		'HopfedHalfHeightFloat',
		'HopfedLateralHalfWidthFloat',
		'HopfedMeanfieldWeightFloat',
		'HopfedRealLateralEigenFloatsArray',
		'HopfedImagLateralEigenFloatsArray',
		'HopfedLateralContourComplexesArray',
		'HopfedEigenComplex',
		'HopfedEigenvalueComplexesArray',
		'HopfedPerturbationComplex',
		'HopfedPerturbationRealFloatsArray',
		'HopfedPerturbationImagFloatsArray',
		'HopfedPerturbationContourRealFloatsArray',
		'HopfedPerturbationContourImagFloatsArray',
		'HopfedInstabilityIndexInt',
		'HopfedInstabilityIndexInt',
		'HopfedInstabilityComplex',
		'HopfedInstablesInt',
		'HopfedIsStableBool',
		'HopfedInstabilityStr',
		'HopfedStdSparseFloat',
		'HopfedParentSingularStr',
		'HopfedIndexIntsTuplesList',
		'HopfedPerturbationNullVariable',
		'HopfedPerturbationWeightFloatsArray',
		'HopfedConstantTimeVariable',
		'HopfedPerturbationComplex',
		'HopfedNeuralPerturbationComplex',
		'HopfedSynapticPerturbationComplexesArray',
		'HopfedSynapticPerturbationMethodVariable',
		'HopfedNeuralPerturbationMethodVariable',
		'HopfedTotalPerturbationComplexesArray',
		'HopfedFlatTotalPerturbationComplexesArray',
		'HopfedInstabilityLambdaFloatsTuple',
		'HopfedInstabilityFrequencyFloat',
		'HopfedOptimizeRoot',
		'HopfedAgentDeriveHopferVariable',
		'HopfedNetworkDeriveHopferVariable'
	]
)
#<DefinePrint>