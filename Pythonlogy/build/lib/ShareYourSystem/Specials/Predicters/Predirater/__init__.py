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
BaseModuleStr="ShareYourSystem.Specials.Predicters.Predicter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import scipy.stats
import numpy as np
from matplotlib import pyplot
#</ImportSpecificModules>

#<DefineLocals>
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

						_PrediratingRunTimeFloat=100.,
						_PrediratingStepTimeFloat=0.1,
						_PrediratingTransferVariable=np.tanh,
						_PrediratingClampFloat=1.,
						
						_PrediratedTimeFloatsArray=None,

						_PrediratedInitialSensorFloatsArray=None,
						_PrediratedInitialRateFloatsArray=None,
						
						_PrediratedSensorTraceFloatsArray=None,
						_PrediratedPerturbativeUnitTraceFloatsArray=None,
						_PrediratedExactUnitTraceFloatsArray=None,
						_PrediratedControlUnitTraceFloatsArray=None,
						
						_PrediratedPerturbativeDecoderTraceFloatsArray=None,
						_PrediratedExactDecoderTraceFloatsArray=None,
						_PrediratedControlDecoderTraceFloatsArray=None,

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
					[0.,self.PrediratingClampFloat],
					[self.PrediratingRunTimeFloat/4.,self.PrediratingRunTimeFloat/2.]
				),
				xrange(self.PredictingSensorsInt)
			)
		)

		#/#################/#
		# Prepare the initial conditions
		#

		#random sensors
		PrediratedInitialRateFloatsArray=scipy.stats.uniform.rvs(
			size=self.PredictingUnitsInt
		)

		#random rates
		PrediratedInitialSensorFloatsArray=scipy.stats.uniform.rvs(
			size=self.PredictingSensorsInt
		)

		#/#################/#
		# Shape the size of all the runs
		#

		#init sensors
		self.PrediratedSensorTraceFloatsArray=np.zeros(
				(self.PredictingSensorsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedSensorTraceFloatsArray[:,0]=PrediratedInitialSensorFloatsArray

		#init perturbative rates
		self.PrediratedPerturbativeUnitTraceFloatsArray=np.zeros(
				(self.PredictingUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedPerturbativeUnitTraceFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init exact rates
		self.PrediratedExactUnitTraceFloatsArray=np.zeros(
				(self.PredictingUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedExactUnitTraceFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init leak control rates
		self.PrediratedControlUnitTraceFloatsArray=np.zeros(
				(self.PredictingUnitsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedControlUnitTraceFloatsArray[:,0]=PrediratedInitialRateFloatsArray

		#init perturbative decoder
		self.PrediratedPerturbativeDecoderTraceFloatsArray=np.zeros(
				(self.PredictingSensorsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedPerturbativeDecoderTraceFloatsArray[:,0]=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray,
				PrediratedInitialRateFloatsArray
			)

		#init exact decoder
		self.PrediratedExactDecoderTraceFloatsArray=np.zeros(
				(self.PredictingSensorsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedExactDecoderTraceFloatsArray[:,0]=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray,
				PrediratedInitialRateFloatsArray
			)

		#init leak control decoder
		self.PrediratedControlDecoderTraceFloatsArray=np.zeros(
				(self.PredictingSensorsInt,len(self.PrediratedTimeFloatsArray))
			)
		self.PrediratedControlDecoderTraceFloatsArray[:,0]=np.dot(
				self.PredictedControlDecoderWeigthFloatsArray,
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
						'shape(self.PrediratedSensorTraceFloatsArray) is '+str(
							np.shape(self.PrediratedSensorTraceFloatsArray)
						),
						('self.',self,[
							'PredictedSensorJacobianFloatsArray'
						])
					]
				)
			'''

			#Current
			PrediratedSensorCurrentFloatsArray=np.dot(
				self.PredictedSensorJacobianFloatsArray,
				self.PrediratedSensorTraceFloatsArray[:,__IndexInt-1]
			)+self.PrediratedCommandFloatsArray[:,__IndexInt]

			#/#################/#
			# Perturbative Rate
			#

			#Input Current
			PrediratedPerturbativeUnitCurrentFloatsArray=np.dot(
				self.PredictedTotalPerturbativeInputWeigthFloatsArray,
				self.PrediratedSensorTraceFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PrediratedPerturbativeUnitCurrentFloatsArray-=np.dot(
				self.PredictedTotalPerturbativeLateralWeigthFloatsArray,
				self.PrediratedPerturbativeUnitTraceFloatsArray[:,__IndexInt-1]
			)

			#transfer
			PrediratedPerturbativeUnitCurrentFloatsArray=self.PrediratingTransferVariable(
				PrediratedPerturbativeUnitCurrentFloatsArray
			)

			#Leak and Cost Current (non transfered)
			PrediratedPerturbativeUnitCurrentFloatsArray-=np.dot(
				np.diag(np.ones(self.PredictingUnitsInt)),
				self.PrediratedPerturbativeUnitTraceFloatsArray[:,__IndexInt-1]
			)

			#/#################/#
			# Exact Rate 
			#

			#Input Current
			PrediratedExactUnitCurrentFloatsArray=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray.T,
				self.PrediratedSensorTraceFloatsArray[:,__IndexInt-1]
			)

			#Lateral Current
			PrediratedExactUnitCurrentFloatsArray-=np.dot(
				self.PredictedLeakExactLateralWeigthFloatsArray,
				self.PrediratedExactUnitTraceFloatsArray[:,__IndexInt-1]
			)
			
			#transfer
			PrediratedExactUnitCurrentFloatsArray=self.PrediratingTransferVariable(
				PrediratedExactUnitCurrentFloatsArray
			)

			#Leak Current (non transfered)
			PrediratedExactUnitCurrentFloatsArray-=np.dot(
				np.diag(np.ones(self.PredictingUnitsInt)),
				self.PrediratedExactUnitTraceFloatsArray[:,__IndexInt-1]
			)

			#/#################/#
			# Control Rate
			#

			#Input Current
			PrediratedControlUnitCurrentFloatsArray=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray.T,
				self.PrediratedSensorTraceFloatsArray[:,__IndexInt-1]
			)

			#transfer
			PrediratedControlUnitCurrentFloatsArray=self.PrediratingTransferVariable(
				PrediratedControlUnitCurrentFloatsArray
			)

			#Leal Current
			PrediratedControlUnitCurrentFloatsArray-=np.dot(
				np.diag(np.ones(self.PredictingUnitsInt)),
				self.PrediratedControlUnitTraceFloatsArray[:,__IndexInt-1]
			)
			
			#/#################/#
			# Euler part
			#

			#sensor
			self.PrediratedSensorTraceFloatsArray[
				:,
				__IndexInt
			]=self.PrediratedSensorTraceFloatsArray[
				:,
				__IndexInt-1
			]+PrediratedSensorCurrentFloatsArray*self.PrediratingStepTimeFloat

			#set
			LocalDict=locals()

			#rate
			for __TagStr in ['Perturbative','Exact','Control']:	

				#set
				getattr(
					self,
					'Predirated'+__TagStr+'UnitTraceFloatsArray'
				)[:,__IndexInt]=getattr(
							self,
							'Predirated'+__TagStr+'UnitTraceFloatsArray'
						)[:,__IndexInt-1]+LocalDict[
				'Predirated'+__TagStr+'UnitCurrentFloatsArray'
				]*self.PrediratingStepTimeFloat
					

			#/#################/#
			# Post process part
			#

			"""
			#Saturate
			self.PrediratedPerturbativeUnitTraceFloatsArray[
				np.where(
					self.PrediratedPerturbativeUnitTraceFloatsArray[
							:,
							__IndexInt
						]>10.
				)
			]=10.
			self.PrediratedPerturbativeUnitTraceFloatsArray[
				np.where(
					self.PrediratedPerturbativeUnitTraceFloatsArray[
							:,
							__IndexInt
						]<-10.
				)
			]=-10.
			"""

			#/#################/#
			# Decoder part
			#

			#dot
			self.PrediratedPerturbativeDecoderTraceFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredictedExactDecoderWeigthFloatsArray,
					self.PrediratedPerturbativeUnitTraceFloatsArray[:,__IndexInt-1]
				)

			#exact control
			self.PrediratedExactDecoderTraceFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredictedExactDecoderWeigthFloatsArray,
					self.PrediratedExactUnitTraceFloatsArray[:,__IndexInt-1]
				)

			#leak control
			self.PrediratedControlDecoderTraceFloatsArray[
				:,
				__IndexInt
			]=np.dot(
					self.PredictedControlDecoderWeigthFloatsArray,
					self.PrediratedControlUnitTraceFloatsArray[:,__IndexInt-1]
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
						self.PrediratedSensorTraceFloatsArray[__IndexInt,:],
						color='g',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedSensorTraceFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedSensorAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedSensorAxis.set_ylim([-0.1,1.5*self.PrediratingClampFloat])

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
						self.PrediratedPerturbativeUnitTraceFloatsArray[__IndexInt,:],
						color='blue',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeUnitTraceFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedExactUnitTraceFloatsArray[__IndexInt,:],
						color='violet',
						linewidth=2
					)
				if __IndexInt<len(self.PrediratedPerturbativeUnitTraceFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PrediratedRateAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedControlUnitTraceFloatsArray[__IndexInt,:],
						color='brown',
						linewidth=1
					)
				if __IndexInt<len(self.PrediratedControlUnitTraceFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedRateAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		#PrediratedRateAxis.set_ylim([-1.,1.])
		PrediratedRateAxis.set_ylim(
			[
				self.PrediratedPerturbativeUnitTraceFloatsArray.min(),
				self.PrediratedPerturbativeUnitTraceFloatsArray.max()
			]
		)

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
						self.PrediratedSensorTraceFloatsArray[__IndexInt],
						color='g',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedSensorTraceFloatsArray)
				else None,
				[0,1]
			)

		#perturbative
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedPerturbativeDecoderTraceFloatsArray[__IndexInt,:],
						color='blue',
						linewidth=3
					)
				if __IndexInt<len(self.PrediratedPerturbativeDecoderTraceFloatsArray)
				else None,
				[0,1]
			)

		#exact
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedExactDecoderTraceFloatsArray[__IndexInt,:],
						color='violet',
						linewidth=2
					)
				if __IndexInt<len(self.PrediratedPerturbativeDecoderTraceFloatsArray)
				else None,
				[0,1]
			)

		#leak
		map(
				lambda __IndexInt:
				PrediratedDecoderAxis.plot(
						self.PrediratedTimeFloatsArray,
						self.PrediratedControlDecoderTraceFloatsArray[__IndexInt,:],
						color='brown',
						linewidth=1
					)
				if __IndexInt<len(self.PrediratedControlDecoderTraceFloatsArray)
				else None,
				[0,1]
			)

		#set
		PrediratedDecoderAxis.set_xlim([0.,self.PrediratingRunTimeFloat])
		PrediratedDecoderAxis.set_ylim([-0.1,1.5*self.PrediratingClampFloat])

		#show
		pyplot.show()



#</DefineClass>

#</DefinePrint>
PrediraterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PredictingUnitsInt',
		'PredictingSensorsInt',
		'PrediratingInputWeigtFloat',
		'PrediratingPerturbativeWeightFloat',

		'PrediratingRunTimeFloat',
		'PrediratingStepTimeFloat',
		'PrediratedTimeFloatsArray',

		'PrediratingInputStatStr',
		'PrediratingInputRandomStatStr',
		'PrediratingLateralRandomStatStr',

		'PrediratedCommandFloatsArray',
		'PredictedSensorJacobianFloatsArray',
		
		'PredictedExactDecoderWeigthFloatsArray',
		'PredictedControlDecoderWeigthFloatsArray',

		'PrediratedNullFloatsArray',
		'PrediratedInputRandomFloatsArray',
		'PrediratedPerturbativeInputWeigthFloatsArray',
		'PredictedTotalPerturbativeInputWeigthFloatsArray',
		
		'PrediratedExactLateralWeigthFloatsArray',
		'PredictedLeakExactLateralWeigthFloatsArray',
		'PrediratedLateralRandomFloatsArray',
		'PrediratedPerturbativeLateralWeigthFloatsArray',
		'PredictedTotalPerturbativeLateralWeigthFloatsArray',
		
		'PrediratedInitialSensorFloatsArray',
		'PrediratedInitialRateFloatsArray',
		
		'PrediratedSensorTraceFloatsArray',
		'PrediratedPerturbativeUnitTraceFloatsArray',
		'PrediratedExactUnitTraceFloatsArray',
		'PrediratedControlUnitTraceFloatsArray',
		
		'PrediratedPerturbativeDecoderTraceFloatsArray',
		'PrediratedExactDecoderTraceFloatsArray',
		'PrediratedControlDecoderTraceFloatsArray'
	]
)
#<DefinePrint>
