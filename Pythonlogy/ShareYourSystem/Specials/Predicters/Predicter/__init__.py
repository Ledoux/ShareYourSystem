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
			_PredictingSensorUnitsInt=-1,
			_PredictingAgentUnitsInt=-1,
			_PredictingDaleBool=False,
			_PredictingDynamicBool=True,
			_PredictingDynamicStr='Track',
			_PredictingCommandVariable=None,
			_PredictingEncodPerturbStdFloat=0.,
			_PredictingRateCostVariable=None,
			_PredictingRateTransferVariable=None,
			_PredictingAgentTimeFloat=10.,
			_PredictingFastSymmetryFloat=1.,
			_PredictingDecoderVariable=None,
			_PredictingDecoderStdFloat=1.,
			_PredictingDecoderTimeFloat=1.,
			_PredictingDecoderNormalisationInt=1,
			_PredictingFastPerturbStdFloat=0.,
			_PredictingInteractionStr="Rate",
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

		#Check
		if self.PredictingDynamicStr=="Track":

			#debug
			self.debug(
				[
					'We set a sensor variable leaking at 100ms'
				]
			)

			#diag
			self.PredictedSensorJacobianFloatsArray=-0.1*np.diag(
				np.ones(
					self.PredictingSensorUnitsInt
				)
			)

		elif self.PredictingDynamicStr in ["Gamma","Gamma-Theta"]:

			#Check
			if self.PredictingDynamicStr=="Gamma" and self.PredictingSensorUnitsInt<3:
				self.PredictingSensorUnitsInt=2
			if self.PredictingDynamicStr=="Gamma-Theta" and self.PredictingSensorUnitsInt<6:
				self.PredictingSensorUnitsInt=6

			#diag
			self.PredictedSensorJacobianFloatsArray=-np.diag(
				(1./self.PredictingDecoderTimeFloat)*np.ones(
					self.PredictingSensorUnitsInt
				)
			)

			#set
			self.PredictedSensorJacobianFloatsArray[0,0]+=(1.5/self.PredictingDecoderTimeFloat)
			self.PredictedSensorJacobianFloatsArray[1,0]+=-(3.7/self.PredictingDecoderTimeFloat)
			self.PredictedSensorJacobianFloatsArray[0,1]+=(3.7/self.PredictingDecoderTimeFloat)
			self.PredictedSensorJacobianFloatsArray[1,1]+=-(1./self.PredictingDecoderTimeFloat)

			#Check
			if self.PredictingDynamicStr=="Gamma-Theta":

				#set
				self.PredictedSensorJacobianFloatsArray[2,3]+=(1./self.PredictingDecoderTimeFloat)
				self.PredictedSensorJacobianFloatsArray[3,4]+=-(1.2/self.PredictingDecoderTimeFloat)
				self.PredictedSensorJacobianFloatsArray[4,5]+=-(1.4/self.PredictingDecoderTimeFloat)
				self.PredictedSensorJacobianFloatsArray[5,2]+=-(1.6/self.PredictingDecoderTimeFloat)

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
			PredictedShapeIntsList=list(np.shape(self.PredictingDecoderVariable))

			#debug
			self.debug(
				[
					'Update the PredictingAgentUnitsInt with the size of the array',
					'PredictedShapeIntsList is ',
					str(PredictedShapeIntsList),
					'len(PredictedShapeIntsList) is',
					str(len(PredictedShapeIntsList))
				]
			)

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
			self.debug(
				[
					'Now',
					('self.',self,[
							'PredictingAgentUnitsInt'
						])
				]
			)

		else:

			#numscipy
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
			self.debug(
				[
					'We build a symmetry fast connectivity',
					('self.',self,[
							'PredictingFastSymmetryFloat',
							'PredictedDecoderFloatsArray'
						])
				]
			)

			#diag
			self.PredictedFastFloatsArray=-self.PredictingFastSymmetryFloat*np.dot(
				self.PredictedDecoderFloatsArray.T,
				self.PredictedDecoderFloatsArray
			)

		else:

			#debug
			self.debug(
				[
					'PredictingFastSymmetryFloat is null'
				]
			)

			#pinv
			self.PredictedDecoderFloatsArray=self.PredictingRateCostVariable*np.linalg.pinv(
				self.PredictedDecoderFloatsArray.T
			)

		#debug
		self.debug(
			[
				'Look if we have to perturb',
				'self.PredictingFastPerturbStdFloat is ',
				str(self.PredictingFastPerturbStdFloat)
			]
		)

		#Check
		if self.PredictingFastPerturbStdFloat>0.:

			#numscipy
			self.NumscipyingStdFloat=self.PredictingFastPerturbStdFloat
			self.NumscipyingRowsInt=self.PredictingAgentUnitsInt
			self.NumscipyingColsInt=self.PredictingAgentUnitsInt
			self.numscipy()

			#debug
			self.debug(
				[
					'We are going to add',
					('self.',self,[
							'NumscipiedRandomFloatsArray'
						])
				]
			)

			#link
			self.PredictedFastFloatsArray+=self.NumscipiedRandomFloatsArray

		#debug
		self.debug(
			[
				'We have builded the fast connections',
				('self.',self,[
						'PredictedFastFloatsArray'
					])
			]
		)

		#/################/#
		# Build the Thresholds
		#

		#Check
		if self.PredictingInteractionStr=="Spike":

			#Compute
			self.PredictedFastFloatsArray=(self.PredictedDecoderFloatsArray**2)/2.

		#Check
		if self.PredictingDynamicBool:

			#/################/#
			# Build the Slow Connection
			#

			#debug
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

			#diag
			self.PredictedSlowFloatsArray=self.PredictedSensorJacobianFloatsArray+(
				1./self.PredictingDecoderTimeFloat
			)*np.diag(
				np.ones(
					self.PredictingSensorUnitsInt
				)
			)

			#debug
			self.debug(
				[
					'In intermediate values',
					('self.',self,[
							'PredictedSlowFloatsArray'
						])
				]
			)

			#link
			self.PredictedSlowFloatsArray=np.dot(
				self.PredictedDecoderFloatsArray.T,
				self.PredictedSlowFloatsArray
			)

			#debug
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

		#/###############/#
		# Renormalize compared to the rate model time constant
		#

		#debug
		self.debug(
			[
				'As we divide by a rate time constant of 10ms in the agent',
				'We need here to multiply by 10 the connectivity',
				('self.',self,[
						'PredictingAgentTimeFloat'
					])
			]
		)

		#set
		self.PredictedFastFloatsArray*=self.PredictingAgentTimeFloat
		if type(self.PredictedSlowFloatsArray)!=None.__class__:
			self.PredictedSlowFloatsArray*=self.PredictingAgentTimeFloat

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
			self.debug(
				[
					'set the LeakingTransferVariable'
				]
			)

			#set
			self.LeakingTransferVariable=self.PredictedNetworkDerivePredicterVariable.PredictingRateTransferVariable
										
			#debug
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

			#/####################/#
			# Set the time constant
			#

			#set
			self.LeakingInteractionStr=self.PredictedNetworkDerivePredicterVariable.PredictingInteractionStr

			#Check
			if self.LeakingInteractionStr=="Spike":
				
				#alias
				self.LeakingThresholdVariable=self.PredictedNetworkDerivePredicterVariable.PredictedThresholdFloatsArray

				#debug
				self.debug(
					[
						'The agents are IF models',
						('self.',self,[
								'LeakingThresholdVariable'
							])
					]
				)

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
			self.debug(
				[
					'The agents are rate models',
					'self.PredictedNetworkDerivePredicterVariable.PredictingAgentTimeFloat is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictingAgentTimeFloat)
				]
			)

			#set
			self.LeakingTimeVariable='#scalar:'+str(
				self.PredictedNetworkDerivePredicterVariable.PredictingAgentTimeFloat
			)+'*ms'


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
				self.debug(
					[
						'PredictingDynamicBool is False',
						"self.LeakingInteractionStr=='Rate' ",
						'So set a direct interaction'
					]
				)

				
				#/####################/#
				# Transfer function Case
				#

				#Check
				if self.LeakingTransferVariable!=None:

					#debug
					self.debug(
						[
							'We are in the rate and there is a transfer function',
							'build the antileak connection'
						]
					)

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

				else:

					#Check
					if self.PredictedNetworkDerivePredicterVariable.PredictingRateCostVariable==None:

						#debug
						self.debug(
							[
								"There is no transfer function neither rate cost ",
								"so put the leak term to null"
							]
						)

						#set
						self.LeakingWeigthVariable='0'

					else:

						#debug
						self.debug(
							[
								"There is no transfer function neither rate cost ",
								"so put the leak term to null"
							]
						)

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
			self.debug(
				[
					'We set here the Command dynamic',
					('self.',self,[
							'LeakingWeigthVariable'
						])
				]
			)

	def predictInteraction(self):

		#Check
		if self.ManagementTagStr=="Jacobian":

			#debug
			'''
			self.debug(
				[
					'We predict in the Jacobian',
					('self.',self,[
							'PredictingDynamicStr'
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
			self.debug(
				[
					'Is it Rate : put x as post',
					'Is it Spike : put c as post',
					"self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool is ",
					self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool
				]
			)

			#set
			self.LeakingInteractionStr='Rate'

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool:

				#debug
				self.debug(
					[
						'There is a dynamic to transfer',
						'so we bind c instead of x'
					]
				)

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

			#/################/#
			# Build the LeakingWeigthVariable
			#

			#debug
			self.debug(
				[
					'We set the weigths in the Decod',
					'self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray)
				]
			)

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray.T

			#Check
			if self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool:

				#debug
				self.debug(
					[
						'We have to rescale with the time constant of the decoder'
					]
				)

				#set
				self.LeakingWeigthVariable*=self.PredictedNetworkDerivePredicterVariable.PredictingDecoderTimeFloat

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
			# Build the LeakingWeigthVariable
			#

			#debug
			self.debug(
				[
					'We set the weigths in the Fast',
					'self.PredictedNetworkDerivePredicterVariable.PredictedFastFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedFastFloatsArray)
				]
			)

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
			self.debug(
				[
					'In the end slow is ',
					('self.',self,[
							'LeakingWeigthVariable'
						])
				]
			)


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

	def viewSample(self):

		#debug
		self.debug(
			[
				'We predict view sample here',
				('self.',self,[
						'StructureTagStr'
					])
			]
		)
		
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
				].__setitem__(
					'linestyle',
					'--'
				),
				#ViewedPyplotDrawVariable
				self.PyplotingDrawVariable
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
		self.NumscipyingStdFloat=0.001

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
		'PredictingDynamicStr',
		'PredictingEncodPerturbStdFloat',
		'PredictingCommandVariable',
		'PredictingRateCostVariable',
		'PredictingRateTransferVariable',
		'PredictingFastSymmetryFloat',
		'PredictingDecoderVariable',
		'PredictingDecoderStdFloat',
		'PredictingDecoderTimeFloat',
		'PredictingDecoderNormalisationInt',
		'PredictingFastPerturbStdFloat',
		'PredictedSensorJacobianFloatsArray',
		'PredictedDecoderFloatsArray',
		'PredictedFastFloatsArray',
		'PredictedSlowFloatsArray',
		'PredictedParentSingularStr',
		'PredictedSensorDerivePredicterVariable',
		'PredictedAgentDerivePredicterVariable',
		'PredictedDecoderDerivePredicterVariable',
		'PredictedNetworkDerivePredicterVariable'
	]
)
#<DefinePrint>