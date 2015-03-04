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
BaseModuleStr="ShareYourSystem.Standards.Controllers.Controller"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import scipy.stats
import numpy as np
from matplotlib import pyplot
#</ImportSpecificModules>

#<DefineLocals>
def getNullFloatsArray(_FloatsArray, _RtolFloat=1e-5):
	u, s, v = np.linalg.svd(_FloatsArray)
	RankInt = (s > _RtolFloat*s[0]).sum()
	return v[RankInt:].T.copy()

def getKrenelFloatsArray(
		_LevelFloatsTuple=None,
		_TimeFloatsTuple=None,
		_RunTimeFloat=100.,
		_StepTimeFloat=0.1,
	):

	#get the bins
	BinsInt=_RunTimeFloat/_StepTimeFloat

	#init
	KrenelFloatsArray=_LevelFloatsTuple[0]*np.ones(
		BinsInt,
		dtype=type(_LevelFloatsTuple[0])
	)

	#Debug
	'''
	print('getKrenelFloatsArray')
	print('_TimeFloatsTuple[0]/_StepTimeFloat:_TimeFloatsTuple[1]/_StepTimeFloat')
	print(_TimeFloatsTuple[0]/_StepTimeFloat,_TimeFloatsTuple[1]/_StepTimeFloat)
	print('_LevelFloatsTuple[1] is '+str(_LevelFloatsTuple[1]))
	print('')
	'''

	#put the second level
	KrenelFloatsArray[
		int(_TimeFloatsTuple[0]/_StepTimeFloat):int(_TimeFloatsTuple[1]/_StepTimeFloat)
	]=_LevelFloatsTuple[1]

	#return
	return KrenelFloatsArray

