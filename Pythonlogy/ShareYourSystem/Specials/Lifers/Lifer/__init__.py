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
SYS.addDo('Lifer','Lif','Lifing','Lifed')
#</DefineAugmentation>

#<DefineLocals>
def getFilterDictByType(**_Dict):

	#init
	FilteredDict={'ComplexDict':{},'DoubleDict':{},'IntDict':{},'StringDict':{}};

	#map
	map(
		lambda __ItemTuple:
		FilteredDict[
			getCTypeNameFromPythonType(
				type(
					__ItemTuple[1]
					)
			)+'Dict'
		].__setitem__(*__ItemTuple),
		_Dict.items()
	)	

	#return
	return FilteredDict;
SYS.getFilterDictByType=getFilterDictByType
def getCTypeNameFromPythonType(_PythonType):

	#import
	import numpy as np

	#check
	if _PythonType in [float,np.float64]:
		return 'Double'
	elif _PythonType in [int]:
		return 'Int'
	elif _PythonType in [str]:
		return 'String'; 
SYS.getCTypeNameFromPythonType=getCTypeNameFromPythonType
def getCArgsFromDict(Dict):
    CArgs=[]
    DictOrderedKeys=Dict.keys()
    for Key in sorted(Dict):
        CArgs.append(Dict[Key]);
    return CArgs;
SYS.getCArgsFromDict=getCArgsFromDict
#</DefineLocals>

#</DefineLocals>

