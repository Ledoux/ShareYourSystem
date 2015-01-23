# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Ploter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Storers.Controller"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

import os
from matplotlib import pyplot
from ShareYourSystem.Standards.Interfacers import Killer
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PloterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'PlotingXVariable',
								'PlotingYVariable',
								'PlotingShowBool',
								'PlotingFigureVariable',
								'PlotedDisplayFunction',
								'PlotedPythonKiller'
							]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_PlotingXVariable=None,
						_PlotingYVariable=None,
						_PlotingShowBool=False,
						_PlotingFigureVariable=None,
						_PlotedDisplayFunction=None,
						_PlotedPythonKiller=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	#@Argumenter.ArgumenterClass()
	def do_plot(
				self
			):	

		#Kill other python processes
		self.PlotedPythonKiller.kill(**{'StatusingProcessStr':"Python"})

		#Check
		if self.PlotingFigureVariable==None:

			#Call the pyplot
			self.PlotedDisplayFunction=pyplot.plot

			#set
			self.PlotingShowBool=True

		#display
		self.PlotedDisplayFunction(
							self.PlotingXVariable,
							self.PlotingYVariable
						)

		#Check
		if self.PlotingShowBool:
			pyplot.show()

		#Return self
		#return self

#</DefineClass>
