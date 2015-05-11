# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Numscipyer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Processer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Numscipyer','Numscipy','Numscipying','Numscipied')
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
def getArgumentVariable(_ComplexVariable):

	#Debug
	'''
	print('l 31 Numscipier')
	print('_ComplexVariable is ')
	print(_ComplexVariable)
	print('')
	'''

	#return
	return 2.*np.arctan(
		np.imag(_ComplexVariable)/(
				np.sqrt(
					np.imag(
						_ComplexVariable
					)**2+np.real(
						_ComplexVariable
					)**2)+np.real(
						_ComplexVariable
					)
			)
		);
SYS.phase=getArgumentVariable
#</DefineLocals>


#<DefineClass>
@DecorationClass()
class NumscipyerClass(BaseClass):
	
	def default_init(self,
			_NumscipyingValueVariable=None,
			_NumscipyingRowsInt=0,
			_NumscipyingColsInt=0,
			_NumscipyingSizeTuple=None,
			_NumscipyingMeanFloat=0.,
			_NumscipyingStdFloat=1.,
			_NumscipyingProbabilityFloat=0.,
			_NumscipyingNormalisationFunction=None,
			_NumscipyingDivideVariable=None,
			_NumscipyingDiscreteStatStr="bernoulli",
			_NumscipyingContinuousStatStr="norm",
			_NumscipyingDiagFloatsArray=None,
			_NumscipyingSymmetryFloat=0.,
			_NumscipiedIndexIntsTuplesList=None,
			_NumscipiedNonNullIndexIntsTuplesList=None,
			_NumscipiedNullIndexIntsListsList=None,
			_NumscipiedNullIndexIntsTuplesList=None,
			_NumscipiedIsDisymmetrizeIndexIntsListsList=None,
			_NumscipiedToDissymetrizeIndexIntsTuplesList=None,
			_NumscipiedToDissymetricsInt=0,
			_NumscipiedIsDissymetricsInt=0,
			_NumscipiedDissymetryFunction=None,
			_NumscipyingSpecificTagVariablesArray=None,
			_NumscipyingRowTagVariablesArray=None,
			_NumscipyingColTagVariablesArray=None,
			_NumscipyingEigenvalueBool=False,
			_NumscipyingEigenvectorBool=False,
			_NumscipyingStatBool=True,
			_NumscipyingGlobalBool=False,
			_NumscipyingSampleFloatsArray=None,
			_NumscipiedDiscreteStatRigidFunction=None,
			_NumscipiedContinuousStatRigidFunction=None,
			_NumscipiedValueFloatsArray=None,
			_NumscipiedNormVariable=None,
			_NumscipiedSymmetricsInt=0,
			_NumscipiedVarianceFloat=0,
			_NumscipiedMeanFloat=0,
			_NumscipiedStdFloat=0,
			_NumscipiedCovarianceFloat=0,
			_NumscipiedSommersFloat=0.,
			_NumscipiedEigenvalueComplexesArray=None,
			_NumscipiedEigenvectorComplexesArray=None,
			_NumscipiedMeanGlobalFloatsArray=None,
			_NumscipiedStdGlobalFloatsArray=None,
			_NumscipiedSampleStepFloat=0.,
			_NumscipiedFourierFrequencyFloatsArray=None,
			_NumscipiedFourierAmplitudeFloatsArray=None,
			_NumscipiedFourierAmplitudeGlobalFloatsArray=None,
			_NumscipiedFourierPhaseFloatsArray=None,
			_NumscipiedFourierPhaseGlobalFloatsArray=None,
			_NumscipiedFourierMaxAmplitudeIndexIntsArray=None,
			_NumscipiedFourierMaxAmplitudeFloatsArray=None,
			_NumscipiedAutocorrelationFloatsArray=None,
			_NumscipiedAutocorrelationGlobalFloatsArray=None,
			_NumscipiedCrosscorrelationFloatsArray=None,
			**_KwargVariablesDict
		):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_numscipy(
				self
			):	

		#debug
		'''
		self.debug(
				[
					'We numscipy here',
				]
			)
		'''

		#/#################/#
		# Set the size of the matrix
		#

		#Check
		if type(self.NumscipyingValueVariable)==None.__class__:

			#debug
			'''
			self.debug(
				[
					'This is an array that we have to build'
				]
			)
			'''

			#set
			if self.NumscipyingSizeTuple==None or len(self.NumscipyingSizeTuple)==0 :

				#set
				self.NumscipyingSizeTuple=(
					self.NumscipyingRowsInt,
					self.NumscipyingColsInt
				)

			else:

				#set
				self.NumscipyingRowsInt=self.NumscipyingSizeTuple[0]
				self.NumscipyingColsInt=self.NumscipyingSizeTuple[1]


			#init
			self.NumscipiedValueFloatsArray=None

		else:

			#debug
			'''
			self.debug(
				[
					'This is an array already built'
				]
			)
			'''

			#set
			self.NumscipyingSizeTuple=np.shape(
				self.NumscipyingValueVariable
			)
			self.NumscipyingRowsInt=self.NumscipyingSizeTuple[0]
			self.NumscipyingColsInt=self.NumscipyingSizeTuple[1]

			#alias
			self.NumscipiedValueFloatsArray=self.NumscipyingValueVariable

		#debug
		'''
		self.debug(
			[
				'We have setted the shape of the matrix',
				('self.',self,['NumscipyingSizeTuple'])
			]
		)
		'''

		#/#################/#
		# Get the continuous stat
		#

		#Check
		if self.NumscipyingStdFloat>0.:

			#import
			import scipy.stats

			#get
			self.NumscipiedContinuousStatRigidFunction=getattr(
				scipy.stats,
				self.NumscipyingContinuousStatStr
			)(
				self.NumscipyingMeanFloat,
				self.NumscipyingStdFloat
			).rvs


		#/#################/#
		# Get the discrete stat
		#

		#Check
		if self.NumscipyingProbabilityFloat>0.:

			#debug
			'''
			self.debug(
				[
					'We numscipy here',
					'We set a discrete skeleton',
					('self.',self,[
							'NumscipyingDiscreteStatStr',
							'NumscipyingProbabilityFloat'
						])
				]
			)
			'''
			
			#/#################/#
			# Get a list of one or zero
			#

			#import
			import scipy.stats

			#get
			self.NumscipiedDiscreteStatRigidFunction=getattr(
				scipy.stats,
				self.NumscipyingDiscreteStatStr
			).rvs

			#prod
			NumscipiedSizeInt=np.prod(self.NumscipyingSizeTuple)

			#set
			NumscipiedRandomIntsArray=self.NumscipiedDiscreteStatRigidFunction(
				self.NumscipyingProbabilityFloat,
				size=NumscipiedSizeInt
			)

			#/#################/#
			# Maybe set a continuous stat for non zero values
			#

			#map
			if self.NumscipiedContinuousStatRigidFunction!=None:

				#Check
				self.NumscipiedValueFloatsArray=np.array(
					map(
						lambda __IndexInt,__BoolInt:
						self.NumscipiedContinuousStatRigidFunction()
						if __BoolInt==1
						else 0.,
						xrange(NumscipiedSizeInt),
						NumscipiedRandomIntsArray,
					)
				)


			else:

				#just floatify
				self.NumscipiedValueFloatsArray=self.NumscipyingMeanFloat*np.array(
					map(
						float,
						NumscipiedRandomIntsArray
					)
				)



			#reshape
			self.NumscipiedValueFloatsArray=self.NumscipiedValueFloatsArray.reshape(
				self.NumscipyingSizeTuple
			)

		#/#################/#
		# If it is a dense matrix then 
		# set direct all the matrix

		#Check
		if type(self.NumscipiedValueFloatsArray)==None.__class__:

			#debug
			'''
			self.debug(
				[
					'This is a random norm distribution',
					('self.',self,[
							'NumscipyingMeanFloat',
							'NumscipyingStdFloat',
							'NumscipiedContinuousStatRigidFunction'
						])
				]
			)
			'''

			#Check
			if self.NumscipiedContinuousStatRigidFunction!=None:

				#set
				self.NumscipiedValueFloatsArray=self.NumscipiedContinuousStatRigidFunction(
					size=self.NumscipyingSizeTuple
				)

			else:

				#set
				self.NumscipiedValueFloatsArray=self.NumscipyingMeanFloat*np.ones(
					self.NumscipyingSizeTuple
				)

		#debug
		'''
		self.debug(
			[
				'at this step',
				('self.',self,[
						'NumscipiedValueFloatsArray',
						'NumscipyingMeanFloat'
					])
			]
		)
		'''

		#/#################/#
		# Normalize maybe 
		# 

		#debug
		'''
		self.debug(
			[
				'Do we have to normalize',
				('self.',self,[
						'NumscipyingDivideVariable',
						'NumscipyingNormalisationFunction'
					])
			]
		)
		'''

		#Check
		if self.NumscipyingDivideVariable!=None:

			#divide
			self.NumscipiedValueFloatsArray=(
				self.NumscipiedValueFloatsArray.T/self.NumscipyingDivideVariable
			).T
		
		#Check
		if self.NumscipyingNormalisationFunction!=None and len(
			self.NumscipyingSizeTuple) and self.NumscipyingSizeTuple[0]==self.NumscipyingSizeTuple[1]:

				#set
				self.NumscipiedNormVariable=self.NumscipyingNormalisationFunction(
					self.NumscipyingSizeTuple[0]
				)

				#debug
				'''
				self.debug(
					[
						'We normalize with',
						'NumscipiedNormVariable is',
						str(NumscipiedNormVariable),
						('self.',self,[
								'NumscipyingStdFloat'
							])
					]
				)
				'''
				
				#normalize
				self.NumscipiedValueFloatsArray/=self.NumscipiedNormVariable

		#/#################/#
		# Symmetrize maybe 
		# 

		#set
		NumscipiedShiftSymmetryFloat=0.5*(self.NumscipyingSymmetryFloat+1.)

		#compute
		self.NumscipiedSymmetricsInt=(
			self.NumscipyingColsInt*(self.NumscipyingColsInt-1)
		)

		#Check
		if self.NumscipyingSymmetryFloat!=0.:

			#debug
			'''
			self.debug(
				[
					'We are going to symmetrize',
					('self.',self,[
						'NumscipyingSymmetryFloat'
					])

				]
			)
			'''

			#Check
			if self.NumscipyingProbabilityFloat==0. and self.NumscipyingStdFloat>0.:

				#/#################/#
				# This is a diluting symmetrization
				# 

				#debug
				self.debug(
					[
						'We do a diluted symmetrization'
					]
				)

				#import 
				import itertools

				#copy
				NumscipiedValueFloatsArray=self.NumscipiedValueFloatsArray[:]

				#build the scale factor
				"""
				#ERWAN version
				NumscipiedScaleFloat=(
					(
						self.NumscipyingSymmetryFloat-1.
					)*0.5
				)+1

				#Build a more or less DisSymmetricRandomArray
				self.NumscipiedValueFloatsArray=2.*(
					(NumscipiedScaleFloat/2.)*(NumscipiedValueFloatsArray+NumscipiedValueFloatsArray.T)
						+(0.5-(NumscipiedScaleFloat/2.))*(NumscipiedValueFloatsArray-NumscipiedValueFloatsArray.T)
					)
				"""

				#CELIAN version

				#compute
				NumscipiedScaleFloat = np.sqrt(
		        	NumscipiedShiftSymmetryFloat**2-NumscipiedShiftSymmetryFloat+0.5
		        )

		        #compute the anti-symm martix
				self.NumscipiedValueFloatsArray = (
					NumscipiedShiftSymmetryFloat * (
						NumscipiedValueFloatsArray + NumscipiedValueFloatsArray.T
					)/2. + (1.-NumscipiedShiftSymmetryFloat) * (
						NumscipiedValueFloatsArray - NumscipiedValueFloatsArray.T
					)/2.
				) / NumscipiedScaleFloat

				#fill diagonal
				np.fill_diagonal(
					NumscipiedValueFloatsArray,
					np.diagonal(self.NumscipiedValueFloatsArray)
				) 

			elif self.NumscipyingProbabilityFloat>0.:

				#/#################/#
				# This is a sparse symmetrization
				# 

				#debug
				'''
				self.debug(
					[
						'We do a targeted symmetrization',
						'First we keep only the upper part and triangularize',
						('self.',self,[
								'NumscipyingSymmetryFloat',
								'NumscipiedSymmetricsInt'
							])
					]
				)		
				'''

				#triu
				self.NumscipiedValueFloatsArray=np.triu(
					self.NumscipiedValueFloatsArray
				)
				self.NumscipiedValueFloatsArray=self.NumscipiedValueFloatsArray+(
					1. if self.NumscipyingSymmetryFloat>=0. else -1.
				)*self.NumscipiedValueFloatsArray.T-np.diag(
					np.diagonal(
							self.NumscipiedValueFloatsArray
						)
					)

				#import
				import itertools

				#filter the upper index tuples
				self.NumscipiedIndexIntsTuplesList=filter(
											lambda __Tuple:
											__Tuple[1]!=__Tuple[0],
											itertools.product(
												xrange(self.NumscipyingColsInt),
												xrange(self.NumscipyingColsInt)
											)
										)

				#/#################/#
				# group by the null and non null index tuples
				#

				#filter
				[
					self.NumscipiedNonNullIndexIntsTuplesList,
					self.NumscipiedNullIndexIntsTuplesList
				]=SYS.groupby(
					lambda __IndexIntsTuple:
					self.NumscipiedValueFloatsArray[
						__IndexIntsTuple
					]!=0.,
					self.NumscipiedIndexIntsTuplesList
				)

				#debug
				'''
				self.debug(
					[
						'Now',
						('self.',self,[
							'NumscipiedNonNullIndexIntsTuplesList'
						])
					]
				)
				'''

				#/#################/#
				# This is a sparse targeting symmetrization
				# 

				#debug
				'''
				self.debug(
					[
						'Ok we have built a sparse symmetric matrix',
						'We are going to dissymetrize by picking index tuples',
						'For now, we have just kept the upper values',
						('self.',self,[
							'NumscipiedIndexIntsTuplesList'
						]),
						'We are just going to pick the non null values',
					]
				)
				'''

				#/#################/#
				# determine a shuffle list of pair to dissymetrize
				#

				#int
				self.NumscipiedToDissymetricsInt=(int)(
					(1.-abs(self.NumscipyingSymmetryFloat))*len(
							self.NumscipiedNonNullIndexIntsTuplesList
					)
				)/2

				#copy
				self.NumscipiedToDissymetrizeIndexIntsTuplesList=self.NumscipiedNonNullIndexIntsTuplesList[:]

				#debug
				'''
				self.debug(
					[
						'Before shuffle',
						('self.',self,[
								'NumscipiedToDissymetrizeIndexIntsTuplesList'
							]),
						'We take the half of self.NumscipiedToDissymetricsInt for the targetting case'
					]
				)
				'''

				#Shuffle and pick the self.NumscipiedToDissymetricsInt/2
				np.random.shuffle(self.NumscipiedToDissymetrizeIndexIntsTuplesList)
				self.NumscipiedToDissymetrizeIndexIntsTuplesList=self.NumscipiedToDissymetrizeIndexIntsTuplesList[
					:(self.NumscipiedToDissymetricsInt/2)
				] if self.NumscipyingStdFloat==0 else self.NumscipiedToDissymetrizeIndexIntsTuplesList[
					:self.NumscipiedToDissymetricsInt
				]

				#debug
				'''
				self.debug(
					[
						'in the end',
						('self.',self,[
							#'NumscipiedNonNullIndexIntsTuplesList',
							'NumscipiedToDissymetrizeIndexIntsTuplesList',
							#'NumscipiedNullIndexIntsTuplesList',	
							'NumscipiedToDissymetricsInt'					
						]),
						'len(self.NumscipiedNonNullIndexIntsTuplesList) is ',
						str(len(self.NumscipiedNonNullIndexIntsTuplesList)),

					]
				)
				'''

				#/#################/#
				# prepare the other list of null tuples
				# in which we are going to transform

				#map
				self.NumscipiedNullIndexIntsListsList=map(
					lambda __IndexInt:
					[],
					xrange(self.NumscipyingColsInt)
				)

				#map
				map(
					lambda __NumscipiedNullIndexIntsTuple:
					self.NumscipiedNullIndexIntsListsList[
						__NumscipiedNullIndexIntsTuple[0]
					].append(
						__NumscipiedNullIndexIntsTuple[1]
					),
					self.NumscipiedNullIndexIntsTuplesList
				)

				#debug
				'''
				self.debug(
					[
						('self.',self,[
								'NumscipiedNullIndexIntsListsList'
							])
					]
				)
				'''

				#/#################/#
				# Now setSymmmetrize for each ToDissymetrize
				# 

				#map
				self.NumscipiedIsDisymmetrizeIndexIntsListsList=map(
					lambda __IndexInt:
					[],
					xrange(self.NumscipyingColsInt)
				)

				#init
				self.NumscipiedIsDissymetricsInt=0

				#set
				self.NumscipiedDissymetryFunction=(lambda : 0.) if self.NumscipyingStdFloat==0. else (
					(lambda : self.NumscipiedContinuousStatRigidFunction()/self.NumscipiedNormVariable)
					if self.NumscipiedNormVariable!=None else self.NumscipiedContinuousStatRigidFunction
				)

				#debug
				'''
				self.debug(
					[
						'before setDisymmetrize',
						('self.',self,[
								'NumscipiedDissymetryFunction'
							])
					]
				)
				'''

				#map
				map(
					lambda __NumscipiedToDissymetrizeIndexIntsTuple:
					self.setDisymmetrize(
						__NumscipiedToDissymetrizeIndexIntsTuple
					),
					self.NumscipiedToDissymetrizeIndexIntsTuplesList
				)
			
				#debug
				'''
				self.debug(
					[
						'In the end',
						('self.',self,
							[
								'NumscipiedToDissymetricsInt',
								'NumscipiedToDissymetrizeIndexIntsTuplesList',
								'NumscipiedIsDisymmetrizeIndexIntsListsList',
								'NumscipiedIsDissymetricsInt',
							]
						)
					]
				)
				'''

		#/#################/#
		# Maybe set a specific diagonal
		# 

		#Check
		if type(self.NumscipyingDiagFloatsArray)!=None.__class__ and len(
			self.NumscipyingDiagFloatsArray)==np.shape(
				self.NumscipiedValueFloatsArray
			)[0]:

			#debug
			'''
			self.debug(('self.',self,['NumscipyingDiagFloatsArray']))
			'''
			
			#map
			'''
			map(
					lambda __RowInt,__NumscipyingDiagFloat:
					self.NumscipiedValueFloatsArray.__setitem__(
						(__RowInt,__RowInt),
						__NumscipyingDiagFloat
					),
					xrange(len(self.NumscipiedValueFloatsArray)),
					self.NumscipyingDiagFloatsArray
				)
			'''

			#fill diagonal
			np.fill_diagonal(
				self.NumscipiedValueFloatsArray,
				np.diagonal(self.NumscipyingDiagFloatsArray)
			) 


		#/#################/#
		# Compute statistic
		# 

		#Check
		if self.NumscipyingStatBool and self.NumscipyingRowsInt==self.NumscipyingColsInt:

			#import
			import itertools

			#debug
			'''
			self.debug(
				[
					'We compute the variance',
					('self.',self,[
							'NumscipiedSymmetricsInt'
						])
				]
			)
			'''

			#list
			NumscipiedLateralIndexIntsList=list(
				itertools.product(
										xrange(self.NumscipyingRowsInt),
										xrange(self.NumscipyingColsInt)
									)
			)

			#variance
			self.NumscipiedMeanFloat=np.sum(
				np.array(
						filter(
								lambda __Float:
								__Float!=None,
								map(
									lambda __Tuple:
									self.NumscipiedValueFloatsArray[__Tuple]
									if __Tuple[0]!=__Tuple[1] else None
									,
									NumscipiedLateralIndexIntsList
								)
							)
						)
					)/(float(self.NumscipiedSymmetricsInt))

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'NumscipiedMeanFloat'
						])
				]
			)
			'''

			#variance
			self.NumscipiedVarianceFloat=np.sum(
				np.array(
					filter(
							lambda __Float:
							__Float!=None,
							map(
								lambda __Tuple:
								(
									self.NumscipiedValueFloatsArray[__Tuple]-self.NumscipiedMeanFloat
								)**2
								if __Tuple[0]!=__Tuple[1] else None
								,NumscipiedLateralIndexIntsList
							)
						)
					)
				)/(float(self.NumscipiedSymmetricsInt-1))

			#compute
			self.NumscipiedSommersFloat = (
				2.*NumscipiedShiftSymmetryFloat-1.
			)/(2.*NumscipiedShiftSymmetryFloat*(NumscipiedShiftSymmetryFloat-1.
				)+1.)

			#debug
			'''
			self.debug(
				[
					('self.',self,
						[
							'NumscipiedVarianceFloat',
							'NumscipiedSymmetricsInt'
						]
					)
				]
			)
			'''

			#deviation
			self.NumscipiedStdFloat=np.sqrt(self.NumscipiedVarianceFloat)

			#covariance
			self.NumscipiedCovarianceFloat=self.NumscipyingColsInt*np.sum(
						np.array(
								filter(
										lambda __Float:
										__Float!=None,
										map(
											lambda __Tuple:
			(
				self.NumscipiedValueFloatsArray[__Tuple]-self.NumscipiedMeanFloat
			)*(
				self.NumscipiedValueFloatsArray[(__Tuple[1],__Tuple[0])]-self.NumscipiedMeanFloat
			) 
											if __Tuple[0]!=__Tuple[1] else None
											,NumscipiedLateralIndexIntsList
										)
									)
								)
							)/(
							float(
								self.NumscipiedSymmetricsInt-1
							)
						)	

		#/#################/#
		# Get the eigenvalues
		#

		#Check
		if self.NumscipyingEigenvectorBool:
			
			pass

		#Check
		if self.NumscipyingEigenvalueBool:

			#debug
			'''
			self.debug(
				[
					'We compute the eigenvalues',
					('self.',self,[
							'NumscipiedValueFloatsArray'
						])
				]
			)
			'''

			#Check
			if self.NumscipyingSymmetryFloat==1.:

				#compute
				self.NumscipiedEigenvalueComplexesArray=np.linalg.eigvalsh(
					self.NumscipiedValueFloatsArray
				)
			else:

				#compute
				self.NumscipiedEigenvalueComplexesArray=np.linalg.eigvals(
					self.NumscipiedValueFloatsArray
				)

			#debug
			'''
			self.debug(
				[
					'We have computed the eigenvalues',
					('self.',self,[
							'NumscipiedEigenvalueComplexesArray'
						])
				]
			)
			'''

		#/#################/#
		# Compute Global
		# 

		#Check
		if self.NumscipyingGlobalBool:

			#debug
			'''
			self.debug(
				[
					'We compute some global properties'
				]
			)
			'''

			#/###############/#
			# Compute basic statistics
			#

			#mean
			self.NumscipiedMeanGlobalFloatsArray=self.NumscipiedValueFloatsArray.mean(
				axis=0
			)

			#std
			self.NumscipiedStdGlobalFloatsArray=self.NumscipiedValueFloatsArray.std(
				axis=0
			)

			#/###############/#
			# Compute fourier amp and phase
			#

			#import
			from scipy.fftpack import fft

			#set
			self.NumscipiedSampleStepFloat=self.NumscipyingSampleFloatsArray[
				1
			]-self.NumscipyingSampleFloatsArray[
				0
			]

			#linspace
			self.NumscipiedFourierFrequencyFloatsArray=np.linspace(
				0.0, 
				1.0/(2.0*self.NumscipiedSampleStepFloat),
				self.NumscipyingColsInt/2
			)

			#fft
			self.NumscipiedFourierGlobalComplexesArray=fft(
				self.NumscipiedStdGlobalFloatsArray
			)

			#amplitude
			self.NumscipiedFourierAmplitudeGlobalFloatsArray=(
					2.0/self.NumscipyingColsInt
				)* np.abs(
					self.NumscipiedFourierGlobalComplexesArray[
						0:self.NumscipyingColsInt/2
					]
				)

			#fourier
			self.NumscipiedFourierComplexesArray=np.array(
					map(
						lambda __NumscipiedValueFloatsArray:
						fft(
							__NumscipiedValueFloatsArray
						),
						self.NumscipiedValueFloatsArray
					)
				)

			#get
			NumscipiedHalfFourierComplexesArray=self.NumscipiedFourierComplexesArray[
						:,
						0:self.NumscipyingColsInt/2
					]

			#ampitude
			self.NumscipiedFourierAmplitudeFloatsArray=(
					2.0/float(self.NumscipyingColsInt)
				)* np.abs(
					NumscipiedHalfFourierComplexesArray
				)

			#phase
			self.NumscipiedFourierPhaseFloatsArray=np.array(
					map(
						lambda __NumscipiedHalfFourierComplexesArray:
						getArgumentVariable(
							__NumscipiedHalfFourierComplexesArray
						),
						NumscipiedHalfFourierComplexesArray
					)
				)

			#import
			import itertools

			#list
			NumscipiedCrossIndexIntsTuplesList=list(
				itertools.product(
					xrange(len(self.NumscipiedFourierPhaseFloatsArray)),
					xrange(len(self.NumscipiedFourierPhaseFloatsArray))
				)
			)

			#debug
			'''
			self.debug(
				[
					'NumscipiedCrossIndexIntsTuplesList is ',
					str(NumscipiedCrossIndexIntsTuplesList)
				]
			)
			'''

			#init
			NumscipiedNoneArray=np.array(
				[None]*len(self.NumscipiedFourierFrequencyFloatsArray)
			)
			NumscipiedNullArray=np.array(
				[0]*len(self.NumscipiedFourierFrequencyFloatsArray)
			)

			#cross phase
			NumscipiedFourierCrossPhaseTuplesList=map(
				lambda __NumscipiedCrossIndexIntsTuple:
				(
					__NumscipiedCrossIndexIntsTuple,
					self.NumscipiedFourierPhaseFloatsArray[
						__NumscipiedCrossIndexIntsTuple[0],
						:
					]-self.NumscipiedFourierPhaseFloatsArray[
						__NumscipiedCrossIndexIntsTuple[1],
						:
					]
				) 
				if __NumscipiedCrossIndexIntsTuple[1]>__NumscipiedCrossIndexIntsTuple[0]
				else (
						__NumscipiedCrossIndexIntsTuple,
						NumscipiedNullArray
					)
					if __NumscipiedCrossIndexIntsTuple[1]==__NumscipiedCrossIndexIntsTuple[0]
					else
					(
						__NumscipiedCrossIndexIntsTuple,
						NumscipiedNoneArray
					),	
				NumscipiedCrossIndexIntsTuplesList
			)

			#Debug
			'''
			print('NumscipiedFourierCrossPhaseTuplesList is ')
			print(NumscipiedFourierCrossPhaseTuplesList)
			print('')
			'''

			#arrayify
			self.NumscipiedFourierCrossPhaseFloatsArray=SYS.arrayify(
				NumscipiedFourierCrossPhaseTuplesList
			)

			#debug
			'''
			self.debug(
				[
					('self.',self,[ 
							'NumscipiedFourierCrossPhaseFloatsArray'
						])
				]
			)
			'''

			#/###############/#
			# Compute at max amplitudes
			#

			#argmax 
			self.NumscipiedFourierMaxAmplitudeIndexIntsArray=np.array(
				map(
					lambda __NumscipiedFourierAmplitudeFloatsArray:
					SYS.argmax(
						__NumscipiedFourierAmplitudeFloatsArray
					),
					self.NumscipiedFourierAmplitudeFloatsArray
				)
			)

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'NumscipiedFourierAmplitudeFloatsArray', 
							'NumscipiedFourierFrequencyFloatsArray',
							'NumscipiedFourierMaxAmplitudeIndexIntsArray'
						])
				]
			)
			'''

			#tuple freq and amp at max
			self.NumscipiedFourierMaxTupleFloatsArray=np.array(
				map(
					lambda __NumscipiedFourierMaxAmplitudeIndexIntsArray,__IndexInt:
					map(
						lambda __NumscipiedFourierMaxAmplitudeIndexInt:
						(
							self.NumscipiedFourierFrequencyFloatsArray[
								__NumscipiedFourierMaxAmplitudeIndexInt
							],
							self.NumscipiedFourierAmplitudeFloatsArray[
								__IndexInt,
								__NumscipiedFourierMaxAmplitudeIndexInt
							]
						),
						__NumscipiedFourierMaxAmplitudeIndexIntsArray
					),
					self.NumscipiedFourierMaxAmplitudeIndexIntsArray,
					xrange(len(self.NumscipiedFourierMaxAmplitudeIndexIntsArray))
				)
			)

			#debug
			'''
			self.debug(
				[
					('self.',self,[ 
							'NumscipiedFourierMaxTupleFloatsArray'
						])
				]
			)
			'''

			#array
			self.NumscipiedFourierMaxCrossPhaseFloatsArray=np.array(
				map(
					lambda __RowIndexInt,__NumscipiedFourierMaxAmplitudeIndexIntsArray:
					map(
						lambda __NumscipiedFourierMaxAmplitudeIndexInt:
						(
							self.NumscipiedFourierFrequencyFloatsArray[
								__NumscipiedFourierMaxAmplitudeIndexInt
							],
							map(
								lambda __ColIndexInt:
								self.NumscipiedFourierCrossPhaseFloatsArray[
									__RowIndexInt,__ColIndexInt,__NumscipiedFourierMaxAmplitudeIndexInt
								],
								xrange(len(self.NumscipiedFourierCrossPhaseFloatsArray))
							)
						),
						__NumscipiedFourierMaxAmplitudeIndexIntsArray
					),
					xrange(len(self.NumscipiedFourierMaxAmplitudeIndexIntsArray)),
					self.NumscipiedFourierMaxAmplitudeIndexIntsArray
				)
			)

			#debug
			self.debug(
				[
					('self.',self,[
							'NumscipiedFourierMaxCrossPhaseFloatsArray'
						])
				]
			)


			#	(
			#		xrange(self.NumscipyingColsInt),
			#		[0]*
			#	)

			"""
			NumscipiedFourierCrossPhaseDict=map(
				lambda __NumscipiedFourierCrossPhaseTuple:
				(
					__NumscipiedFourierCrossPhaseTuple[0][0],
					__NumscipiedFourierCrossPhaseTuple[1]
				),
				self.NumscipiedFourierCrossPhaseTuplesList
			)
			"""

			"""
			self.NumscipiedFourierMaxCrossPhaseFloatsArray=np.array(
				map(
					lambda __NumscipiedFourierMaxAmplitudeIndexIntsArray,__IndexInt:
					self.NumscipiedFourierCrossPhaseTuplesList[
						__IndexInt,
						:
					],
					self.NumscipiedFourierMaxAmplitudeIndexIntsArray,
					xrange(len(self.NumscipiedFourierMaxAmplitudeIndexIntsArray))
				)
			)
			"""

			#/###############/#
			# Compute correlations
			#

			#import
			from scipy import signal

			#acf
			self.NumscipiedAutocorrelationGlobalFloatsArray=signal.correlate(
				self.NumscipiedMeanGlobalFloatsArray,
				self.NumscipiedMeanGlobalFloatsArray,
				mode="same"
			)

			#cut
			#self.NumscipiedAutocorrelationGlobalFloatsArray=self.NumscipiedAutocorrelationGlobalFloatsArray[
			#	self.NumscipiedAutocorrelationGlobalFloatsArray.size/2:
			#]

			#debug
			'''
			self.debug(
				[
					'We computed the correlations',
					('self.',self,[
							'NumscipiedAutocorrelationGlobalFloatsArray'
						])
				]
			)
			'''

			#/###############/#
			# Compute local maxima
			#

			"""
			#Maxima
			self.NumscipiedMaxGlobalIndexIntsArray=SYS.argmax(
				self.NumscipiedMeanGlobalFloatsArray
			)
			
			#debug
			self.debug(
				[
					'We found the local extrema',
					('self.',self,[
							'NumscipiedMaxGlobalIndexIntsArray'
						])
				]
			)

			#map
			NumscipiedMaxIndexIntsArray=map(
				lambda __SimulatedFloatsArray:
				SYS.argmax(__SimulatedFloatsArray),
				SimulatedFloatsArray
			)
			"""


		#/#################/#
		# Reset to None
		# 

		#set
		self.NumscipiedDiscreteStatRigidFunction=None
		self.NumscipiedContinuousStatRigidFunction=None

	def setDisymmetrize(self,_IndexTuple):

		#debug
		'''
		self.debug(
			[
				'We setDisymmetrize here',
				'_IndexTuple is ',
				str(_IndexTuple),
				('self.',self,[
						'NumscipiedIsDisymmetrizeIndexIntsListsList'
					])
			]
		)
		'''

		#set
		NumscipiedNullIndexIntsList=self.NumscipiedNullIndexIntsListsList[
			_IndexTuple[0]
		]

		#Check
		if len(NumscipiedNullIndexIntsList)>0:

			#len
			NumscipiedTrialsInt=len(NumscipiedNullIndexIntsList)

			#init
			NumscipiedDissymetryBool=False

			#loop
			for __CountInt in xrange(NumscipiedTrialsInt):

				#rand
				NumscipiedRandomInt=np.random.randint(NumscipiedTrialsInt)

				#get
				NumscipiedColIndexInt=NumscipiedNullIndexIntsList[NumscipiedRandomInt]

				#debug
				'''
				self.debug(
					[
						'We try for',
						'NumscipiedRandomInt is '+str(NumscipiedRandomInt),
						'NumscipiedColIndexInt is '+str(NumscipiedColIndexInt),
						'__CountInt is '+str(__CountInt)
					]
				)
				'''

				#Check
				if _IndexTuple[0] not in self.NumscipiedIsDisymmetrizeIndexIntsListsList[
					NumscipiedColIndexInt
				]:

					#append
					self.NumscipiedIsDisymmetrizeIndexIntsListsList[
						NumscipiedColIndexInt 
					].append(
						_IndexTuple[0]
					)

					#/###############/#
					# Set to zero for sparse target 
					# or pick a new random

					#call
					NumscipiedDissymetryFloat=self.NumscipiedDissymetryFunction()

					#debug
					'''
					self.debug(
						[
							'We set to zero for sparse target',
							'Or pick a new random value for sparse dilute',
							'NumscipiedDissymetryFloat is '+str(NumscipiedDissymetryFloat)
						]
					)
					'''

					#temp
					NumscipiedTempFloat=self.NumscipiedValueFloatsArray[
						_IndexTuple[1], 
						_IndexTuple[0]
					]

					#set to zero for sparse 
					self.NumscipiedValueFloatsArray[
						_IndexTuple[1], 
						_IndexTuple[0]
					]=NumscipiedDissymetryFloat

					#Check
					if self.NumscipyingStdFloat==0:

						#debug
						'''
						self.debug(
							[
								'This is the targeting case where we have also to set something elsewhere ',
								'in the row to keep the number of incoming ones constant',
								'NumscipiedTempFloat is '+str(NumscipiedTempFloat)
							]
						)
						'''

						#set to 1
						self.NumscipiedValueFloatsArray[
							_IndexTuple[0], 
							NumscipiedColIndexInt
						]=NumscipiedTempFloat

					#remove
					NumscipiedNullIndexIntsList.pop(NumscipiedRandomInt)

					#set
					NumscipiedDissymetryBool=True

					#increment
					self.NumscipiedIsDissymetricsInt+=1

					#break
					break

			#Check
			if NumscipiedDissymetryBool==False:

				#debug
				self.debug(
					[
						'We could not find a good index'
					]
				)

		#debug
		'''
		self.debug(
			[
				('self.',self,[
					'NumscipiedToDissymetrizeIndexIntsTuplesList',
					'NumscipiedNullIndexIntsListsList',
					'NumscipiedIsDisymmetrizeIndexIntsListsList'
				])
			]
		)
		'''

		



	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Remove the num scipy array if None
			#

			#Check
			if type(self.NumscipiedValueFloatsArray)!=None.__class__:

				#get the shape
				ShapeList=np.shape(self.PrintingCopyVariable.NumscipiedValueFloatsArray)

				#get a str repr
				self.PrintingCopyVariable.NumscipiedValueFloatsArray='< numscipy array of shape '+str(ShapeList)+' >'

				#forcePrint
				self.forcePrint(
					['NumscipiedValueFloatsArray'],
					'NumscipierClass'
				)

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>