#<DefineClass>
@DecorationClass()
class LiferClass(BaseClass):
	
	def default_init(self, 
			_LifingConstantTimeFloat=0.02, 
			_LifingRefractoryPeriodFloat=0.,
			_LifingStationaryCurrentFloat=None, 
			_LifingStationaryRateFloat=None, 
			_LifingCurrentToFloatBool=True,
			_LifingNoiseFloat=5., 
			_LifingResetFloat=-60., 
			_LifingThresholdFloat=-50.,
			_LifingComputeStationaryBool=True,
			_LifingPerturbationLambdaVariable=None,
			_LifingPerturbationFrequencyFloat=None,
			_LifingPerturbationMethodStr='Brunel',
			_LifedSwigVariable=None,
			_LifedStationaryCurrentFloat=None,
			_LifedStationaryRateFloat=None,
			_LifedPerturbationNullFloat=0.,
			_LifedPerturbationMethodVariable=None,
			_LifedPerturbationMeanComplexVariable=None,
			_LifedPerturbationNoiseComplexVariable=None,
			_LifedInverseStationaryFunctionVariable=None,
			**_KwargVariablesDict
		):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_lif(self):
		
		#/##################/#
		# Get the swig function
		#

		#Check
		if self.LifedSwigVariable==None:

			#import
			import sys
			from os.path import dirname
			sys.path.append(dirname(__file__))
			import CIntegrateAndFireTransferFunction

			#get
			self.LifedSwigVariable=CIntegrateAndFireTransferFunction.CIntegrateAndFireTransferFunctionClass()

		#debug
		'''
		self.debug(
			[
				'We have getted dthe Lif swig variable',
				('self.',self,[
						'LifedSwigVariable'
					])
			]
		)
		'''

		#/##################/#
		# Look if the stationary point was already computed
		#

		#set
		self.LifedSwigVariable.IntDict['ComputeStationary']=int(
			self.LifingComputeStationaryBool
		)

		#Check
		if self.LifingComputeStationaryBool:

			#debug
			'''
			self.debug(
				[
					'We lif compute stationary here',
					('self.',self,[
							'LifingConstantTimeFloat',
							'LifingRefractoryPeriodFloat',
							'LifingStationaryRateFloat',
							'LifingStationaryCurrentFloat',
							'LifingNoiseFloat',
							'LifingResetFloat',
							'LifingThresholdFloat'
						])
				]
			)
			'''

			#Check
			if self.LifingCurrentToFloatBool:

				#debug
				"""
				self.debug(
					[
						"This is rate from current",
						('self.',self,[
								'LifingConstantTimeFloat',
								'LifingRefractoryPeriodFloat',
								'LifingStationaryCurrentFloat',
								'LifingNoiseFloat',
								'LifingResetFloat',
								'LifingThresholdFloat'	
							])
					]
				)
				"""
				
				#Set inside the Swig
				self.LifedSwigVariable.setDicts(
					*getCArgsFromDict(
						getFilterDictByType(**{
								'ConstantTime':self.LifingConstantTimeFloat,
								'RefractoryPeriod':self.LifingRefractoryPeriodFloat,
								'StationaryCurrent':self.LifingStationaryCurrentFloat, 
								'VoltageNoise':self.LifingNoiseFloat, 
								'VoltageReset':self.LifingResetFloat, 
								'VoltageThreshold':self.LifingThresholdFloat
							}
						)
					)
				)

				#Compute the IntegralLowerBound and the IntegralUpperBound
				self.LifedSwigVariable.computeIntegralLowerBound();
				self.LifedSwigVariable.computeIntegralUpperBound();
		    	
				#set
				self.LifedStationaryRateFloat=self.LifedSwigVariable.getLifStationaryRate();

			#Check
			else:

				#debug
				"""
				self.debug(
					[
						"This is current from rate",
						('self',self,[
								'LifingStationaryRateFloat'
							])
					]
				)
				"""

				#temp
				LifedTempRateFloat=self.LifingStationaryRateFloat

				#set
				if self.LifedInverseStationaryFunctionVariable == None:

					#get
					#self.LifedInverseStationaryFunctionVariable=SYS.getInverseFunction(
					#	lambda __StationaryCurrentFloat:
					#	__StationaryCurrentFloat
					#)

					self.LifedInverseStationaryFunctionVariable=SYS.getInverseFunction(
						lambda __StationaryCurrentFloat:
						self.mapSetAttr(
								{
									'LifingStationaryCurrentFloat':__StationaryCurrentFloat,
									'LifingStationaryRateFloat':None,
									'LifingCurrentToFloatBool':True
								}
							).lif(
							).LifedStationaryRateFloat
						)
				
				#set
				self.LifedStationaryCurrentFloat = self.LifedInverseStationaryFunctionVariable(
					LifedTempRateFloat
				)

				#set
				self.LifingStationaryRateFloat = LifedTempRateFloat

				#set
				self.LifingCurrentToFloatBool=False
				
				#set
				self.LifedStationaryRateFloat = None

		#/##################/#
		# Compute a perturbaton
		#

		#Check
		if self.LifingPerturbationFrequencyFloat!=0. or self.LifingPerturbationLambdaVariable!=None:

			#/##################/#
			# Get the method
			#

			#get
			self.LifedPerturbationMethodVariable=getattr(
				self.LifedSwigVariable,
				'set'+self.LifingPerturbationMethodStr+'LifPerturbationRate'
			)

			#get
			self.LifedPerturbationNullFloat=self.LifedSwigVariable.getLifPerturbationNullRate(
					'StationaryCurrent'
				)

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'LifedPerturbationNullFloat'
						])
				]
			)
			'''
			
			#Choose
			if self.LifingPerturbationFrequencyFloat!=0.:

				#import
				import numpy as np

				#set
				LifedPerturbationPreVariable=2.*np.pi*self.LifingPerturbationFrequencyFloat*1j

			else:

				#set
				LifedPerturbationPreVariable=self.LifingPerturbationLambdaVariable

			#call
			self.LifedPerturbationMethodVariable(
				LifedPerturbationPreVariable
			)

			#unpack
			if LifedPerturbationPreVariable==0.:

				self.LifedPerturbationMeanComplexVariable=self.LifedSwigVariable.DoubleDict["PerturbationMean"]
				self.LifedPerturbationNoiseComplexVariable=self.LifedSwigVariable.DoubleDict["PerturbationNoise"]

			else:

				self.LifedPerturbationMeanComplexVariable=self.LifedSwigVariable.ComplexDict["PerturbationMean"]
				self.LifedPerturbationNoiseComplexVariable=self.LifedSwigVariable.ComplexDict["PerturbationNoise"]

			#debug
			'''
			self.debug(
				[
					('self.',self,[
							'LifedPerturbationMeanComplexVariable'
						]),
					'LifedPerturbationPreVariable is '+str(LifedPerturbationPreVariable)
				]
			)
			'''

	def mimic__print(self,**_KwargVariablesDict):

		#/##################/#
		# Modify the printing Variable
		#

		#Check
		if self.PrintingSelfBool:

			#/##################/#
			# Print things if they are computed
			#

			#map
			map(
					lambda __KeyStr:
					self.forcePrint(
						[__KeyStr],
						'LiferClass'
					)
					if getattr(self.PrintingCopyVariable,__KeyStr) not in [None,0.]
					else None,
					[
						'LifingConstantTimeFloat', 
						'LifingRefractoryPeriodFloat',
						'LifingNoiseFloat', 
						'LifingResetFloat', 
						'LifingThresholdFloat',
						'LifingPerturbationLambdaVariable',
						'LifingPerturbationFrequencyFloat',
						'LifingPerturbationMethodStr',
						'LifedPerturbationNullFloat',
						'LifedPerturbationMeanComplexVariable',
						'LifedPerturbationNoiseComplexVariable'
					]+(['LifingStationaryCurrentFloat'] if self.LifingCurrentToFloatBool else [])
					+(['LifingStationaryRateFloat'] if self.LifingCurrentToFloatBool==False else [])
					+(['LifedStationaryCurrentFloat'] if self.LifingCurrentToFloatBool==False else [])
					+(['LifedStationaryRateFloat'] if self.LifingCurrentToFloatBool else [])
				)

		#/##################/#
		# Call the base method
		#

		#call
		BaseClass._print(self,**_KwargVariablesDict)

#</DefineClass>

#</DefinePrint>
LiferClass.PrintingClassSkipKeyStrsList.extend(
	[
		'LifingConstantTimeFloat', 
		'LifingRefractoryPeriodFloat',
		'LifingStationaryCurrentFloat', 
		'LifingStationaryRateFloat',
		'LifingCurrentToFloatBool',
		'LifingNoiseFloat', 
		'LifingResetFloat', 
		'LifingThresholdFloat',
		'LifingComputeStationaryBool',
		'LifingPerturbationLambdaVariable',
		'LifingPerturbationFrequencyFloat',
		'LifingPerturbationMethodStr',
		'LifedSwigVariable',
		'LifedStationaryCurrentFloat',
		'LifedStationaryRateFloat',
		'LifedPerturbationNullFloat',
		'LifedPerturbationMethodVariable',
		'LifedPerturbationNullFloat=0.,',
		'LifedPerturbationMeanComplexVariable',
		'LifedPerturbationNoiseComplexVariable',
		'LifedInverseStationaryFunctionVariable'
	]
)
#<DefinePrint>