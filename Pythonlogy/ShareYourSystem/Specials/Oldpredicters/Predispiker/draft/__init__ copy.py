# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Predispiker

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Predicters.Predicter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Predirater=BaseModule
import numpy as np
import scipy
from matplotlib import pyplot
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{
})
class PredispikerClass(BaseClass):
	
	def default_init(self,

						_PredispikingNeuronUnitsInt=0,
						_PredispikingSensorUnitsInt=0,
						_PredispikingPerturbativeWeightFloat=0.1,

						_PredispikingRestVoltageFloat=-60.,
						_PredispikingThresholdVoltageFloatsArray=None,
						_PredispikingResetVoltageFloatsArray=None,
						_PredispikingConstantTimeFloat=10.,
						_PredispikingDelayTimeFloat=0.,
						
						_PredispikingRunTimeFloat=100.,
						_PredispikingStepTimeFloat=0.1,
						_PredispikedTimeFloatsArray=None,

						_PredispikingInputRandomStatStr='norm',
						_PredispikingLateralRandomStatStr='norm',

						_PredispikedCommandFloatsArray=None,
						_PredispikedJacobianFloatsArray=None,
						
						_PredispikedInputRandomFloatsArray=None,
						_PredispikedPerturbativeInputWeigthFloatsArray=None,
						_PredispikedNullFloatsArray=None,
						
						_PredispikedExactLateralWeigthFloatsArray=None,
						_PredispikedLateralRandomFloatsArray=None,
						
						_PredispikedInitialSensorFloatsArray=None,
						_PredispikedInitialNeuronFloatsArray=None,
						
						_PredispikedSensorFloatsArray=None,
						_PredispikedPerturbativeNeuronFloatsArray=None,
						_PredispikedExactNeuronFloatsArray=None,
						_PredispikedLeakNeuronFloatsArray=None,
						
						_PredispikedPerturbativeDecoderFloatsArray=None,
						_PredispikedExactDecoderFloatsArray=None,
						_PredispikedLeakDecoderFloatsArray=None,

						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_predispike(self):
		
		#/#################/#
		# External care : Prepare time and the command
		#

		#arange
		self.PredispikedTimeFloatsArray=np.arange(
			0.,
			self.PredispikingRunTimeFloat,
			self.PredispikingStepTimeFloat
		)

		#array
		self.PredispikedCommandFloatsArray=np.array(
			map(
				lambda __IndexInt:
				Predirater.getKrenelFloatsArray(
					[0.,1.],
					[self.PredispikingRunTimeFloat/4.,self.PredispikingRunTimeFloat/2.]
				),
				xrange(self.PredispikingSensorUnitsInt)
			)
		)

		#debug
		'''
		self.debug(
			[
				'We have prepared the time and the commands',
				('self.',self,['PredispikedCommandFloatsArray'])
			]
		)
		'''

		#/#################/#
		# Sensor care : Prepare the input weigth and the null matrix
		#

		self.PredispikedJacobianFloatsArray=-(1./self.PredispikingConstantTimeFloat)*np.diag(
			np.ones(
				self.PredispikingSensorUnitsInt
			)
		)

		#debug
		'''
		self.debug(
			[
				'We have prepared the sensor jacobian',
				('self.',self,['PredispikedJacobianFloatsArray'])
			]
		)
		'''

		#/#################/#
		# Neuron care : Prepare the input weigth, null matrix, exact and perturbativ matrix
		#

		#random
		self.PredispikedExactDecoderWeigthFloatsArray=scipy.stats.uniform.rvs(
			size=(
				self.PredispikingSensorUnitsInt,
				self.PredispikingNeuronUnitsInt
			)
		)
		
		#find the null space
		self.PredispikedNullFloatsArray=Predirater.getNullFloatsArray(
			self.PredispikedExactDecoderWeigthFloatsArray
		)

		#debug
		'''
		PredispikedProductArray=np.dot(
			self.PredispikedExactDecoderWeigthFloatsArray,
			self.PredispikedNullFloatsArray
		)
		self.debug(
				[
					('self.',self,[
						'PredispikedExactDecoderWeigthFloatsArray',
						'PredispikingNeuronUnitsInt'
						]
					),
					("locals()['",locals(),['PredispikedProductArray'],"']")
				]
			)
		'''

		#random
		self.PredispikedInputRandomFloatsArray=self.PredispikingPerturbativeWeightFloat*getattr(
			scipy.stats,
			self.PredispikingInputRandomStatStr
		).rvs(
			size=(
				np.shape(self.PredispikedNullFloatsArray)[1],
				self.PredispikingSensorUnitsInt
			)
		)

		#dot
		self.PredispikedPerturbativeInputWeigthFloatsArray=np.dot(
				self.PredispikedNullFloatsArray,
				self.PredispikedInputRandomFloatsArray
			)

		#dot
		self.PredispikedExactLateralWeigthFloatsArray=np.dot(
				self.PredispikedExactDecoderWeigthFloatsArray.T,
				self.PredispikedExactDecoderWeigthFloatsArray
			)

		#random
		self.PredispikedLateralRandomFloatsArray=self.PredispikingPerturbativeWeightFloat*getattr(
			scipy.stats,
			self.PredispikingLateralRandomStatStr
		).rvs(
			size=(
				np.shape(self.PredispikedNullFloatsArray)[1],
				self.PredispikingNeuronUnitsInt
			)
		)

		#dot
		self.PredispikedPerturbativeLateralWeigthFloatsArray=np.dot(
				self.PredispikedNullFloatsArray,
				self.PredispikedLateralRandomFloatsArray
			)

		#pinv
		self.PredispikedLeakDecoderWeigthFloatsArray=np.linalg.pinv(
				self.PredispikedExactDecoderWeigthFloatsArray.T
			)

		#debug
		'''
		PredispikedPinvFloatsArray=np.dot(
			self.PredispikedLeakDecoderWeigthFloatsArray,
			self.PredispikedExactDecoderWeigthFloatsArray.T
		)
		self.debug(
			[
				'PredispikedPinvFloatsArray is ',
				str(PredispikedPinvFloatsArray)
			]
		)
		'''

		#/#################/#
		# Prepare the initial conditions
		#

		#random sensors
		PredispikedInitialNeuronFloatsArray=scipy.stats.uniform.rvs(
			size=self.PredispikingNeuronUnitsInt
		)

		#random rates
		PredispikedInitialSensorFloatsArray=scipy.stats.uniform.rvs(
			size=self.PredispikingSensorUnitsInt
		)

		#/#################/#
		# Shape the size of all the runs
		#

		#init sensors
		self.PredispikedSensorFloatsArray=np.zeros(
				(self.PredispikingSensorUnitsInt,len(self.PredispikedTimeFloatsArray))
			)
		self.PredispikedSensorFloatsArray[:,0]=PredispikedInitialSensorFloatsArray

		#init perturbative rates
		self.PredispikedPerturbativeNeuronFloatsArray=np.zeros(
				(self.PredispikingNeuronUnitsInt,len(self.PredispikedTimeFloatsArray))
			)
		self.PredispikedPerturbativeNeuronFloatsArray[:,0]=PredispikedInitialNeuronFloatsArray

		#init exact rates
		self.PredispikedExactNeuronFloatsArray=np.zeros(
				(self.PredispikingNeuronUnitsInt,len(self.PredispikedTimeFloatsArray))
			)
		self.PredispikedExactNeuronFloatsArray[:,0]=PredispikedInitialNeuronFloatsArray

		#init leak control rates
		self.PredispikedLeakNeuronFloatsArray=np.zeros(
				(self.PredispikingNeuronUnitsInt,len(self.PredispikedTimeFloatsArray))
			)
		self.PredispikedLeakNeuronFloatsArray[:,0]=PredispikedInitialNeuronFloatsArray

		#init perturbative decoder
		self.PredispikedPerturbativeDecoderFloatsArray=np.zeros(
				(self.PredispikingSensorUnitsInt,len(self.PredispikedTimeFloatsArray))
			)
		self.PredispikedPerturbativeDecoderFloatsArray[:,0]=np.dot(
				self.PredispikedExactDecoderWeigthFloatsArray,
				PredispikedInitialNeuronFloatsArray
			)

		#init exact decoder
		self.PredispikedExactDecoderFloatsArray=np.zeros(
				(self.PredispikingSensorUnitsInt,len(self.PredispikedTimeFloatsArray))
			)
		self.PredispikedExactDecoderFloatsArray[:,0]=np.dot(
				self.PredispikedExactDecoderWeigthFloatsArray,
				PredispikedInitialNeuronFloatsArray
			)

		#init leak control decoder
		self.PredispikedLeakDecoderFloatsArray=np.zeros(
				(self.PredispikingSensorUnitsInt,len(self.PredispikedTimeFloatsArray))
			)
		self.PredispikedLeakDecoderFloatsArray[:,0]=np.dot(
				self.PredispikedLeakDecoderWeigthFloatsArray,
				PredispikedInitialNeuronFloatsArray
			)

		#/#################/#
		# integrativ Loop
		#

		#for loop
		for __IndexInt in xrange(1,len(self.PredispikedTimeFloatsArray)):

			#/#################/#
			# Sensor part
			#

			#debug
			'''
			self.debug(
					[
						'shape(self.PredispikedCommandFloatsArray) is '+str(
							np.shape(self.PredispikedCommandFloatsArray)
						),
						'shape(self.PredispikedSensorFloatsArray) is '+str(
							np.shape(self.PredispikedSensorFloatsArray)
						),
						('self.',self,[
							'PredispikedJacobianFloatsArray'
						])
					]
				)
			'''

			#Current
			PredispikedSensorCurrentFloatsArray=np.dot(
				self.PredispikedJacobianFloatsArray,
				self.PredispikedSensorFloatsArray[:,__IndexInt-1]
			)+self.PredispikedCommandFloatsArray[:,__IndexInt]

			#/#################/#
			# Perturbative Neuron part
			#

			#Input Current
			PredispikedPerturbativeNeuronCurrentFloatsArray=np.dot(
				self.PredispikedExactDecoderWeigthFloatsArray.T+self.PredispikedPerturbativeInputWeigthFloatsArray,
				self.PredispikedCommandFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PredispikedPerturbativeNeuronCurrentFloatsArray-=np.dot(
					self.PredispikedExactLateralWeigthFloatsArray+self.PredispikedPerturbativeLateralWeigthFloatsArray,
					self.PredispikedPerturbativeNeuronFloatsArray[:,__IndexInt-1]
				)

			#/#################/#
			# Exact Neuron part
			#

			#Input Current
			PredispikedExactNeuronCurrentFloatsArray=np.dot(
				self.PredispikedExactDecoderWeigthFloatsArray.T,
				self.PredispikedCommandFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PredispikedExactNeuronCurrentFloatsArray-=np.dot(
				self.PredispikedExactLateralWeigthFloatsArray,
				self.PredispikedExactNeuronFloatsArray[:,__IndexInt-1]
			)
			
			#/#################/#
			# Leak Control Neuron part
			#

			#Input Current
			PredispikedLeakNeuronCurrentFloatsArray=np.dot(
				self.PredispikedExactDecoderWeigthFloatsArray.T+self.PredispikedPerturbativeInputWeigthFloatsArray,
				self.PredispikedCommandFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PredispikedLeakNeuronCurrentFloatsArray-=np.dot(
				np.diag(np.ones(self.PredispikingNeuronUnitsInt)),
				self.PredispikedLeakNeuronFloatsArray[:,__IndexInt-1]
			)
	
			#/#################/#
			# Euler part
			#

			#sensor
			self.PredispikedSensorFloatsArray[
				:,
				__IndexInt
			]=self.PredispikedSensorFloatsArray[
				:,
				__IndexInt-1
			]+PredispikedSensorCurrentFloatsArray*self.PrediratingStepTimeFloat

			#set
			LocalDict=locals()

			#rate
			for __TagStr in ['Perturbative','Exact','Leak']:	

				#set
				getattr(
					self,
					'Predispiked'+__TagStr+'NeuronFloatsArray'
				)[:,__IndexInt]=getattr(
							self,
							'Predispiked'+__TagStr+'NeuronFloatsArray'
						)[:,__IndexInt-1]+LocalDict[
				'Predispiked'+__TagStr+'NeuronCurrentFloatsArray'
				]*self.PredispikingStepTimeFloat
					

			#/#################/#
			# Decoder part
			#

			#dot
			self.PredispikedPerturbativeDecoderFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredispikedExactDecoderWeigthFloatsArray,
					self.PredispikedPerturbativeNeuronFloatsArray[:,__IndexInt-1]
				)

			#exact control
			self.PredispikedExactDecoderFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredispikedExactDecoderWeigthFloatsArray,
					self.PredispikedExactNeuronFloatsArray[:,__IndexInt-1]
				)

			#leak control
			self.PredispikedLeakDecoderFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredispikedLeakDecoderWeigthFloatsArray,
					self.PredispikedLeakNeuronFloatsArray[:,__IndexInt-1]
				)


		#/#################/#
		# Plot
		#

		#debug
		self.debug(
			[
				'len(self.PredispikedTimeFloatsArray) is '+str(len(self.PredispikedTimeFloatsArray)),
				'np.shape(self.PredispikedCommandFloatsArray) is '+str(np.shape(self.PredispikedCommandFloatsArray))
			]
		)

		#init
		pyplot.figure()

		#/#################/#
		# Command and sensors
		#

		#subplot
		PredispikedSensorAxis=pyplot.subplot(3,1,1)

		#command
		map(
				lambda __IndexInt:
				PredispikedSensorAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedCommandFloatsArray[__IndexInt]
					)
				if __IndexInt<len(self.PredispikedCommandFloatsArray)
				else None,
				[0]
			)

		#sensor
		map(
				lambda __IndexInt:
				PredispikedSensorAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedSensorFloatsArray[__IndexInt,:],
						color='g',
						linewidth=3
					)
				if __IndexInt<len(self.PredispikedSensorFloatsArray)
				else None,
				[0,1]
			)

		#set
		PredispikedSensorAxis.set_xlim([0.,self.PredispikingRunTimeFloat])
		PredispikedSensorAxis.set_ylim([-0.1,3.])

		#/#################/#
		# rates
		#

		#subplot
		PredispikedNeuronAxis=pyplot.subplot(3,1,2)

		#perturbative
		map(
				lambda __IndexInt:
				PredispikedNeuronAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedPerturbativeNeuronFloatsArray[__IndexInt,:],
						color='blue',
						linewidth=3
					)
				if __IndexInt<len(self.PredispikedPerturbativeNeuronFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PredispikedNeuronAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedExactNeuronFloatsArray[__IndexInt,:],
						color='violet',
						linewidth=2
					)
				if __IndexInt<len(self.PredispikedPerturbativeNeuronFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PredispikedNeuronAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedLeakNeuronFloatsArray[__IndexInt,:],
						color='brown',
						linewidth=1
					)
				if __IndexInt<len(self.PredispikedLeakNeuronFloatsArray)
				else None,
				[0,1]
			)

		#set
		PredispikedNeuronAxis.set_xlim([0.,self.PredispikingRunTimeFloat])
		#PredispikedNeuronAxis.set_ylim([-1.,1.])
		PredispikedNeuronAxis.set_ylim(
			[
				self.PredispikedPerturbativeNeuronFloatsArray.min(),
				self.PredispikedPerturbativeNeuronFloatsArray.max()
			]
		)

		#/#################/#
		# decoders
		#

		#subplot
		PredispikedDecoderAxis=pyplot.subplot(3,1,3)

		#sensor
		map(
				lambda __IndexInt:
				PredispikedDecoderAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedSensorFloatsArray[__IndexInt],
						color='g',
						linewidth=3
					)
				if __IndexInt<len(self.PredispikedSensorFloatsArray)
				else None,
				[0,1]
			)

		#perturbative
		map(
				lambda __IndexInt:
				PredispikedDecoderAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedPerturbativeDecoderFloatsArray[__IndexInt,:],
						color='blue',
						linewidth=3
					)
				if __IndexInt<len(self.PredispikedPerturbativeDecoderFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PredispikedDecoderAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedExactDecoderFloatsArray[__IndexInt,:],
						color='violet',
						linewidth=2
					)
				if __IndexInt<len(self.PredispikedPerturbativeDecoderFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PredispikedDecoderAxis.plot(
						self.PredispikedTimeFloatsArray,
						self.PredispikedLeakDecoderFloatsArray[__IndexInt,:],
						color='brown',
						linewidth=1
					)
				if __IndexInt<len(self.PredispikedLeakDecoderFloatsArray)
				else None,
				[0,1]
			)

		#set
		PredispikedDecoderAxis.set_xlim([0.,self.PredispikingRunTimeFloat])
		PredispikedDecoderAxis.set_ylim([-0.1,3.])

		#show
		pyplot.show()



