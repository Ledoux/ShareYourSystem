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
			_PredictingUnitsInt=1,
			_PredictingDaleBool=False,
			_PredictingDynamicBool=True,
			_PredictingDecoderVariable=None,
			_PredictingTimeVariable='#scalar:10.*ms',
			_PredictingDynamicStr='Track',
			_PredictedDecoderFloatsArray=None,
			_PredictedJacobianFloatsArray=None,
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

			#set default
			LeakedSensorDerivePredicter.LeakingUnitsInt=1

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

			#set default
			LeakedAgentDerivePredicter.LeakingUnitsInt=1

	def predictPopulation(self):

		#Check
		if self.ManagementTagStr=='Sensor':

			#debug
			'''
			self.debug(
				[
					'We predict in the Sensor',
					('self.',self,[
							'PredictingTimeVariable'
						])
				]
			)
			'''

			#Check
			self.LeakingTimeVariable=self.PredictingTimeVariable

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
				if 'Encoder' in LeakedInteractionsDeriveManager.ManagementDict:

					#get
					LeakedEncoderDerivePredicter=LeakedInteractionsDeriveManager.ManagementDict[
						'Encoder'
					]

				else:

					#manage
					LeakedEncoderDerivePredicter=LeakedInteractionsDeriveManager.manage(
						'Encoder'
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

			#set
			self.LeakingUnitsInt=self.PredictingUnitsInt

			#import 
			import numpy

			#Check
			if type(self.PredictingDecoderVariable) in [list,tuple,numpy.ndarray]: 

				#Check
				self.PredictedDecoderFloatsArray=self.PredictingDecoderVariable

			else:

				#numscipy
				self.NumscipyingRowsInt=self.LeakingUnitsInt
				self.NumscipyingColsInt=self.PredictedSensorDerivePredicterVariable.LeakingUnitsInt
				self.numscipy()

				#Check
				self.PredictedDecoderFloatsArray=self.NumscipiedRandomFloatsArray


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

				#set the connect target
				LeakedSlowDerivePredicter.ConnectingKeyVariable=self

				#debug
				'''
				self.debug(
					[
						'We have defined the Slow interaction in the Agent'
					]
				)
				'''
	
		#Check
		elif self.ManagementTagStr=='Decoder':

			#debug
			'''
			self.debug(
				[
					'We predict in the Decoder',
					('self.',self,[
							'PredictingTimeVariable'
						])
				]
			)
			'''

			#Check
			self.LeakingTimeVariable=self.PredictingTimeVariable


	def predictInput(self):

		if self.ManagementTagStr=='Command':
	
			#set
			self.LeakingWeigthVariable="#custom:#clock:200*ms:5.*mV*int(t==200*ms)"

	def predictInteraction(self):

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
			self.ConnectingKeyVariable=self.PredictedSensorDerivePredicterVariable

			#/################/#
			# Build the Jacobian
			#

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

		#Check
		elif self.ManagementTagStr=='Encoder':

			#debug
			'''
			self.debug(
				[
					'We predict in the Encoder interaction',
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
			self.ConnectingKeyVariable=self.PredictedAgentDerivePredicterVariable

			#link
			self.LeakingWeigthVariable=self.PredictedAgentDerivePredicterVariable.PredictedDecoderFloatsArray


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
		'PredictingSensorsInt',
		'PredictingUnitsInt',
		'PredictingDaleBool',
		'PredictingDynamicBool',
		'PredictingDecoderVariable',
		'PredictingTimeVariable',
		'PredictingDynamicStr',
		'PredictedDecoderFloatsArray',
		'PredictedJacobianFloatsArray',
		'PredictedParentSingularStr',
		'PredictedSensorDerivePredicterVariable',
		'PredictedAgentDerivePredicterVariable',
		'PredictedDecoderDerivePredicterVariable',
		'PredictedNetworkDerivePredicterVariable'
	]
)
#<DefinePrint>