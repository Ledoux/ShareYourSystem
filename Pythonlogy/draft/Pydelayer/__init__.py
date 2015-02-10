# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Pydelayer is a Runner that make run a special instance
of dde23 from the pydelay module and use a global states Moniter
to track the differenciated variables, moreover with a 
bufferring manner to not overload the pythonic memory.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Specials.Simulaters.Runner"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
from pydelay import dde23
import operator
from ShareYourSystem.Specials.Simulaters import Equationer
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PydelayerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'PydelayingKwargVariablesDict',
		'PydelayingHistoryFunctionsDict',
		'PydelayingBufferStepTimeFloat',
		'PydelayedUnitsInt',
		'PydelayedEquationDictsList',
		'PydelayedParamDictsList',
		'PydelayedDde23Variable',
		'PydelayedVariableStrsList',
		'PydelayedBufferFloatsArray',
		'PydelayedBufferStepsInt',
		'PydelayedBufferStopTimeFloat',
		'PydelayedMoniterSampleTimeIndexIntsArray'
	]

	def default_init(self,
						_PydelayingKwargVariablesDict=None,
						_PydelayingStopTimeFloat=20.,
						_PydelayingSampleStepTimeFloat=0.1,
						_PydelayingMoniterVariableIndexIntsArray=None,
						_PydelayingHistoryFunctionsDict=None,
						_PydelayingBufferStepTimeFloat=5.,
						_PydelayedUnitsInt=0,
						_PydelayedEquationDictsList=None,
						_PydelayedParamDictsList=None,
						_PydelayedDde23Variable=None,
						_PydelayedVariableStrsList=None,
						_PydelayedBufferFloatsArray=None,
						_PydelayedBufferStepsInt=0,
						_PydelayedBufferStopTimeFloat=0.,
						_PydelayedMoniterSampleTimeIndexIntsArray=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def mimic_simulate(self):

		#debug
		'''
		self.debug(('self.',self,[
						'PydelayingKwargVariablesDict'
					]))
		'''

		#pydelay first
		self.pydelay(
				_PydelayingStopTimeFloat=self.SimulatingStopTimeFloat
			)

		#reset
		self.PydelayedBufferStopTimeFloat=0

		#while
		while self.PydelayedBufferStopTimeFloat<self.SimulatingStopTimeFloat:

			#increment
			self.RunningStopTimeFloat=self.PydelayedBufferStopTimeFloat+self.PydelayingBufferStepTimeFloat

			#run
			self.run()

			#equal
			self.PydelayedBufferStopTimeFloat=self.RunningStopTimeFloat

	def mimic_run(self):
		
		#debug
		'''
		self.debug(
					[
						'We run the PydelayedDde23Variable',
						('self.',self,['RunningStopTimeFloat'])
					]
				)
		'''

		#set
		self.PydelayedDde23Variable.set_sim_params(
				tfinal=self.RunningStopTimeFloat
			)

		#run
		self.PydelayedDde23Variable.run()

		#debug
		'''
		self.debug(
					[
						'Now we sample',
						('self.',self,[
							'PydelayedBufferStopTimeFloat',
							'RunningStopTimeFloat',
							'PydelayingSampleStepTimeFloat'
							]
						)
					]
				)
		'''

		#sample and update the instance with that
		SampleDict=self.PydelayedDde23Variable.sample(
					self.PydelayedBufferStopTimeFloat,
					self.RunningStopTimeFloat,
					self.PydelayingSampleStepTimeFloat
				)

		#map
		self.PydelayedBufferFloatsArray=np.array(
			map(
				lambda __PydelayedVariableStr:
				SampleDict[__PydelayedVariableStr],
				self.PydelayedVariableStrsList
			)
		)

		#debug
		'''
		self.debug(('self.',self,['PydelayedBufferFloatsArray']))
		'''

		#moniter
		self['<StateMoniters>VariableMoniter'].monit(
			self.PydelayedMoniterSampleTimeIndexIntsArray+(int)(
				self.PydelayedBufferStopTimeFloat/self.PydelayingSampleStepTimeFloat
				)
		)

	def do_pydelay(
				self,
				**_KwargVariablesDict
			):	

		#debug
		'''
		self.debug(('self.',self,[]))
		'''

		#network first
		self.network(
			**{
				'RecruitingConcludeConditionTuplesList':[
					(
						'MroClassesList',
						operator.contains,
						Equationer.EquationerClass
					)
				]
			}
		)

		#link
		self.PydelayedDeriveEquationersList=self.NetworkedDeriveConnectersList

		#map populate and neurongroup
		self.PydelayedEquationDictsList=map(
			lambda __PydelayedDeriveEquationer:
			__PydelayedDeriveEquationer.populate(
				).equation(
				).EquationingDifferentialDict,
			self.PydelayedDeriveEquationersList
		)

		#Check
		if 'eqns' not in self.PydelayingKwargVariablesDict:
			self.PydelayingKwargVariablesDict['eqns']={}

		#update
		map(
				lambda __PydelayedEquationDict:
				self.PydelayingKwargVariablesDict['eqns'].update(__PydelayedEquationDict),
				self.PydelayedEquationDictsList
			)

		#map populate and neurongroup
		self.PydelayedParamDictsList=map(
			lambda __PydelayedDeriveEquationer:
			__PydelayedDeriveEquationer.EquationingParamDict,
			self.PydelayedDeriveEquationersList
		)

		#Check
		if 'params' not in self.PydelayingKwargVariablesDict:
			self.PydelayingKwargVariablesDict['params']={}

		#update
		map(
				lambda __PydelayedParamDict:
				self.PydelayingKwargVariablesDict['params'].update(__PydelayedParamDict),
				self.PydelayedParamDictsList
			)

		#map populate and neurongroup
		self.PydelayedCodeStrsList=map(
			lambda __PydelayedDeriveEquationer:
			__PydelayedDeriveEquationer.EquationingCodeStr,
			self.PydelayedDeriveEquationersList
		)

		#Check
		if 'supportcode' not in self.PydelayingKwargVariablesDict:
			self.PydelayingKwargVariablesDict['supportcode']=""

		#update
		map(
				lambda __PydelayedCodeStr:
				self.PydelayingKwargVariablesDict.__setitem__(
					'supportcode',
					self.PydelayingKwargVariablesDict['supportcode']+'\n'+__PydelayedCodeStr
				),
				self.PydelayedCodeStrsList
			)

		#debug
		'''
		self.debug(('self.',self,['PydelayingKwargVariablesDict']))
		'''

		#bind
		self.PydelayedUnitsInt=len(self.PydelayingKwargVariablesDict['eqns'])

		#set
		self.PydelayedVariableStrsList=self.PydelayingKwargVariablesDict['eqns'].keys()

		#Initialise the solver
		self.PydelayedDde23Variable = dde23(
			**self.PydelayingKwargVariablesDict
		)

		#Set params inside the solver
		self.PydelayedDde23Variable.set_sim_params(
				dtmax=self.PydelayingSampleStepTimeFloat
			)

		#Check if the init conditions was not yet define else give them equal to 0
		if type(self.SimulatingInitFloatsArray)==None.__class__:
			self.SimulatingInitFloatsArray=np.zeros(1,dtype=float)
		if len(self.SimulatingInitFloatsArray)!=self.PydelayedUnitsInt:
			self.SimulatingInitFloatsArray=np.array([0.]*self.PydelayedUnitsInt)
		
		#Check if there is an history setted, else give the history as just the constant value of initial conditions
		if len(self.PydelayingHistoryFunctionsDict)!=self.PydelayedUnitsInt:

			#dict
			self.PydelayingHistoryFunctionsDict=dict(
				map(
					lambda __Int,__KeyStr:
					(__KeyStr,lambda _Time:self.SimulatingInitFloatsArray[__Int]),
					xrange(self.PydelayedUnitsInt),
					self.PydelayingKwargVariablesDict['eqns'].keys()
				)
			)

			#hist_from_funcs
			self.PydelayedDde23Variable.hist_from_funcs(self.PydelayingHistoryFunctionsDict)

		#Set the size of the Buffer
		if self.PydelayingStopTimeFloat<self.PydelayingBufferStepTimeFloat:
			self.PydelayedBufferStepsInt=(int)(
				self.PydelayingStopTimeFloat/self.PydelayingSampleStepTimeFloat
			)
		else:
			self.PydelayedBufferStepsInt=(int)(
				self.PydelayingBufferStepTimeFloat/self.PydelayingSampleStepTimeFloat
			)

		#debug
		'''
		self.debug(('self.',self,[
						'PydelayedBufferStepsInt',
						'SimulatingStopTimeFloat',
						'PydelayingBufferStepTimeFloat'
					]))
		'''
		
		#init the buffer array
		self.PydelayedBufferFloatsArray=np.array(
				(
					self.PydelayedUnitsInt,
					self.PydelayedBufferStepsInt
				),
				dtype=float
			)

		#set
		self.PydelayedMoniterSampleTimeIndexIntsArray=np.array(
			xrange(self.PydelayedBufferStepsInt)
		)

		#Check
		if self.PydelayingMoniterVariableIndexIntsArray==None:
			self.PydelayingMoniterVariableIndexIntsArray=np.array(xrange(self.PydelayedUnitsInt))

		#collect the global monitor
		self.collect(
			"StateMoniters",
			"Variable",
			SYS.MoniterClass().update(
					{
						'MoniteringVariableStr':'PydelayedBufferFloatsArray',
						'MoniteringSampleTimeIndexIntsArray':self.PydelayedMoniterSampleTimeIndexIntsArray,
						'MoniteringVariableIndexIntsArray':self.PydelayingMoniterVariableIndexIntsArray,
						'MoniteredTotalVariablesArray':np.zeros(
									(
										self.PydelayedUnitsInt,
										(int)(
											self.PydelayingStopTimeFloat-self.SimulatingStartTimeFloat
										)/self.PydelayingSampleStepTimeFloat
									)
								,dtype=float
							)	
					}
				)
		)

		#Debug
		'''
		self.debug('self["<StateMoniters>VariableMoniter"].MoniteredTotalVariablesArray is '+str(
			self["<StateMoniters>VariableMoniter"].MoniteredTotalVariablesArray))
		'''
		
#</DefineClass>
