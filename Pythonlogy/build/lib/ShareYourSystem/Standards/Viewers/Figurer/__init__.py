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
BaseModuleStr="ShareYourSystem.Standards.Viewers.Viewer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
SYS.addDo("Figurer","Figure","Figuring","Figured")
#</DefineAugmentation>

#<ImportSpecificModules>
#from matplotlib import pyplot
#from Figurers import Paneler,Axer,Ploter
#</ImportSpecificModules>

#<DefineDoStrsList>
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class FigurerClass(BaseClass):
	
	def default_init(self,
						_FiguredPyplotVariable=None,
						
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_figure(self):	

		#import pyplot
		from matplotlib import pyplot

		#subplots
		self.FiguredPyplotVariable = pyplot.figure()

	def mimic_view(self):

		#import mpld3
		import mpld3

		mpld3.fig_to_html(fig, template_type="simple")

#</DefineClass>

#</DefinePrint>
FigurerClass.PrintingClassSkipKeyStrsList.extend(
	[
		'FiguredPyplotVariable',
	]
)
#<DefinePrint>
