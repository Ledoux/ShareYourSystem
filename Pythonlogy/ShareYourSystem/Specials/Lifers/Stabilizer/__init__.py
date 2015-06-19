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
			_StabilizingConstantTimeVariable = None,
			_StabilizingDelayTimeVariable = 0.002,
			_StabilizingDecayTimeVariable = 0.,
			_StabilizingRiseTimeVariable = 0.,
			_StabilizingScanFrequencyVariable = None,
			_StabilizedConstantTimeVariable = None,
			_StabilizedDelayTimeVariable = None,
			_StabilizedDecayTimeVariable = None,
			_StabilizedRiseTimeVariable = None,
			_StabilizedParentSingularStr = "",
			_StabilizedNetworkDeriveStationarizerVariable = None,
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
		# Determine the time constant structures
		# 

		#set
		self.StabilizingConstantTimeVariable=self.StaionarizingConstantTimeVariable

		#map
		map(
			lambda __TimeStr:
			SYS.setInitArray(
				self,
				'Stabilize',
				__TimeStr+'Time'
			),
			[
				'Constant',
				'Delay',
				'Decay',
				'Rise'
			]
		)

		#/###################/#
		# Determine the null perturb solutions
		# 

		#Check
		if self.HopfingDoStabilityBool:

			#Check
			if self.HopfingInteractionStr=="Rate":

				#ones
				#self.HopfedPerturbationNullVariable=np.ones(
				#	self.HopfingUnitsInt
				#)

				self.HopfedPerturbationNullVariable=1.

			elif self.LeakingInteractionStr=="Spike":

				#set
				self.LifingConstantTimeFloat = self.LeakingTimeVariable
				self.LifingVoltageResetFloat = self.LeakingResetVariable
				self.LifingVoltageThresholdFloat = self.LeakingThresholdVariable
				self.LifingStationaryCurrentFloat = 0.
				#self.LifingVoltageNoiseFloat = self.Hopfing
				#self.Lifing
 

 		#/###################/#
		# Build the always fixed terms of the perturbation matrix
		# 

		#debug
		'''
		self.debug(
			[
				'We compute the StabilizedPerturbationWeightFloatsArray',
				('self.',self,[
						'StabilizedPerturbationNullVariable',
						'StabilizedConstantTimeVariable'
					])
			]
		)
		'''

		#set
		self.StabilizedPerturbationWeightFloatsArray=self.StationarizedLateralWeightFloatsArray[
			:
		]

		#mul
		SYS.setMatrixArray(
			self.StabilizedPerturbationWeightFloatsArray,
			self.StabilizedConstantTimeVariable,
			np.ndarray.__mul__
		)

		#debug
		self.debug(
			[
				'In the end',
				('self.',self,[
						'StabilizedPerturbationWeightFloatsArray'
					])
			]
		)

		#/###################/#
		# Determine which function to get for the synaptic computation
		#

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

		#/###################/#
		# Prepare the combinations to consider
		#

		#import 
		import itertools

		#list
		self.StabilizedIndexIntsTuplesList=list(
			itertools.product(
				xrange(self.StabilizingUnitsInt),
				xrange(self.StabilizingUnitsInt)
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

		#get
		self.StabilizedNeuralPerturbationMethodVariable=getattr(
			self,
			'get'+self.StabilizingInteractionStr+'NeuralNullPerturbationComplex'
		)

		#get
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

		#/################/#
		# Look for a hopf instability
		#

		#Check
		if self.StabilizedIsStableBool:

			#import 
			import scipy.optimize


			#get
			self.StabilizedNeuralPerturbationMethodVariable=getattr(
				self,
				'get'+self.StabilizingInteractionStr+'NeuralPerturbationComplex'
			)

			#debug
			"""
			self.debug(
				[
					"There is no rate instability so we do a Hopf scan analysis",
					('self.',self,['StabilizingScanFrequencyVariable'])
				]
			)
			"""

			#type
			StabilizedScanType=type(self.StabilizingScanFrequencyVariable)

			#Check
			if StabilizedScanType==None.__class__:

				#Check
				self.StabilizedStabilityScanFrequencyFloatsArray=np.logspace(0,3,10)

			elif StabilizedScanType in [np.float64,float]:

				#Check
				self.StabilizedStabilityScanFrequencyFloatsArray=np.array(
					[self.StabilizingScanFrequencyVariable]
				)

			else:

				#Check
				self.StabilizedStabilityScanFrequencyFloatsArray=np.array(
					self.StabilizingScanFrequencyVariable
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
								(self.StabilizingUnitsInt,self.StabilizingUnitsInt),
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
										(self.StabilizingUnitsInt,self.StabilizingUnitsInt),
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
		self.LifingVoltageNoiseFloat = self.StabilizingStdWeightFloat *  self.StabilizingConstantTimeVariable * _StationaryRateFloat

		#lif
		self.lif()

		#return
		return self.LifedStationaryRateFloat

	"""
	def getStationarySpikeRootFloatsTuple(self,_StationaryRateFloatsTuple):
			
		#center
		LifingStationaryCurrentFloatsArray = np.dot(self.StabilizedLateralWeightFloatsArray,_StationaryRateFloatsTuple)

		#noise
		LifingVoltageNoiseFloatsArray = self.StabilizingStdWeightFloat *  self.StabilizingConstantTimeVariable * _StationaryRateFloat

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
			if self.StabilizingDoStabilityBool:

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
							'StabilizingConstantTimeVariable',
							'StabilizingDelayTimeVariable',
							'StabilizingDecayTimeVariable',
							'StabilizingRiseTimeVariable',
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
		'StabilizingUnitsInt',
		'StabilizingDelayTimeVariable',
		'StabilizingDecayTimeVariable',
		'StabilizingRiseTimeVariable',
		'StabilizingScanFrequencyVariable',
		'StabilizedParentSingularStr',
		'StabilizedNetworkDeriveStationarizerVariable'
	]
)
#<DefinePrint>