#</DefinePrint>
NumscipyerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'NumscipyingValueVariable',
		'NumscipyingRowsInt',
		'NumscipyingColsInt',
		'NumscipyingSizeTuple',
		'NumscipyingMeanFloat',
		'NumscipyingStdFloat',
		'NumscipyingProbabilityFloat',
		'NumscipyingNormalisationFunction',
		'NumscipyingDivideVariable',
		'NumscipyingDiscreteStatStr',
		'NumscipyingContinuousStatStr',
		'NumscipyingDiagFloatsArray',
		'NumscipyingSymmetryFloat',
		'NumscipyingSymmetryStr',
		'NumscipyingSpecificTagVariablesArray',
		'NumscipyingRowTagVariablesArray',
		'NumscipyingColTagVariablesArray',
		'NumscipyingStatBool',
		'NumscipyingGlobalBool',
		'NumscipyingSampleFloatsArray',
		'NumscipiedDiscreteStatRigidFunction',
		'NumscipiedContinuousStatRigidFunction',
		'NumscipiedValueFloatsArray',
		'NumscipiedNormVariable',
		'NumscipiedSymmetricsInt',
		'NumscipiedIndexIntsTuplesList',
		'NumscipiedNonNullIndexIntsTuplesList',
		'NumscipiedNullIndexIntsListsList',
		'NumscipiedNullIndexIntsTuplesList',
		'NumscipiedIsDisymmetrizeIndexIntsListsList',
		'NumscipiedToDissymetrizeIndexIntsTuplesList',
		'NumscipiedToDissymetricsInt',
		'NumscipiedIsDissymetricsInt',
		'NumscipiedDissymetryFunction',
		'NumscipiedVarianceFloat',
		'NumscipiedMeanFloat',
		'NumscipiedStdFloat',
		'NumscipiedCovarianceFloat',
		'NumscipiedSommersFloat',
		'NumscipyingEigenvalueBool',
		'NumscipyingEigenvectorBool',
		'NumscipiedEigenvalueComplexesArray',
		'NumscipiedEigenvectorComplexesArray',
		'NumscipiedMeanGlobalFloatsArray',
		'NumscipiedStdGlobalFloatsArray',
		'NumscipiedSampleStepFloat',
		'NumscipiedFourierFrequencyFloatsArray',
		'NumscipiedFourierAmplitudeFloatsArray',
		'NumscipiedFourierAmplitudeGlobalFloatsArray',
		'NumscipiedFourierPhaseFloatsArray',
		'NumscipiedFourierPhaseGlobalFloatsArray',
		'NumscipiedFourierMaxAmplitudeIndexIntsArray',
		'NumscipiedFourierMaxAmplitudeFloatsArray',
		'NumscipiedAutocorrelationFloatsArray',
		'NumscipiedAutocorrelationGlobalFloatsArray',
		'NumscipiedCrosscorrelationFloatsArray'
	]
)
#<DefinePrint>
