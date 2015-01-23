# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Figurer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Analyzers.Controller"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from matplotlib import pyplot
from Figurers import Paneler,Axer,Ploter
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Figurer","Figure","Figuring","Figured"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class FigurerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'FiguredDerivePanelersList',
									'FiguredDeriveAxersList',
									'FiguredDerivePlotersList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_FiguredDerivePanelersList=None,
						_FiguredDeriveAxersList=None,
						_FiguredDerivePlotersList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	#@Argumenter.ArgumenterClass()
	def do_figure(
				self
			):	

		#first mobilize
		self.mobilize(
			[
				'Paneler','Axer','Ploter'
			]
		)

		#Return self
		#return self

#</DefineClass>
