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
from scipy import integrate
import numpy
import collections
from pydelay import dde23
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PydelayerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'PydelayingKwargVariablesDict',
		'PydelayingHistoryFunctionsDict',
		'PydelayedDde23Variable'
	]

	def default_init(self,
						_PydelayingKwargVariablesDict=None,
						_PydelayingHistoryFunctionsDict=None,
						_PydelayedDde23Variable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)



	def mimic_run(self):
		
		#run
		self.PydelayedDde23Variable.run()

		#debug
		self.debug(('self.',self,['SimulatingStartTimeFloat','SimulatingStopTimeFloat']))

		#sample and update the instance with that
		self.update(
			self.PydelayedDde23Variable.sample(
				self.SimulatingStartTimeFloat,
				self.SimulatingStopTimeFloat,
				self.EuleringStepTimeFloat
			)
		)

		
		#moniter
		map(
				lambda __PopulatedStateDeriveMoniter:
				__PopulatedStateDeriveMoniter.monit(
					__IntegratingStepInt
				),
				self.PopulatedStateDeriveMonitersList
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

		# Initialise the solver
		self.PydelayedDde23Variable = dde23(
			**self.PydelayingKwargVariablesDict
		)

		# Set params inside the solver
		self.PydelayedDde23Variable.set_sim_params(
				tfinal=self.SimulatingStopTimeFloat, 
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

		#debug
		'''
		self.debug(('self.',self,[

					]))
		'''

#</DefineClass>
