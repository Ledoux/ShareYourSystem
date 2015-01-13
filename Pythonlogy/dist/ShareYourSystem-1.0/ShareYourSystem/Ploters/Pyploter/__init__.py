# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Pyploter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Ploters.Ploter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from matplotlib import pyplot
from ShareYourSystem.Functers import Imitater
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Pyploter","Pyplot","Pyploting","Pyploted"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class PyploterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'PyplotedFigureVariable'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_PyplotedFigureVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	@Imitater.ImitaterClass()
	def figure(self):

		#pyplot first
		self.pyplot()

		#parent method
		BaseClass.figure(self)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	#@Argumenter.ArgumenterClass()
	def do_pyplot(
				self
			):	

		#init
		self.PyplotedFigureVariable=pyplot.figure()

		#Return self
		#return self

#</DefineClass>
