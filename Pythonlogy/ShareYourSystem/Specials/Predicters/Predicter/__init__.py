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
			_PredictingDecoderVariable=None,
			_PredictingTimeFloat=1.,
			_PredictingDynamicStr='Track',
			_PredictingCostFloat=1.,
			_PredictedJacobianFloatsArray=None,
			_PredictedDecoderFloatsArray=None,
			_PredictedFastFloatsArray=None,
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
		if (self.ParentDeriveTeamerVariable==None or 'Populations' in self.TeamDict or self.ParentDeriveTeamerVariable.TeamTagStr not in [
			'Traces',
			'Samples',
			'Events',
			'Interactomes',
			'Interactions',
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
					'Populations',
					'Inputs',
					'Interactomes',
					'Interactions',
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

		#debug
		'''
		self.debug(
			[
				'We predict network here',
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
		# Check for Sensor
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
		# Check for Agent
		# 

		#Check
		if 'Agent' in LeakedPopulationsDeriveManager.ManagementDict:

			#get
			LeakedAgentDerivePredicter=LeakedPopulationsDeriveManager.ManagementDict[
				'Agent'
			]

		else:

			#manage
			LeakedAgentDerivePredicter=LeakedPopulationsDeriveManager.manage(
				'Agent'
			).ManagedValueVariable

		#/###################/#
		# Check for Decoder
		# 

		#Check
		if 'Decoder' in LeakedPopulationsDeriveManager.ManagementDict:

			#get
			LeakedDecoderDerivePredicter=LeakedPopulationsDeriveManager.ManagementDict[
				'Decoder'
			]

		else:

			#manage
			LeakedDecoderDerivePredicter=LeakedPopulationsDeriveManager.manage(
				'Decoder'
			).ManagedValueVariable

		#debug
		self.debug(
			[
				'Ok we have created the Decoder'
			]
		)

		#import
		import numpy as np

		#/################/#
		# Build the Jacobian
		#

		#Check
		if self.PredictingDynamicStr=="Track":

			#diag
			self.PredictedJacobianFloatsArray=-(1./0.01)*np.diag(
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
			self.PredictedJacobianFloatsArray=-np.diag(
				(1./self.PredictingTimeFloat)*np.ones(
					self.PredictingSensorUnitsInt
				)
			)

			#set
			self.PredictedJacobianFloatsArray[0,0]+=(1.5/self.PredictingTimeFloat)
			self.PredictedJacobianFloatsArray[1,0]+=-(3.7/self.PredictingTimeFloat)
			self.PredictedJacobianFloatsArray[0,1]+=(3.7/self.PredictingTimeFloat)
			self.PredictedJacobianFloatsArray[1,1]+=-(1./self.PredictingTimeFloat)

			#Check
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

		#/################/#
		# Build the DecoderFloatsArray
		#

		#Check
		if type(self.PredictingDecoderVariable) in [list,tuple,np.ndarray]: 

			#Check
			self.PredictedDecoderFloatsArray=self.PredictingDecoderVariable

		else:

			#numscipy
			self.NumscipyingRowsInt=self.PredictingAgentUnitsInt
			self.NumscipyingColsInt=self.PredictingSensorUnitsInt
			self.numscipy()

			#Check
			self.PredictedDecoderFloatsArray=self.NumscipiedRandomFloatsArray

		#/################/#
		# Build the Fast Connection
		#

		#diag
		self.PredictedFastFloatsArray=np.dot(
			self.PredictedDecoderFloatsArray.T,
			self.PredictedDecoderFloatsArray
		)

		#Check
		if self.PredictingDynamicStr:

			#/################/#
			# Build the Slow Connection
			#

			#diag
			self.PredictedSlowFloatsArray=self.PredictedJacobianFloatsArray+self.PredictingTimeFloat*np.diag(
				np.ones(
					self.PredictingSensorUnitsInt
				)
			)

			#dot
			self.PredictedSlowFloatsArray=np.dot(
				self.PredictedSlowFloatsArray,
				self.PredictedDecoderFloatsArray
			)

			#link
			self.PredictedSlowFloatsArray=np.dot(
				self.PredictedDecoderFloatsArray.T,
				self.PredictedSlowFloatsArray
			)

	def predictPopulation(self):

		#debug
		self.debug(
			[
				'We predict Population here'
			]
		)

		#Check
		if self.ManagementTagStr=='Sensor':

			#debug
			'''
			self.debug(
				[
					'We predict in the Sensor',
					('self.',self,[
							'PredictingTimeFloat'
						])
				]
			)
			'''

			#/####################/#
			# Simplify the leak equation
			#

			#set
			self.LeakingTimeVariable='#scalar:1.*second'

			#set
			self.LeakingWeigthVariable='0'

			#/####################/#
			# Find the Sensor Population
			#

			#set
			self.PredictedNetworkDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Determine the number of leaking units
			#

			#debug
			self.debug(
				[
					'Look for LeakingUnitsInt',
					('self.',self,[
							'LeakingUnitsInt',
							'PredictingSensorUnitsInt'
						])
				]
			)

			#set default
			if self.LeakingUnitsInt==0:
				self.LeakingUnitsInt=1

			#set
			if self.PredictedNetworkDerivePredicterVariable.PredictingSensorUnitsInt>-1:
				self.LeakingUnitsInt=self.PredictedNetworkDerivePredicterVariable.PredictingSensorUnitsInt

			#/###################/#
			# Check for Inputs in the Sensor
			#

			#Check
			if 'Inputs' in self.TeamDict:

				#get
				LeakedInputsDeriveManager=self.TeamDict[
					'Inputs'
				]

			else:

				#team
				LeakedInputsDeriveManager=self.team(
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

			#/###################/#
			# Check for Interactions in the Sensor
			#

			#Check
			if 'Interactions' in self.TeamDict:

				#get
				LeakedInteractionsDeriveManager=self.TeamDict[
					 'Interactions'
				]

			else:

				#team
				LeakedInteractionsDeriveManager=self.team(
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


			#Check
			if self.LeakingInteractionStr=='Rate':

				#/###################/#
				# Specify the Sensor to Agent interaction
				#

				#Check
				if 'Encod' in LeakedInteractionsDeriveManager.ManagementDict:

					#get
					LeakedEncoderDerivePredicter=LeakedInteractionsDeriveManager.ManagementDict[
						'Encod'
					]

				else:

					#manage
					LeakedEncoderDerivePredicter=LeakedInteractionsDeriveManager.manage(
						'Encod'
					).ManagedValueVariable

				#debug
				'''
				self.debug(
					[
						'We have defined the Encoder interaction in the Sensor'
					]
				)
				'''

		elif self.ManagementTagStr=='Agent':

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
			self.PredictedSensorDerivePredicterVariable=self.ParentDeriveTeamerVariable.ManagementDict['Sensor']

			#set
			self.PredictedNetworkDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Set the mu cost
			#

			#str
			self.LeakingWeigthVariable=str(self.PredictedNetworkDerivePredicterVariable.PredictingCostFloat)
			
			#/####################/#
			# LeakingUnitsInt
			#

			#debug
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

			#set default
			if self.LeakingUnitsInt==0:
				self.LeakingUnitsInt=1

			#set
			if self.PredictedNetworkDerivePredicterVariable.PredictingAgentUnitsInt>-1:
				self.LeakingUnitsInt=self.PredictedNetworkDerivePredicterVariable.PredictingAgentUnitsInt

			#/####################/#
			# Build the decoder weigths
			#

			#debug
			'''
			self.debug(
				[
					'We have defined the Encoder interaction in the Sensor'
				]
			)
			'''

			#/###################/#
			# Check for Interactions in the Agent
			#

			#Check
			if 'Interactions' in self.TeamDict:

				#get
				LeakedInteractionsDeriveManager=self.TeamDict[
					 'Interactions'
				]

			else:

				#team
				LeakedInteractionsDeriveManager=self.team(
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
			LeakedFastDerivePredicter.ConnectingKeyVariable=self

			#debug
			self.debug(
				[
					'We have defined the Fast interaction in the Agent',
					'Look maybe for slow',
					'self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool)
				]
			)

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

				#Check
				if 'Slow' in LeakedInteractionsDeriveManager.ManagementDict:

					#get
					LeakedSlowDerivePredicter=LeakedInteractionsDeriveManager.ManagementDict[
						'Slow'
					]

				else:

					#manage
					LeakedSlowDerivePredicter=LeakedInteractionsDeriveManager.manage(
						'Slow'
					).ManagedValueVariable

				#debug
				'''
				self.debug(
					[
						'We have defined the Decod interaction in the Agent'
					]
				)
				'''

				#set the connect target
				LeakedSlowDerivePredicter.ConnectingKeyVariable=self

			else:

				#Check
				if self.LeakingInteractionStr=='Rate':

					#debug
					self.debug(
						[
							'PredictingDynamicBool is False',
							"self.LeakingInteractionStr=='Rate'",
							'So set a direct interaction'
						]
					)

					#/###################/#
					# Specify the Decoder interaction
					#

					#Check
					if 'Decod' in LeakedInteractionsDeriveManager.ManagementDict:

						#get
						LeakedDecodDerivePredicter=LeakedInteractionsDeriveManager.ManagementDict[
							'Decod'
						]

					else:

						#manage
						LeakedDecodDerivePredicter=LeakedInteractionsDeriveManager.manage(
							'Decod'
						).ManagedValueVariable

					#set the connect target
					LeakedDecodDerivePredicter.ConnectingKeyVariable=self.ParentDeriveTeamerVariable.ManagementDict[
						'Decoder'
					]

		#Check
		elif self.ManagementTagStr=='Decoder':

			#debug
			'''
			self.debug(
				[
					'We predict in the Decoder',
					('self.',self,[
							'PredictingTimeFloat'
						])
				]
			)
			'''

			#/####################/#
			# Determine the parent
			#

			#set
			self.PredictedAgentDerivePredicterVariable=self.ParentDeriveTeamerVariable.ManagementDict['Agent']

			#set
			self.PredictedNetworkDerivePredicterVariable=self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

			#/####################/#
			# Determine the number of leaking units
			#

			#debug
			self.debug(
				[
					'Look for LeakingUnitsInt',
					('self.',self,[
							'LeakingUnitsInt',
							'PredictingSensorUnitsInt'
						])
				]
			)

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
				self.debug(
					[
						'self.PredictedNetworkDerivePredicterVariable.PredictingDynamicBool is False',
						'set LeakingTimeVariable to 0'
					]
				)

				#set
				self.LeakingTimeVariable=0.
			
	def predictInput(self):

		#Check
		if self.ManagementTagStr=='Command':
	
			#set
			self.LeakingWeigthVariable="#custom:#clock:200*ms:5.*mV*int(t==200*ms)"

	def predictInteraction(self):

		#Check
		if self.ManagementTagStr=='Jacobian':

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
			self.PredictedAgentDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.ParentDeriveTeamerVariable.ManagementDict['Agent']

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.PredictedNetworkDerivePredicterVariable

			#set
			self.ConnectingKeyVariable=self.PredictedSensorDerivePredicterVariable

			#debug
			'''
			self.debug(
				[
					'We have determine the relations for predictInteraction',
					('self.',self,[
						'ConnectingKeyVariable'
					])
				]
			)
			'''

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedJacobianFloatsArray

		#Check
		elif self.ManagementTagStr=='Encod':

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
			self.PredictedAgentDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.ParentDeriveTeamerVariable.ManagementDict['Agent']

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedSensorDerivePredicterVariable.PredictedNetworkDerivePredicterVariable
	
			#set
			self.ConnectingKeyVariable=self.PredictedAgentDerivePredicterVariable

			#/################/#
			# Build the LeakingWeigthVariable
			#

			#debug
			self.debug(
				[
					'We set the weigths in the Encod',
					'self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray)
				]
			)

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray.T

		elif self.ManagementTagStr=='Decod':

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
			self.PredictedDecoderDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable.ManagementDict['Decoder']

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
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedDecoderFloatsArray

		elif self.ManagementTagStr=='Fast':

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

			#import 
			import numpy

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedFastFloatsArray

		elif self.ManagementTagStr=='Slow':

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
			self.PredictedSensorDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.ParentDeriveTeamerVariable['Sensor']

			#set
			self.PredictedNetworkDerivePredicterVariable=self.PredictedAgentDerivePredicterVariable.PredictedNetworkDerivePredicterVariable
	
			#/################/#
			# Build the LeakingWeigthVariable
			#

			#import 
			import numpy as np

			#debug
			self.debug(
				[
					'We set the weigths in the Slow',
					'self.PredictedNetworkDerivePredicterVariable.PredictedSlowFloatsArray is ',
					str(self.PredictedNetworkDerivePredicterVariable.PredictedSlowFloatsArray)
				]
			)

			#link
			self.LeakingWeigthVariable=self.PredictedNetworkDerivePredicterVariable.PredictedSlowFloatsArray






	def viewSample(self):

		#debug
		'''
		self.debug(
			[
				'We predict view sample here'
			]
		)
		'''
		
		#Check
		self.ViewingXScaleFloat=1000.
		self.ViewingYScaleFloat=1000.

		#base
		BaseClass.viewSample(self)

		#/#################/#
		# Special Decoder case
		#

		#Check
		if self.BrianedParentPopulationDeriveBrianerVariable.ManagementTagStr=='Decoder':

			#debug
			self.debug(
				[
					'We view Sample Decoder here',
					'We add also the view of the sensor'
				]
			)

	def setDebugNeurongroup(self):

		#/################/#
		# Call the base
		# 

		#set
		BaseClass.setDebugNeurongroup(self)

		#Check
		if self.ManagementTagStr=='Decoder':

			#Check
			PrintStr='In the Decod, LeakingWeigthVariable is \n'
			LeakingWeigthVariable=self.PredictedAgentDerivePredicterVariable.TeamDict['Interactions'].ManagementDict['Decod'].LeakingWeigthVariable
			PrintStr+=str(LeakingWeigthVariable)

			#print
			print PrintStr


		
	def brianTrace(self):

		#/###################/#
		# std
		#

		#debug
		self.debug(
			[
				'We reduce the size of initial conditions'
			]
		)

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
			if self.LeakedParentPopulationDeriveLeakerVariable.ManagementTagStr=='Sensor':

				#debug
				self.debug(
					[
						'We set a special label name for the Sensor'
					]
				)

				#set
				self.BrianingActivityStr="x"

			#Check
			elif self.LeakedParentPopulationDeriveLeakerVariable.ManagementTagStr=='Decoder':

				#debug
				self.debug(
					[
						'We set a special label name for the Decoder'
					]
				)

				#set
				self.BrianingActivityStr="\hat{x}"

		#Check
		elif self.ManagementTagStr=='*I_Command':

			#debug
			self.debug(
				[
					'We set a special label name for the I_Command'
				]
			)

			#set
			self.BrianingActivityStr="c"


		#/################/#
		# brianTrace base
		#

		#debug
		self.debug(
			[
				'We call the base method'
			]
		)

		#call the base
		BaseClass.brianTrace(self)


		a=getattr(
			self.BrianedParentPopulationDeriveBrianerVariable.BrianedNeurongroupVariable,
			self.RecordKeyStr
		)

		#debug
		self.debug(
			[
				'In the end',
				'a is ',
				str(a)
			]
		)

		
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
		'PredictingDecoderVariable',
		'PredictingTimeFloat',
		'PredictingDynamicStr',
		'PredictedJacobianFloatsArray',
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