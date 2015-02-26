# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Simulater

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Controllers.Controller"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class SimulaterClass(BaseClass):
	
	def default_init(self,
						_SimulatingStopTimeFloat=100.,
						_SimulatingInitFloatsArray=None,
						_SimulatingStepTimeFloat=0.1,
						_SimulatingStartTimeFloat=0.,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)



	def simulate_integrate(self):
		self.integrate()

	def simulate_pydelay(self):
		self.pydelay()

	def do_simulate(
				self,
				**_KwargVariablesDict
			):	

		#debug
		'''
		self.debug(('self.',self,[

					]))
		'''
		pass

#</DefineClass>

#</DefinePrint>
ParenterClass.PrintingClassSkipKeyStrsList.extend(
	[
		'SimulatingStopTimeFloat',
		'SimulatingInitFloatsArray',
		'SimulatingStepTimeFloat',
		'SimulatingStartTimeFloat'
	]
)
#<DefinePrint>
