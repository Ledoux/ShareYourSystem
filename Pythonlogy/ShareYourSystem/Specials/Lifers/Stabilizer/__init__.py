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
SYS.addDo('Stabilizer','Stabilize','Stabilizing','Stabilized')
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
class StabilizerClass(BaseClass):
	
	def default_init(self,
			_StationarizingUnitsInt = 1,
			_StationarizingLateralWeightVariable = None,
			_StationarizingConstantTimeVariable = 0.02, 
			_StationarizingDelayTimeVariable = 0.002,
			_StationarizingDecayTimeVariable = 0.,
			_StationarizingRiseTimeVariable = 0.,
			_StationarizingNormalisationInt= 0.5,
			_StationarizingPerturbationEnvelopBool=True,
			_StationarizingDoStationaryBool=True,
			_StationarizingDoStabilityBool=True,
			_StationarizingDoStationarizBool=False,
			_StationarizingInteractionStr="Rate",
			_StationarizingRestVariable=-48.,
			_StationarizingStabilityScanFrequencyVariable=None,
			_StationarizingStationarizScanFrequencyVariable=None,
			_StationarizingStationarizCurrentVariable=None,
			_StabilizedLateralWeightFloatsArray=None,
			_StabilizedMeanfieldWeightFloat=0.,
			_StabilizedHalfHeightFloat=0.,
			_StabilizedLateralHalfWidthFloat=0., 
			_StabilizedLateralContourComplexesArray=None,
			_StabilizedEigenComplex=None,
			_StabilizedEigenvalueComplexesArray=None,
			_StabilizedInstabilityIndexInt=-1,
			_StabilizedInstabilityComplex=None,
			_StabilizedInstabilityLambdaFloatsTuple=None,
			_StabilizedInstabilityFrequencyFloat=0.,
			_StabilizedIsStableBool=True,
			_StabilizedInstablesInt=0,
			_StabilizedInstabilityStr="",
			_StabilizedStdSparseFloat=0.,
			_StabilizedParentSingularStr="",
			_StabilizedIndexIntsTuplesList=None,
			_StabilizedPerturbationNullVariable=None,
			_StabilizedPerturbationWeightFloatsArray=None,
			_StabilizedConstantTimeVariable=None,
			_StabilizedDelayTimeVariable=None,
			_StabilizedDecayTimeVariable=None,
			_StabilizedRiseTimeVariable=None,
			_StabilizedPerturbationComplex=None,
			_StabilizedNeuralPerturbationComplex=None,
			_StabilizedSynapticPerturbationComplexesArray=None,
			_StabilizedSynapticPerturbationMethodVariable=None,
			_StabilizedNeuralPerturbationMethodVariable=None,
			_StabilizedTotalPerturbationComplexesArray=None,
			_StabilizedFlatTotalPerturbationComplexesArray=None,
			_StabilizedDeterminantFunctionVariable=None,
			_StabilizedDeterminantFloatsTuple=None,
			_StabilizedStabilityScanFrequencyFloatsArray=None,
			_StabilizedOptimizeRoot=None,
			_StabilizedStationarizScanFrequencyFloatsArray=None,
			_StabilizedStationarizCurrentFloatsArray=None,
			_StabilizedStationarizRateComplexesArray=None,
			_StabilizedStationarizRateAmplitudeFloatsArray=None,
			_StabilizedStationarizRatePhaseFloatsArray=None,
			_StabilizedAgentDeriveStabilizerVariable=None,
			_StabilizedNetworkDeriveStabilizerVariable=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_stabilize(self):

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
			self.StabilizedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['StabilizedParentSingularStr'])
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
		]) and self.StabilizedParentSingularStr!='Population':

			#/########################/#
			# Network level
			# 

			#debug
			'''
			self.debug(
				[
					'It is a Network level for the stabilize',
				]
			)
			'''

			#/########################/#
			# Determine parent level
			# 

			#alias
			self.StabilizedNetworkDeriveStabilizerVariable=self

			#/########################/#
			# stabilizeNetwork
			# 

			#stabilize
			self.stabilizeNetwork()

			#/########################/#
			# structure stabilize 
			# 

			#debug
			'''
			self.debug(
				[
					'We structure all the stabilizeing children...'
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
						'stabilize'
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
						'StabilizedParentSingularStr'
					])
				]
			)
			'''

			#set
			StabilizedMethodKeyStr='stabilize'+self.StabilizedParentSingularStr

			#Check
			if hasattr(self,StabilizedMethodKeyStr):

				#/########################/#
				# call the special stabilize<StabilizedParentSingularStr> method
				#

				#debug
				'''
				self.debug(
					[
						'It is a '+self.StabilizedParentSingularStr+' level',
						'We stabilize<StabilizedParentSingularStr>'
					]
				)
				'''

				#call
				getattr(
					self,
					StabilizedMethodKeyStr
				)()

				#debug
				'''
				self.debug(
					[
						'Ok we have setted stabilize'+self.StabilizedParentSingularStr
					]
				)
				'''	
	
	def stabilizeNetwork(self):

		#/###################/#
		# Check for Populations
		# 

		#get
		StabilizedPopulationsDeriveManager=self.getTeamer(
			"Populations"
		)

		#debug
		'''
		self.debug(
			[
				'We stabilize network here',
			]
		)
		'''

		#import
		import numpy as np

		#alias
		self.StabilizedLateralWeightFloatsArray=np.array(
			self.StationarizingLateralWeightVariable
		)

		#set
		self.StationarizingUnitsInt=len(self.StabilizedLateralWeightFloatsArray)

		#/###################/#
		# Determine the time constant structure
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
		if self.StationarizingDoStationaryBool:

			#debug
			"""
			self.debug(
				[
					'We compute the stationary solutions'
				]
			)
			"""

		#/###################/#
		# Determine the perturb solutions
		# 

		#Check
		if self.StationarizingDoStabilityBool:

			#Check
			if self.StationarizingInteractionStr=="Rate":

				#ones
				#self.StabilizedPerturbationNullVariable=np.ones(
				#	self.StationarizingUnitsInt
				#)

				self.StabilizedPerturbationNullVariable=1.

			elif self.LeakingInteractionStr=="Spike":

				#set
				self.LifingConstantTimeFloat = self.LeakingTimeVariable
				self.LifingVoltageResetFloat = self.LeakingResetVariable
				self.LifingVoltageThresholdFloat = self.LeakingThresholdVariable
				self.LifingStationaryCurrentFloat = 0.
				#self.LifingVoltageNoiseFloat = self.Stationarizing
				#self.Lifing

			#debug
			'''
			self.debug(
				[
					'We compute the StabilizedPerturbationWeightFloatsArray',
					('self.',self,[
							'StabilizedLateralWeightFloatsArray',
							'StabilizedPerturbationNullVariable',
							'StabilizedConstantTimeVariable'
						])
				]
			)
			'''

			#set
			self.StabilizedPerturbationWeightFloatsArray=self.StabilizedLateralWeightFloatsArray[
				:
			]

			#mul
			SYS.setMatrixArray(
				self.StabilizedPerturbationWeightFloatsArray,
				self.StabilizedPerturbationNullVariable,
				np.ndarray.__mul__
			)

			#mul
			SYS.setMatrixArray(
				self.StabilizedPerturbationWeightFloatsArray,
				self.StabilizedConstantTimeVariable,
				np.ndarray.__mul__
			)

			#debug
			'''
			self.debug(
				[
					'In the end',
					('self.',self,[
							'StabilizedPerturbationWeightFloatsArray'
						])
				]
			)
			'''

			#Check
			if SYS.getIsNullBool(
				self.StabilizedRiseTimeVariable
			):

				#Check
				if SYS.getIsNullBool(
					self.StabilizedDecayTimeVariable
				):
					
					#Check
					if SYS.getIsNullBool(
						self.StabilizedDelayTimeVariable
					):

						#set
						self.StabilizedSynapticPerturbationMethodVariable=None

					else:

						#set
						self.StabilizedSynapticPerturbationMethodVariable=self.getSynapticDelayPerturbationVariable

				else:

					#set
					self.StabilizedSynapticPerturbationMethodVariable=self.getSynapticDecayPerturbationVariable

			else:

				#set
				self.StabilizedSynapticPerturbationMethodVariable=self.getSynapticRisePerturbationVariable

			#get
			self.StabilizedNeuralPerturbationMethodVariable=getattr(
				self,
				'get'+self.StationarizingInteractionStr+'NeuralPerturbationComplex'
			)

			#import 
			import itertools

			#list
			self.StabilizedIndexIntsTuplesList=list(
				itertools.product(
					xrange(self.StationarizingUnitsInt),
					xrange(self.StationarizingUnitsInt)
				)
			)

			#debug
			'''
			self.debug(
				[
					'We set a one root get',
					('self.',self,[
							'StabilizedIndexIntsTuplesList'
						])	
				]
			)
			self.getGlobalPerturbationRootFloatsTuple(
								(0.1,2.*np.pi*1.)
							)
			'''

			#import
			from numpy import linalg

			#set
			self.StabilizedDeterminantFunctionVariable=linalg.det

			#/################/#
			# Look for a rate instability
			#

			StabilizedRateDetermintantFloatsTuple=self.getGlobalPerturbationRootFloatsTuple(
				(0.,0.)
			)

			#get
			self.StabilizedIsStableBool=StabilizedRateDetermintantFloatsTuple[0]>0.

			#debug
			""""
			self.debug(
				[
					'Is it rate instable ?',
					"StabilizedRateDetermintantFloatsTuple is "+str(StabilizedRateDetermintantFloatsTuple),
					('self.',self,[
							'StabilizedTotalPerturbationComplexesArray',
							'StabilizedFlatTotalPerturbationComplexesArray',
							'StabilizedIsStableBool'
						])
				]
			)
			"""

			#Check
			if self.StabilizedIsStableBool:

				#import 
				import scipy.optimize

				#debug
				"""
				self.debug(
					[
						"There is no rate instability so we do a Hopf scan analysis",
						('self.',self,['StationarizingStabilityScanFrequencyVariable'])
					]
				)
				"""

				#type
				StabilizedScanType=type(self.StationarizingStabilityScanFrequencyVariable)

				#Check
				if StabilizedScanType==None.__class__:

					#Check
					self.StabilizedStabilityScanFrequencyFloatsArray=np.logspace(0,3,10)

				elif StabilizedScanType in [np.float64,float]:

					#Check
					self.StabilizedStabilityScanFrequencyFloatsArray=np.array(
						[self.StationarizingStabilityScanFrequencyVariable]
					)

				else:

					#Check
					self.StabilizedStabilityScanFrequencyFloatsArray=np.array(
						self.StationarizingStabilityScanFrequencyVariable
					)

				#debug
				"""
				self.debug(
					[
						('self.',self,['StabilizedStabilityScanFrequencyFloatsArray'])
					]
				)
				"""

				#loop
				for __ScanFrequencyFloat in self.StabilizedStabilityScanFrequencyFloatsArray:
				#for __ScanFrequencyFloat in [100.]:

					#debug
					'''
					self.debug(
						[
							'We try to find an instability around '+str(__ScanFrequencyFloat)+'Hz'
						]
					)
					'''

					#Get the solve of the ScipyOptimizeRoot
					StabilizedOptimizeRoot=scipy.optimize.root(
							self.getGlobalPerturbationRootFloatsTuple,
							(-0.1,2.*np.pi*__ScanFrequencyFloat),
							#method='lm',
							#tol=0.001
							options={
										#'maxiter':1000,
										#'ftol':0.001,
										#'direc':np.array([-0.1,0.1])
									},
						)

					#debug
					"""
					self.debug(
						[
							'StabilizedOptimizeRoot is ',
							str(StabilizedOptimizeRoot)
						]
					)
					"""

					#set
					self.StabilizedOptimizeRoot=StabilizedOptimizeRoot

					#Check
					if StabilizedOptimizeRoot.success:

						#Check
						if StabilizedOptimizeRoot.x[0]>0.:

							#set
							self.StabilizedIsStableBool=False

							#set
							self.StabilizedInstabilityStr="Hopf"

							#set
							self.StabilizedInstabilityLambdaFloatsTuple=tuple(
								StabilizedOptimizeRoot.x
							)

							#set
							self.StabilizedInstabilityFrequencyFloat=self.StabilizedInstabilityLambdaFloatsTuple[1]/(
								2.*np.pi
							)

							#break
							break


				#/################/#
				# Do tranfer maybe
				#

				#Check
				if self.StationarizingDoStationarizBool:

					#debug
					'''
					self.debug(
						[
							"We compute stabilize here",
							('self.',self,[
									'StationarizingStationarizCurrentVariable'
								])
						]
					)
					'''

					#type
					StabilizedStationarizCurrentType=type(
						self.StationarizingStationarizCurrentVariable
					)

					#Check
					if StabilizedStationarizCurrentType==None.__class__:

						#array
						self.StabilizedStationarizCurrentFloatsArray=[1.]*self.StationarizingUnitsInt

					elif StabilizedStationarizCurrentType in [np.float64,float]:

						#array
						self.StabilizedStationarizCurrentFloatsArray=[
								self.StationarizingStationarizCurrentVariable
							]*self.StationarizingUnitsInt

					else:

						#array
						self.StabilizedStationarizCurrentFloatsArray=self.StationarizingStationarizCurrentVariable

					#array
					self.StabilizedStationarizCurrentFloatsArray=np.array(
						self.StabilizedStationarizCurrentFloatsArray
					)

					#import 
					import scipy.linalg

					#debug
					"""
					self.debug(
						[
							"we do a stabilize scan analysis",
							('self.',self,['StationarizingStationarizScanFrequencyVariable'])
						]
					)
					"""

					#type
					StabilizedScanType=type(self.StationarizingStationarizScanFrequencyVariable)

					#Check
					if StabilizedScanType==None.__class__:

						#Check
						self.StabilizedStationarizScanFrequencyFloatsArray=np.logspace(0,3,10)

					elif StabilizedScanType in [np.float64,float]:

						#Check
						self.StabilizedStationarizScanFrequencyFloatsArray=np.array(
							[self.StationarizingStationarizScanFrequencyVariable]
						)

					else:

						#Check
						self.StabilizedStationarizScanFrequencyFloatsArray=np.array(
							self.StationarizingStationarizScanFrequencyVariable
						)

					#debug
					"""
					self.debug(
						[
							('self.',self,['StabilizedStationarizScanFrequencyFloatsArray'])
						]
					)
					"""

					#init
					self.StabilizedStationarizRateComplexesArray=np.zeros(
							(
								self.StationarizingUnitsInt,
								len(self.StabilizedStationarizScanFrequencyFloatsArray)
							),
							dtype=complex
						)
					self.StabilizedStationarizRateAmplitudeFloatsArray=np.zeros(
							(
								self.StationarizingUnitsInt,
								len(self.StabilizedStationarizScanFrequencyFloatsArray)
							),
							dtype=float
						)
					self.StabilizedStationarizRatePhaseFloatsArray=np.zeros(
							(
								self.StationarizingUnitsInt,
								len(self.StabilizedStationarizScanFrequencyFloatsArray)
							),
							dtype=float
						)

					#loop
					for __IndexInt,__ScanFrequencyFloat in enumerate(
						self.StabilizedStationarizScanFrequencyFloatsArray
					):

						#set
						self.StabilizedPerturbationComplex=1j*2.*np.pi*__ScanFrequencyFloat

						#set
						self.setStabilizedTotalPerturbationComplexesArray()

						#solve
						StabilizedStationarizRateComplexesArray = scipy.linalg.solve(
							self.StabilizedTotalPerturbationComplexesArray,
							self.StabilizedStationarizCurrentFloatsArray
						)

						#lu
						self.StabilizedStationarizRateComplexesArray[
							:,
							__IndexInt
						]=StabilizedStationarizRateComplexesArray

						#amp and phase
						self.StabilizedStationarizRateAmplitudeFloatsArray[
							:,
							__IndexInt
						]=np.abs(
							StabilizedStationarizRateComplexesArray
						)
						self.StabilizedStationarizRatePhaseFloatsArray[
							:,
							__IndexInt
						]=np.angle(
							StabilizedStationarizRateComplexesArray
						)

					#debug
					'''
					self.debug(
						[
							'after the solve decomposition',
							('self.',self,[
								'StabilizedStationarizCurrentFloatsArray',
								'StabilizedStationarizRateComplexesArray',
								'StabilizedStationarizRateAmplitudeFloatsArray',
								'StabilizedStationarizRatePhaseFloatsArray'
							])	
						]
					)
					'''

					#find the Extremum
					self.NumscipiedFourierFrequencyFloatsArray=self.StabilizedStationarizScanFrequencyFloatsArray
					self.NumscipiedFourierAmplitudeFloatsArray=self.StabilizedStationarizRateAmplitudeFloatsArray
					self.NumscipiedFourierPhaseFloatsArray=self.StabilizedStationarizRatePhaseFloatsArray
					self.setExtremum()

					#debug
					self.debug(
						[
							('self.',self,[ 
									'NumscipiedFourierMaxTupleFloatsArray',
									'NumscipiedFourierMaxCrossPhaseFloatsArray'
								])
						]
					)

			else:

				#set
				self.StabilizedInstabilityStr="Rate"

			#debug
			'''
			self.debug(
				[
					'In the end ',
					('self.',self,[
						'StabilizedTotalPerturbationComplexesArray',
						'StabilizedDeterminantFloatsTuple',
						'StabilizedIsStableBool',
						'StabilizedInstabilityStr',
						'StabilizedInstabilityLambdaFloatsTuple',
						'StabilizedInstabilityFrequencyFloat'
					])
				]
			)
			'''
				
	

	def getSynapticDelayPerturbationVariable(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'StabilizedDelayTimeVariable'
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return SYS.setMatrixArray(
					np.ones(
								(self.StationarizingUnitsInt,self.StationarizingUnitsInt),
								dtype=complex
							),
					np.exp(
						-self.StabilizedDelayTimeVariable*_PerturbationComplex
					),
					np.ndarray.__mul__,
					_AxisInt=1
				)


	def getSynapticDecayPerturbationVariable(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'StabilizedDecayTimeVariable',
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return SYS.setMatrixArray(
					SYS.setMatrixArray(
						self.getSynapticDelayPerturbationVariable(_PerturbationComplex),
						1.+self.StabilizedDecayTimeVariable*_PerturbationComplex,
						np.ndarray.__div__,
						_AxisInt=1
					),
					1.+self.StabilizedRiseTimeVariable*_PerturbationComplex,
					np.ndarray.__div__,
					_AxisInt=1
				)

	def getSynapticRisePerturbationVariable(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'StabilizedRiseTimeVariable'
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return SYS.setMatrixArray(
					self.getSynapticRisePerturbationVariable(_PerturbationComplex),
					1.+self.StabilizedRiseTimeVariable*_PerturbationComplex,
					np.ndarray.__div__,
					_AxisInt=1
				)			

	def getSynapticPerturbationVariable(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'StabilizedDelayTimeVariable',
						'StabilizedDecayTimeVariable',
						'StabilizedRiseTimeVariable'
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return SYS.setMatrixArray(
					SYS.setMatrixArray(
						SYS.setMatrixArray(
							np.ones(
										(self.StationarizingUnitsInt,self.StationarizingUnitsInt),
										dtype=complex
									),
							np.exp(
								-self.StabilizedDelayTimeVariable*_PerturbationComplex
							),
							np.ndarray.__mul__,
							_AxisInt=1
						),
						1.+self.StabilizedDecayTimeVariable*_PerturbationComplex,
						np.ndarray.__div__,
						_AxisInt=1
					),
					1.+self.StabilizedRiseTimeVariable*_PerturbationComplex,
					np.ndarray.__div__,
					_AxisInt=1
				)

	def getRateNeuralPerturbationComplex(self,_PerturbationComplex):

		#debug
		"""
		self.debug(
			[
				('self.',self,[
						'StabilizedPerturbationNullVariable',
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		"""

		#return
		return self.StabilizedPerturbationNullVariable/(
			1.+_PerturbationComplex*self.StabilizedConstantTimeVariable
		)

	def getLeakNeuralPerturbationComplex(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'StabilizedConstantTimeVariable'
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return 1.+_PerturbationComplex*self.StabilizedConstantTimeVariable

	def getSpikeNeuralPerturbationComplex(self,_PulsationVariable):

		#debug
		self.debug(
			[
				'We call the lif perturb function'
			]
		)

		#lif
		self.lif(
			_PerturbationLambdaVariable=_PulsationVariable,
			_PerturbationMethodStr='Brunel'
		)

		#return
		return self.LifedPerturbationMeanComplexVariable

	def setStabilizedTotalPerturbationComplexesArray(self):

		#/###############/#
		# Prepare the complex pulsation perturbation
		# init StabilizedTotalPerturbationComplexesArray

		#alias
		PerturbationComplex=self.StabilizedPerturbationComplex

		#copy
		self.StabilizedTotalPerturbationComplexesArray=-np.array(
			self.StabilizedPerturbationWeightFloatsArray[:],
			dtype=complex
		)

		#/###############/#
		# Synaptic coupling
		#

		"""
		#exp
		self.StabilizedSynapticPerturbationVariable=self.getSynapticPerturbationVariable(
				PerturbationComplex
			)

		#debug
		self.debug(
			[
				('self.',self,[
						'StabilizedSynapticPerturbationVariable'
					])
			]
		)
		"""

		#Check
		if self.StabilizedSynapticPerturbationMethodVariable!=None:

			#mul
			SYS.setMatrixArray(
				self.StabilizedTotalPerturbationComplexesArray,
				self.StabilizedSynapticPerturbationMethodVariable(
					PerturbationComplex
				),
				np.ndarray.__mul__
			)

		#debug
		'''
		self.debug(
			[
				'Ok we have mul the synaptic coupling',
				('self.',self,[
						'StabilizedTotalPerturbationComplexesArray'
					])
			]
		)
		'''

		#/###############/#
		# Neural response coupling
		#

		#exp
		self.StabilizedNeuralPerturbationComplex=self.StabilizedNeuralPerturbationMethodVariable(
			PerturbationComplex
		)

		#debug
		"""
		self.debug(
			[
				('self.',self,[
						'StabilizedNeuralPerturbationComplex',
						'StabilizedNeuralPerturbationMethodVariable'
					])
			]
		)
		"""

		#mul
		SYS.setMatrixArray(
			self.StabilizedTotalPerturbationComplexesArray,
			self.StabilizedNeuralPerturbationMethodVariable(
				PerturbationComplex
			),
			np.ndarray.__mul__
		)

		#debug
		'''
		self.debug(
			[
				'Ok we have mul the neural coupling',
				('self.',self,[
						'StabilizedTotalPerturbationComplexesArray'
					])
			]
		)
		'''

		#/###############/#
		# fill diagonal with also the leak identity term
		#

		"""
		#fill
		np.fill_diagonal(
			self.StabilizedTotalPerturbationComplexesArray,
			self.getLeakNeuralPerturbationComplex(
					PerturbationComplex
				)+np.diag(
					self.StabilizedTotalPerturbationComplexesArray
				)
		)
		"""

		#fill
		np.fill_diagonal(
			self.StabilizedTotalPerturbationComplexesArray,
			1.+np.diag(
					self.StabilizedTotalPerturbationComplexesArray
				)
		)


		#/###############/#
		# multiply all by the LeakNeuralPerturbationVariable
		#

		#get the numerator leak term
		StabilizedLeakNeuralPerturbationVariable=self.getLeakNeuralPerturbationComplex(PerturbationComplex)

		#mul
		self.StabilizedFlatTotalPerturbationComplexesArray=SYS.setMatrixArray(
			self.StabilizedTotalPerturbationComplexesArray.T,
			StabilizedLeakNeuralPerturbationVariable,
			np.ndarray.__mul__
		).T

		#debug
		"""
		self.debug(
			[
				"PerturbationComplex is "+str(PerturbationComplex),
				"StabilizedLeakNeuralPerturbationVariable is "+str(StabilizedLeakNeuralPerturbationVariable),
				('self.',self,[
						'StabilizedTotalPerturbationComplexesArray',
						'StabilizedFlatTotalPerturbationComplexesArray'
					])
			]
		)
		"""

	def getGlobalPerturbationRootFloatsTuple(self,_PerturbationFloatsTuple):

		#pack
		self.StabilizedPerturbationComplex=_PerturbationFloatsTuple[
			0
		]+1j*_PerturbationFloatsTuple[
			1
		]

		#set
		self.setStabilizedTotalPerturbationComplexesArray()

		#/###############/#
		# compute det
		#

		#det
		StabilizedDeterminantComplex=self.StabilizedDeterminantFunctionVariable(
			self.StabilizedTotalPerturbationComplexesArray
		)
	
		#debug
		'''
		self.debug(
			[
				'In the end ',
				('self.',self,[
						'StabilizedTotalPerturbationComplexesArray'
					]),
				'PerturbationComplex is '+str(PerturbationComplex),
				'StabilizedDeterminantComplex is '+str(StabilizedDeterminantComplex)
			]
		)
		'''

		#set
		self.StabilizedDeterminantFloatsTuple=(
			StabilizedDeterminantComplex.real,
			StabilizedDeterminantComplex.imag
		)

		#return
		return self.StabilizedDeterminantFloatsTuple


	def getStationaryRateRootFloat(self,_StationaryRateFloat):
			
		#return
		return 0.

	def getStationarySpikeRootFloat(self,_StationaryRateFloat):
			
		#center
		self.LifingStationaryCurrentFloat = 0.

		#noise
		self.LifingVoltageNoiseFloat = self.StationarizingStdWeightFloat *  self.StationarizingConstantTimeVariable * _StationaryRateFloat

		#lif
		self.lif()

		#return
		return self.LifedStationaryRateFloat

	"""
	def getStationarySpikeRootFloatsTuple(self,_StationaryRateFloatsTuple):
			
		#center
		LifingStationaryCurrentFloatsArray = np.dot(self.StabilizedLateralWeightFloatsArray,_StationaryRateFloatsTuple)

		#noise
		LifingVoltageNoiseFloatsArray = self.StationarizingStdWeightFloat *  self.StationarizingConstantTimeVariable * _StationaryRateFloat

		#lif
		self.lif()

		#return
		return self.LifedStationaryRateFloat
	"""

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
			if self.StationarizingDoStabilityBool:

				#map
				map(
						lambda __KeyStr:
						self.forcePrint(
							[__KeyStr],
							'StabilizerClass'
						)
						if getattr(
							self.PrintingCopyVariable,
							__KeyStr
						) not in [None,0.,""]
						else None,
						[
							'StationarizingConstantTimeVariable',
							'StationarizingDelayTimeVariable',
							'StationarizingDecayTimeVariable',
							'StationarizingRiseTimeVariable',
							'StabilizedInstabilityStr',
							'StabilizedInstabilityFrequencyFloat',
							'StabilizedIsStableBool'
						]
					)

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=StabilizerClass
#<DefineLocals>

#</DefinePrint>
StabilizerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'StationarizingUnitsInt',
		'StationarizingLateralWeightVariable',
		'StationarizingConstantTimeVariable',
		'StationarizingDelayTimeVariable',
		'StationarizingDecayTimeVariable',
		'StationarizingRiseTimeVariable',
		'StationarizingMeanWeightFloat',
		'StationarizingNormalisationInt',
		'StationarizingSymmetryFloat',
		'StationarizingDoStationaryBool',
		'StationarizingDoStabilityBool',
		'StationarizingDoStationarizBool',
		'StationarizingInteractionStr',
		'StationarizingRestVariable',
		'StationarizingStabilityScanFrequencyVariable',
		'StationarizingStationarizScanFrequencyVariable',
		'StationarizingStationarizCurrentVariable',
		'StabilizedLateralWeightFloatsArray',
		'StabilizedHalfHeightFloat',
		'StabilizedLateralHalfWidthFloat',
		'StabilizedMeanfieldWeightFloat',
		'StabilizedEigenComplex',
		'StabilizedEigenvalueComplexesArray',
		'StabilizedPerturbationComplex',
		'StabilizedPerturbationRealFloatsArray',
		'StabilizedPerturbationImagFloatsArray',
		'StabilizedInstabilityIndexInt',
		'StabilizedInstabilityIndexInt',
		'StabilizedInstabilityComplex',
		'StabilizedInstablesInt',
		'StabilizedIsStableBool',
		'StabilizedInstabilityStr',
		'StabilizedStdSparseFloat',
		'StabilizedParentSingularStr',
		'StabilizedIndexIntsTuplesList',
		'StabilizedPerturbationNullVariable',
		'StabilizedPerturbationWeightFloatsArray',
		'StabilizedConstantTimeVariable',
		'StabilizedDelayTimeVariable',
		'StabilizedDecayTimeVariable',
		'StabilizedRiseTimeVariable',
		'StabilizedPerturbationComplex',
		'StabilizedNeuralPerturbationComplex',
		'StabilizedSynapticPerturbationComplexesArray',
		'StabilizedSynapticPerturbationMethodVariable',
		'StabilizedNeuralPerturbationMethodVariable',
		'StabilizedTotalPerturbationComplexesArray',
		'StabilizedFlatTotalPerturbationComplexesArray',
		'StabilizedInstabilityLambdaFloatsTuple',
		'StabilizedInstabilityFrequencyFloat',
		'StabilizedDeterminantFunctionVariable',
		'StabilizedDeterminantFloatsTuple',
		'StabilizedStabilityScanFrequencyFloatsArray',
		'StabilizedOptimizeRoot',
		'StabilizedStationarizScanFrequencyFloatsArray',
		'StabilizedStationarizCurrentFloatsArray',
		'StabilizedStationarizRateComplexesArray',
		'StabilizedStationarizRateAmplitudeFloatsArray',
		'StabilizedStationarizRatePhaseFloatsArray',
		'StabilizedNetworkDeriveStabilizerVariable'
	]
)
#<DefinePrint>