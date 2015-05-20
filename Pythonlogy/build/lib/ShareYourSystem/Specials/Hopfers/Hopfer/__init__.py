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
BaseModuleStr="ShareYourSystem.Standards.Recorders.Leaker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Hopfer','Hopf','Hopfing','Hopfed')
#</DefineAugmentation>

#<ImportSpecificModules>
Leaker=BaseModule
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
			_HopfingLateralWeigthVariable = None,
			_HopfingConstantTimeVariable = 10.0,
			_HopfingDelayTimeVariable = 2.0,
			_HopfingDecayTimeVariable = 0.,
			_HopfingRiseTimeVariable = 0.,
			_HopfingMeanWeightFloat = 0.0,
			_HopfingStdWeightFloat = 1.0,
			_HopfingSparseWeigthFloat=0.,
			_HopfingSwitchWeigthFloat=0.5,
			_HopfingNormalisationInt= 0.5,
			_HopfingSymmetryFloat = 0.0,
			_HopfingPerturbationEnvelopBool=True,
			_HopfingDoStationaryBool=False,
			_HopfingDoStabilityBool=False,
			_HopfingContourSamplesInt=50,
			_HopfingInteractionStr="Rate",
			_HopfedLateralWeigthFloatsArray=None,
			_HopfedMeanfieldWeigthFloat=0.,
			_HopfedRealLateralEigenFloatsArray = None,
			_HopfedImagLateralEigenFloatsArray = None,
			_HopfedHalfHeightFloat=0.,
			_HopfedLateralHalfWidthFloat=0., 
			_HopfedLateralContourComplexesArray=None,
			_HopfedEigenComplex=None,
			_HopfedPerturbationContourRealFloatsArray = None,
			_HopfedPerturbationContourImagFloatsArray = None,
			_HopfedInstabilityIndexInt=-1,
			_HopfedInstabilityContourIndexInt=-1,
			_HopfedInstabilityContourComplex=None,
			_HopfedIsStableBool=True,
			_HopfedInstabilityStr="",
			_HopfedStdSparseFloat=0.,
			_HopfedParentSingularStr="",
			_HopfedConstantTimeFloatsArray=None,
			_HopfedDelayTimeFloatsArray=None,
			_HopfedNeuralPerturbationComplexesArray=None,
			_HopfedSynapticPerturbationComplexesArray=None,
			_HopfedTotalPerturbationComplexesArray=None,
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
		HopfedLateralType=type(self.HopfingLateralWeigthVariable)

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
			self.NumscipyingEigenvalueBool=True
			self.NumscipyingNormalisationFunction=lambda __ColsInt:__ColsInt**0.5

			#Check
			#if self.HopfingInteractionStr=="Spike":
			self.NumscipyingSparseFloat=self.HopfingSparseWeigthFloat
			self.NumscipyingSwitchFloat=self.HopfingSwitchWeigthFloat

			#numscipy
			self.numscipy(
				)

			#alias
			self.HopfedLateralWeigthFloatsArray=self.NumscipiedValueFloatsArray

			#debug
			self.debug(
				[
					'We have setted the laterals',
					('self.',self,[
						'HopfedLateralWeigthFloatsArray'
					])
				]
			)

			#set
			self.HopfedMeanfieldWeigthFloat=self.HopfingStdWeightFloat if self.HopfingStdWeightFloat>0. else self.HopfingMeanWeightFloat

			#Check
			if self.HopfedMeanfieldWeigthFloat==0.:

				#return
				self.HopfedIsStableBool=True

				#return 
				return self


			#/###################/#
			# Determine the stationary solutions
			# 

			#Check
			if self.HopfingDoStationaryBool:

				#debug
				self.debug(
					[
						'We compute the stationary solutions'
					]
				)


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

			#real and imag
			self.HopfedRealLateralEigenFloatsArray=np.real(
				self.NumscipiedEigenvalueComplexesArray
			)
			self.HopfedImagLateralEigenFloatsArray=np.imag(
				self.NumscipiedEigenvalueComplexesArray
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

				#map
				HopfedPerturbationFloatsTuplesList=map(
					lambda __NumscipiedEigenvalueComplex:
					self.setAttr(
						'HopfedEigenComplex',
						__NumscipiedEigenvalueComplex
					).getSolutionFloatsTuple(),
					self.NumscipiedEigenvalueComplexesArray
				)
			
			else:

				#Check
				if self.HopfingDoStabilityBool:

					#for
					for __NumscipiedEigenvalueComplex in self.NumscipiedEigenvalueComplexesArray:

						#set
						self.HopfedInstabilityPerturbationComplex=self.setAttr(
							'HopfedEigenComplex',
							__NumscipiedEigenvalueComplex
						).getSolutionFloatsTuple(
						)


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
				self.HopfedStdSparseFloat=np.sqrt(self.NumscipyingSparseFloat*(1.-self.NumscipyingSparseFloat))
				
				#set
				self.HopfedLateralContourComplexesArray*=self.HopfedStdSparseFloat
	          	      
			#/###############/#
			# Compute for each eigen of the contour a possible solution
			#

			#Check
			if self.HopfingPerturbationEnvelopBool:

				#map
				HopfedPerturbationContourFloatsTuplesList=map(
					lambda __HopfedContourComplex:
					self.setAttr(
						'HopfedEigenComplex',
						__HopfedContourComplex
					).getSolutionFloatsTuple(),
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
				

				#Check
				if self.HopfingDoStabilityBool:

					#get
					self.HopfedInstabilityContourIndexInt = np.argmax(
						self.HopfedPerturbationContourRealFloatsArray
					)
				
				#get	
				self.HopfedInstabilityContourComplex=self.HopfedLateralContourComplexesArray[
					self.HopfedInstabilityContourIndexInt
				]

				#set
				self.HopfedIsStableBool=self.HopfedPerturbationContourRealFloatsArray[
					self.HopfedInstabilityContourIndexInt
				]<0.

				#Check
				if self.HopfedIsStableBool==False:

					#set
					self.HopfedInstabilityStr='Rate' if self.HopfedPerturbationContourImagFloatsArray[
						self.HopfedInstabilityContourIndexInt
					]==0. else 'Hopf'

				#debug
				'''
				self.debug(
					[
						('self.',self,[
								'HopfedInstabilityContourIndexInt',
								'HopfedInstabilityContourComplex',
								'HopfedIsStableBool',
								'HopfedInstabilityStr'
							])
					]
				)
				'''

			else:

				#Check
				if self.HopfingDoStabilityBool:

					#for
					for __HopfedContourComplex in self.HopfedLateralContourComplexesArray:

						#set
						self.setAttr(
							'HopfedEigenComplex',
							__HopfedContourComplex
						).getSolutionFloatsTuple(
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


		else:

			#debug
			self.debug(
				[
					'We know already the weigth matrix'
				]
			)

			#import
			import numpy as np

			#alias
			self.HopfedLateralWeigthFloatsArray=np.array(
				self.HopfingLateralWeigthVariable
			)

			#set
			self.HopfingUnitsInt=len(self.HopfedLateralWeigthFloatsArray)

			#/###################/#
			# Determine the time constant
			# 

			

			#map
			map(
				lambda __TimeStr:
				self.setTimeFloatsArray(
					__TimeStr
				),
				[
					'Constant',
					'Delay',
					'Decay',
					'Rise'
				]
			)
			



			#/###################/#
			# Determine the stationary solutions
			# 

			#Check
			if self.HopfingDoStationaryBool:

				#debug
				self.debug(
					[
						'We compute the stationary solutions'
					]
				)

			#/###################/#
			# Determine the perturb solutions
			# 

			#Check
			if self.HopfingDoStabilityBool:

				#Check
				if self.HopfingInteractionStr=="Rate":

					#ones
					self.HopfedNullPerturbationFloatsArray=np.ones(
						self.HopfingUnitsInt
					)

				#debug
				self.debug(
					[
						'We compute the perturbative solutions',
						('self.',self,[
								'HopfedLateralWeigthFloatsArray',
								'HopfedNullPerturbationFloatsArray',
								'HopfedConstantTimeFloatsArray'
							])
					]
				)

				#get
				self.HopfedSetNeuralComplexMethod=getattr(
					self,
					'set'+self.HopfingInteractionStr+'NeuralPerturbationComplex'
				)

				#set
				self.HopfedPerturbationWeigthFloatsArray=np.array(
					map(
						lambda __RowInt:
						self.HopfedLateralWeigthFloatsArray[
							__RowInt,
							:
						]*self.HopfedNullPerturbationFloatsArray[
							__RowInt
						]*self.HopfedConstantTimeFloatsArray[
							__RowInt
						],
						xrange(
							self.HopfingUnitsInt
						)
					)
				)

				#self.HopfedPerturbationWeigthFloatsArray
				#self.HopfedNullPerturbationFloatsArray
		
	


	def setTimeFloatsArray(self,_KeyStr):

		#get
		HopfingTimeVariable=getattr(
			self,
			'Hopfing'+_KeyStr+'TimeVariable'
		)

		#type
		HopfedTimeType=type(HopfingTimeVariable)

		#Check
		if HopfedTimeType in [list,np.array]:

			#array
			setattr(
				self,
				'Hopfed'+_KeyStr+'TimeFloatsArray',
				np.array(
					HopfingTimeVariable
				)
			)

		else:

			#array
			setattr(
				self,
				'Hopfed'+_KeyStr+'TimeFloatsArray',
				np.array(
					[HopfingTimeVariable]*self.HopfingUnitsInt
				)
			)


	def setPerturbationWeigthFloat(_RowInt,_ColInt):

		#set
		self.HopfedPerturbationWeigthFloatsArray[
			_RowInt,_ColInt
		]=self.HopfedLateralWeigthFloatsArray[
				_RowInt,_ColInt
		]*self.HopfedNullPerturbationFloatsArray[
			_RowInt
		]*self.HopfedConstantTimeFloatsArray[
			_RowInt
		]

	def setRateNeuralPerturbationComplex(_PulsationVariable,_RowInt):

		#set
		self.HopfedNeuralPerturbationComplexesArray=self.HopfedNullPerturbationFloatsArray/(
			1.+_PulsationVariable*self.HopfedConstantTimeFloatsArray
		)

	def setSpikeNeuralPerturbationComplex(_PulsationVariable,_RowInt):

		pass

	def setSynapticPerturbationComplex(_PulsationVariable,_RowInt,_ColInt):

		#exp
		self.HopfedSynapticPerturbationComplexesArray=np.exp(
			-_PulsationVariable*self.HopfedDelayTimeFloatsArray[
				_RowInt,_ColInt
			]
		)/(
			(1.+_PulsationVariable*self.HopfedDecayTimeFloatsArray[
				_RowInt,_ColInt
			])*(
			1.+_PulsationVariable*self.HopfedRiseTimeFloatsArray[
				_RowInt,_ColInt
			])
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

			#set
			self.LeakingTimeVariable=self.HopfedNetworkDeriveHopferVariable.HopfingConstantTimeVariable
			
			#set
			self.LeakingInteractionStr=self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'LeakingInteractionStr'
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

			#/####################/#
			# Spike case
			#

			else:

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

			#/####################/#
			# Check for Interactions
			#

			#get
			HopfedInteractionsDeriveHopfer=self.getTeamer(
				"Interactions"
			)

			#get
			HopfedInteractionsDeriveHopfer.getManager(
				"/"
			)

	def hopfInteraction(self):

		#Check
		if self.ManagementTagStr=='/':

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
			self.LeakingWeigthVariable=self.HopfedNetworkDeriveHopferVariable.HopfedLateralWeigthFloatsArray

			#Check
			if self.HopfedNetworkDeriveHopferVariable.HopfingDelayTimeVariable!=0.:
				self.LeakingDelayVariable=self.HopfedNetworkDeriveHopferVariable.HopfingDelayTimeVariable

			#set
			self.LeakingInteractionStr=self.HopfedNetworkDeriveHopferVariable.HopfingInteractionStr

	def hopfInput(self):

		#debug
		self.debug(
			[
				'We hopfInput here'
			]
		)

		#Check
		if self.ManagementTagStr=="Rest":

			#debug
			self.debug(
				[
					'We hopf Input Rest here'
				]
			)

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
			if self.LeakingWeigthVariable==None:

				#get
				self.LeakingWeigthVariable='#scalar:-60*mV'
	
	def getStationaryRateRootFloatsTuple(self,_StationaryRateFloat):
			
		#return
		return 0.

	def getGlobalPerturbationRootFloatsTuple(self,_PerturbationComplex):

		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationComplex

		#map
		map(
			lambda __HopfedIndexIntsTuple:
			self.setSynapticPerturbationComplex(
				__HopfedIndexIntsTuple
			).HopfedSetNeuralComplexMethod(
				__HopfedIndexIntsTuple[0]
			),
			self.HopfedIndexIntsTuplesList
		)

		#mul
		self.HopfedTotalPerturbationComplexesArray=self.HopfedPerturbationWeigthFloatsArray*self.HopfedSynapticPerturbationComplexesArray
			
		#map 
		map(
			lambda __RowInt:
			self.HopfedTotalPerturbationComplexesArray.__setitem__(
				__RowInt,
				self.HopfedNeuralPerturbationComplexesArray
			),
			xrange(self.HopfingUnitsInt)
		)

		#fill
		np.fill_diagonal(
			self.HopfedTotalPerturbationComplexesArray,
			1.-np.diag(self.HopfedTotalPerturbationComplexesArray)
		)
		

	def getUniqueDelayPerturbationRootFloatsTuple(self,_PerturbationComplex):
			
		#split
		PerturbationRealFloat,PerturbationImagFloat = _PerturbationComplex

		#compute
		PrefixComplex=(1./self.HopfedMeanfieldWeigthFloat)*np.exp(
				PerturbationRealFloat*self.HopfingDelayTimeVariable
			)

		#compute
		CosFloat=np.cos(PerturbationImagFloat*self.HopfingDelayTimeVariable)
		SinFloat=np.sin(PerturbationImagFloat*self.HopfingDelayTimeVariable)

		#compute
		NeuralFloat=(1.+self.HopfingConstantTimeVariable*PerturbationRealFloat)

		#compute
		FirstRootFloat = PrefixComplex*(
			NeuralFloat*CosFloat-self.HopfingConstantTimeVariable*PerturbationImagFloat*SinFloat
		)-self.HopfedEigenComplex.real

		#compute
		SecondRootFloat = PrefixComplex*(
			self.HopfingConstantTimeVariable*PerturbationImagFloat*CosFloat+NeuralFloat*SinFloat
		)-self.HopfedEigenComplex.imag
		
		#return
		return (FirstRootFloat,SecondRootFloat)

	def getSolutionFloatsTuple(self):

		#import
		import scipy.optimize

		#return
		return scipy.optimize.fsolve(self.getUniqueDelayPerturbationRootFloatsTuple, (0,0))

	#/######################/#
	# Augment view
	#
		
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
			if self.HopfedMeanfieldWeigthFloat==0.:

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
			# draw
			#

			#list
			ViewedPerturbationDrawDerivePyploter.PyplotingDrawVariable=[
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

#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=HopferClass
#<DefineLocals>

#</DefinePrint>
HopferClass.PrintingClassSkipKeyStrsList.extend(
	[
		'HopfingUnitsInt',
		'HopfingLateralWeigthVariable',
		'HopfingConstantTimeVariable',
		'HopfingDelayTimeVariable',
		'HopfingDecayTimeVariable',
		'HopfingRiseTimeVariable',
		'HopfingMeanWeightFloat',
		'HopfingStdWeightFloat',
		'HopfingSparseWeigthFloat',
		'HopfingSwitchWeigthFloat',
		'HopfingNormalisationInt',
		'HopfingSymmetryFloat',
		'HopfingPerturbationEnvelopBool',
		'HopfingDoStationaryBool',
		'HopfingDoStabilityBool',
		'HopfingContourSamplesInt',
		'HopfingInteractionStr',
		'HopfedLateralWeigthFloatsArray',
		'HopfedHalfHeightFloat',
		'HopfedLateralHalfWidthFloat',
		'HopfedMeanfieldWeigthFloat',
		'HopfedRealLateralEigenFloatsArray',
		'HopfedImagLateralEigenFloatsArray',
		'HopfedLateralContourComplexesArray',
		'HopfedEigenComplex',
		'HopfedPerturbationComplex',
		'HopfedPerturbationRealFloatsArray',
		'HopfedPerturbationImagFloatsArray',
		'HopfedPerturbationContourRealFloatsArray',
		'HopfedPerturbationContourImagFloatsArray',
		'HopfedInstabilityIndexInt',
		'HopfedInstabilityContourIndexInt',
		'HopfedInstabilityContourComplex',
		'HopfedIsStableBool',
		'HopfedInstabilityStr',
		'HopfedStdSparseFloat',
		'HopfedParentSingularStr',
		'HopfedConstantTimeFloatsArray',
		'HopfedDelayTimeFloatsArray',
		'HopfedNeuralPerturbationComplexesArray',
		'HopfedSynapticPerturbationComplexesArray',
		'HopfedTotalPerturbationComplexesArray',
		'HopfedAgentDeriveHopferVariable',
		'HopfedNetworkDeriveHopferVariable'
	]
)
#<DefinePrint>