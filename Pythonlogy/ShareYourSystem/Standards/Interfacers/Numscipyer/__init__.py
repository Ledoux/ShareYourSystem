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
			_NumscipyingSpecificTagVariablesArray=None,
			_NumscipyingRowTagVariablesArray=None,
			_NumscipyingColTagVariablesArray=None,
			_NumscipiedDiscreteStatRigidFunction=None,
			_NumscipiedContinuousStatRigidFunction=None,
			_NumscipiedRandomFloatsArray=None,
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
			).rvs


		#/#################/#
		# Get the discrete stat
		#

		#init
		self.NumscipiedRandomFloatsArray=None

		#Check
		if self.NumscipyingProbabilityFloat>0.:

			#debug
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
						self.NumscipyingStdFloat*self.NumscipiedContinuousStatRigidFunction(
							self.NumscipyingMeanFloat
						)
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
								'NumscipyingStdFloat'
							])
					]
				)
				'''
				
				#set
				self.NumscipiedRandomFloatsArray=self.NumscipyingStdFloat*self.NumscipiedContinuousStatRigidFunction(
					self.NumscipyingMeanFloat,
					size=self.NumscipyingSizeTuple
				)

		#/#################/#
		# Normalize maybe 
		# 

		#Check
		if self.NumscipyingDivideVariable!=None:
			self.NumscipiedRandomFloatsArray=(
				self.NumscipiedRandomFloatsArray.T/self.NumscipyingDivideVariable
			).T
		
		#Check
		if self.NumscipyingNormalisationFunction!=None and len(
			self.NumscipyingSizeTuple) and self.NumscipyingSizeTuple[0]==self.NumscipyingSizeTuple[1]:

				#normalize
				self.NumscipiedRandomFloatsArray/=self.NumscipyingNormalisationFunction(
					self.NumscipyingSizeTuple[0]
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
			map(
					lambda __RowInt,__NumscipyingDiagFloat:
					self.NumscipiedRandomFloatsArray.__setitem__(
						(__RowInt,__RowInt),
						__NumscipyingDiagFloat
					),
					xrange(len(self.NumscipiedRandomFloatsArray)),
					self.NumscipyingDiagFloatsArray
				)

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
		'NumscipyingSpecificTagVariablesArray',
		'NumscipyingRowTagVariablesArray',
		'NumscipyingColTagVariablesArray',
		'NumscipiedDiscreteStatRigidFunction',
		'NumscipiedContinuousStatRigidFunction',
		'NumscipiedRandomFloatsArray'
	]
)
#<DefinePrint>
