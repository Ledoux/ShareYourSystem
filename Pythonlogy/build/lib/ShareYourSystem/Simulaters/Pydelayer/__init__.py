# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Pydelayer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Simulaters.Populater"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import numpy as np
from pydelay import dde23
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PydelayerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'PydelayingKwargVariablesDict',
		'PydelayingHistoryFunctionsDict',
		'PydelayingBufferStepTimeFloat',
		'PydelayedDde23Variable',
		'PydelayedVariableStrsList',
		'PydelayedBufferFloatsArray',
		'PydelayedBufferStepsInt',
		'PydelayedBufferStopTimeFloat',
		'PydelayedMoniterSampleTimeIndexIntsArray'
	]

	def default_init(self,
						_PydelayingKwargVariablesDict=None,
						_PydelayingMoniterVariableIndexIntsArray=None,
						_PydelayingHistoryFunctionsDict=None,
						_PydelayingBufferStepTimeFloat=5.,
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
		self.debug(
					[
						'We run the PydelayedDde23Variable',
						('self.',self,['RunningStopTimeFloat'])
					]
				)

		#set
		self.PydelayedDde23Variable.set_sim_params(
				tfinal=self.RunningStopTimeFloat
			)

		#run
		self.PydelayedDde23Variable.run()

		#debug
		self.debug(
					[
						'Now we sample',
						('self.',self,[
							'PydelayedBufferStopTimeFloat',
							'RunningStopTimeFloat',
							'EuleringStepTimeFloat'
							]
						)
					]
				)

		#sample and update the instance with that
		SampleDict=self.PydelayedDde23Variable.sample(
					self.PydelayedBufferStopTimeFloat,
					self.RunningStopTimeFloat,
					self.EuleringStepTimeFloat
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
		self.debug(('self.',self,['PydelayedBufferFloatsArray']))

		#moniter
		self['<StateMoniters>VariableMoniter'].monit(
			self.PydelayedMoniterSampleTimeIndexIntsArray+(int)(
				self.PydelayedBufferStopTimeFloat/self.EuleringStepTimeFloat
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

		#bind
		self.PopulatingUnitsInt=len(self.PydelayingKwargVariablesDict['eqns'])

		#set
		self.PydelayedVariableStrsList=self.PydelayingKwargVariablesDict['eqns'].keys()

		# Initialise the solver
		self.PydelayedDde23Variable = dde23(
			**self.PydelayingKwargVariablesDict
		)

		# Set params inside the solver
		self.PydelayedDde23Variable.set_sim_params(
				dtmax=self.EuleringStepTimeFloat
			)

		#Check if the init conditions was not yet define else give them equal to 0
		if len(self.SimulatingInitFloatsArray)!=self.PopulatingUnitsInt:
			self.SimulatingInitFloatsArray=[0.]*self.PopulatingUnitsInt
		
		#Check if there is an history setted, else give the history as just the constant value of initial conditions
		if len(self.PydelayingHistoryFunctionsDict)!=self.PopulatingUnitsInt:

			#dict
			self.PydelayingHistoryFunctionsDict=dict(
				map(
					lambda __Int,__KeyStr:
					(__KeyStr,lambda _Time:self.SimulatingInitFloatsArray[__Int]),
					xrange(self.PopulatingUnitsInt),
					self.PydelayingKwargVariablesDict['eqns'].keys()
				)
			)

			#hist_from_funcs
			self.PydelayedDde23Variable.hist_from_funcs(self.PydelayingHistoryFunctionsDict)

		#Set the size of the Buffer
		if self.SimulatingStopTimeFloat<self.PydelayingBufferStepTimeFloat:
			self.PydelayedBufferStepsInt=(int)(self.SimulatingStopTimeFloat/self.EuleringStepTimeFloat)
		else:
			self.PydelayedBufferStepsInt=(int)(
				self.PydelayingBufferStepTimeFloat/self.EuleringStepTimeFloat)

		#debug
		self.debug(('self.',self,[
						'PydelayedBufferStepsInt',
						'SimulatingStopTimeFloat',
						'PydelayingBufferStepTimeFloat'
					]))

		#init the buffer array
		self.PydelayedBufferFloatsArray=np.array(
				(
					self.PopulatingUnitsInt,
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
			self.PydelayingMoniterVariableIndexIntsArray=np.array(xrange(self.PopulatingUnitsInt))

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
										self.PopulatingUnitsInt,
										(int)(
											self.SimulatingStopTimeFloat-self.SimulatingStartTimeFloat
										)/self.EuleringStepTimeFloat
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