#</DefineClass>

#</DefinePrint>
PredispikerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PredispikingNeuronUnitsInt',
		'PredispikingSensorUnitsInt',
		'PredispikingPerturbativeWeightFloat',
		
		'PredispikingRunTimeFloat',
		'PredispikingStepTimeFloat',

		'PredispikedTimeFloatsArray',
		'PredispikedCommandFloatsArray',
		'PredispikedJacobianFloatsArray',
		'PredispikedExactDecoderWeigthFloatsArray',
		'PredispikedInputRandomFloatsArray',
		'PredispikedPerturbativeInputWeigthFloatsArray',
		'PredispikedExactDecoderWeigthFloatsArray',
		'PredispikedExactLateralWeigthFloatsArray',
		'PredispikedLateralRandomFloatsArray',
		'PredispikedExactLateralWeigthFloatsArray',
		'PredispikedPerturbativeLateralWeigthFloatsArray',
		'PredispikedNullFloatsArray',
		'PredispikedInitialSensorFloatsArray',
		'PredispikedInitialNeuronFloatsArray',
		'PredispikedSensorFloatsArray',
		'PredispikedPerturbativeNeuronFloatsArray',
		'PredispikedExactNeuronFloatsArray',
		'PredispikedLeakNeuronFloatsArray',

		'PredispikedPerturbativeDecoderFloatsArray',
		'PredispikedExactDecoderFloatsArray',
		'PredispikedLeakDecoderWeigthFloatsArray',
		'PredispikedLeakDecoderFloatsArray'
	]
)
#<DefinePrint>
	
