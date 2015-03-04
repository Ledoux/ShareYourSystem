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
						_PrediratedDecoderWeigthFloatsArray=None,
						_PrediratedInputRandomFloatsArray=None,
						_PrediratedInputPerturbativeFloatsArray=None,
						_PrediratedNullFloatsArray=None,
						_PrediratedLateralWeigthFloatsArray=None,
						_PrediratedLateralRandomFloatsArray=None,
						_PrediratedLateralPerturbativeFloatsArray=None,
						_PrediratedInitialSensorFloatsArray=None,
						_PrediratedInitialRateFloatsArray=None,
						_PrediratedSensorFloatsArray=None,
						_PrediratedRateFloatsArray=None,
						_PrediratedDecoderFloatsArray=None,
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
		self.PrediratedInputPerturbativeFloatsArray=0.*np.dot(
				self.PrediratedNullFloatsArray,
				self.PrediratedInputRandomFloatsArray
			)

		#dot
		self.PrediratedExactLateralWeigthFloatsArray=np.dot(
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

		#init rates
		self.PrediratedRateFloatsArray=np.zeros(
				(self.PrediratingRateUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedRateFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init decoder
		self.PrediratedDecoderFloatsArray=np.zeros(
				(self.PrediratingSensorUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedDecoderFloatsArray[:,0]=np.dot(
				self.PrediratedDecoderWeigthFloatsArray,
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
			# Rate part
			#

			#Input Current
			PrediratedRateCurrentFloatsArray=np.dot(
				self.PrediratedDecoderWeigthFloatsArray.T+self.PrediratedInputPerturbativeFloatsArray,
				self.PrediratedCommandFloatsArray[:,__IndexInt]
			)

			#Lateral Current
			PrediratedRateCurrentFloatsArray-=np.dot(
				self.PrediratedExactLateralWeigthFloatsArray+self.PrediratedLateralPerturbativeWeigthFloatsArray,
				self.PrediratedRateFloatsArray[:,__IndexInt-1]
			)
			
			#Euler
			self.PrediratedRateFloatsArray[
				:,
				__IndexInt
			]=self.PrediratedRateFloatsArray[
				:,
				__IndexInt-1
			]+PrediratedRateCurrentFloatsArray*self.PrediratingStepTimeFloat

			#/#################/#
			# Decoder part
			#

			self.PrediratedDecoderFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PrediratedDecoderWeigthFloatsArray,
					self.PrediratedRateFloatsArray[:,__IndexInt-1]
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

		#Command and sensors
		PrediratedSensorAxis=pyplot.subplot(3,1,1)
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
		PrediratedSensorAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedSensorAxis.set_ylim([-0.1,3.])

		#rates
		PrediratedRateAxis=pyplot.subplot(3,1,2)
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedRateFloatsArray[__IndexInt,:],
						color='b',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedRateFloatsArray)
				else None,
				[0,1]
			)
		PrediratedRateAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedRateAxis.set_ylim([-0.1,1.])

		#decoder
		PrediratedDecoderAxis=pyplot.subplot(3,1,3)
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
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedDecoderFloatsArray[__IndexInt,:],
						color='r',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedDecoderFloatsArray)
				else None,
				[0,1]
			)
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
		'PrediratedInputPerturbativeFloatsArray',
		'PrediratedDecoderWeigthFloatsArray',
		'PrediratedLateralRandomFloatsArray',
		'PrediratedExactLateralWeigthFloatsArray',
		'PrediratedLateralPerturbativeWeigthFloatsArray',
		'PrediratedNullFloatsArray',
		'PrediratedInitialSensorFloatsArray',
		'PrediratedInitialRateFloatsArray',
		'PrediratedSensorFloatsArray',
		'PrediratedRateFloatsArray',
		'PrediratedDecoderFloatsArray'
	]
)
#<DefinePrint>
