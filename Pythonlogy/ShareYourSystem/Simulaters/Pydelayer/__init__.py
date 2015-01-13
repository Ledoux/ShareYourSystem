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
BaseModuleStr="ShareYourSystem.Simulaters.Rater"
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
class SimulaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
		'PydelayingEquationsDict',
		'PydelayingHistoryFunctionsDict',
		'PydelayedDde23Variable'
	]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_PydelayingEquationsDict=None,
						_PydelayingParametersDict=None,
						_PydelayingHistoryFunctionsDict=None,
						_PydelayedDde23Variable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	#@Argumenter.ArgumenterClass()
	def do_simulate(
				self,
				**_KwargVariablesDict
			):	

		#debug
		'''
		self.debug(('self.',self,[]))
		'''

		#Check
		if len(self.PydelayingEquationsDict)>0:

			# Initialise the solver
			self.PydelayedDde23Variable = dde23(
				eqns=collections.OrderedDict(self.PydelayingEquationsDict.items()), 
				params=self.PydelayingParametersDict
			)

			self.PydelayedDde23Variable.set_sim_params(
					tfinal=self.SimulatingStopTimeFloat, 
					dtmax=self.SimulatingStepTimeFloat
				)

			#Check
			if len(self.SimulatingInitFloatsList)!=len(self.PydelayingEquationsDict):
				self.SimulatingInitFloatsList=[0.]*len(self.PydelayingEquationsDict)
			
			#Check
			if len(self.PydelayingHistoryFunctionsDict)!=len(self.PydelayingEquationsDict):
				self.PydelayingHistoryFunctionsDict=dict(
					map(
						lambda __Int,__KeyStr:
						(__KeyStr,lambda _Time:self.SimulatingInitFloatsList[__Int]),
						xrange(len(self.PydelayingEquationsDict)),
						self.PydelayingEquationsDict.keys()
					)
				)
				self.PydelayedDde23Variable.hist_from_funcs(self.PydelayingHistoryFunctionsDict)

		#debug
		'''
		self.debug(('self.',self,[

					]))
		'''

		#Return self
		#return self

#</DefineClass>
