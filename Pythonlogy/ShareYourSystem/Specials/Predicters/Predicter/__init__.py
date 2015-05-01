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

class DynamicDict(dict):

	def __init__(self,*_LiargVariablesList,**_KwargVariablesDict):

		#init
		dict.__init__(self,*_LiargVariablesList,**_KwargVariablesDict)

		#map
		map(
			lambda __ItemTuple:
			self.__setitem__(
				*__ItemTuple
			) if __ItemTuple[0] not in self
			else None,
			[
				('ModeStr',"Track"),
				('ConstantTimeFloat',2.)
			]
		)

#</DefineLocals>

#<DefineClass>
@DecorationClass()
class PredicterClass(BaseClass):
	
	def default_init(self,
			_PredictingSensorUnitsInt=1,
			_PredictingAgentUnitsInt=1,
			_PredictingDaleBool=False,
			_PredictingDynamicBool=True,
			_PredictingJacobianVariable=None,
			_PredictingCommandVariable=None,
			_PredictingEncodPerturbStdFloat=0.,
			_PredictingRateCostVariable=None,
			_PredictingRateTransferVariable=None,
			_PredictingAgentRestVariable=None,
			_PredictingAgentResetVariable=None,
			_PredictingAgentTimeFloat=10.,
			_PredictingFastSymmetryFloat=1.,
			_PredictingDecoderVariable=None,
			_PredictingDecoderMeanFloat=1.,
			_PredictingDecoderStdFloat=1.,
			_PredictingDecoderProbabilityFloat=0.,
			_PredictingDecoderTimeFloat=1.,
			_PredictingDecoderNormalisationInt=1,
			_PredictingFastPerturbStdFloat=0.,
			_PredictingSlowPerturbStdFloat=0.,
			_PredictingInteractionStr="Rate",
			_PredictingEncodPlasticBool=False,
			_PredictingFastPlasticBool=False,
			_PredictedDynamicDict=None,
			_PredictedSensorJacobianFloatsArray=None,
			_PredictedDecoderFloatsArray=None,
			_PredictedFastFloatsArray=None,
			_PredictedThresholdFloatsArray=None,
			_PredictedSlowFloatsArray=None,
			_PredictedParentSingularStr="",
			_PredictedSensorDerivePredicterVariable=None,
			_PredictedAgentDerivePredicterVariable=None,
			_PredictedDecoderDerivePredicterVariable=None,
			_PredictedNetworkDerivePredicterVariable=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_predict(self):

		#/#################/#
		# Determine if it is an inside structure or the top
		#

		#debug
		'''
		self.debug(
			[
				'We leak here',
				'First look for deeper teams in the structure',
			]
		)
		'''

		#Check
		if self.ParentedTotalSingularListDict!=None and len(
			self.ParentedTotalSingularListDict
		)>0:

			#debug
			'''
			self.debug(
				[
					'self.ParentedTotalSingularListDict.keys() is ',
					str(self.ParentedTotalSingularListDict.keys())
				]
			)
			'''

			#get
			self.PredictedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['PredictedParentSingularStr'])
			]
		)
		'''

		#Check
		if (self.ParentDeriveTeamerVariable==None or "Populations" in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces',
			'Samples',
			'Events',
			'Interactomes',
			"Interactions",
			'Inputs'
		]) and self.PredictedParentSingularStr!='Population':

			#/########################/#
			# Network level
			# 

			#debug
			'''
			self.debug(
				[
					'It is a Network level for the predict',
				]
			)
			'''

			#/########################/#
			# Determine parent level
			# 

			#alias
			self.PredictedNetworkDerivePredicterVariable=self

			#/########################/#
			# predictNetwork
			# 

			#predict
			self.predictNetwork()

			#/########################/#
			# structure predict 
			# 

			#debug
			'''
			self.debug(
				[
					'We structure all the predicting children...'
				]
			)	
			'''

			#structure
			self.structure(
				[
					"Populations",
					'Inputs',
					'Interactomes',
					"Interactions",
				],
				'#all',
				_ManagerCommandSetList=[
						'predict'
					]
			)

			#/########################/#
			# leak
			#

			#leak
			self.leak()
			

		else:

			#/########################/#
			# Inside structure
			#

			#debug
			'''
			self.debug(
				[
					'Ok we check if this parentsingular has a special method ',
					('self.',self,[
						'PredictedParentSingularStr'
					])
				]
			)
			'''

			#set
			PredictedMethodKeyStr='predict'+self.PredictedParentSingularStr

			#Check
			if hasattr(self,PredictedMethodKeyStr):

				#/########################/#
				# call the special predict<PredictedParentSingularStr> method
				#

				#debug
				'''
				self.debug(
					[
						'It is a '+self.PredictedParentSingularStr+' level',
						'We predict<PredictedParentSingularStr>'
					]
				)
				'''

				#call
				getattr(
					self,
					PredictedMethodKeyStr
				)()

				#debug
				'''
				self.debug(
					[
						'Ok we have setted predict'+self.PredictedParentSingularStr
					]
				)
				'''	
	
	def predictNetwork(self):

		#/###################/#
		# Check for Populations
		# 

		#get
		LeakedPopulationsDeriveManager=self.getTeamer("Populations")

		#debug
		'''
		self.debug(
			[
				'We predict network here',
				'Check for a sensor population'
			]
		)
		'''

		#/###################/#
		# Check for Sensor
		# 

		#get
		LeakedSensorDerivePredicter=LeakedPopulationsDeriveManager.getManager("Sensor")

		#/###################/#
		# Check for Agent
		# 

		#get
		LeakedAgentDerivePredicter=LeakedPopulationsDeriveManager.getManager("Agent")

		#/###################/#
		# Check for Decoder
		# 

		#get
		LeakedDecoderDerivePredicter=LeakedPopulationsDeriveManager.getManager("Decoder")

		#debug
		'''
		self.debug(
			[
				'Ok we have created the Decoder'
			]
		)
		'''

		#import
		import numpy as np

		#/################/#
		# Build the Jacobian
		#

		#init
		self.PredictedDynamicDict=DynamicDict(
				self.PredictingJacobianVariable
			) if self.PredictingJacobianVariable!=None else DynamicDict()

		#alias
		PredictedConstantTimeFloat=self.PredictedDynamicDict['ConstantTimeFloat']

		#Check
		if self.PredictedDynamicDict["ModeStr"]=="Track":

			
			#debug
			'''
			self.debug(
				[
					'We set a sensor variable leaking at'+str(PredictedConstantTimeFloat)
				]
			)
			'''

			#diag
			self.PredictedSensorJacobianFloatsArray=-(1./PredictedConstantTimeFloat)*np.diag(
				np.ones(
					self.PredictingSensorUnitsInt
				)
			)

		elif self.PredictedDynamicDict["ModeStr"]=="Damp":

			#Check
			if self.PredictedDynamicDict["LoopIntsList"]==[1.]:
				self.PredictingSensorUnitsInt=2
			if self.PredictedDynamicDict["LoopIntsList"]==[1.,2.]:
				self.PredictingSensorUnitsInt=6

			#debug
			'''
			self.debug(
				[
					'We build the oscillatory jacobian matrix',
					('self.',self,[
							'PredictingSensorUnitsInt'
						])
				]
			)
			'''

			#diag
			self.PredictedSensorJacobianFloatsArray=-np.diag(
				(1./PredictedConstantTimeFloat)*np.ones(
					self.PredictingSensorUnitsInt
				)
			)

			#set
			self.PredictedSensorJacobianFloatsArray[0,0]+=(1.5/PredictedConstantTimeFloat)
			self.PredictedSensorJacobianFloatsArray[1,0]+=-(3.7/PredictedConstantTimeFloat)
			self.PredictedSensorJacobianFloatsArray[0,1]+=(3.7/PredictedConstantTimeFloat)
			self.PredictedSensorJacobianFloatsArray[1,1]+=-(1./PredictedConstantTimeFloat)

			#Check
			if self.PredictedDynamicDict["LoopIntsList"]==[1.,2.]:

				#set
				self.PredictedSensorJacobianFloatsArray[2,3]+=(1./PredictedConstantTimeFloat)
				self.PredictedSensorJacobianFloatsArray[3,4]+=-(1.2/PredictedConstantTimeFloat)
				self.PredictedSensorJacobianFloatsArray[4,5]+=-(1.4/PredictedConstantTimeFloat)
				self.PredictedSensorJacobianFloatsArray[5,2]+=-(1.6/PredictedConstantTimeFloat)

		#debug
		'''
		self.debug(
			[
				'We have prepared the sensor jacobian',
				('self.',self,['PredictedSensorJacobianFloatsArray'])
			]
		)
		'''

		#/################/#
		# Build the DecoderFloatsArray
		#

		#Check
		if type(self.PredictingDecoderVariable) in [list,tuple,np.ndarray]: 

			#Check
			self.PredictedDecoderFloatsArray=np.array(
				self.PredictingDecoderVariable
			)

			#shape
			PredictedShapeIntsList=list(
				np.shape(self.PredictingDecoderVariable)
			)

			#debug
			'''
			self.debug(
				[
					'Update the PredictingAgentUnitsInt with the size of the array',
					'PredictedShapeIntsList is ',
					str(PredictedShapeIntsList),
					'len(PredictedShapeIntsList) is',
					str(len(PredictedShapeIntsList))
				]
			)
			'''

			#Check
			if len(PredictedShapeIntsList)==1:

				#get
				self.PredictingAgentUnitsInt=PredictedShapeIntsList[0]

				#recast into a 2D array
				self.PredictedDecoderFloatsArray=np.array(
					[self.PredictedDecoderFloatsArray]
				)
			else:

				#get
				self.PredictingAgentUnitsInt=PredictedShapeIntsList[1]

			#debug
			'''
			self.debug(
				[
					'Now',
					('self.',self,[
							'PredictingAgentUnitsInt'
						])
				]
			)
			'''

		else:

			#numscipy
			self.NumscipyingProbabilityFloat=self.PredictingDecoderProbabilityFloat
			self.NumscipyingMeanFloat=self.PredictingDecoderMeanFloat
			self.NumscipyingStdFloat=self.PredictingDecoderStdFloat
			self.NumscipyingRowsInt=self.PredictingSensorUnitsInt
			self.NumscipyingColsInt=self.PredictingAgentUnitsInt
			self.numscipy()

			#Check
			self.PredictedDecoderFloatsArray=self.NumscipiedRandomFloatsArray

		#debug
		self.debug(
			[
				'We normalize the PredictedDecoderFloatsArray',
				('self.',self,[
						'PredictedDecoderFloatsArray',
						'PredictingDecoderNormalisationInt'
					])
			]
		)

		#norm
		self.PredictedDecoderFloatsArray/=self.PredictingAgentUnitsInt**self.PredictingDecoderNormalisationInt

		#/################/#
		# Build the Fast Connection
		#

		#Check
		if self.PredictingFastSymmetryFloat>0.:

			#debug
			'''
			self.debug(
				[
					'We build a symmetry fast connectivity',
					('self.',self,[
							'PredictingFastSymmetryFloat',
							'PredictedDecoderFloatsArray'
						])
				]
			)
			'''

			#diag
			self.PredictedFastFloatsArray=-self.PredictingFastSymmetryFloat*np.dot(
				self.PredictedDecoderFloatsArray.T,
				self.PredictedDecoderFloatsArray
			)

		else:

			#debug
			'''
			self.debug(
				[
					'PredictingFastSymmetryFloat is null'
				]
			)
			'''

			#pinv
			self.PredictedDecoderFloatsArray=self.PredictingRateCostVariable*np.linalg.pinv(
				self.PredictedDecoderFloatsArray.T
			)

		#debug
		'''
		self.debug(
			[
				'Look if we have to perturb',
				'self.PredictingFastPerturbStdFloat is ',
				str(self.PredictingFastPerturbStdFloat)
			]
		)
		'''

		#Check
		if self.PredictingFastPerturbStdFloat>0.:

			#numscipy
			self.NumscipyingStdFloat=self.PredictingFastPerturbStdFloat
			self.NumscipyingSizeTuple=(self.PredictingAgentUnitsInt,self.PredictingAgentUnitsInt)
			self.numscipy()

			#debug
			'''
			self.debug(
				[
					'We are going to add this perturbation to fast',
					('self.',self,[
							'NumscipiedRandomFloatsArray',
							'PredictedFastFloatsArray'
						])
				]
			)
			'''

			#link
			self.PredictedFastFloatsArray+=self.NumscipiedRandomFloatsArray

		#debug
		'''
		self.debug(
			[
				'We have builded the fast connections',
				('self.',self,[
						'PredictedFastFloatsArray'
					])
			]
		)
		'''

		#/################/#
		# Build the Thresholds
		#

		#Check
		if self.PredictingInteractionStr=="Spike":

			#Compute
			#self.PredictedThresholdFloatsArray=np.sum(
			#	(self.PredictedDecoderFloatsArray**2)/2.,axis=0
			#)
			#set
			self.PredictedThresholdFloatsArray=np.array(
				[
					sum(
						self.PredictedDecoderFloatsArray[:,__IndexInt]**2
					)/2. for __IndexInt in xrange(self.PredictingAgentUnitsInt)
				]
			)

			#debug
			self.debug(
				[
					'We have setted the thresholds',
					('self.',self,[
							'PredictedDecoderFloatsArray',
							'PredictedThresholdFloatsArray'
						])
				]
			)

		#/################/#
		# PredictingDynamicBool Case
		#

		#Check
		if self.PredictingDynamicBool:

			#/################/#
			# Build the Slow Connection
			#

			#debug
			'''
			self.debug(
				[
					'We build the PredictedSlowFloatsArray',
					'CAREFUL PredictingDecoderTimeFloat has to be in ms',
					('self.',self,[
						'PredictedSensorJacobianFloatsArray',
						'PredictingDecoderTimeFloat'
						]),
					'AND ALSO here Slow is D.T(A+lambdaI) just (not D.T(A+lambdaI)D)'
				]
			)
			'''

			#diag
			self.PredictedSlowFloatsArray=self.PredictedSensorJacobianFloatsArray+(
				1./self.PredictingDecoderTimeFloat
			)*np.diag(
				np.ones(
					self.PredictingSensorUnitsInt
				)
			)

			#debug
			'''
			self.debug(
				[
					'In intermediate values',
					('self.',self,[
							'PredictedSlowFloatsArray'
						])
				]
			)
			'''

			#link
			self.PredictedSlowFloatsArray=np.dot(
				self.PredictedDecoderFloatsArray.T,
				self.PredictedSlowFloatsArray
			)

			#debug
			'''
			self.debug(
				[
					'We have built the slow connection',
					('self.',self,[
							'PredictedSlowFloatsArray',
							'PredictedSensorJacobianFloatsArray',
							'PredictingDecoderTimeFloat',
							'PredictedDecoderFloatsArray'
						])
				]
			)
			'''

			#/################/#
			# Perturb maybe
			#

			#Check
			if self.PredictingSlowPerturbStdFloat>0.:

				#numscipy
				self.NumscipyingStdFloat=self.PredictingSlowPerturbStdFloat
				self.NumscipyingSizeTuple=(
					self.PredictingAgentUnitsInt,
					self.PredictingSensorUnitsInt
				)
				self.numscipy()

				#debug
				'''
				self.debug(
					[
						'We are going to add this perturbation to fast',
						('self.',self,[
								'NumscipiedRandomFloatsArray',
								'PredictedSlowFloatsArray'
							])
					]
				)
				'''

				#link
				self.PredictedSlowFloatsArray+=self.NumscipiedRandomFloatsArray


		#/###############/#
		# Renormalize compared to the rate model time constant
		#

		#Check
		if self.PredictingInteractionStr=="Rate":

			#debug
			'''
			self.debug(
				[
					'As we divide by a rate time constant of 10ms in the agent',
					'We need here to multiply by 10 the connectivity',
					('self.',self,[
							'PredictingAgentTimeFloat'
						])
				]
			)
			'''

			#set
			self.PredictedFastFloatsArray*=self.PredictingAgentTimeFloat

		#Check
		if type(self.PredictedSlowFloatsArray)!=None.__class__:

			#mul
			self.PredictedSlowFloatsArray*=self.PredictingAgentTimeFloat

		#/###############/#
		# Consider the sum of Antileak
		#

		#Check
		if self.PredictingRateTransferVariable!=None:

			#debug
			'''
			self.debug(
				[
					'There is a rate transfer function so add the leak term into the fast',
					('self.',self,[
							'PredictedFastFloatsArray'
						])
				]
			)
			'''
			
			#set
			self.PredictedFastFloatsArray+=np.diag(
				np.ones(
					self.PredictingAgentUnitsInt
				)
			)

	def predictPopulation(self):

		#debug
		'''
		self.debug(
			[
				'We predict Population here'
			]
		)
		'''

		#Check
		if self.ManagementTagStr=="Sensor":

			#debug
			'''
			self.debug(
				[
					'We predict in the Sensor',
					('self.',self,[
							'PredictingDecoderTimeFloat'
						])
				]
			)
			'''

			#/####################/#
			# Simplify the leak equation
			#

			#set
			self.LeakingTimeVariable='#scalar:1.*ms'

			#set
			self.LeakingWeigthVariable='0'

			#/####################/#
			# Determine the relations
			#

			#set
			self.PredictedNetworkDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Determine the number of leaking units
			#

			#debug
			'''
			self.debug(
				[
					'Look for LeakingUnitsInt',
					('self.',self,[
							'LeakingUnitsInt',
							'PredictingSensorUnitsInt'
						])
				]
			)
			'''

			#set default
			if self.LeakingUnitsInt==0:
				self.LeakingUnitsInt=1

			#set
			if self.PredictedNetworkDerivePredicterVariable.PredictingSensorUnitsInt>-1:
				self.LeakingUnitsInt=self.PredictedNetworkDerivePredicterVariable.PredictingSensorUnitsInt

			#/###################/#
			# Check for Inputs in the Sensor
			#

			#get
			LeakedInputsDeriveManager=self.getTeamer("Inputs")

			#/###################/#
			# Specify the Command Input in the Sensor
			#

			#get
			LeakedCommandDerivePredicter=LeakedInputsDeriveManager.getManager("Command")

			#/###################/#
			# Check for Interactions in the Sensor
			#

			#get
			LeakedInteractionsDerivePredicter=self.getTeamer("Interactions")

			#/###################/#
			# Specify the Jacobian Interaction in the Sensor
			#	

			#get
			LeakedJacobianDerivePredicter=LeakedInteractionsDerivePredicter.getManager("Jacobian")

			#/###################/#
			# Specify the Sensor to Agent interaction
			#

			#get
			LeakedEncoderDerivePredicter=LeakedInteractionsDerivePredicter.getManager("Encod")

			#debug
			'''
			self.debug(
				[
					'It is a rate sensor to agent interaction'
					'We have defined the Encoder interaction in the Sensor'
				]
			)
			'''

		elif self.ManagementTagStr=="Agent":

			#debug
			'''
			self.debug(
				[
					'We predict in the Agent',
					('self.',self,[
							'PredictingDecoderVariable',
							'LeakingUnitsInt',
							'PredictedSensorDerivePredicterVariable'
						])
				]
			)
			'''

			#/####################/#
			# Find the Sensor Population
			#

			#set
			self.PredictedSensorDerivePredicterVariable=self.ParentDeriveTeamerVariable.ManagementDict["Sensor"]

			#set
			self.PredictedNetworkDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Set the TransferVariable
			#

			#debug
			'''
			self.debug(
				[
					'set the LeakingTransferVariable'
				]
			)
			'''

			#set
			self.LeakingTransferVariable=self.PredictedNetworkDerivePredicterVariable.PredictingRateTransferVariable
										
			#debug
			'''
			self.debug(
				[
					'self.PredictedNetworkDerivePredicterVariable.PredictingRateCostVariable is ',
					str(
						self.PredictedNetworkDerivePredicterVariable.PredictingRateCostVariable
					),
					'Determine the interaction',
					'self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr is ',
					self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr
				]
			)
			'''

			#/####################/#
			# Set the time constant
			#

			#set
			self.LeakingInteractionStr=self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr

			#/####################/#
			# LeakingUnitsInt
			#

			#debug
			'''
			self.debug(
				[
					'Look for LeakingUnitsInt',
					('self.',self,[
							'LeakingUnitsInt'
						]),
					'self.PredictedNetworkDerivePredicterVariable.PredictingAgentUnitsInt is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictingAgentUnitsInt)
				]
			)
			'''

			#set default
			if self.LeakingUnitsInt==0:
				self.LeakingUnitsInt=1

			#set
			if self.PredictedNetworkDerivePredicterVariable.PredictingAgentUnitsInt>-1:
				self.LeakingUnitsInt=self.PredictedNetworkDerivePredicterVariable.PredictingAgentUnitsInt

			#/####################/#
			# Spike case 
			#

			#Check
			if self.LeakingInteractionStr=="Spike":
				
				#/####################/#
				# Add a rest input
				#

				#Check
				if self.PredictedNetworkDerivePredicterVariable.PredictingAgentRestVariable!=None:
					PredictedRestVariable=self.PredictedNetworkDerivePredicterVariable.PredictingAgentRestVariable
				else:
					PredictedRestVariable=-0.06

				#alias
				self.getTeamer(
					"Inputs"
				).getManager(
					"Rest"
				).setAttr(
					"LeakingWeigthVariable",
					PredictedRestVariable
				)

				#/####################/#
				# Add a reset if units >1
				#

				#debug
				'''
				self.debug(
					[
						'do we have to add a reset',
						('self.',self,['LeakingUnitsInt'])
					]
				)
				'''

				#Check
				if self.LeakingUnitsInt>1 and self.PredictedNetworkDerivePredicterVariable.PredictingAgentResetVariable:

					#Check
					self.LeakingResetVariable=self.PredictedNetworkDerivePredicterVariable.PredictingAgentResetVariable
					

				#debug
				'''
				self.debug(
					[
						'The agents are IF models',
						('self.',self,[
								'LeakingThresholdVariable'
							])
					]
				)
				'''

				#/####################/#
				# Set a threshold
				#

				#alias
				self.LeakingThresholdVariable=1000.*PredictedRestVariable+self.PredictedNetworkDerivePredicterVariable.PredictedThresholdFloatsArray

				#debug
				'''
				self.debug(
					[
						'We have setted the LeakingThresholdVariable',
						('self.',self,[
								'LeakingThresholdVariable'
							]),
						'PredictedRestVariable is',
						str(PredictedRestVariable),
						'self.PredictedNetworkDerivePredicterVariable.PredictedThresholdFloatsArray is ',
						str(self.PredictedNetworkDerivePredicterVariable.PredictedThresholdFloatsArray)
					]
				)
				'''

			else:

				#debug
				'''
				self.debug(
					[
						'The agents are rate models',
						'In the Agent, we set a time constant that is 10ms'
					]
				)
				'''

				pass

			#debug
			'''
			self.debug(
				[
					'self.PredictedNetworkDerivePredicterVariable.PredictingAgentTimeFloat is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictingAgentTimeFloat)
				]
			)
			'''

			#set
			self.LeakingTimeVariable='#scalar:'+str(
				self.PredictedNetworkDerivePredicterVariable.PredictingAgentTimeFloat
			)+'*ms'

			#/###################/#
			# Check for Interactions in the Agent
			#

			#get
			LeakedInteractionsDerivePredicter=self.getTeamer(
				"Interactions"
			)

			#/###################/#
			# Specify the Fast interaction
			#

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingFastSymmetryFloat>0.:	

				#get
				LeakedFastDerivePredicter=LeakedInteractionsDerivePredicter.getManager("Fast")

				#set the connect target
				LeakedFastDerivePredicter.ConnectingKeyVariable=self

				#debug
				'''
				self.debug(
					[
						'We have defined the Fast interaction in the Agent',
						'Look maybe for slow',
						'self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool is ',
						str(self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool)
					]
				)
				'''


			#/###################/#
			# Specify the Decoder interaction
			#

			#get
			LeakedDecodDerivePredicter=LeakedInteractionsDerivePredicter.getManager("Decod")

			#set the connect target
			LeakedDecodDerivePredicter.ConnectingKeyVariable=self.ParentDeriveTeamerVariable.ManagementDict[
				"Decoder"
			]

			#/###################/#
			# Rate Case
			#

			#Check
			if self.LeakingInteractionStr=="Rate":

				#debug
				'''
				self.debug(
					[
						'PredictingDynamicBool is False',
						"self.LeakingInteractionStr=='Rate' ",
						'So set a direct interaction'
					]
				)
				'''
				
				#/####################/#
				# Transfer function Case
				#

				#Check
				if self.LeakingTransferVariable!=None:

					#debug
					'''
					self.debug(
						[
							'We are in the rate and there is a transfer function',
							'build the antileak interaction'
						]
					)
					'''

					"""
					#/###################/#
					# Specify the Antileak interaction
					#

					#Check
					if "Antileak" in LeakedInteractionsDerivePredicter.ManagementDict:

						#get
						LeakedAntileakDerivePredicter=LeakedInteractionsDerivePredicter.ManagementDict[
							"Antileak"
						]

					else:

						#manage
						LeakedAntileakDerivePredicter=LeakedInteractionsDerivePredicter.manage(
							"Antileak"
						).ManagedValueVariable

					#set the connect target
					LeakedAntileakDerivePredicter.ConnectingKeyVariable=self

					#debug
					'''
					self.debug(
						[
							"We have defined the Antileak interaction in the Agent"
						]
					)
					'''
					"""

				else:

					#Check
					if self.PredictedNetworkDerivePredicterVariable.PredictingRateCostVariable==None:

						#debug
						'''
						self.debug(
							[
								"There is no transfer function neither rate cost ",
								"so put the leak term to null"
							]
						)
						'''

						#set
						self.LeakingWeigthVariable='0'

					else:

						#debug
						'''
						self.debug(
							[
								"There is no transfer function neither rate cost ",
								"so put the leak term to null"
							]
						)
						'''

						#set
						self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictingRateCostVariable

			"""
			#/###################/#
			# Specify the *J_EncodI_Command' 
			#

			#get
			self.getTeamer(
					"Traces"
				).getManager(
					"*J_EncodI_Command"
				).getTeamer(
					"Samples"
				).getManager(
					"Default"
				)
			"""

		#Check
		elif self.ManagementTagStr=="Decoder":

			#debug
			'''
			self.debug(
				[
					'We predict in the Decoder',
					('self.',self,[
							'PredictingDecoderTimeFloat'
						])
				]
			)
			'''

			#/####################/#
			# Determine the parent
			#

			#set
			self.PredictedAgentDerivePredicterVariable=self.ParentDeriveTeamerVariable.ManagementDict["Agent"]

			#set
			self.PredictedSensorDerivePredicterVariable=self.ParentDeriveTeamerVariable.ManagementDict["Sensor"]

			#set
			self.PredictedNetworkDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			
			#/####################/#
			# Determine the number of leaking units
			#

			#debug
			'''
			self.debug(
				[
					'Look for LeakingUnitsInt',
					('self.',self,[
							'LeakingUnitsInt',
							'PredictingSensorUnitsInt'
						])
				]
			)
			'''

			#set default
			if self.LeakingUnitsInt==0:
				self.LeakingUnitsInt=1

			#set
			if self.PredictedNetworkDerivePredicterVariable.PredictingSensorUnitsInt>-1:
				self.LeakingUnitsInt=self.PredictedNetworkDerivePredicterVariable.PredictingSensorUnitsInt


			#/####################/#
			# The Decoder
			#

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool==False:

				#debug
				'''
				self.debug(
					[
						'self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool is False',
						'set LeakingTimeVariable to 0'
					]
				)
				'''

				#set
				self.LeakingTimeVariable=0.

			else:

				#set
				self.LeakingTimeVariable=self.PredictingDecoderTimeFloat


			#/###################/#
			# PredictingDynamicBool
			#

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool:

				#debug
				'''
				self.debug(
					[
						'PredictingDynamicBool is true'
					]
				)
				'''

				#/###################/#
				# Specify the Slow interaction
				#

				#get
				LeakedSlowDerivePredicter=self.getTeamer(
						"Interactions"
					).getManager(
						"Slow"
					)

				#debug
				'''
				self.debug(
					[
						'We have defined the Decod interaction in the Agent'
					]
				)
				'''

				#set the connect target
				LeakedSlowDerivePredicter.ConnectingKeyVariable=self.ParentDeriveTeamerVariable.ManagementDict[
					"Agent"
				]

			
	def predictInput(self):

		#Check
		if self.ManagementTagStr=='Command':
			
			#/####################/#
			# Determine the parent
			#

			#set
			self.PredictedAgentDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Determine the LeakingWeigthVariable
			#
	
			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingCommandVariable!=None:

				#set
				self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictingCommandVariable
			
			else:

				#set
				self.LeakingWeigthVariable="#custom:#clock:200*ms:5.*mV*int(t==200*ms)"


			#debug
			'''
			self.debug(
				[
					'We set here the Command dynamic',
					('self.',self,[
							'LeakingWeigthVariable'
						])
				]
			)
			'''

	def predictInteraction(self):

		#Check
		if self.ManagementTagStr=="Jacobian":

			#debug
			'''
			self.debug(
				[
					'We predict in the Jacobian',
					('self.',self,[
							'PredictingDynamicDict'
						])
				]
			)
			'''

			#/################/#
			# Determine the relations
			#

			#set
			self.PredictedSensorDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.PredictedAgentDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.ParentDeriveTeamerVariable.ManagementDict[
				"Agent"
			]

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.PredictedNetworkDerivePredicterVariable

			#set
			self.ConnectingKeyVariable=self.PredictedSensorDerivePredicterVariable

			#debug
			'''
			self.debug(
				[
					'We have determined the relations for predictInteraction',
					('self.',self,[
						'ConnectingKeyVariable'
					])
				]
			)
			'''

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedSensorJacobianFloatsArray

		#Check
		elif self.ManagementTagStr=="Encod":

			#debug
			'''
			self.debug(
				[
					'We predict in the Encod interaction',
					('self.',self,[
						])
				]
			)
			'''

			#/################/#
			# Determine the relations
			#

			#set
			self.PredictedSensorDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.PredictedAgentDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.ParentDeriveTeamerVariable.ManagementDict["Agent"]

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.PredictedNetworkDerivePredicterVariable
	
			#set
			self.ConnectingKeyVariable=self.PredictedAgentDerivePredicterVariable

			#/################/#
			# Build the variable in the sensor to be the input in the Agent
			#

			#debug
			'''
			self.debug(
				[
					'Is it Rate : put x as post',
					'Is it Spike : put c as post',
					"self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool is ",
					self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool
				]
			)
			'''

			#set
			self.LeakingInteractionStr='Rate'

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool:

				#debug
				'''
				self.debug(
					[
						'There is a dynamic to transfer',
						'so we bind c instead of x'
					]
				)
				'''

				#set
				self.LeakingVariableStr='I_Command'

			#/################/#
			# Build the LeakingWeigthVariable
			#

			#debug
			'''
			self.debug(
				[
					'We set the weigths in the Encod',
					'self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray is ',
					str(
						self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray
					),
					'but dont forget to also multiply by the agent time constant',
					('self.',self,[

					])
				]
			)
			'''
			
			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictingAgentTimeFloat*self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray.T

			#debug
			'''
			self.debug(
				[
					'Look if we have to perturb',
					'self.PredictedNetworkDerivePredicterVariable.PredictingEncodPerturbStdFloat is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictingEncodPerturbStdFloat)
				]
			)
			'''

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingEncodPerturbStdFloat>0.:

				#numscipy
				self.NumscipyingStdFloat=self.PredictedNetworkDerivePredicterVariable.PredictingEncodPerturbStdFloat
				self.NumscipyingRowsInt=self.PredictedNetworkDerivePredicterVariable.PredictingAgentUnitsInt
				self.NumscipyingColsInt=self.PredictedNetworkDerivePredicterVariable.PredictingSensorUnitsInt
				self.numscipy()

				#link
				self.LeakingWeigthVariable+=self.NumscipiedRandomFloatsArray

			#/################/#
			# Say that we want to record it
			#

			#set
			self.LeakingRecordBool=True

		elif self.ManagementTagStr=="Decod":

			#debug
			'''
			self.debug(
				[
					'We predict in the Decod interaction',
					('self.',self,[
						])
				]
			)
			'''

			#/################/#
			# Determine the relations
			#

			#set
			self.PredictedAgentDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.PredictedDecoderDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable.ManagementDict["Decoder"]

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.ConnectingKeyVariable=self.PredictedDecoderDerivePredicterVariable

			#/####################/#
			# Determine the interaction
			#

			#link
			self.LeakingInteractionStr=self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr

			#/################/#
			# Build the LeakingWeigthVariable
			#

			#debug
			'''
			self.debug(
				[
					'We set the weigths in the Decod',
					'self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray)
				]
			)
			'''

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray.T

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool:

				#Check
				if self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr=="Rate":

					#debug
					'''
					self.debug(
						[
							'We have to rescale with the time constant of the decoder'
						]
					)
					'''

					#set
					self.LeakingWeigthVariable*=self.PredictedNetworkDerivePredicterVariable.PredictingDecoderTimeFloat

			#debug
			'''
			self.debug(
				[
					'In the end ',
					('self.',self,[
							'LeakingWeigthVariable'
						]),
					'self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray)
				]
			)
			'''

		elif self.ManagementTagStr=="Fast":

			#debug
			'''
			self.debug(
				[
					'We predict in the Fast interaction',
					('self.',self,[
						])
				]
			)
			'''

			#/################/#
			# Determine the relations
			#

			#set
			self.PredictedAgentDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.PredictedNetworkDerivePredicterVariable
	
			#/################/#
			# Determine the interactions
			#

			#link
			self.LeakingInteractionStr=self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr

			#/################/#
			# Build the LeakingWeigthVariable
			#

			#debug
			'''
			self.debug(
				[
					'We set the weigths in the Fast',
					'self.PredictedNetworkDerivePredicterVariable.PredictedFastFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedFastFloatsArray)
				]
			)
			'''

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedFastFloatsArray

		elif self.ManagementTagStr=="Slow":

			#debug
			'''
			self.debug(
				[
					'We predict in the Slow interaction',
					('self.',self,[
						])
				]
			)
			'''

			#/################/#
			# Determine the relations
			#

			#set
			self.PredictedAgentDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.PredictedSensorDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable["Sensor"]

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.PredictedNetworkDerivePredicterVariable
	
			#/################/#
			# Build the LeakingWeigthVariable
			#

			#debug
			'''
			self.debug(
				[
					'We set the weigths in the Slow',
					'self.PredictedNetworkDerivePredicterVariable.PredictedSlowFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedSlowFloatsArray)
				]
			)
			'''

			#Check
			if type(self.LeakingWeigthVariable)==None.__class__:

				#link
				self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedSlowFloatsArray

			#debug
			'''
			self.debug(
				[
					'In the end slow is ',
					('self.',self,[
							'LeakingWeigthVariable'
						])
				]
			)
			'''

		"""
		elif self.ManagementTagStr=="Antileak":

			#debug
			'''
			self.debug(
				[
					'We predict in the Antileak interaction',
					('self.',self,[
						])
				]
			)
			'''

			#/################/#
			# Determine the relations
			#

			#set
			self.PredictedAgentDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#set
			self.PredictedDecoderDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable.ManagementDict["Decoder"]

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/################/#
			# set LeakingWeigthVariable
			#

			#debug
			'''
			self.debug(
				[
					'We have setted the LeakingWeigthVariable in the antileak'
				]
			)
			'''

			#set
			#self.LeakingWeigthVariable='#scalar:1.'
			self.LeakingWeigthVariable=np.diag(
				np.ones(
					self.PredictedAgentDerivePredicterVariable.LeakingUnitsInt
				)
			)

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingRateCostVariable!=None:

				#debug
				'''
				self.debug(
					[
						'There is a cost'
					]
				)
				'''

				#mul
				self.LeakingWeigthVariable*=self.PredictedNetworkDerivePredicterVariable.PredictingRateCostVariable
		"""

	"""
	def brianInteraction(self):

		#/################/#
		# Base method
		#

		BaseClass.brianInteraction(self)

		#Check
		if self.ManagementTagStr=="Antileak":

			#special unique self connect
			self.BrianedSynapsesVariable.connect(False)

			#special unique self connect
			self.BrianedSynapsesVariable.connect('i==j')
	"""

	def leakInput(self):

		#call the base
		BaseClass.leakInput(self)

		#Check
		if self.ManagementTagStr=='Command':

			#/####################/#
			# Remove from record if it is DynamicBool False
			#

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool==False:

				#append
				self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList=SYS.append(
							self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList,
							self.LeakedSymbolStr
						)

				#debug
				'''
				self.debug(
					[
						'We have removed the I_Command from record and plot',
						'self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList is ',
						str(self.LeakedParentPopulationDeriveLeakerVariable.LeakedRecordSkipStrsList)
					]
				)
				'''


	def leakInteraction(self):

		#call the base
		BaseClass.leakInteraction(self)

		#Check
		if self.ManagementTagStr=="Encod":

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingEncodPlasticBool:

				#debug
				self.debug(
					[
						'We make the encod synapses plastic'
					]
				)

				#Check
				if self.LeakingInteractionStr=="Rate":
					
					#debug
					self.debug(
						[
							'It is a rate model',
							('self.',self,[
									'LeakedSymbolStr',
									'LeakingSymbolStr',
									'BrianingSynapsesDict'
								])
						]
					)

					#set
					BrianedModelStr='beta : 1'
					BrianedModelStr+='\nlambda : 1'
					BrianedModelStr+='\nd'+self.LeakingSymbolPrefixStr+'/dt=beta*('
					BrianedModelStr+='I_Command_post-lambda*'+self.LeakingSymbolPrefixStr+')'	

					#add
					self.BrianingSynapsesDict['model']+=BrianedModelStr

					#debug
					self.debug(
						[
							'after update of the model',
							('self.',self,[
									'BrianingSynapsesDict'
								])
						]
					)


				else:

					#debug
					self.debug(
						[
							'It is a spike model',
							('self.',self,[
									'LeakedSymbolStr',
									'LeakingSymbolStr',
									'BrianingSynapsesDict'
								])
						]
					)


					#set
					BrianedPreStr='\n'+self.LeakingSymbolPrefixStr+'+=0.*('+self.PredictedDecoderDerivePredicterVariable.LeakedSymbolStr+'_post'
					BrianedPreStr+='/mV)-'+self.LeakingSymbolPrefixStr

					#add
					self.BrianingSynapsesDict['pre']+=BrianedPreStr

					#debug
					self.debug(
						[
							'after update of the model',
							('self.',self,[
									'BrianingSynapsesDict'
								])
						]
					)

		#Check
		elif self.ManagementTagStr=='Fast':

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingFastPlasticBool:

				#debug
				self.debug(
					[
						'We make the fast synapses plastic'
					]
				)

				#Check
				if self.LeakingInteractionStr=="Rate":
					
					#debug
					self.debug(
						[
							'It is a rate model',
							('self.',self,[
									'LeakedSymbolStr',
									'LeakingSymbolStr',
									'BrianingSynapsesDict'
								])
						]
					)

					#set
					BrianedModelStr='epsilon : 1'
					BrianedModelStr+='\nalpha : 1'
					BrianedModelStr+='\nd'+self.LeakingSymbolPrefixStr+'/dt=epsilon*('
					BrianedModelStr+='dot(I_Command_post,'+self.PredictedAgentDerivePredicterVariable.LeakedSymbolStr+'_post)-alpha*'+self.LeakingSymbolPrefixStr+')'	

					#add
					self.BrianingSynapsesDict['model']+=BrianedModelStr

					#debug
					self.debug(
						[
							'after update of the model',
							('self.',self,[
									'BrianingSynapsesDict'
								])
						]
					)

				else:

					#debug
					self.debug(
						[
							'It is a spike model',
							('self.',self,[
									'LeakedSymbolStr',
									'LeakingSymbolStr',
									'BrianingSynapsesDict'
								])
						]
					)

					#add
					self.BrianingSynapsesDict['model']+='alpha : 1'

					#set
					BrianedPreStr='\n'+self.LeakingSymbolPrefixStr+'+=0.*(('+self.PredictedAgentDerivePredicterVariable.LeakedSymbolStr+'_post'
					if self.PredictedNetworkDerivePredicterVariable.PredictingAgentRestVariable!=None:
						BrianedPreStr+=str(
							self.PredictedNetworkDerivePredicterVariable.PredictingAgentRestVariable
						)+')/mV)+0.*((1+alpha)/2.)*'+self.LeakingSymbolPrefixStr
					else:
						BrianedPreStr+=')/mV)+0.*((1+alpha)/2.)*'+self.LeakingSymbolPrefixStr

					#add
					self.BrianingSynapsesDict['pre']+=BrianedPreStr

					#debug
					self.debug(
						[
							'after update of the model',
							('self.',self,[
									'BrianingSynapsesDict'
								])
						]
					)







		


	def viewSample(self):

		#debug
		'''
		self.debug(
			[
				'We predict view sample here',
				('self.',self,[
						'StructureTagStr'
					])
			]
		)
		'''

		#Check
		self.ViewingXScaleFloat=1000.
		self.ViewingYScaleFloat=1000.

		#base
		BaseClass.viewSample(self)

		#/#################/#
		# Special Agent case
		#

		#Check
		if self.BrianedParentPopulationDeriveBrianerVariable.ManagementTagStr=="Agent":

			#Check
			"""
			if self.BrianedParentPopulationDeriveBrianerVariable.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool:

				#Check
				ViewedCommandDerivePredicter=self.BrianedParentPopulationDeriveBrianerVariable.TeamDict[
					'Traces'
				].ManagementDict[
					'*J_EncodI_Command'
				].TeamDict[
					'Samples'
				].ManagementDict[
					'Default'
				]

				#debug
				self.debug(
					[
						'We view Sample Agent here',
						'We add also the view of the command',
						#'ViewedSensorDerivePredicter is ',
						#SYS._str(ViewedSensorDerivePredicter),
						'ViewedCommandDerivePredicter.PyplotingDrawVariable is ',
						SYS._str(ViewedCommandDerivePredicter.PyplotingDrawVariable)
					]
				)

				#import 
				import copy

				#copy
				ViewedPyplotDrawVariable=copy.deepcopy(
					ViewedSensorDerivePredicter.PyplotingDrawVariable
				)

				#set
				map(
					lambda __ItemTuple:
					__ItemTuple[1][
						'#kwarg'
					].update(
						{
							'linestyle':'--',
							'linewidth':1
						}
					),
					ViewedPyplotDrawVariable
					#self.PyplotingDrawVariable
				)

				#add
				self.PyplotingDrawVariable.extend(
					ViewedPyplotDrawVariable
				)

				#debug
				'''
				self.debug(
					[
						'In the end',
						('self.',self,[
							'PyplotingDrawVariable'
						])
						
					]
				)
				'''
			"""

		#/#################/#
		# Special Decoder case
		#

		#Check
		elif self.BrianedParentPopulationDeriveBrianerVariable.ManagementTagStr=="Decoder":

			#
			ViewedSensorDerivePredicter=self.BrianedParentPopulationDeriveBrianerVariable.PredictedSensorDerivePredicterVariable.TeamDict[
				'Traces'
			].ManagementDict[
				'*U'
			].TeamDict[
				'Samples'
			].ManagementDict[
				'Default'
			]

			#debug
			'''
			self.debug(
				[
					'We view Sample Decoder here',
					'We add also the view of the sensor',
					#'ViewedSensorDerivePredicter is ',
					#SYS._str(ViewedSensorDerivePredicter),
					'ViewedSensorDerivePredicter.PyplotingDrawVariable is ',
					SYS._str(ViewedSensorDerivePredicter.PyplotingDrawVariable)
				]
			)
			'''
			
			#import 
			import copy

			#copy
			ViewedPyplotDrawVariable=copy.deepcopy(
				ViewedSensorDerivePredicter.PyplotingDrawVariable
			)

			#set
			map(
				lambda __ItemTuple:
				__ItemTuple[1][
					'#kwarg'
				].update(
					{
						'alpha':0.3
					}
				),
				ViewedPyplotDrawVariable
			)

			#set
			map(
				lambda __ItemTuple:
				__ItemTuple[1][
					'#kwarg'
				].update(
					{
						'linestyle':'--'
					}
				),
				self.PyplotingDrawVariable
			)

			#:
			ViewedReversePyplotDrawVariable=ViewedPyplotDrawVariable[:]
			ViewedReversePyplotDrawVariable.reverse()

			#add
			map(
				lambda __Variable:
				self.PyplotingDrawVariable.insert(
					0,
					__Variable
				),
				ViewedReversePyplotDrawVariable
			)

			#debug
			'''
			self.debug(
				[
					'In the end',
					('self.',self,[
						'PyplotingDrawVariable'
					])
					
				]
			)
			'''

	def pyplotFigure(self):

		#debug
		'''
		self.debug(
			[
				'We pyplot figure predict here'
			]
		)
		'''

		#Check
		if self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr=="Spike":

			#debug
			'''
			self.debug(
				[
					"It it a spike model, we make bigger the size",
					('self.',self,[
							'PyplotingShapeVariable'
						])
				]
			)
			'''

			#add
			self.PyplotingGridIntsTuple=(
				self.PyplotingGridIntsTuple[0]+7,
				self.PyplotingGridIntsTuple[1]
			)

		#call the base
		BaseClass.pyplotFigure(self)




	def setDebugNeurongroup(self):

		#/################/#
		# Call the base
		# 

		#set
		BaseClass.setDebugNeurongroup(self)

		#Check
		if self.ManagementTagStr=="Decoder":

			#Check
			PrintStr='In the Decod, LeakingWeigthVariable is \n'
			LeakingWeigthVariable=self.PredictedAgentDerivePredicterVariable.TeamDict["Interactions"
			].ManagementDict["Decod"].LeakingWeigthVariable
			PrintStr+=str(LeakingWeigthVariable)

			#print
			print PrintStr

	def brianTrace(self):

		#/###################/#
		# std
		#

		#debug
		'''
		self.debug(
			[
				'We reduce the size of initial conditions'
			]
		)
		'''

		#set
		self.NumscipyingStdFloat=0.00001

		#/################/#
		# switch case
		#

		#Check
		if self.ManagementTagStr=='*U':

			#/###################/#
			# Switch case
			#

			#Check
			if self.LeakedParentPopulationDeriveLeakerVariable.ManagementTagStr=="Sensor":

				#debug
				'''
				self.debug(
					[
						'We set a special label name for the Sensor'
					]
				)
				'''

				#set
				self.BrianingActivityStr="x"

			#Check
			if self.LeakedParentPopulationDeriveLeakerVariable.ManagementTagStr=="Agent":

				#debug
				'''
				self.debug(
					[
						'We set a special label name for the Agent'
					]
				)
				'''

				#Check
				if self.LeakedParentPopulationDeriveLeakerVariable.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr=="Rate":

					#set
					self.BrianingActivityStr="r" 

				else:

					#set
					self.BrianingActivityStr="V"

					#debug
					'''
					self.debug(
						[
							'We init under the thresholds',
							'self.LeakedParentPopulationDeriveLeakerVariable.LeakingThresholdVariable is ',
							str(self.LeakedParentPopulationDeriveLeakerVariable.LeakingThresholdVariable)
						]
					)
					'''

					#set
					self.NumscipyingMeanFloat=100.*(
						self.LeakedParentPopulationDeriveLeakerVariable.LeakingThresholdVariable.min()-0.5
					)




			#Check
			elif self.LeakedParentPopulationDeriveLeakerVariable.ManagementTagStr=="Decoder":

				#debug
				'''
				self.debug(
					[
						'We set a special label name for the Decoder'
					]
				)
				'''

				#set
				self.BrianingActivityStr="\hat{x}"

		#Check
		elif self.ManagementTagStr=='*I_Command':

			#debug
			'''
			self.debug(
				[
					'We set a special label name for the I_Command'
				]
			)
			'''

			#set
			self.BrianingActivityStr="c"


		#/################/#
		# brianTrace base
		#

		#debug
		'''
		self.debug(
			[
				'We call the base method',
				str(BaseClass.brianTrace)
			]
		)
		'''

		#call the base
		BaseClass.brianTrace(self)



		
	"""
	def leakSample(self):

		#debug
		'''
		self.debug(
			[
				'We predict leak Sample here'
			]
		)
		'''

		#set
		self.ViewingXScaleFloat=1000.
		self.ViewingYScaleFloat=1000.
	"""

#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=PredicterClass
#<DefineLocals>

#</DefinePrint>
PredicterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'PredictingSensorUnitsInt',
		'PredictingAgentUnitsInt',
		'PredictingDaleBool',
		'PredictingDynamicBool',
		'PredictingJacobianVariable',
		'PredictingEncodPerturbStdFloat',
		'PredictingCommandVariable',
		'PredictingRateCostVariable',
		'PredictingRateTransferVariable',
		'PredictingAgentTimeFloat',
		'PredictingAgentRestVariable',
		'PredictingAgentResetVariable',
		'PredictingFastSymmetryFloat',
		'PredictingSlowPerturbStdFloat',
		'PredictingDecoderVariable',
		'PredictingDecoderMeanFloat',
		'PredictingDecoderStdFloat',
		'PredictingDecoderProbabilityFloat',
		'PredictingDecoderTimeFloat',
		'PredictingDecoderNormalisationInt',
		'PredictingEncodPlasticBool',
		'PredictingFastPerturbStdFloat',
		'PredictingInteractionStr',
		'PredictingFastPlasticBool',
		'PredictedDynamicDict',
		'PredictedSensorJacobianFloatsArray',
		'PredictedDecoderFloatsArray',
		'PredictedFastFloatsArray',
		'PredictedThresholdFloatsArray',
		'PredictedSlowFloatsArray',
		'PredictedParentSingularStr',
		'PredictedSensorDerivePredicterVariable',
		'PredictedAgentDerivePredicterVariable',
		'PredictedDecoderDerivePredicterVariable',
		'PredictedNetworkDerivePredicterVariable'
	]
)
#<DefinePrint>