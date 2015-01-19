# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Consoler 
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Packager"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from IPython.display import HTML,display
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConsolerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
								'ConsolingWidthInt',
								'ConsolingHeightInt',
								'ConsolingTitleStr',
								'ConsolingIdStr',
								'ConsolingUrlStr',
								'ConsoledHtmlStr',
								'ConsoledHtmlVariable'
							]

	def default_init(self,
						_ConsolingWidthInt=100,
						_ConsolingHeightInt=100,
						_ConsolingTitleStr="Server-side",
						_ConsolingIdStr="Server",
						_ConsolingUrlStr="http://127.0.0.1:4200",
						_ConsoledHtmlStr="",
						_ConsoledHtmlVariable=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_console(self):

		#Check
		self.ConsoledHtmlStr+="<h1>"+self.ConsolingTitleStr+"</h1><iframe id=\""+self.ConsolingIdStr+"\" width=\""+str(
			self.ConsolingWidthInt
			)+"\" height=\""+str(self.ConsolingHeightInt
			)+"\" src=\""+self.ConsolingUrlStr+"\" frameborder=\"1\"></iframe>"

		#Html
		self.ConsoledHtmlVariable=HTML(self.ConsoledHtmlStr)
		
		#display
		display(self.ConsoledHtmlVariable)

#</DefineClass>
