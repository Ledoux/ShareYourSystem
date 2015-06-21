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
#BaseModuleStr="ShareYourSystem.Standards.Recorders.Leaker"
BaseModuleStr="ShareYourSystem.Specials.Lifers.Lifer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo('Stationarizer','Stationarize','Stationarizing','Stationarized')
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Recorders import Leaker
import scipy.stats
import numpy as np
#</ImportSpecificModules>

#<DefineLocals>
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class StationarizerClass(BaseClass):
	
	def default_init(self,
			_StationarizingUnitsInt = 1,
			_StationarizingLateralWeightVariable = None,
			_StationarizingConstantTimeVariable = None, 
			_StationarizingThresholdVariable = None, 
			_StationarizingResetVariable = None, 
			_StationarizingRateVariable = None, 
			_StationarizingPopulationTagVariable = None, 
			_StationarizingInteractionStr="Rate",
			_StationarizedConstantTimeFloatsList = None,
			_StationarizedThresholdFloatsList = None, 
			_StationarizedResetFloatsList = None, 
			_StationarizedRateFloatsList = None, 
			_StationarizedPopulationTagStrsList = None,
			_StationarizedParentSingularStr = "",
			_StationarizedNetworkDeriveStationarizerVariable = None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	
	def do_stationarize(self):

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
			self.StationarizedParentSingularStr=self.ParentedTotalSingularListDict.keys()[0]

		#debug
		'''
		self.debug(
			[
				'Ok',
				('self.',self,['StationarizedParentSingularStr'])
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
		]) and self.StationarizedParentSingularStr!='Population':

			#/########################/#
			# Network level
			# 

			#debug
			'''
			self.debug(
				[
					'It is a Network level for the stationarize',
				]
			)
			'''

			#/########################/#
			# Determine parent level
			# 

			#alias
			self.StationarizedNetworkDeriveStationarizerVariable=self

			#/########################/#
			# stationarizeNetwork
			# 

			#stationarize
			self.stationarizeNetwork()

			#/########################/#
			# structure stationarize 
			# 

			#debug
			'''
			self.debug(
				[
					'We structure all the stationarizeing children...'
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
						'stationarize'
					]
			)
			
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
						'StationarizedParentSingularStr'
					])
				]
			)
			'''

			#set
			StationarizedMethodKeyStr='stationarize'+self.StationarizedParentSingularStr

			#Check
			if hasattr(self,StationarizedMethodKeyStr):

				#/########################/#
				# call the special stationarize<StationarizedParentSingularStr> method
				#

				#debug
				'''
				self.debug(
					[
						'It is a '+self.StationarizedParentSingularStr+' level',
						'We stationarize<StationarizedParentSingularStr>'
					]
				)
				'''

				#call
				getattr(
					self,
					StationarizedMethodKeyStr
				)()

				#debug
				'''
				self.debug(
					[
						'Ok we have setted stationarize'+self.StationarizedParentSingularStr
					]
				)
				'''	
	
	def stationarizeNetwork(self):

		#/###################/#
		# Determine the weights
		# 

		#debug
		'''
		self.debug(
			[
				'We stationarize network here',
			]
		)
		'''

		#import
		import numpy as np

		#Check
		if type(self.StationarizingLateralWeightVariable) != None.__class__:

			#alias
			self.StationarizedLateralWeightFloatsArray=np.array(
				self.StationarizingLateralWeightVariable
			)

			#set
			self.StationarizingUnitsInt=len(self.StationarizedLateralWeightFloatsArray)

		#/###################/#
		# Determine the time constant structure
		# 

		#map
		map(
			lambda __TagStr:
			SYS.setInitList(
				self,'Stationarize',__TagStr
			),
			[
				'ConstantTime',
				'Threshold',
				'Reset',
				'Rate'
			]
		)

		#debug
		'''
		self.debug(
			[
				"Now ",
				('self.',self,[
						"DoUnitsInt",
						"StationarizedThresholdFloatsList",
						"StationarizedResetFloatsList"
					])
			]
		)
		'''

		#Check
		self.StationarizingUnitsInt=max(self.StationarizingUnitsInt,self.DoUnitsInt)

		#/###################/#
		# Determine the name
		# 

		#Check
		if self.StationarizingPopulationTagVariable == None:

			#set
			self.StationarizedPopulationTagStrsList=map(
				str,range(self.StationarizingUnitsInt)
			)
		
		else:

			#set
			self.StationarizedPopulationTagStrsList=self.StationarizingPopulationTagVariable

		#/###################/#
		# Check for Populations
		# 

		#get
		StationarizedPopulationsDeriveTeamer=self.getTeamer(
			"Populations"
		)

		#map
		map(
			lambda __StationarizedPopulationTagStr:
			StationarizedPopulationsDeriveTeamer.getManager(
				str(__StationarizedPopulationTagStr)
			),
			self.StationarizedPopulationTagStrsList,
		)


	def stationarizePopulation(self):

		#debug
		'''
		self.debug(
			[
				'We stationarize population here'
			]
		)
		'''

		#Determine parent
		self.StationarizedNetworkDeriveStationarizerVariable = self.ParentDeriveTeamerVariable.ParentDeriveTeamerVariable

		#map
		map(
			lambda __TagStr,__NetworkVariable:
			setattr(
				self,
				"Lifing"+__TagStr+"Float",
				__NetworkVariable[self.ManagementIndexInt]
			)
			if len(__NetworkVariable)>self.ManagementIndexInt and __NetworkVariable[self.ManagementIndexInt]!=None
			else None,
			*zip(
				*(map(
					lambda __TagStr:
					(
						__TagStr,
						getattr(
							self.StationarizedNetworkDeriveStationarizerVariable,
							"Stationarized"+__TagStr+"FloatsList"
						)
					),
					[
						"ConstantTime",
						"Threshold",
						"Reset"
					]
				)+[
						(
							"StationaryRate",
							getattr(
									self.StationarizedNetworkDeriveStationarizerVariable,
									"StationarizedRateFloatsList"
								)
						)
					]
				)
			)
		)

		#debug
		'''
		self.debug(
			[
				('self.',self,[
						'LifingConstantTimeFloat',
						'LifingStationaryCurrentFloat',
						'LifingStationaryRateFloat',
					]
				)
			]
		)
		'''

		#Check
		if self.StationarizedNetworkDeriveStationarizerVariable.StationarizingInteractionStr=="Spike":

			#set
			self.LifingCurrentToFloatBool=self.LifingStationaryCurrentFloat!=None

			#lif
			self.lif()

		#debug
		'''
		self.debug(
			[
				"After lif",
				('self.',self,[
						'LifedStationaryCurrentFloat',
						'LifedStationaryRateFloat'
					]
				)
			]
		)
		'''

	def getStationaryRateRootFloat(self,_StationaryStationaryRateFloat):
			
		#return
		return 0.

	def getStationarySpikeRootFloat(self,_StationaryStationaryRateFloat):
			
		#center
		self.LifingStationaryCurrentFloat = 0.

		#noise
		self.LifingVoltageNoiseFloat = self.StationarizingStdWeightFloat *  self.StationarizingConstantTimeVariable * _StationaryStationaryRateFloat

		#lif
		self.lif()

		#return
		return self.LifedStationaryStationaryRateFloat

	"""
	def getStationarySpikeRootFloatsTuple(self,_StationaryStationaryRateFloatsTuple):
			
		#center
		LifingStationaryCurrentFloatsArray = np.dot(self.StationarizedLateralWeightFloatsArray,_StationaryStationaryRateFloatsTuple)

		#noise
		LifingVoltageNoiseFloatsArray = self.StationarizingStdWeightFloat *  self.StationarizingConstantTimeVariable * _StationaryStationaryRateFloat

		#lif
		self.lif()

		#return
		return self.LifedStationaryStationaryRateFloat
	"""

	#/######################/#
	# Augment view
	#
	
	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Print things if they are computed
			#

			#Check
			if self.StationarizedNetworkDeriveStationarizerVariable==self:

				#map
				map(
						lambda __KeyStr:
						self.forcePrint(
							[__KeyStr],
							'StationarizerClass'
						)
						if getattr(
							self.PrintingCopyVariable,
							__KeyStr
						) not in [None,0.,""]
						else None,
						[
							'StationarizingConstantTimeVariable'
						]
					)

			else:

				#/##################/#
				# Call the base method
				#


				#call
				BaseClass._print(self,**_KwargVariablesDict)

				#return
				return 


		#/##################/#
		# Call the base method
		#

		#call
		Leaker.LeakerClass._print(self,**_KwargVariablesDict)


#</DefineClass>

#</DefineLocals>
Leaker.LeakersStructurerClass.ManagingValueClass=StationarizerClass
#<DefineLocals>

#</DefinePrint>
StationarizerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'StationarizingUnitsInt',
		'StationarizingLateralWeightVariable',
		'StationarizingConstantTimeVariable',
		'StationarizingThresholdVariable',
		'StationarizingResetVariable',
		'StationarizingRateVariable',
		'StationarizingPopulationTagVariable',
		'StationarizingInteractionStr',
		'StationarizingLateralWeightFloatsArray',
		'StationarizedConstantTimeFloatsList',
		'StationarizedThresholdFloatsList',
		'StationarizedResetFloatsList',
		'StationarizedRateFloatsList',
		'StationarizedPopulationTagStrsList',
		'StationarizedParentSingularStr',
		'StationarizedNetworkDeriveStationarizerVariable'
	]
)
#<DefinePrint>