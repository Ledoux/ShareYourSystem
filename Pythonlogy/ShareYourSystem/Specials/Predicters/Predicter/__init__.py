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
BaseModuleStr="ShareYourSystem.Standards.Recorders.Leaker"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Predicter','Predict','Predicting','Predicted')
#</DefineAugmentation>

#<ImportSpecificModules>
Leaker=BaseModule
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
def getNullFloatsArray(_FloatsArray, _RtolFloat=1e-5):
	u, s, v = np.linalg.svd(_FloatsArray)
	RankInt = (s > _RtolFloat*s[0]).sum()
	return v[RankInt:].T.copy()
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PredicterClass(BaseClass):
	
	def default_init(self,
			_PredictingSensorsInt=1,
			_PredictingDaleBool=False,
			_PredictingTimeVariable='#scalar:10.*ms',
			_PredictingDynamicStr='Track',
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_predict(self):

		#Check
		if self.ManagementTagStr=='Sensor':

			#debug
			self.debug(
				[
					'We predict in the Sensor',
					('self.',self,[
							'PredictingTimeVariable'
						])
				]
			)

			#Check
			self.LeakingTimeVariable=self.PredictingTimeVariable

		#Check
		if self.ManagementTagStr=='Decoder':

			#debug
			self.debug(
				[
					'We predict in the Decoder',
					('self.',self,[
							'PredictingTimeVariable'
						])
				]
			)

			#Check
			self.LeakingTimeVariable=self.PredictingTimeVariable

		if self.ManagementTagStr=='Jacobian':

			#debug
			self.debug(
				[
					'We predict in the Jacobian',
					('self.',self,[
							'PredictingDynamicStr'
						])
				]
			)

			#Check
			if self.PredictingDynamicStr=="Track":

				#diag
				self.PredictedJacobianFloatsArray=-np.diag(
					np.ones(
						self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable.LeakingUnitsInt
					)
				)

			elif self.PredictingDynamicStr in ["Gamma","Gamma-Theta"]:

				if self.PredictingDynamicStr=="Gamma" and self.PredictingSensorsInt<3:
					self.PredictingSensorsInt=2
				if self.PredictingDynamicStr=="Gamma-Theta" and self.PredictingSensorsInt<6:
					self.PredictingSensorsInt=6

				self.PredictedJacobianFloatsArray=-np.diag(
					(1./self.PredictingTimeFloat)*np.ones(
						self.PredictingSensorsInt
					)
				)

				#set
				self.PredictedJacobianFloatsArray[0,0]+=(1.5/self.PredictingTimeFloat)
				self.PredictedJacobianFloatsArray[1,0]+=-(3.7/self.PredictingTimeFloat)
				self.PredictedJacobianFloatsArray[0,1]+=(3.7/self.PredictingTimeFloat)
				self.PredictedJacobianFloatsArray[1,1]+=-(1./self.PredictingTimeFloat)

				if self.PredictingDynamicStr=="Gamma-Theta":

					#set
					self.PredictedJacobianFloatsArray[2,3]+=(1./self.PredictingTimeFloat)
					self.PredictedJacobianFloatsArray[3,4]+=-(1.2/self.PredictingTimeFloat)
					self.PredictedJacobianFloatsArray[4,5]+=-(1.4/self.PredictingTimeFloat)
					self.PredictedJacobianFloatsArray[5,2]+=-(1.6/self.PredictingTimeFloat)

			#debug
			'''
			self.debug(
				[
					'We have prepared the sensor jacobian',
					('self.',self,['PredictedJacobianFloatsArray'])
				]
			)
			'''

			#link
			self.LeakingWeigthVariable=self.PredictedJacobianFloatsArray

			"""
			#/#################/#
			# Prepare the Decoders weigths
			#

			#Perturbative and exact 

			#random
			self.PredictedExactDecoderWeigthFloatsArray=(
				self.PredictingDecoderMeanWeigtFloat+self.PredictingDecoderStdWeigtFloat*getattr(
					scipy.stats,
					self.PredictingInputStatStr
				).rvs(
					size=(
						self.PredictingSensorsInt,
						self.PredictingUnitsInt
					)
				)
			)/(self.PredictingUnitsInt**self.PredictingNormalisationInt)
			
			#debug
			'''
			self.debug(
				[
					'We have setted the PredictedExactDecoderWeigthFloatsArray',
					('self.',self,[
						'PredictedExactDecoderWeigthFloatsArray',
						'PredictingDecoderMeanWeigtFloat',
						'PredictingDecoderStdWeigtFloat'
					])
				]
			)
			'''

			#find the null space
			self.PredictedNullFloatsArray=getNullFloatsArray(
				self.PredictedExactDecoderWeigthFloatsArray
			)

			#debug
			'''
			PredictedProductArray=np.dot(
				self.PredictedExactDecoderWeigthFloatsArray,
				self.PredictedNullFloatsArray
			)
			self.debug(
					[
						('self.',self,[
							'PredictedExactDecoderWeigthFloatsArray',
							'PredictingUnitsInt'
							]
						),
						("locals()['",locals(),['PredictedProductArray'],"']")
					]
				)
			'''

			#debug
			'''
			PredictedPinvFloatsArray=np.dot(
				self.PredictedControlDecoderWeigthFloatsArray,
				self.PredictedExactDecoderWeigthFloatsArray.T
			)
			self.debug(
				[
					'PredictedPinvFloatsArray is ',
					str(PredictedPinvFloatsArray)
				]
			)
			'''

			#/#################/#
			# Build the perturbative input random matrices
			#

			#random
			self.PredictedInputRandomFloatsArray=self.PredictingPerturbativeInputWeightFloat*getattr(
				scipy.stats,
				self.PredictingInputRandomStatStr
			).rvs(
				size=(
					np.shape(self.PredictedNullFloatsArray)[1],
					self.PredictingSensorsInt
				)
			)

			#dot
			self.PredictedPerturbativeInputWeigthFloatsArray=np.dot(
					self.PredictedNullFloatsArray,
					self.PredictedInputRandomFloatsArray
				)/(self.PredictingUnitsInt**self.PredictingNormalisationInt)

			#/#################/#
			# Build all the perturbative input
			#

			#sum
			self.PredictedTotalPerturbativeInputWeigthFloatsArray=self.PredictedExactDecoderWeigthFloatsArray.T+self.PredictedPerturbativeInputWeigthFloatsArray


			#/#################/#
			# Build all the possible lateral connectivities
			#

			#Exact

			#dot
			self.PredictedExactLateralWeigthFloatsArray=np.dot(
					self.PredictedExactDecoderWeigthFloatsArray.T,
					self.PredictedExactDecoderWeigthFloatsArray
				)

			#debug
			'''
			self.debug(
					[
						('self.',self,[
							'PredictedExactLateralWeigthFloatsArray',
						])
					]
				)
			'''

			#Perturbative

			#random
			self.PredictedLateralRandomFloatsArray=self.PredictingPerturbativeLateralWeightFloat*getattr(
				scipy.stats,
				self.PredictingLateralRandomStatStr
			).rvs(
				size=(
					np.shape(self.PredictedNullFloatsArray)[1],
					self.PredictingUnitsInt
				)
			)/(self.PredictingUnitsInt**(self.PredictingNormalisationInt/2.))

			#dot
			self.PredictedPerturbativeLateralWeigthFloatsArray=np.dot(
					self.PredictedNullFloatsArray,
					self.PredictedLateralRandomFloatsArray
				)
			"""

		else:

			#/###################/#
			# Call the base method
			#

			#debug
			'''
			self.debug(
				[
					'Network level',
					'Now we leak'
				]
			)
			'''

			#leak
			self.leak()

	def leakNetwork(self):

		#/###################/#
		# Call the base method
		# 

		#call
		BaseClass.leakNetwork(self)

		#/###################/#
		# Check for Populations
		# 

		#debug
		'''
		self.debug(
			[
				'We leak predict network here',
				'Check for a sensor population'
			]
		)
		'''

		#Check
		if 'Populations' in self.TeamDict:

			#get
			LeakedPopulationsDeriveManager=self.TeamDict[
				'Populations'
			]

		else:

			#team
			LeakedPopulationsDeriveManager=self.team(
				'Populations'
			).TeamedValueVariable

		#/###################/#
		# Specify the Sensor Population
		#

		#Check
		if 'Sensor' in LeakedPopulationsDeriveManager.ManagementDict:

			#get
			LeakedSensorDerivePredicter=LeakedPopulationsDeriveManager.ManagementDict[
				'Sensor'
			]

		else:



			#manage
			LeakedSensorDerivePredicter=LeakedPopulationsDeriveManager.manage(
				'Sensor'
			).ManagedValueVariable

			#set default
			LeakedSensorDerivePredicter.LeakingUnitsInt=1

		#set
		if LeakedSensorDerivePredicter.LeakingWeigthVariable==None:
			LeakedSensorDerivePredicter.LeakingWeigthVariable='0'

		#debug
		'''
		self.debug(
			[
				'We have defined the Sensor and a default LeakingUnitsInt',
				'id(LeakedSensorDerivePredicter) is '+str(id(LeakedSensorDerivePredicter))
			]
		)
		'''

		#/###################/#
		# Special Sensor setting
		# 

		#debug
		'''
		self.debug(
			[
				'we have maybe to define inside the Sensor Inputs and Interactions',
				"'Inputs' in LeakedSensorDerivePredicter.TeamDict is '",
				str('Inputs' in LeakedSensorDerivePredicter.TeamDict)
			]
		)
		'''

		#/###################/#
		# Check for Inputs in the Sensor
		#

		#Check
		if 'Inputs' in LeakedSensorDerivePredicter.TeamDict:

			#get
			LeakedInputsDeriveManager=LeakedSensorDerivePredicter.TeamDict[
				'Inputs'
			]

		else:

			#team
			LeakedInputsDeriveManager=LeakedSensorDerivePredicter.team(
				'Inputs'
			).TeamedValueVariable

		#/###################/#
		# Specify the Command Input in the Sensor
		#

		#Check
		if 'Command' in LeakedInputsDeriveManager.ManagementDict:

			#get
			LeakedCommandDerivePredicter=LeakedInputsDeriveManager.ManagementDict[
				'Command'
			]

		else:

			#manage
			LeakedCommandDerivePredicter=LeakedInputsDeriveManager.manage(
				'Command'
			).ManagedValueVariable


		#set
		LeakedCommandDerivePredicter.LeakingWeigthVariable="#custom:#clock:200*ms:5.*mV*int(t==200*ms)"

		#/###################/#
		# Check for Interactions in the Sensor
		#

		#Check
		if 'Interactions' in LeakedSensorDerivePredicter.TeamDict:

			#get
			LeakedInteractionsDeriveManager=LeakedSensorDerivePredicter.TeamDict[
				 'Interactions'
			]

		else:

			#team
			LeakedInteractionsDeriveManager=LeakedSensorDerivePredicter.team(
				 'Interactions'
			).TeamedValueVariable

		#/###################/#
		# Specify the Jacobian Interaction in the Sensor
		#	

		#Check
		if 'Jacobian' in LeakedInteractionsDeriveManager.ManagementDict:

			#get
			LeakedJacobianDerivePredicter=LeakedInteractionsDeriveManager.ManagementDict[
				'Jacobian'
			]

		else:

			#manage
			LeakedJacobianDerivePredicter=LeakedInteractionsDeriveManager.manage(
				'Jacobian'
			).ManagedValueVariable

		#set the connect target
		LeakedJacobianDerivePredicter.ConnectingKeyVariable=LeakedSensorDerivePredicter

		#set
		LeakedJacobianDerivePredicter.LeakingWeigthVariable='#array'

		#debug
		'''
		self.debug(
			[
				'Ok we have setted the sensor',
				'LeakedSensorDerivePredicter is ',
				SYS._str(LeakedSensorDerivePredicter)
			]
		)
		'''

		"""
		#Check
		if self.PredictingDaleBool==False:

			#/###################/#
			# Specify the P Population
			#

			#Check
			if 'P' not in LeakedPopulationsDeriveManager:

				#get
				LeakedPDerivePredicter=LeakedPopulationsDeriveManager.ManagementDict[
					'P'
				]

			else:

				#manage
				LeakedPDerivePredicter=LeakedPopulationsDeriveManager.manage(
					'P'
				).ManagedValueVariable

			#set
			LeakedPDerivePredicter.LeakingUnitsInt=1

			#debug
			'''
			self.debug(
				[
					'We have defined the rate P model and a default LeakingUnitsInt',
					'id(LeakedPDerivePredicter) is '+str(id(LeakedPDerivePredicter))
				]
			)
			'''

			#/###################/#
			# Check for Interactions in the P
			#

			#Check
			if 'Interactions' in LeakedPDerivePredicter.TeamDict:

				#get
				LeakedInteractionsDeriveManager=LeakedPDerivePredicter.TeamDict[
					 'Interactions'
				]

			else:

				#team
				LeakedInteractionsDeriveManager=LeakedPDerivePredicter.team(
					 'Interactions'
				).TeamedValueVariable

			#/###################/#
			# Specify the Fast interaction
			#

			#Check
			if 'Fast' in LeakedInteractionsDeriveManager.ManagementDict:

				#get
				LeakedFastDerivePredicter=LeakedInteractionsDeriveManager.ManagementDict[
					'Fast'
				]

			else:

				#manage
				LeakedFastDerivePredicter=LeakedInteractionsDeriveManager.manage(
					'Fast'
				).ManagedValueVariable

			#set the connect target
			LeakedFastDerivePredicter.ConnectingKeyVariable=LeakedPDerivePredicter

			#debug
			'''
			self.debug(
				[
					'We have defined the Fast interaction in the P'
				]
			)
			'''
		"""


	def leakPopulation(self):

		#predict
		self.predict()

		#/##################/#
		# Base method
		#

		#call
		BaseClass.leakPopulation(self)

	def leakInteraction(self):

		#predict
		self.predict()

		#/##################/#
		# Base method
		#

		#call
		BaseClass.leakInteraction(self)



#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=PredicterClass
#<DefineLocals>

#</DefinePrint>
PredicterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PredictingJacobianFloatsArray',

		'PredictingUnitsInt',
		'PredictingSensorsInt',
		
		'PredictingDynamicStr',
		'PredictingTimeFloat',
		'PredictingInputStatStr',
		'PredictingDecoderMeanWeigtFloat',
		'PredictingDecoderStdWeigtFloat',
		'PredictingNormalisationInt',

		'PredictingCostFloat',
		'PredictingPerturbativeInputWeightFloat',
		'PredictingPerturbativeLateralWeightFloat',
		'PredictingInputRandomStatStr',
		'PredictingLateralRandomStatStr',

		'PredictedJacobianFloatsArray',
		
		'PredictedLeakWeigthFloatsArray',

		'PredictedControlDecoderWeigthFloatsArray',
		'PredictedExactDecoderWeigthFloatsArray',

		'PredictedInputRandomFloatsArray',
		'PredictedPerturbativeInputWeigthFloatsArray',
		'PredictedNullFloatsArray',
		'PredictedTotalPerturbativeInputWeigthFloatsArray',
		
		'PredictedExactLateralWeigthFloatsArray',
		'PredictedLateralRandomFloatsArray',
		'PredictedPerturbativeLateralWeigthFloatsArray',
		'PredictedTotalPerturbativeLateralWeigthFloatsArray',
	]
)
#<DefinePrint>