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
SYS.addDo('Transferer','Transfer','Transfering','Transfered')
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
class TransfererClass(BaseClass):
	
	def default_init(self,
			_TransferingUnitsInt = 1,
			_TransferingLateralWeightVariable = None,
			_TransferingConstantTimeVariable = 0.02, 
			_TransferingDelayTimeVariable = 0.002,
			_TransferingDecayTimeVariable = 0.,
			_TransferingRiseTimeVariable = 0.,
			_TransferingNormalisationInt= 0.5,
			_TransferingPerturbationEnvelopBool=True,
			_TransferingDoStationaryBool=True,
			_TransferingDoStabilityBool=True,
			_TransferingDoTransferBool=False,
			_TransferingInteractionStr="Rate",
			_TransferingRestVariable=-48.,
			_TransferingStabilityScanFrequencyVariable=None,
			_TransferingTransferScanFrequencyVariable=None,
			_TransferingTransferCurrentVariable=None,
			_TransferedLateralWeightFloatsArray=None,
			_TransferedMeanfieldWeightFloat=0.,
			_TransferedHalfHeightFloat=0.,
			_TransferedLateralHalfWidthFloat=0., 
			_TransferedLateralContourComplexesArray=None,
			_TransferedEigenComplex=None,
			_TransferedEigenvalueComplexesArray=None,
			_TransferedInstabilityIndexInt=-1,
			_TransferedInstabilityComplex=None,
			_TransferedInstabilityLambdaFloatsTuple=None,
			_TransferedInstabilityFrequencyFloat=0.,
			_TransferedIsStableBool=True,
			_TransferedInstablesInt=0,
			_TransferedInstabilityStr="",
			_TransferedStdSparseFloat=0.,
			_TransferedParentSingularStr="",
			_TransferedIndexIntsTuplesList=None,
			_TransferedPerturbationNullVariable=None,
			_TransferedPerturbationWeightFloatsArray=None,
			_TransferedConstantTimeVariable=None,
			_TransferedDelayTimeVariable=None,
			_TransferedDecayTimeVariable=None,
			_TransferedRiseTimeVariable=None,
			_TransferedPerturbationComplex=None,
			_TransferedNeuralPerturbationComplex=None,
			_TransferedSynapticPerturbationComplexesArray=None,
			_TransferedSynapticPerturbationMethodVariable=None,
			_TransferedNeuralPerturbationMethodVariable=None,
			_TransferedTotalPerturbationComplexesArray=None,
			_TransferedFlatTotalPerturbationComplexesArray=None,
			_TransferedDeterminantFunctionVariable=None,
			_TransferedDeterminantFloatsTuple=None,
			_TransferedStabilityScanFrequencyFloatsArray=None,
			_TransferedOptimizeRoot=None,
			_TransferedTransferScanFrequencyFloatsArray=None,
			_TransferedTransferCurrentFloatsArray=None,
			_TransferedTransferRateComplexesArray=None,
			_TransferedTransferRateAmplitudeFloatsArray=None,
			_TransferedTransferRatePhaseFloatsArray=None,
			_TransferedAgentDeriveTransfererVariable=None,
			_TransferedNetworkDeriveTransfererVariable=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_transfer(self):

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
			self.TransferedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['TransferedParentSingularStr'])
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
		]) and self.TransferedParentSingularStr!='Population':

			#/########################/#
			# Network level
			# 

			#debug
			'''
			self.debug(
				[
					'It is a Network level for the transfer',
				]
			)
			'''

			#/########################/#
			# Determine parent level
			# 

			#alias
			self.TransferedNetworkDeriveTransfererVariable=self

			#/########################/#
			# transferNetwork
			# 

			#transfer
			self.transferNetwork()

			#/########################/#
			# structure transfer 
			# 

			#debug
			'''
			self.debug(
				[
					'We structure all the transfering children...'
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
						'transfer'
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
						'TransferedParentSingularStr'
					])
				]
			)
			'''

			#set
			TransferedMethodKeyStr='transfer'+self.TransferedParentSingularStr

			#Check
			if hasattr(self,TransferedMethodKeyStr):

				#/########################/#
				# call the special transfer<TransferedParentSingularStr> method
				#

				#debug
				'''
				self.debug(
					[
						'It is a '+self.TransferedParentSingularStr+' level',
						'We transfer<TransferedParentSingularStr>'
					]
				)
				'''

				#call
				getattr(
					self,
					TransferedMethodKeyStr
				)()

				#debug
				'''
				self.debug(
					[
						'Ok we have setted transfer'+self.TransferedParentSingularStr
					]
				)
				'''	
	
	def transferNetwork(self):

		#/###################/#
		# Check for Populations
		# 

		#get
		TransferedPopulationsDeriveManager=self.getTeamer(
			"Populations"
		)

		#debug
		'''
		self.debug(
			[
				'We predict network here',
			]
		)
		'''

		#/###############/#
		# Set implication
		#

		#set
		self.TransferingDoStabilityBool=True


		#debug
		'''
		self.debug(
			[
				'We know already the weigth matrix'
			]
		)
		'''

		#import
		import numpy as np

		#alias
		self.TransferedLateralWeightFloatsArray=np.array(
			self.TransferingLateralWeightVariable
		)

		#set
		self.TransferingUnitsInt=len(self.TransferedLateralWeightFloatsArray)

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
		if self.TransferingDoStationaryBool:

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
		if self.TransferingDoStabilityBool:

			#Check
			if self.TransferingInteractionStr=="Rate":

				#ones
				#self.TransferedPerturbationNullVariable=np.ones(
				#	self.TransferingUnitsInt
				#)

				self.TransferedPerturbationNullVariable=1.

			elif self.LeakingInteractionStr=="Spike":

				#set
				self.LifingConstantTimeFloat = self.LeakingTimeVariable
				self.LifingVoltageResetFloat = self.LeakingResetVariable
				self.LifingVoltageThresholdFloat = self.LeakingThresholdVariable
				self.LifingStationaryCurrentFloat = 0.
				#self.LifingVoltageNoiseFloat = self.Transfering
				#self.Lifing

			#debug
			'''
			self.debug(
				[
					'We compute the TransferedPerturbationWeightFloatsArray',
					('self.',self,[
							'TransferedLateralWeightFloatsArray',
							'TransferedPerturbationNullVariable',
							'TransferedConstantTimeVariable'
						])
				]
			)
			'''

			#set
			self.TransferedPerturbationWeightFloatsArray=self.TransferedLateralWeightFloatsArray[
				:
			]

			#mul
			SYS.setMatrixArray(
				self.TransferedPerturbationWeightFloatsArray,
				self.TransferedPerturbationNullVariable,
				np.ndarray.__mul__
			)

			#mul
			SYS.setMatrixArray(
				self.TransferedPerturbationWeightFloatsArray,
				self.TransferedConstantTimeVariable,
				np.ndarray.__mul__
			)

			#debug
			'''
			self.debug(
				[
					'In the end',
					('self.',self,[
							'TransferedPerturbationWeightFloatsArray'
						])
				]
			)
			'''

			#Check
			if SYS.getIsNullBool(
				self.TransferedRiseTimeVariable
			):

				#Check
				if SYS.getIsNullBool(
					self.TransferedDecayTimeVariable
				):
					
					#Check
					if SYS.getIsNullBool(
						self.TransferedDelayTimeVariable
					):

						#set
						self.TransferedSynapticPerturbationMethodVariable=None

					else:

						#set
						self.TransferedSynapticPerturbationMethodVariable=self.getSynapticDelayPerturbationVariable

				else:

					#set
					self.TransferedSynapticPerturbationMethodVariable=self.getSynapticDecayPerturbationVariable

			else:

				#set
				self.TransferedSynapticPerturbationMethodVariable=self.getSynapticRisePerturbationVariable

			#get
			self.TransferedNeuralPerturbationMethodVariable=getattr(
				self,
				'get'+self.TransferingInteractionStr+'NeuralPerturbationComplex'
			)

			#import 
			import itertools

			#list
			self.TransferedIndexIntsTuplesList=list(
				itertools.product(
					xrange(self.TransferingUnitsInt),
					xrange(self.TransferingUnitsInt)
				)
			)

			#debug
			'''
			self.debug(
				[
					'We set a one root get',
					('self.',self,[
							'TransferedIndexIntsTuplesList'
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
			self.TransferedDeterminantFunctionVariable=linalg.det

			#/################/#
			# Look for a rate instability
			#

			TransferedRateDetermintantFloatsTuple=self.getGlobalPerturbationRootFloatsTuple(
				(0.,0.)
			)

			#get
			self.TransferedIsStableBool=TransferedRateDetermintantFloatsTuple[0]>0.

			#debug
			""""
			self.debug(
				[
					'Is it rate instable ?',
					"TransferedRateDetermintantFloatsTuple is "+str(TransferedRateDetermintantFloatsTuple),
					('self.',self,[
							'TransferedTotalPerturbationComplexesArray',
							'TransferedFlatTotalPerturbationComplexesArray',
							'TransferedIsStableBool'
						])
				]
			)
			"""

			#Check
			if self.TransferedIsStableBool:

				#import 
				import scipy.optimize

				#debug
				"""
				self.debug(
					[
						"There is no rate instability so we do a Hopf scan analysis",
						('self.',self,['TransferingStabilityScanFrequencyVariable'])
					]
				)
				"""

				#type
				TransferedScanType=type(self.TransferingStabilityScanFrequencyVariable)

				#Check
				if TransferedScanType==None.__class__:

					#Check
					self.TransferedStabilityScanFrequencyFloatsArray=np.logspace(0,3,10)

				elif TransferedScanType in [np.float64,float]:

					#Check
					self.TransferedStabilityScanFrequencyFloatsArray=np.array(
						[self.TransferingStabilityScanFrequencyVariable]
					)

				else:

					#Check
					self.TransferedStabilityScanFrequencyFloatsArray=np.array(
						self.TransferingStabilityScanFrequencyVariable
					)

				#debug
				"""
				self.debug(
					[
						('self.',self,['TransferedStabilityScanFrequencyFloatsArray'])
					]
				)
				"""

				#loop
				for __ScanFrequencyFloat in self.TransferedStabilityScanFrequencyFloatsArray:
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
					TransferedOptimizeRoot=scipy.optimize.root(
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
							'TransferedOptimizeRoot is ',
							str(TransferedOptimizeRoot)
						]
					)
					"""

					#set
					self.TransferedOptimizeRoot=TransferedOptimizeRoot

					#Check
					if TransferedOptimizeRoot.success:

						#Check
						if TransferedOptimizeRoot.x[0]>0.:

							#set
							self.TransferedIsStableBool=False

							#set
							self.TransferedInstabilityStr="Hopf"

							#set
							self.TransferedInstabilityLambdaFloatsTuple=tuple(
								TransferedOptimizeRoot.x
							)

							#set
							self.TransferedInstabilityFrequencyFloat=self.TransferedInstabilityLambdaFloatsTuple[1]/(
								2.*np.pi
							)

							#break
							break


				#/################/#
				# Do tranfer maybe
				#

				#Check
				if self.TransferingDoTransferBool:

					#debug
					'''
					self.debug(
						[
							"We compute transfer here",
							('self.',self,[
									'TransferingTransferCurrentVariable'
								])
						]
					)
					'''

					#type
					TransferedTransferCurrentType=type(
						self.TransferingTransferCurrentVariable
					)

					#Check
					if TransferedTransferCurrentType==None.__class__:

						#array
						self.TransferedTransferCurrentFloatsArray=[1.]*self.TransferingUnitsInt

					elif TransferedTransferCurrentType in [np.float64,float]:

						#array
						self.TransferedTransferCurrentFloatsArray=[
								self.TransferingTransferCurrentVariable
							]*self.TransferingUnitsInt

					else:

						#array
						self.TransferedTransferCurrentFloatsArray=self.TransferingTransferCurrentVariable

					#array
					self.TransferedTransferCurrentFloatsArray=np.array(
						self.TransferedTransferCurrentFloatsArray
					)

					#import 
					import scipy.linalg

					#debug
					"""
					self.debug(
						[
							"we do a transfer scan analysis",
							('self.',self,['TransferingTransferScanFrequencyVariable'])
						]
					)
					"""

					#type
					TransferedScanType=type(self.TransferingTransferScanFrequencyVariable)

					#Check
					if TransferedScanType==None.__class__:

						#Check
						self.TransferedTransferScanFrequencyFloatsArray=np.logspace(0,3,10)

					elif TransferedScanType in [np.float64,float]:

						#Check
						self.TransferedTransferScanFrequencyFloatsArray=np.array(
							[self.TransferingTransferScanFrequencyVariable]
						)

					else:

						#Check
						self.TransferedTransferScanFrequencyFloatsArray=np.array(
							self.TransferingTransferScanFrequencyVariable
						)

					#debug
					"""
					self.debug(
						[
							('self.',self,['TransferedTransferScanFrequencyFloatsArray'])
						]
					)
					"""

					#init
					self.TransferedTransferRateComplexesArray=np.zeros(
							(
								self.TransferingUnitsInt,
								len(self.TransferedTransferScanFrequencyFloatsArray)
							),
							dtype=complex
						)
					self.TransferedTransferRateAmplitudeFloatsArray=np.zeros(
							(
								self.TransferingUnitsInt,
								len(self.TransferedTransferScanFrequencyFloatsArray)
							),
							dtype=float
						)
					self.TransferedTransferRatePhaseFloatsArray=np.zeros(
							(
								self.TransferingUnitsInt,
								len(self.TransferedTransferScanFrequencyFloatsArray)
							),
							dtype=float
						)

					#loop
					for __IndexInt,__ScanFrequencyFloat in enumerate(
						self.TransferedTransferScanFrequencyFloatsArray
					):

						#set
						self.TransferedPerturbationComplex=1j*2.*np.pi*__ScanFrequencyFloat

						#set
						self.setTransferedTotalPerturbationComplexesArray()

						#solve
						TransferedTransferRateComplexesArray = scipy.linalg.solve(
							self.TransferedTotalPerturbationComplexesArray,
							self.TransferedTransferCurrentFloatsArray
						)

						#lu
						self.TransferedTransferRateComplexesArray[
							:,
							__IndexInt
						]=TransferedTransferRateComplexesArray

						#amp and phase
						self.TransferedTransferRateAmplitudeFloatsArray[
							:,
							__IndexInt
						]=np.abs(
							TransferedTransferRateComplexesArray
						)
						self.TransferedTransferRatePhaseFloatsArray[
							:,
							__IndexInt
						]=np.angle(
							TransferedTransferRateComplexesArray
						)

					#debug
					'''
					self.debug(
						[
							'after the solve decomposition',
							('self.',self,[
								'TransferedTransferCurrentFloatsArray',
								'TransferedTransferRateComplexesArray',
								'TransferedTransferRateAmplitudeFloatsArray',
								'TransferedTransferRatePhaseFloatsArray'
							])	
						]
					)
					'''

					#find the Extremum
					self.NumscipiedFourierFrequencyFloatsArray=self.TransferedTransferScanFrequencyFloatsArray
					self.NumscipiedFourierAmplitudeFloatsArray=self.TransferedTransferRateAmplitudeFloatsArray
					self.NumscipiedFourierPhaseFloatsArray=self.TransferedTransferRatePhaseFloatsArray
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
				self.TransferedInstabilityStr="Rate"

			#debug
			'''
			self.debug(
				[
					'In the end ',
					('self.',self,[
						'TransferedTotalPerturbationComplexesArray',
						'TransferedDeterminantFloatsTuple',
						'TransferedIsStableBool',
						'TransferedInstabilityStr',
						'TransferedInstabilityLambdaFloatsTuple',
						'TransferedInstabilityFrequencyFloat'
					])
				]
			)
			'''
				
	def setTimeFloatsArray(self,_KeyStr):

		#get
		TransferingTimeVariable=getattr(
			self,
			'Transfering'+_KeyStr+'TimeVariable'
		)

		#type
		TransferedTimeType=type(TransferingTimeVariable)

		#Check
		if TransferedTimeType in [list,np.array]:

			#array
			setattr(
				self,
				'Transfered'+_KeyStr+'TimeVariable',
				np.array(
					TransferingTimeVariable
				)
			)

		else:

			#array
			setattr(
				self,
				'Transfered'+_KeyStr+'TimeVariable',
				#np.array(
					#[TransferingTimeVariable]*self.TransferingUnitsInt
				#)	
				TransferingTimeVariable
			)

	def getSynapticDelayPerturbationVariable(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'TransferedDelayTimeVariable'
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return SYS.setMatrixArray(
					np.ones(
								(self.TransferingUnitsInt,self.TransferingUnitsInt),
								dtype=complex
							),
					np.exp(
						-self.TransferedDelayTimeVariable*_PerturbationComplex
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
						'TransferedDecayTimeVariable',
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return SYS.setMatrixArray(
					SYS.setMatrixArray(
						self.getSynapticDelayPerturbationVariable(_PerturbationComplex),
						1.+self.TransferedDecayTimeVariable*_PerturbationComplex,
						np.ndarray.__div__,
						_AxisInt=1
					),
					1.+self.TransferedRiseTimeVariable*_PerturbationComplex,
					np.ndarray.__div__,
					_AxisInt=1
				)

	def getSynapticRisePerturbationVariable(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'TransferedRiseTimeVariable'
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return SYS.setMatrixArray(
					self.getSynapticRisePerturbationVariable(_PerturbationComplex),
					1.+self.TransferedRiseTimeVariable*_PerturbationComplex,
					np.ndarray.__div__,
					_AxisInt=1
				)			

	def getSynapticPerturbationVariable(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'TransferedDelayTimeVariable',
						'TransferedDecayTimeVariable',
						'TransferedRiseTimeVariable'
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
										(self.TransferingUnitsInt,self.TransferingUnitsInt),
										dtype=complex
									),
							np.exp(
								-self.TransferedDelayTimeVariable*_PerturbationComplex
							),
							np.ndarray.__mul__,
							_AxisInt=1
						),
						1.+self.TransferedDecayTimeVariable*_PerturbationComplex,
						np.ndarray.__div__,
						_AxisInt=1
					),
					1.+self.TransferedRiseTimeVariable*_PerturbationComplex,
					np.ndarray.__div__,
					_AxisInt=1
				)

	def getRateNeuralPerturbationComplex(self,_PerturbationComplex):

		#debug
		"""
		self.debug(
			[
				('self.',self,[
						'TransferedPerturbationNullVariable',
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		"""

		#return
		return self.TransferedPerturbationNullVariable/(
			1.+_PerturbationComplex*self.TransferedConstantTimeVariable
		)

	def getLeakNeuralPerturbationComplex(self,_PerturbationComplex):

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'TransferedConstantTimeVariable'
					]),
				'_PerturbationComplex is '+str(_PerturbationComplex)
			]
		)
		'''

		#return
		return 1.+_PerturbationComplex*self.TransferedConstantTimeVariable

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

	def setTransferedTotalPerturbationComplexesArray(self):

		#/###############/#
		# Prepare the complex pulsation perturbation
		# init TransferedTotalPerturbationComplexesArray

		#alias
		PerturbationComplex=self.TransferedPerturbationComplex

		#copy
		self.TransferedTotalPerturbationComplexesArray=-np.array(
			self.TransferedPerturbationWeightFloatsArray[:],
			dtype=complex
		)

		#/###############/#
		# Synaptic coupling
		#

		"""
		#exp
		self.TransferedSynapticPerturbationVariable=self.getSynapticPerturbationVariable(
				PerturbationComplex
			)

		#debug
		self.debug(
			[
				('self.',self,[
						'TransferedSynapticPerturbationVariable'
					])
			]
		)
		"""

		#Check
		if self.TransferedSynapticPerturbationMethodVariable!=None:

			#mul
			SYS.setMatrixArray(
				self.TransferedTotalPerturbationComplexesArray,
				self.TransferedSynapticPerturbationMethodVariable(
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
						'TransferedTotalPerturbationComplexesArray'
					])
			]
		)
		'''

		#/###############/#
		# Neural response coupling
		#

		#exp
		self.TransferedNeuralPerturbationComplex=self.TransferedNeuralPerturbationMethodVariable(
			PerturbationComplex
		)

		#debug
		"""
		self.debug(
			[
				('self.',self,[
						'TransferedNeuralPerturbationComplex',
						'TransferedNeuralPerturbationMethodVariable'
					])
			]
		)
		"""

		#mul
		SYS.setMatrixArray(
			self.TransferedTotalPerturbationComplexesArray,
			self.TransferedNeuralPerturbationMethodVariable(
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
						'TransferedTotalPerturbationComplexesArray'
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
			self.TransferedTotalPerturbationComplexesArray,
			self.getLeakNeuralPerturbationComplex(
					PerturbationComplex
				)+np.diag(
					self.TransferedTotalPerturbationComplexesArray
				)
		)
		"""

		#fill
		np.fill_diagonal(
			self.TransferedTotalPerturbationComplexesArray,
			1.+np.diag(
					self.TransferedTotalPerturbationComplexesArray
				)
		)


		#/###############/#
		# multiply all by the LeakNeuralPerturbationVariable
		#

		#get the numerator leak term
		TransferedLeakNeuralPerturbationVariable=self.getLeakNeuralPerturbationComplex(PerturbationComplex)

		#mul
		self.TransferedFlatTotalPerturbationComplexesArray=SYS.setMatrixArray(
			self.TransferedTotalPerturbationComplexesArray.T,
			TransferedLeakNeuralPerturbationVariable,
			np.ndarray.__mul__
		).T

		#debug
		"""
		self.debug(
			[
				"PerturbationComplex is "+str(PerturbationComplex),
				"TransferedLeakNeuralPerturbationVariable is "+str(TransferedLeakNeuralPerturbationVariable),
				('self.',self,[
						'TransferedTotalPerturbationComplexesArray',
						'TransferedFlatTotalPerturbationComplexesArray'
					])
			]
		)
		"""

	def getGlobalPerturbationRootFloatsTuple(self,_PerturbationFloatsTuple):

		#pack
		self.TransferedPerturbationComplex=_PerturbationFloatsTuple[
			0
		]+1j*_PerturbationFloatsTuple[
			1
		]

		#set
		self.setTransferedTotalPerturbationComplexesArray()

		#/###############/#
		# compute det
		#

		#det
		TransferedDeterminantComplex=self.TransferedDeterminantFunctionVariable(
			self.TransferedTotalPerturbationComplexesArray
		)
	
		#debug
		'''
		self.debug(
			[
				'In the end ',
				('self.',self,[
						'TransferedTotalPerturbationComplexesArray'
					]),
				'PerturbationComplex is '+str(PerturbationComplex),
				'TransferedDeterminantComplex is '+str(TransferedDeterminantComplex)
			]
		)
		'''

		#set
		self.TransferedDeterminantFloatsTuple=(
			TransferedDeterminantComplex.real,
			TransferedDeterminantComplex.imag
		)

		#return
		return self.TransferedDeterminantFloatsTuple


	def getStationaryRateRootFloat(self,_StationaryRateFloat):
			
		#return
		return 0.

	def getStationarySpikeRootFloat(self,_StationaryRateFloat):
			
		#center
		self.LifingStationaryCurrentFloat = 0.

		#noise
		self.LifingVoltageNoiseFloat = self.TransferingStdWeightFloat *  self.TransferingConstantTimeVariable * _StationaryRateFloat

		#lif
		self.lif()

		#return
		return self.LifedStationaryRateFloat

	"""
	def getStationarySpikeRootFloatsTuple(self,_StationaryRateFloatsTuple):
			
		#center
		LifingStationaryCurrentFloatsArray = np.dot(self.TransferedLateralWeightFloatsArray,_StationaryRateFloatsTuple)

		#noise
		LifingVoltageNoiseFloatsArray = self.TransferingStdWeightFloat *  self.TransferingConstantTimeVariable * _StationaryRateFloat

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
			if self.TransferingDoStabilityBool:

				#map
				map(
						lambda __KeyStr:
						self.forcePrint(
							[__KeyStr],
							'TransfererClass'
						)
						if getattr(
							self.PrintingCopyVariable,
							__KeyStr
						) not in [None,0.,""]
						else None,
						[
							'TransferingConstantTimeVariable',
							'TransferingDelayTimeVariable',
							'TransferingDecayTimeVariable',
							'TransferingRiseTimeVariable',
							'TransferedInstabilityStr',
							'TransferedInstabilityFrequencyFloat',
							'TransferedIsStableBool'
						]
					)

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=TransfererClass
#<DefineLocals>

#</DefinePrint>
TransfererClass.PrintingClassSkipKeyStrsList.extend(
	[
		'TransferingUnitsInt',
		'TransferingLateralWeightVariable',
		'TransferingConstantTimeVariable',
		'TransferingDelayTimeVariable',
		'TransferingDecayTimeVariable',
		'TransferingRiseTimeVariable',
		'TransferingMeanWeightFloat',
		'TransferingNormalisationInt',
		'TransferingSymmetryFloat',
		'TransferingDoStationaryBool',
		'TransferingDoStabilityBool',
		'TransferingDoTransferBool',
		'TransferingInteractionStr',
		'TransferingRestVariable',
		'TransferingStabilityScanFrequencyVariable',
		'TransferingTransferScanFrequencyVariable',
		'TransferingTransferCurrentVariable',
		'TransferedLateralWeightFloatsArray',
		'TransferedHalfHeightFloat',
		'TransferedLateralHalfWidthFloat',
		'TransferedMeanfieldWeightFloat',
		'TransferedEigenComplex',
		'TransferedEigenvalueComplexesArray',
		'TransferedPerturbationComplex',
		'TransferedPerturbationRealFloatsArray',
		'TransferedPerturbationImagFloatsArray',
		'TransferedInstabilityIndexInt',
		'TransferedInstabilityIndexInt',
		'TransferedInstabilityComplex',
		'TransferedInstablesInt',
		'TransferedIsStableBool',
		'TransferedInstabilityStr',
		'TransferedStdSparseFloat',
		'TransferedParentSingularStr',
		'TransferedIndexIntsTuplesList',
		'TransferedPerturbationNullVariable',
		'TransferedPerturbationWeightFloatsArray',
		'TransferedConstantTimeVariable',
		'TransferedDelayTimeVariable',
		'TransferedDecayTimeVariable',
		'TransferedRiseTimeVariable',
		'TransferedPerturbationComplex',
		'TransferedNeuralPerturbationComplex',
		'TransferedSynapticPerturbationComplexesArray',
		'TransferedSynapticPerturbationMethodVariable',
		'TransferedNeuralPerturbationMethodVariable',
		'TransferedTotalPerturbationComplexesArray',
		'TransferedFlatTotalPerturbationComplexesArray',
		'TransferedInstabilityLambdaFloatsTuple',
		'TransferedInstabilityFrequencyFloat',
		'TransferedDeterminantFunctionVariable',
		'TransferedDeterminantFloatsTuple',
		'TransferedStabilityScanFrequencyFloatsArray',
		'TransferedOptimizeRoot',
		'TransferedTransferScanFrequencyFloatsArray',
		'TransferedTransferCurrentFloatsArray',
		'TransferedTransferRateComplexesArray',
		'TransferedTransferRateAmplitudeFloatsArray',
		'TransferedTransferRatePhaseFloatsArray',
		'TransferedNetworkDeriveTransfererVariable'
	]
)
#<DefinePrint>