#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PrediraterClass(BaseClass):
	
	def default_init(self,

						_PrediratingRateUnitsInt=0,
						_PrediratingSensorUnitsInt=0,

						_PrediratingRunTimeFloat=100.,
						_PrediratingStepTimeFloat=0.1,
						_PrediratedTimeFloatsArray=None,
						
						_PrediratedCommandFloatsArray=None,
						_PrediratedJacobianFloatsArray=None,
						
						_PrediratedInputRandomFloatsArray=None,
						_PrediratedInputPerturbativeWeigthFloatsArray=None,
						_PrediratedNullFloatsArray=None,
						
						_PrediratedLateralWeigthFloatsArray=None,
						_PrediratedLateralRandomFloatsArray=None,
						
						_PrediratedInitialSensorFloatsArray=None,
						_PrediratedInitialRateFloatsArray=None,
						
						_PrediratedSensorFloatsArray=None,
						_PrediratedPerturbativeRateFloatsArray=None,
						_PrediratedExactRateFloatsArray=None,
						_PrediratedLeakRateFloatsArray=None,
						
						_PrediratedPerturbativeDecoderFloatsArray=None,
						_PrediratedExactDecoderFloatsArray=None,
						_PrediratedLeakDecoderFloatsArray=None,
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_predirate(self):
		
		#/#################/#
		# External care : Prepare time and the command
		#

		#arange
		self.PrediratedTimeFloatsArray=np.arange(
			0.,
			self.PrediratingRunTimeFloat,
			self.PrediratingStepTimeFloat
		)

		#array
		self.PrediratedCommandFloatsArray=np.array(
			map(
				lambda __IndexInt:
				getKrenelFloatsArray(
					[0.,1.],
					[self.PrediratingRunTimeFloat/4.,self.PrediratingRunTimeFloat/2.]
				),
				xrange(self.PrediratingSensorUnitsInt)
			)
		)

		#debug
		'''
		self.debug(
			[
				'We have prepared the time and the commands',
				('self.',self,['PrediratedCommandFloatsArray'])
			]
		)
		'''

		#/#################/#
		# Sensor care : Prepare the input weigth and the null matrix
		#

		self.PrediratedJacobianFloatsArray=-np.diag(
			np.ones(
				self.PrediratingSensorUnitsInt
			)
		)

		#debug
		'''
		self.debug(
			[
				'We have prepared the sensor jacobian',
				('self.',self,['PrediratedJacobianFloatsArray'])
			]
		)
		'''

		#/#################/#
		# Rate care : Prepare the input weigth, null matrix, exact and perturbativ matrix
		#

		#random
		self.PrediratedDecoderWeigthFloatsArray=scipy.stats.uniform.rvs(
			size=(
				self.PrediratingSensorUnitsInt,
				self.PrediratingRateUnitsInt
			)
		)
		
		#find the null space
		self.PrediratedNullFloatsArray=getNullFloatsArray(
			self.PrediratedDecoderWeigthFloatsArray
		)

		#debug
		'''
		PrediratedProductArray=np.dot(self.PrediratedDecoderWeigthFloatsArray,self.PrediratedNullFloatsArray)
		self.debug(
				[
					('self.',self,[
						'PrediratedDecoderWeigthFloatsArray',
						'PrediratingRateUnitsInt'
						]
					),
					("locals()['",locals(),['PrediratedProductArray'],"']")
				]
			)
		'''

		#random
		self.PrediratedInputRandomFloatsArray=scipy.stats.uniform.rvs(
			size=(
				np.shape(self.PrediratedNullFloatsArray)[1],
				self.PrediratingSensorUnitsInt
			)
		)

		#dot
		self.PrediratedInputPerturbativeWeigthFloatsArray=0.*np.dot(
				self.PrediratedNullFloatsArray,
				self.PrediratedInputRandomFloatsArray
			)

		#dot
		self.PrediratedLateralExactWeigthFloatsArray=np.dot(
				self.PrediratedDecoderWeigthFloatsArray.T,
				self.PrediratedDecoderWeigthFloatsArray
			)

		#random
		self.PrediratedLateralRandomFloatsArray=scipy.stats.uniform.rvs(
			size=(
				self.PrediratingRateUnitsInt,
				self.PrediratingRateUnitsInt
			)
		)

		#dot
		self.PrediratedLateralPerturbativeWeigthFloatsArray=0.*np.dot(
				np.shape(self.PrediratedNullFloatsArray)[1],
				self.PrediratedLateralRandomFloatsArray
			)

		#pinv
		self.PrediratedLeakDecoderWeigthFloatsArray=np.linalg.pinv(
				self.PrediratedDecoderWeigthFloatsArray.T
			)

		#debug
		'''
		PrediratedPinvFloatsArray=np.dot(
			self.PrediratedLeakDecoderWeigthFloatsArray,
			self.PrediratedDecoderWeigthFloatsArray.T
		)
		self.debug(
			[
				'PrediratedPinvFloatsArray is ',
				str(PrediratedPinvFloatsArray)
			]
		)
		'''

		#/#################/#
		# Prepare the initial conditions
		#

		#random sensors
		PrediratedInitialRateFloatsArray=scipy.stats.uniform.rvs(
			size=self.PrediratingRateUnitsInt
		)

		#random rates
		PrediratedInitialSensorFloatsArray=scipy.stats.uniform.rvs(
			size=self.PrediratingSensorUnitsInt
		)

		#init sensors
		self.PrediratedSensorFloatsArray=np.zeros(
				(self.PrediratingSensorUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedSensorFloatsArray[:,0]=PrediratedInitialSensorFloatsArray

		#init perturbative rates
		self.PrediratedPerturbativeRateFloatsArray=np.zeros(
				(self.PrediratingRateUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedPerturbativeRateFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init exact rates
		self.PrediratedExactRateFloatsArray=np.zeros(
				(self.PrediratingRateUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedExactRateFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init leak control rates
		self.PrediratedLeakRateFloatsArray=np.zeros(
				(self.PrediratingRateUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedLeakRateFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init decoder
		self.PrediratedPerturbativeDecoderFloatsArray=np.zeros(
				(self.PrediratingSensorUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedPerturbativeDecoderFloatsArray[:,0]=np.dot(
				self.PrediratedDecoderWeigthFloatsArray,
				PrediratedInitialRateFloatsArray
			)

		#init leak control decoder
		self.PrediratedLeakDecoderFloatsArray=np.zeros(
				(self.PrediratingSensorUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedLeakDecoderFloatsArray[:,0]=np.dot(
				self.PrediratedLeakDecoderWeigthFloatsArray,
				PrediratedInitialRateFloatsArray
			)

		#/#################/#
		# integrativ Loop
		#

		#for loop
		for __IndexInt in xrange(1,len(self.PrediratedTimeFloatsArray)):

			#/#################/#
			# Sensor part
			#

			#debug
			'''
			self.debug(
					[
						'shape(self.PrediratedCommandFloatsArray) is '+str(
							np.shape(self.PrediratedCommandFloatsArray)
						),
						'shape(self.PrediratedSensorFloatsArray) is '+str(
							np.shape(self.PrediratedSensorFloatsArray)
						),
						('self.',self,[
							'PrediratedJacobianFloatsArray'
						])
					]
				)
			'''

			#Current
			PrediratedSensorCurrentFloatsArray=np.dot(
				self.PrediratedJacobianFloatsArray,
				self.PrediratedSensorFloatsArray[:,__IndexInt-1]
			)+self.PrediratedCommandFloatsArray[:,__IndexInt]

			#Euler
			self.PrediratedSensorFloatsArray[
				:,
				__IndexInt
			]=self.PrediratedSensorFloatsArray[
				:,
				__IndexInt-1
			]+PrediratedSensorCurrentFloatsArray*self.PrediratingStepTimeFloat

			#/#################/#
			# Perturbative Rate part
			#

			#Input Current
			PrediratedRateCurrentFloatsArray=np.dot(
				self.PrediratedDecoderWeigthFloatsArray.T+self.PrediratedInputPerturbativeWeigthFloatsArray,
				self.PrediratedSensorFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PrediratedRateCurrentFloatsArray-=np.dot(
				self.PrediratedLateralExactWeigthFloatsArray+self.PrediratedLateralPerturbativeWeigthFloatsArray,
				self.PrediratedPerturbativeRateFloatsArray[:,__IndexInt-1]
			)
			
			#Euler
			self.PrediratedPerturbativeRateFloatsArray[
				:,
				__IndexInt
			]=self.PrediratedPerturbativeRateFloatsArray[
				:,
				__IndexInt-1
			]+PrediratedRateCurrentFloatsArray*self.PrediratingStepTimeFloat

			#/#################/#
			# Exact Rate part
			#

			#Input Current
			PrediratedRateExactCurrentFloatsArray=np.dot(
				self.PrediratedDecoderWeigthFloatsArray.T,
				self.PrediratedSensorFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PrediratedRateExactCurrentFloatsArray-=np.dot(
				self.PrediratedLateralExactWeigthFloatsArray,
				self.PrediratedPerturbativeRateFloatsArray[:,__IndexInt-1]
			)
			
			#Euler
			self.PrediratedExactRateFloatsArray[
				:,
				__IndexInt
			]=self.PrediratedExactRateFloatsArray[
				:,
				__IndexInt-1
			]+PrediratedRateExactCurrentFloatsArray*self.PrediratingStepTimeFloat


			#/#################/#
			# Leak Control Rate part
			#

			#Input Current
			PrediratedLeakRateCurrentFloatsArray=np.dot(
				self.PrediratedDecoderWeigthFloatsArray.T+self.PrediratedInputPerturbativeWeigthFloatsArray,
				self.PrediratedSensorFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PrediratedLeakRateCurrentFloatsArray-=np.dot(
				np.diag(np.ones(self.PrediratingRateUnitsInt)),
				self.PrediratedLeakRateFloatsArray[:,__IndexInt-1]
			)
			
			#Euler
			self.PrediratedLeakRateFloatsArray[
				:,
				__IndexInt
			]=self.PrediratedLeakRateFloatsArray[
				:,
				__IndexInt-1
			]+PrediratedLeakRateCurrentFloatsArray*self.PrediratingStepTimeFloat

			#/#################/#
			# Decoder part
			#

			#dot
			self.PrediratedPerturbativeDecoderFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PrediratedPerturbativeDecoderWeigthFloatsArray,
					self.PrediratedPerturbativeRateFloatsArray[:,__IndexInt-1]
				)

			#exact control
			self.PrediratedExactDecoderFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PrediratedExactDecoderWeigthFloatsArray,
					self.PrediratedExactRateFloatsArray[:,__IndexInt-1]
				)

			#leak control
			self.PrediratedLeakDecoderFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PrediratedLeakDecoderWeigthFloatsArray,
					self.PrediratedLeakRateFloatsArray[:,__IndexInt-1]
				)


		#/#################/#
		# Plot
		#

		#debug
		self.debug(
			[
				'len(self.PrediratedTimeFloatsArray) is '+str(len(self.PrediratedTimeFloatsArray)),
				'np.shape(self.PrediratedCommandFloatsArray) is '+str(np.shape(self.PrediratedCommandFloatsArray))
			]
		)

		#init
		pyplot.figure()

		#/#################/#
		# Command and sensors
		#

		#subplot
		PrediratedSensorAxis=pyplot.subplot(3,1,1)

		#command
		map(
				lambda __IndexInt:
				PrediratedSensorAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedCommandFloatsArray[__IndexInt]
					)
				if __IndexInt<len(self.PrediratedCommandFloatsArray)
				else None,
				[0]
			)

		#sensor
		map(
				lambda __IndexInt:
				PrediratedSensorAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedSensorFloatsArray[__IndexInt,:],
						color='g',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedSensorFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedSensorAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedSensorAxis.set_ylim([-0.1,3.])

		#/#################/#
		# rates
		#

		#subplot
		PrediratedRateAxis=pyplot.subplot(3,1,2)

		#perturbative
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedPerturbativeRateFloatsArray[__IndexInt,:],
						color='b',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeRateFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedPerturbativeRateFloatsArray[__IndexInt,:],
						color='b',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeRateFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedLeakRateFloatsArray[__IndexInt,:],
						color='violet',
						linewidth=1
					)
				if __IndexInt<len(self.PrediratedLeakRateFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedRateAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedRateAxis.set_ylim([-0.1,1.])

		#/#################/#
		# decoders
		#

		#subplot
		PrediratedDecoderAxis=pyplot.subplot(3,1,3)

		#sensor
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedSensorFloatsArray[__IndexInt],
						color='g',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedSensorFloatsArray)
				else None,
				[0,1]
			)

		#perturbative
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedPerturbativeDecoderFloatsArray[__IndexInt,:],
						color='r',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeDecoderFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedExactDecoderFloatsArray[__IndexInt,:],
						color='r',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeDecoderFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedLeakDecoderFloatsArray[__IndexInt,:],
						color='pink',
						linewidth=1
					)
				if __IndexInt<len(self.PrediratedLeakDecoderFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedDecoderAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedDecoderAxis.set_ylim([-0.1,3.])

		#show
		pyplot.show()



#</DefineClass>

#</DefinePrint>
PrediraterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PrediratingRateUnitsInt',
		'PrediratingSensorUnitsInt',
		'PrediratingRunTimeFloat',
		'PrediratingStepTimeFloat',
		'PrediratedTimeFloatsArray',
		'PrediratedCommandFloatsArray',
		'PrediratedJacobianFloatsArray',
		'PrediratedDecoderWeigthFloatsArray',
		'PrediratedInputRandomFloatsArray',
		'PrediratedInputPerturbativeWeigthFloatsArray',
		'PrediratedDecoderWeigthFloatsArray',
		'PrediratedLateralWeigthFloatsArray',
		'PrediratedLateralRandomFloatsArray',
		'PrediratedLateralExactWeigthFloatsArray',
		'PrediratedLateralPerturbativeWeigthFloatsArray',
		'PrediratedNullFloatsArray',
		'PrediratedInitialSensorFloatsArray',
		'PrediratedInitialRateFloatsArray',
		'PrediratedSensorFloatsArray',
		'PrediratedPerturbativeRateFloatsArray',
		'PrediratedLeakRateFloatsArray',
		'PrediratedPerturbativeDecoderFloatsArray',
		'PrediratedLeakDecoderWeigthFloatsArray',
		'PrediratedLeakDecoderFloatsArray'
	]
)
#<DefinePrint>
