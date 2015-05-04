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

#<DefineClass>
@DecorationClass()
class NumscipyerClass(BaseClass):
	
	def default_init(self,
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
			_NumscipyingSymmetryStr='Fuzzy',
			_NumscipyingSpecificTagVariablesArray=None,
			_NumscipyingRowTagVariablesArray=None,
			_NumscipyingColTagVariablesArray=None,
			_NumscipyingEigenvalueBool=False,
			_NumscipyingEigenvectorBool=False,
			_NumscipyingStatBool=True,
			_NumscipiedDiscreteStatRigidFunction=None,
			_NumscipiedContinuousStatRigidFunction=None,
			_NumscipiedRandomFloatsArray=None,
			_NumscipiedSymmetricsInt=0,
			_NumscipiedVarianceFloat=0,
			_NumscipiedMeanFloat=0,
			_NumscipiedStdFloat=0,
			_NumscipiedCovarianceFloat=0,
			_NumscipiedSommersFloat=0.,
			_NumscipiedEigenvalueComplexesArray=None,
			_NumscipiedEigenvectorComplexesArray=None,
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

		#init
		self.NumscipiedRandomFloatsArray=None

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
				self.NumscipiedRandomFloatsArray=np.array(
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
				self.NumscipiedRandomFloatsArray=np.array(
					map(
						float,
						NumscipiedRandomIntsArray
					)
				)

			#reshape
			self.NumscipiedRandomFloatsArray=self.NumscipiedRandomFloatsArray.reshape(
				self.NumscipyingSizeTuple
			)

		#/#################/#
		# If it is a dense matrix then 
		# set direct all the matrix

		#Check
		if type(self.NumscipiedRandomFloatsArray)==None.__class__:

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
					self.NumscipiedRandomFloatsArray=self.NumscipiedContinuousStatRigidFunction(
						size=self.NumscipyingSizeTuple
					)

				else:

					#set
					self.NumscipiedRandomFloatsArray=self.NumscipyingMeanFloat*np.ones(
						self.NumscipyingSizeTuple
					)


		#debug
		'''
		self.debug(
			[
				'at this step',
				('self.',self,[
						'NumscipiedRandomFloatsArray',
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
			self.NumscipiedRandomFloatsArray=(
				self.NumscipiedRandomFloatsArray.T/self.NumscipyingDivideVariable
			).T
		
		#Check
		if self.NumscipyingNormalisationFunction!=None and len(
			self.NumscipyingSizeTuple) and self.NumscipyingSizeTuple[0]==self.NumscipyingSizeTuple[1]:

				#set
				NumscipiedNormVariable=self.NumscipyingNormalisationFunction(
					self.NumscipyingSizeTuple[0]
				)

				#debug
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

				#normalize
				self.NumscipiedRandomFloatsArray/=NumscipiedNormVariable

		#/#################/#
		# Symmetrize maybe 
		# 

		#set
		NumscipiedShiftSymmetryFloat=0.5*(self.NumscipyingSymmetryFloat+1.)

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

			#import 
			import itertools

			#copy
			NumscipiedRandomFloatsArray=self.NumscipiedRandomFloatsArray[:]

			

			#build the scale factor
			"""
			#ERWAN version
			NumscipiedScaleFloat=(
				(
					self.NumscipyingSymmetryFloat-1.
				)*0.5
			)+1

			#Build a more or less DisSymmetricRandomArray
			self.NumscipiedRandomFloatsArray=2.*(
				(NumscipiedScaleFloat/2.)*(NumscipiedRandomFloatsArray+NumscipiedRandomFloatsArray.T)
					+(0.5-(NumscipiedScaleFloat/2.))*(NumscipiedRandomFloatsArray-NumscipiedRandomFloatsArray.T)
				)
			"""

			#CELIAN version

			#compute
			NumscipiedScaleFloat = np.sqrt(
	        	NumscipiedShiftSymmetryFloat**2-NumscipiedShiftSymmetryFloat+0.5
	        )

	        #compute the anti-symm martix
			self.NumscipiedRandomFloatsArray = (
				NumscipiedShiftSymmetryFloat * (
					NumscipiedRandomFloatsArray + NumscipiedRandomFloatsArray.T
				)/2. + (1.-NumscipiedShiftSymmetryFloat) * (
					NumscipiedRandomFloatsArray - NumscipiedRandomFloatsArray.T
				)/2.
			) / NumscipiedScaleFloat

			#fill diagonal
			np.fill_diagonal(
				NumscipiedRandomFloatsArray,
				np.diagonal(self.NumscipiedRandomFloatsArray)
			) 		

		#/#################/#
		# Maybe set a specific diagonal
		# 

		#Check
		if type(self.NumscipyingDiagFloatsArray)!=None.__class__ and len(
			self.NumscipyingDiagFloatsArray)==np.shape(
				self.NumscipiedRandomFloatsArray
			)[0]:

			#debug
			'''
			self.debug(('self.',self,['NumscipyingDiagFloatsArray']))
			'''
			
			#map
			'''
			map(
					lambda __RowInt,__NumscipyingDiagFloat:
					self.NumscipiedRandomFloatsArray.__setitem__(
						(__RowInt,__RowInt),
						__NumscipyingDiagFloat
					),
					xrange(len(self.NumscipiedRandomFloatsArray)),
					self.NumscipyingDiagFloatsArray
				)
			'''

			#fill diagonal
			np.fill_diagonal(
				self.NumscipiedRandomFloatsArray,
				np.diagonal(self.NumscipyingDiagFloatsArray)
			) 


		#/#################/#
		# Compute statistic
		# 

		#Check
		if self.NumscipyingStatBool and self.NumscipyingRowsInt==self.NumscipyingColsInt:

			#import
			import itertools

			#compute
			self.NumscipiedSymmetricsInt=(
				self.NumscipyingColsInt*(self.NumscipyingColsInt-1)
			)

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
									self.NumscipiedRandomFloatsArray[__Tuple]
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
									self.NumscipiedRandomFloatsArray[__Tuple]-self.NumscipiedMeanFloat
								)**2
								if __Tuple[0]!=__Tuple[1] else None
								,NumscipiedLateralIndexIntsList
							)
						)
					)
				)/(float(self.NumscipiedSymmetricsInt-1))

			#
			self.NumscipiedSommersFloat = (
				2.*NumscipiedShiftSymmetryFloat-1.
			)/(2.*NumscipiedShiftSymmetryFloat*(NumscipiedShiftSymmetryFloat-1.
				)+1.)

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
				self.NumscipiedRandomFloatsArray[__Tuple]-self.NumscipiedMeanFloat
			)*(
				self.NumscipiedRandomFloatsArray[(__Tuple[1],__Tuple[0])]-self.NumscipiedMeanFloat
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
							'NumscipiedRandomFloatsArray'
						])
				]
			)
			'''

			#Check
			if self.NumscipyingSymmetryFloat==1.:

				#compute
				self.NumscipiedEigenvalueComplexesArray=np.linalg.eigvalsh(
					self.NumscipiedRandomFloatsArray
				)
			else:

				#compute
				self.NumscipiedEigenvalueComplexesArray=np.linalg.eigvals(
					self.NumscipiedRandomFloatsArray
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
		# Reset to None
		# 

		#set
		self.NumscipiedDiscreteStatRigidFunction=None
		self.NumscipiedContinuousStatRigidFunction=None

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
			if type(self.NumscipiedRandomFloatsArray)!=None.__class__:

				#get the shape
				ShapeList=np.shape(self.PrintingCopyVariable.NumscipiedRandomFloatsArray)

				#get a str repr
				self.PrintingCopyVariable.NumscipiedRandomFloatsArray='< numscipy array of shape '+str(ShapeList)+' >'

				#forcePrint
				self.forcePrint(
					['NumscipiedRandomFloatsArray'],
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
		'NumscipiedDiscreteStatRigidFunction',
		'NumscipiedContinuousStatRigidFunction',
		'NumscipiedRandomFloatsArray',
		'NumscipiedSymmetricsInt',
		'NumscipiedVarianceFloat',
		'NumscipiedMeanFloat',
		'NumscipiedStdFloat',
		'NumscipiedCovarianceFloat',
		'NumscipiedSommersFloat',
		'NumscipyingEigenvalueBool',
		'NumscipyingEigenvectorBool',
		'NumscipiedEigenvalueComplexesArray',
		'NumscipiedEigenvectorComplexesArray'
	]
)
#<DefinePrint>
