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
			_PredictingJacobianFloatsArray=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_predict(self):

		"""
		#/#################/#
		# Sensor care : Prepare the input weigth and the null matrix
		#

		if self.PredictingDynamicStr=="leak":

			self.PredictedSensorJacobianFloatsArray=-np.diag(
				(1./self.PredictingConstantTimeFloat)*np.ones(
					self.PredictingSensorsInt
				)
			)

		elif self.PredictingDynamicStr in ["Gamma","Gamma-Theta"]:

			if self.PredictingDynamicStr=="Gamma" and self.PredictingSensorsInt<3:
				self.PredictingSensorsInt=2
			if self.PredictingDynamicStr=="Gamma-Theta" and self.PredictingSensorsInt<6:
				self.PredictingSensorsInt=6

			self.PredictedSensorJacobianFloatsArray=-np.diag(
				(1./self.PredictingConstantTimeFloat)*np.ones(
					self.PredictingSensorsInt
				)
			)

			#set
			self.PredictedSensorJacobianFloatsArray[0,0]+=(1.5/self.PredictingConstantTimeFloat)
			self.PredictedSensorJacobianFloatsArray[1,0]+=-(3.7/self.PredictingConstantTimeFloat)
			self.PredictedSensorJacobianFloatsArray[0,1]+=(3.7/self.PredictingConstantTimeFloat)
			self.PredictedSensorJacobianFloatsArray[1,1]+=-(1./self.PredictingConstantTimeFloat)

			if self.PredictingDynamicStr=="Gamma-Theta":

				#set
				self.PredictedSensorJacobianFloatsArray[2,3]+=(1./self.PredictingConstantTimeFloat)
				self.PredictedSensorJacobianFloatsArray[3,4]+=-(1.2/self.PredictingConstantTimeFloat)
				self.PredictedSensorJacobianFloatsArray[4,5]+=-(1.4/self.PredictingConstantTimeFloat)
				self.PredictedSensorJacobianFloatsArray[5,2]+=-(1.6/self.PredictingConstantTimeFloat)

		#debug
		'''
		self.debug(
			[
				'We have prepared the sensor jacobian',
				('self.',self,['PredictedSensorJacobianFloatsArray'])
			]
		)
		'''

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

		#/###################/#
		# Call the base method
		#

		#debug
		self.debug(
			[
				'Now we leak'
			]
		)

		#leak
		self.leak()

	def leakNetwork(self):

		#/###################/#
		# Check for Populations
		# 

		#debug
		self.debug(
			[
				'We leak predict network here',
				'Check for a sensor population'
			]
		)

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
			LeakedCommandDerivePredicter=LeakedPopulationsDeriveManager.ManagementDict[
				'Command'
			]

		else:

			#manage
			LeakedCommandDerivePredicter=LeakedInputsDeriveManager.manage(
				'Command'
			).ManagedValueVariable

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
			LeakedCommandDerivePredicter=LeakedInteractionsDeriveManager.ManagementDict[
				'Jacobian'
			]

		else:

			#manage
			LeakedCommandDerivePredicter=LeakedInteractionsDeriveManager.manage(
				'Jacobian'
			).ManagedValueVariable

	"""
	def leakPopulation(self):


		#Check
		if self.ManagementTagStr=='Sensor':

			#debug
			self.debug(
				[
					'We are in the sensor Population'
				]
			)

		#/###################/#
		# Set the same command input in the 
		# neuron populations


		#/###################/#
		# Specify the Jacobian interaction
		#

		#Check
		if 'Interactions' in self.TeamDict:

			#get
			LeakedInteractionDeriveManager=self.TeamDict[
				'Interactions'
			]
		else:

			#team
			self.team(
				'Interactions'
			).TeamedValueVariable

		#Check
		if 'Jacobian' in LeakedInteractionDeriveManager.ManagementDict:

			#get
			LeakedJacobianDerivePredicter=LeakedInteractionDeriveManager.ManagementDict[
				'Jacobian'
			]
		else:

			#manage
			LeakedJacobianDerivePredicter=LeakedInteractionDeriveManager.manage(
				'Jacobian' 
			)

		#set
		LeakedJacobianDerivePredicter



		self.PredictingJacobianFloatsArray=

		#/###################/#
		# Call the base method
		#

		#debug
		self.debug(
			[
				'Now we call the base method'
			]
		)

		#leak
		BaseClass.leakPopulation(self)
	"""


#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=PredicterClass
#<DefineLocals>

#</DefinePrint>
PredicterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PredictingUnitsInt',
		'PredictingSensorsInt',
		
		'PredictingDynamicStr',
		'PredictingConstantTimeFloat',
		'PredictingInputStatStr',
		'PredictingDecoderMeanWeigtFloat',
		'PredictingDecoderStdWeigtFloat',
		'PredictingNormalisationInt',

		'PredictingCostFloat',
		'PredictingPerturbativeInputWeightFloat',
		'PredictingPerturbativeLateralWeightFloat',
		'PredictingInputRandomStatStr',
		'PredictingLateralRandomStatStr',

		'PredictedSensorJacobianFloatsArray',
		
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