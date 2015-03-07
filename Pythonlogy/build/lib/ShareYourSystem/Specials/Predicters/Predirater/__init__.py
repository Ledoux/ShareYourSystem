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
BaseModuleStr="ShareYourSystem.Specials.Predicters.Prediploter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.appendDoStrsList(['Predirater','Predirate','Predirating','Predirated'])
#</DefineAugmentation>

#<ImportSpecificModules>
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
def getThresholdArray(_Variable,_ThresholdFloat=1.):

	#Check
	if type(_Variable) in [np.float64,float,int]:

		#return
		return max(
				min(
					_Variable,
					_ThresholdFloat
					),
				-_ThresholdFloat
			)
	else:

		#return
		return map(
			lambda __ElementVariable:
			getThresholdArray(
				__ElementVariable,
				_ThresholdFloat=_ThresholdFloat
			),
			_Variable
		)
SYS.getThresholdArray=getThresholdArray
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PrediraterClass(BaseClass):
	
	def default_init(self,

						_PrediratingTransferVariable=np.tanh,
											
						_PrediratedInitialRateFloatsArray=None,
						
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
		# Prepare the initial conditions
		#

		#random sensors
		PrediratedInitialRateFloatsArray=scipy.stats.uniform.rvs(
			size=self.PredictingUnitsInt
		)

		#/#################/#
		# Shape the size of all the runs
		#

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
				self.PredictedLeakWeigthFloatsArray,
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
				self.PredictedLeakWeigthFloatsArray,
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
				self.PredictedLeakWeigthFloatsArray,
				self.PrediratedControlUnitTraceFloatsArray[:,__IndexInt-1]
			)
			
			#/#################/#
			# Euler part
			#

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


	def mimic_prediplot(self):

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
		PrediratedRateAxis.set_ylim(
			[
				max(-10.,self.PrediratedPerturbativeUnitTraceFloatsArray.min()),
				min(10.,self.PrediratedPerturbativeUnitTraceFloatsArray.max())
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
		'PrediratingRunTimeFloat',
		'PrediratingStepTimeFloat',
		'PrediratingTransferVariable',
		'PrediratingClampFloat',
		
		'PrediratedTimeFloatsArray',
		'PrediratedCommandFloatsArray',

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
