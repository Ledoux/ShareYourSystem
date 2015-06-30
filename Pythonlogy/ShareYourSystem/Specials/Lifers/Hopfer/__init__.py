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
BaseModuleStr="ShareYourSystem.Specials.Lifers.Stationarizer"
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
			_HopfingStationaryRateFloat=30.,
			_HopfingExternalNoiseFloat=0.,
			_HopfedLateralWeightFloatsArray = None,
			_HopfedInstabilityComplexesArray =  None,
			_HopfedMeanfieldWeightFloat=0.,
			_HopfedEigenComplex=None,
			_HopfedPerturbationNullFloatsArray = None,
			_HopfedPerturbationComplexesArray = None,
			_HopfedPerturbationRealFloatsArray = None,
			_HopfedPerturbationImagFloatsArray = None,
			_HopfedContourPerturbationComplexesArray = None,
			_HopfedContourPerturbationRealFloatsArray = None,
			_HopfedContourPerturbationImagFloatsArray = None,
			_HopfedSolutionComplexesArray = None,
			_HopfedSolutionRealFloatsArray = None,
			_HopfedSolutionImagFloatsArray = None,
			_HopfedContourSolutionComplexesArray=None,
			_HopfedContourSolutionRealFloatsArray = None,
			_HopfedContourSolutionImagFloatsArray = None,
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
			_HopfedStationaryExternalCurrentFloat=0.,
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

		#set
		self.StationarizingPopulationTagVariable=["Agent"]

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
				'We hopf network here',
				'Check for an Agent population'
			]
		)
		'''

		#/###################/#
		# Check for Agent
		# 

		#get
		self.HopfedAgentDeriveHopferVariable=HopfedPopulationsDeriveManager.getManager(
			self.StationarizingPopulationTagVariable[0]
		)
			
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

			#import
			import numpy as np

			#numscipy
			self.NumscipyingRowsInt=self.HopfingUnitsInt
			self.NumscipyingColsInt=self.HopfingUnitsInt
			self.NumscipyingStdFloat=self.HopfingStdWeightFloat/np.sqrt(
					self.HopfingUnitsInt
				)
			self.NumscipyingMeanFloat=self.HopfingMeanWeightFloat/self.HopfingUnitsInt
			self.NumscipyingSymmetryFloat=self.HopfingSymmetryFloat
			self.NumscipyingEigenvalueBool=False
			self.NumscipyingMeanForceStr="rows"
			self.NumscipyingSparseFloat=self.HopfingSparseWeightFloat
			self.NumscipyingSwitchFloat=self.HopfingSwitchWeightFloat

			#numscipy
			self.numscipy(
				)

			#alias
			if self.HopfingInteractionStr=="Rate":
				self.HopfedLateralWeightFloatsArray = self.HopfingConstantTimeVariable*self.NumscipiedValueFloatsArray
			else:
				self.HopfedLateralWeightFloatsArray = 1.*self.NumscipiedValueFloatsArray

			#debug
			'''
			self.debug(
				[
					"Ok the Js are ",
					('self.',self,[
							'HopfedLateralWeightFloatsArray'
						])
				]
			)
			'''

			#Check
			if self.HopfingInteractionStr=="Spike":

				#debug
				'''
				self.debug(
					[
						"We have to modify the matrix G",
						"First we compute the stationary solution"
					]
				)	
				'''

				#/###################/#
				# Determine the stationary solutions
				# 

				#set
				self.HopfedInternalNoiseFloat=np.sqrt(
					self.HopfingStationaryRateFloat*self.HopfingConstantTimeVariable
				)*self.NumscipyingStdFloat

				#set
				self.HopfedTotalNoiseFloat=np.sqrt(
					self.HopfedInternalNoiseFloat**2 + self.HopfingExternalNoiseFloat**2
				)
				
				#debug
				self.debug(
					[
						"We compute the stationary rest external current",
						('self.',self,[
								'HopfingStationaryRateFloat',
								'HopfedInternalNoiseFloat',
								'HopfingExternalNoiseFloat',
								'HopfedTotalNoiseFloat'
							])
					]
				)

				#stationarize
				self.stationarize(
					_RateVariable=[self.HopfingStationaryRateFloat],
					_ConstantTimeVariable=[self.HopfingConstantTimeVariable],
					_NoiseVariable=[self.HopfedTotalNoiseFloat],
					_InteractionStr="Spike"
				)

				#set
				self.HopfedStationaryExternalCurrentFloat = self.HopfedAgentDeriveHopferVariable.LifedStationaryCurrentFloat+self.HopfingConstantTimeVariable*self.HopfingUnitsInt*self.HopfingMeanWeightFloat*self.HopfingStationaryRateFloat

				#debug
				'''
				self.debug(
					[
						"We have computed the rest external current",
						"self.HopfedAgentDeriveHopferVariable.LifedStationaryCurrentFloat is "+str(
							self.HopfedAgentDeriveHopferVariable.LifedStationaryCurrentFloat),
						('self.',self,[
								"HopfedStationaryExternalCurrentFloat"
							]
						)
					]
				)
				'''

				#/###################/#
				# Determine the null perturbations
				# 

				#debug
				'''
				self.debug(
					[
						"We compute then the null perturbation ",
					]
				)
				'''

				#lif
				self.HopfedAgentDeriveHopferVariable.lif(
					_PerturbationLambdaVariable=0.,
					_ComputeNoisePerturbationBool=True
				)

				#debug
				'''
				self.debug(
					[
						"We have lifed",
						('self.',self,[
								'LifedPerturbationMeanNullFloat',
								'LifedPerturbationStdNullFloat',
							])
					]
				)
				'''

				#set
				self.HopfedPerturbationNullFloatsArray = self.HopfingConstantTimeVariable*self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanNullFloat*self.HopfedLateralWeightFloatsArray[:,:]
				#self.HopfedPerturbationNullFloatsArray+=(
				#	self.HopfedAgentDeriveHopferVariable.LifedPerturbationNoiseNullFloat/(
				#	2.*self.HopfedAgentDeriveHopferVariable.LifingNoiseFloat
				#)
				#)*(self.HopfedLateralWeightFloatsArray**2)
				
			else:

				#set
				self.HopfedPerturbationNullFloatsArray = self.HopfedLateralWeightFloatsArray[:,:]

			#/##############/#
			# Compute the eigenvalues for the lateral and the null perturb matrix
			#
		
			#import
			import numpy as np

			#eigenvalues
			self.HopfedPerturbationComplexesArray = np.linalg.eigvals(
				self.HopfedPerturbationNullFloatsArray
			)

			#debug
			'''
			self.debug(
				[
					"We have computed the eigenvalues",
					('self.',self,[
							'HopfedLateralEigenvalueComplexesArray',
							'HopfedPerturbationComplexesArray',
						])
				]
			)
			'''

			#/##############/#
			# Look the shape of the meanfield
			#

			#else:
			#	#alias
			#	self.HopfedLateralEigenvalueComplexesArray = self.NumscipiedEigenvalueComplexesArray

			
			#set
			self.HopfedMeanfieldWeightFloat = self.HopfingStdWeightFloat if self.HopfingStdWeightFloat>0. else self.HopfingMeanWeightFloat

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
			self.HopfedPerturbationRealFloatsArray=np.real(
				self.HopfedPerturbationComplexesArray
			)
			self.HopfedPerturbationImagFloatsArray=np.imag(
				self.HopfedPerturbationComplexesArray
			)

			#debug
			'''
			self.debug(
				[
					'We have built the real and imag',
					('self.',self,[
							'HopfedRealLateralEigenFloatsArray',
							'HopfedImagLateralEigenFloatsArray',
							'HopfedPerturbationRealFloatsArray',
							'HopfedPerturbationImagFloatsArray'
						])
				]
			)
			'''

			#/###############/#
			# Compute for each eigenvalues of J a possible solution
			#

			#Check
			if self.HopfingPerturbationEnvelopBool:

				#set
				if self.HopfingInteractionStr == "Rate":
					self.HopfedInstabilityComplexesArray = 1. * self.HopfedLateralWeightFloatsArray
				else:
					self.HopfedInstabilityComplexesArray = self.HopfingConstantTimeVariable * self.HopfedLateralWeightFloatsArray

				#import
				import scipy.optimize
				self.optimize=scipy.optimize

				#map
				HopfedSolutionFloatsTuplesList=SYS.filterNone(
					map(
						lambda __OptimizeRoot:
						__OptimizeRoot.x
						if __OptimizeRoot.success and np.sum(__OptimizeRoot.fun**2)<0.001
						else None,
						map(
							lambda __HopfedPerturbationComplex:
							self.setAttr(
								'HopfedEigenComplex',
								__HopfedPerturbationComplex
							).optimize.root(
								getattr(
									self,
									'get'+self.HopfingInteractionStr+'PerturbationSolutionFloatsTuple'
								), 
								(-1.,2.*np.pi*100.)
							),
							#self.HopfedPerturbationComplexesArray
							np.linalg.eigvals(
								self.HopfedInstabilityComplexesArray
							)
						)
					)
				)

				#debug
				self.debug(
					[
						"HopfedSolutionFloatsTuplesList is "+str(HopfedSolutionFloatsTuplesList)
					]
				)

					
			#unpack
			[
				HopfedSolutionRealFloatsTuple,
				HopfedSolutionImagFloatsTuple
			]=SYS.unzip(
				HopfedSolutionFloatsTuplesList,
				[0,1]
			)
			self.HopfedSolutionRealFloatsArray=np.array(
				HopfedSolutionRealFloatsTuple
			)
			self.HopfedSolutionImagFloatsArray=np.array(
				HopfedSolutionImagFloatsTuple
			)
			
			#/###############/#
			# Build the contour of the ellipse J eigen values real and ima
			#

			#debug
			'''
			self.debug(
				[
					"We build the contours",
					('self.',self,[
							'HopfingConstantTimeVariable',
							'NumscipiedSommersFloat',
							'NumscipyingStdFloat'
						])
				]
			)
			'''

			#set
			HopfedSommerFloat=self.NumscipiedSommersFloat

			#list
			self.HopfedContourPerturbationComplexesArray=[
				__Float + (
					1.-HopfedSommerFloat
				)*np.sqrt(
					1.-(__Float/(1.+HopfedSommerFloat))**2
				)*1j for __Float in np.linspace(
					-1.-HopfedSommerFloat,
					1.+HopfedSommerFloat,
					self.HopfingContourSamplesInt
				)
			]

			#list
			self.HopfedContourPerturbationComplexesArray+=list(
				np.array(
					self.HopfedContourPerturbationComplexesArray
				).conjugate()[::-1]  
			)

			#array
			self.HopfedContourPerturbationComplexesArray=np.array(
				self.HopfedContourPerturbationComplexesArray
			)

			#debug
			self.debug(
				[
					"We normalize the contour with the sdt",
					('self.',self,[
							'NumscipyingStdFloat',
							'HopfingStdWeightFloat'
						])
				]
			)

			#Check
			if self.HopfingStdWeightFloat>0.:

				#set
				self.HopfedContourPerturbationComplexesArray *= self.HopfingStdWeightFloat

			else:

				#sqrt
				self.HopfedStdSparseFloat=np.sqrt(
					self.NumscipyingSparseFloat*(1.-self.NumscipyingSparseFloat)
				)
				
				#set
				self.HopfedContourPerturbationComplexesArray *= self.HopfedStdSparseFloat

			
			#Check
			if self.HopfingInteractionStr == "Rate":

				#set
				self.HopfedContourPerturbationComplexesArray *= self.HopfingConstantTimeVariable
				
			else:

				#set
				self.HopfedContourPerturbationComplexesArray *= self.HopfingConstantTimeVariable*self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanNullFloat
				
			#real and imag
			self.HopfedContourPerturbationRealFloatsArray=np.real(
				self.HopfedContourPerturbationComplexesArray
			)
			self.HopfedContourPerturbationImagFloatsArray=np.imag(
				self.HopfedContourPerturbationComplexesArray
			)    

			#/###############/#
			# Compute for each eigen of the contour a possible solution
			#

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'HopfingPerturbationEnvelopBool'
						])
				]
			)
			'''

			#Check
			if self.HopfingPerturbationEnvelopBool:

				#Check
				if self.HopfingInteractionStr == "Spike":
					HopfedContourInstabilityArray = self.HopfedContourPerturbationComplexesArray/self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanNullFloat
				else:
					HopfedContourInstabilityArray = self.HopfedContourPerturbationComplexesArray

				#map
				HopfedContourSolutionFloatsTuplesList=SYS.filterNone(
					map(
						lambda __OptimizeRoot:
						__OptimizeRoot.x
						if __OptimizeRoot.success and np.sum(__OptimizeRoot.fun**2)<0.001
						else None,
						map(
							lambda __HopfedContourComplex:
							self.setAttr(
								'HopfedEigenComplex',
								__HopfedContourComplex
							).optimize.root(
									getattr(
										self,
										'get'+self.HopfingInteractionStr+'PerturbationSolutionFloatsTuple'
									), 
									(-0.1,2.*np.pi*10.)
								),
							HopfedContourInstabilityArray
							#[:2]
						)
					)
				)
				

				"""
				#map
				HopfedContourSolutionFloatsTuplesList=map(
					lambda __HopfedLateralEigenvalueComplex:
					self.optimize.fsolve(
						self.getRatePerturbationSolutionFloatsTuple, 
						(
							__HopfedLateralEigenvalueComplex.real,
							__HopfedLateralEigenvalueComplex.imag	
						)
					),
					self.HopfedContourPerturbationComplexesArray
				)
				"""

				#unpack
				[
					HopfedContourSolutionRealFloatsTuple,
					HopfedContourSolutionImagFloatsTuple
				]=SYS.unzip(
					HopfedContourSolutionFloatsTuplesList,
					[0,1]
				)
				self.HopfedContourSolutionRealFloatsArray=np.array(HopfedContourSolutionRealFloatsTuple)
				self.HopfedContourSolutionImagFloatsArray=np.array(HopfedContourSolutionImagFloatsTuple)
				
				#debug
				"""
				self.debug(
					[
						('self.',self,[
								'HopfingDoStabilityBool',
								'HopfedSolutionRealFloatsArray',
							])
					]
				)
				"""

				#get
				self.HopfedInstabilityIndexInt = np.argmax(
					self.HopfedSolutionRealFloatsArray
				)

				#find
				InstableEigenIndexIntsArray=np.where(
					self.HopfedSolutionRealFloatsArray>0.
				)[0]
			
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
				self.HopfedInstabilityComplex=self.HopfedSolutionRealFloatsArray[
					self.HopfedInstabilityIndexInt
				]

				#set
				self.HopfedIsStableBool=self.HopfedSolutionRealFloatsArray[
					self.HopfedInstabilityIndexInt
				]<0.

				#Check
				if self.HopfedIsStableBool==False:

					#set
					self.HopfedInstabilityStr='Rate' if self.HopfedSolutionImagFloatsArray[
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
				for __HopfedContourComplex in self.HopfedContourPerturbationComplexesArray:

					#set
					self.setAttr(
						'HopfedEigenComplex',
						__HopfedContourComplex
					).getRatePerturbationSolutionFloatsTuple(
					)

			#debug
			'''
			self.debug(
				[
					('self.',self,[
						'HopfedContourPerturbationRealFloatsArray',
						'HopfedContourPerturbationImagFloatsArray'

					])
				]
			)
			'''

				
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

				#/####################/#
				# Check for Inputs
				#

				#debug
				self.debug(
					[
						"We check the external constant input to set in order to have the good rate",
						('self.',self,[
								"LifingStationaryRateFloat",
								"LifedStationaryCurrentFloat"
							])
					]
				)

				#get
				HopfedInputsDeriveHopfer=self.getTeamer(
					"Inputs"
				)

				#get
				HopfedInputsDeriveHopfer.getManager(
					"Rest"
				)

				#get
				#HopfedInputsDeriveHopfer.getManager(
				#	"Stimulation"
				#)

				#/####################/#
				# Neuron properties
				#

				#debug
				'''
				self.debug(
					[
						"We set the spikes attributes"
					]
				)
				'''

				#set
				self.LeakingThresholdVariable="#scalar:U>"+str(self.LifingThresholdFloat)+"*mV"
				self.LeakingResetVariable="#scalar:U="+str(self.LifingResetFloat)+"*mV"
				self.LeakingRefractoryVariable=0.5

				#Check
				if self.HopfedNetworkDeriveHopferVariable.HopfingExternalNoiseFloat>0.:

					#debug
					self.debug(
						[
							"We add external noise"
						]
					)

					#set
					self.LeakingNoiseStdVariable=self.HopfedNetworkDeriveHopferVariable.HopfingExternalNoiseFloat

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
			self.LeakingWeightVariable=self.HopfedNetworkDeriveHopferVariable.HopfedLateralWeightFloatsArray[:]

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

				#debug
				self.debug(
					[
						"We set the external+rest current",
						"self.HopfedNetworkDeriveHopferVariable.HopfedStationaryExternalCurrentFloat is "+str(
							self.HopfedNetworkDeriveHopferVariable.HopfedStationaryExternalCurrentFloat
						)
					]
				)

				#get
				#self.LeakingWeightVariable='#scalar:-70*mV'
				self.LeakingWeightVariable='#scalar:'+str(
					self.HopfedNetworkDeriveHopferVariable.HopfedStationaryExternalCurrentFloat
				)+'*mV'
				

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

			#set
			HopfedCenterFloat = self.HopfingConstantTimeVariable*self.HopfingUnitsInt*self.NumscipiedCenterFloat
			HopfedWidthFloat = self.HopfingConstantTimeVariable*np.sqrt(
				self.HopfingUnitsInt
			)*self.NumscipiedWidthFloat
			HopfedHeightFloat = self.HopfingConstantTimeVariable*np.sqrt(
				self.HopfingUnitsInt
			)*self.NumscipiedHeightFloat

			#Check
			if self.HopfingInteractionStr == "Spike":
				HopfedWidthFloat *= self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanNullFloat
				HopfedHeightFloat *= self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanNullFloat
				
			#Add the matrix contour Ellipse
			PyplotedBifurcationEllipse=matplotlib.patches.Ellipse(
				xy=(HopfedCenterFloat,0.), 
			 	width=HopfedWidthFloat,
			 	height=HopfedHeightFloat,
			 	color='r'
			)
			PyplotedBifurcationEllipse.set_alpha(0.2)

			#Add the Wiener Circle
			PyplotedBifurcationCircle=matplotlib.patches.Ellipse(
				xy=(0.,0.), 
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
							self.HopfedContourPerturbationRealFloatsArray,
							self.HopfedContourPerturbationImagFloatsArray
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
							self.HopfedPerturbationRealFloatsArray,
							self.HopfedPerturbationImagFloatsArray
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
				#[
				#	self.HopfedContourPerturbationRealFloatsArray,
				#	self.HopfedContourPerturbationImagFloatsArray
				#]
				[
					self.HopfedPerturbationRealFloatsArray,
					self.HopfedPerturbationImagFloatsArray
				]
			)
			ViewedMinFloat=ViewedVariablesArray.min()
			ViewedMaxFloat=max(ViewedVariablesArray.max(),1.25)
			ViewedLimFloatsArray=[ViewedMinFloat,ViewedMaxFloat]

			#view
			ViewedConnectivityChartDerivePyploter.view(
				_XLabelStr="$Re(\lambda_{G})$",
				_YLabelStr="$Im(\lambda_{G})$",
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
				#[
				#	self.HopfedContourSolutionRealFloatsArray,
				#	self.HopfedContourSolutionImagFloatsArray
				#]
				[
					self.HopfedSolutionRealFloatsArray,
					self.HopfedSolutionImagFloatsArray
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
							self.HopfedContourSolutionRealFloatsArray,
							self.HopfedContourSolutionImagFloatsArray
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
							self.HopfedSolutionRealFloatsArray,
							self.HopfedSolutionImagFloatsArray
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
			if self.HopfedNetworkDeriveHopferVariable==self:

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
							'HopfedIsStableBool'
						]
					)

			else:

				#/##################/#
				# Call the base method
				#


				#call
				BaseClass._print(self,**_KwargVariablesDict)

				#return
				return 

		#/##################/#
		# Call the base method
		#

		#call
		Leaker.LeakerClass._print(self,**_KwargVariablesDict)

	#/#################/#
	# Other functions
	#

	def getInverseSynapticComplex(self,_PerturbationComplex):

		return np.exp(
					_PerturbationComplex*self.HopfingDelayTimeVariable
				)

	def getRatePerturbationSolutionFloatsTuple(self,_PerturbationFloatsTuple):
	
		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationFloatsTuple

		#set
		PerturbationComplex = PerturbationRealFloat+1j*PerturbationImagFloat

		#set
		CurrentComplex = (
			(
				1.+PerturbationComplex*self.HopfingConstantTimeVariable
			)*self.getInverseSynapticComplex(
				PerturbationComplex
			)
		) - self.HopfedEigenComplex

		#return
		return (CurrentComplex.real,CurrentComplex.imag)

	def getSpikePerturbationSolutionFloatsTuple(self,_PerturbationFloatsTuple):
	
		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationFloatsTuple

		#set
		PerturbationComplex = PerturbationRealFloat+1j*PerturbationImagFloat

		'''
		#lif
		self.HopfedAgentDeriveHopferVariable.lif(
			_PerturbationLambdaVariable = PerturbationComplex,
			_ComputeStationaryBool = False,
			_PerturbationMethodStr = "Rate"
		)

		#append
		SYS.TempList.append([
			PerturbationComplex,
			self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanComplexVariable,
			0
		])
		'''

		#lif
		self.HopfedAgentDeriveHopferVariable.lif(
			_PerturbationLambdaVariable = PerturbationComplex,
			_ComputeStationaryBool = False,
			#_PerturbationMethodStr = "Brunel"
			#_PerturbationMethodStr = "Hakim"
			_PerturbationMethodStr = "Rate"
		)

		'''
		#set
		SYS.TempList[-1][-1]=self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanComplexVariable
		'''

		#debug
		'''
		self.debug(
			[
				"PerturbationComplex is "+str(PerturbationComplex),
				"self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanComplexVariable is "+str(
					self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanComplexVariable),
				"SYS.TempList[-1] is "+str(SYS.TempList[-1])
			]
		)
		'''

		#Check
		if self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanComplexVariable==0.:
			self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanComplexVariable=0.000000001*1j

		#set
		CurrentComplex = (
			self.getInverseSynapticComplex(
				PerturbationComplex
			)*(
				1./self.HopfedAgentDeriveHopferVariable.LifedPerturbationMeanComplexVariable
			)
		) - self.HopfedEigenComplex



		#Check
		'''
		if PerturbationComplex.real < -100. or PerturbationComplex.imag > 500.*(2.*np.pi) or PerturbationComplex.imag < -500.*(2.*np.pi):

			#debug
			#self.debug(
			#	[
			#		"HAaaaa",
			#		"PerturbationComplex is "+str(PerturbationComplex)
			#	]
			#)

			#return
			return (CurrentComplex.real+10000000000.,CurrentComplex.imag+10000000000.)
		'''

		#return
		return (CurrentComplex.real,CurrentComplex.imag)
	
	"""
	def getRatePerturbationSolutionFloatsTuple(self,_PerturbationFloatsTuple):

		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationFloatsTuple

		#set
		PerturbationComplex = PerturbationRealFloat+1j*PerturbationImagFloat

		#lif
		#self.lif(
		#	_PerturbationLambdaVariable=PerturbationRealFloat+1j*PerturbationImagFloat
		#)

		#set
		PerturbationArray = - np.exp(
					-PerturbationComplex*self.HopfingDelayTimeVariable
				)*self.HopfingConstantTimeVariable*self.HopfedLateralWeightFloatsArray

		#debug
		'''
		self.debug(
			[
				"np.diag(PerturbationArray) is "+str(np.diag(PerturbationArray))
			]
		)
		'''

		#fill
		np.fill_diagonal(
			PerturbationArray,
			(1.+PerturbationComplex*self.HopfingConstantTimeVariable) + np.diag(
				PerturbationArray
			)
		)
		
		#exp
		DeterminantComplex = np.linalg.det(
			PerturbationArray
		)

		#exp
		#DeterminantComplex = np.linalg.det(
		#	self.HopfingConstantTimeVariable*self.HopfedLateralWeightFloatsArray
		#)

		#debug
		'''
		self.debug(
			[
				"PerturbationComplex is "+str(PerturbationComplex),
				"DeterminantComplex is "+str(DeterminantComplex)
			]
		)
		'''

		#return
		return (DeterminantComplex.real,DeterminantComplex.imag)
	"""	
	

	"""
	def getSpikePerturbationSolutionFloatsTuple(self,_PerturbationFloatsTuple):

		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationFloatsTuple

		#

		#lif
		self.lif(
			_PerturbationLambdaVariable=PerturbationRealFloat+1j*PerturbationImagFloat
		)

		#
		self.LifedPerturbationMeanComplex*self.HopfedLateralWeightFloatsArray[self.HopfedUnitInt,:]
	"""	


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
		'HopfingDelayTimeVariable',
		'HopfingMeanWeightFloat',
		'HopfingStdWeightFloat',
		'HopfingSparseWeightFloat',
		'HopfingSwitchWeightFloat',
		'HopfingNormalisationInt',
		'HopfingSymmetryFloat',
		'HopfingPerturbationEnvelopBool',
		'HopfingContourSamplesInt',
		'HopfingInteractionStr',
		'HopfingStationaryRateFloat',
		'HopfedLateralWeightFloatsArray',
		'HopfedInstabilityComplexesArray',
		'HopfedMeanfieldWeightFloat',
		'HopfedEigenComplex',
		'HopfedPerturbationNullFloatsArray',
		'HopfedPerturbationComplexesArray',
		'HopfedPerturbationRealFloatsArray',
		'HopfedPerturbationImagFloatsArray',
		'HopfedContourPerturbationComplexesArray',
		'HopfedContourPerturbationRealFloatsArray',
		'HopfedContourPerturbationImagFloatsArray',
		'HopfedSolutionComplexesArray',
		'HopfedSolutionRealFloatsArray',
		'HopfedSolutionImagFloatsArray',
		'HopfedContourSolutionComplexesArray',
		'HopfedContourSolutionRealFloatsArray',
		'HopfedContourSolutionImagFloatsArray',
		'HopfedInstabilityIndexInt',
		'HopfedInstabilityIndexInt',
		'HopfedInstabilityComplex',
		'HopfedInstablesInt',
		'HopfedIsStableBool',
		'HopfedInstabilityStr',
		'HopfedStdSparseFloat',
		'HopfedIndexIntsTuplesList',
		'HopfedPerturbationComplex',
		'HopfedInstabilityFrequencyFloat',
		'HopfedStationaryExternalCurrentFloat',
		'HopfedParentSingularStr',
		'HopfedAgentDeriveHopferVariable',
		'HopfedNetworkDeriveHopferVariable'
	]
)
#<DefinePrint>