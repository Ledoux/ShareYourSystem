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
						_PrediratedInputWeigthFloatsArray=None,
						_PrediratedNullFloatsArray=None,
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
		# Rate care : Prepare the input weigth and the null matrix
		#

		#random
		self.PrediratedInputWeigthFloatsArray=scipy.stats.uniform.rvs(
			size=(
				self.PrediratingSensorUnitsInt,
				self.PrediratingRateUnitsInt
			)
		)
		
		#find the null space
		self.PrediratedNullFloatsArray=getNullFloatsArray(
			self.PrediratedInputWeigthFloatsArray
		)

		#debug
		'''
		PrediratedProductArray=np.dot(self.PrediratedInputWeigthFloatsArray,self.PrediratedNullFloatsArray)
		self.debug(
				[
					('self.',self,[
						'PrediratedInputWeigthFloatsArray',
						'PrediratingRateUnitsInt'
						]
					),
					("locals()['",locals(),['PrediratedProductArray'],"']")
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

		#init rates
		self.PrediratedRateFloatsArray=np.zeros(
				(self.PrediratingRateUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedRateFloatsArray[:,0]=PrediratedInitialRateFloatsArray

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

			#Current
			self.PrediratedCurrentFloatsArray=0

			#Euler
			self.PrediratedRateFloatsArray[
				:,
				__IndexInt
			]=self.PrediratedRateFloatsArray[:,__IndexInt-1]+0

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

		#Command
		PrediratedSensorAxis=pyplot.subplot(3,1,1)
		map(
				lambda __IndexInt:
				PrediratedSensorAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedCommandFloatsArray[__IndexInt]
					),
				[0]
			)
		map(
				lambda __IndexInt:
				PrediratedSensorAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedSensorFloatsArray[__IndexInt,:],
						color='g',
						linewidth=3
					),
				[0,1]
			)
		PrediratedSensorAxis.set_ylim([-0.1,3.])


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
		'PrediratedInputWeigthFloatsArray',
		'PrediratedNullFloatsArray',
		'PrediratedInitialSensorFloatsArray',
		'PrediratedInitialRateFloatsArray',
		'PrediratedSensorFloatsArray',
		'PrediratedRateFloatsArray',
		'PrediratedDecoderFloatsArray'
	]
)
#<DefinePrint>
