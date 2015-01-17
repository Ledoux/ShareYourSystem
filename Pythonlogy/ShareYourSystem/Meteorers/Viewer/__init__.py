# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Viewer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Meteorers.Meteorer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from IPython.display import HTML,display
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ViewerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
								'ViewingWidthInt',
								'ViewingHeigthInt',
								'ViewedHTMLVariable'
							]

	def default_init(self, 
						_ViewingWidthInt=1000,
						_ViewingHeigthInt=400,
						_ViewedHTMLVariable=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_view(self):
		
		#meteor first
		self.meteor()

		#display
		self.ViewedHTMLVariable=HTML(
			"<iframe width=\""+str(self.ViewingWidthInt
				)+"\" height=\""+str(self.ViewingHeigthInt
				)+"\" src=\""+self.MeteoredUrlStr+"\" frameborder=\"0\" allowfullscreen></iframe>"
			)

		#display
		display(self.ViewedHTMLVariable)

#</DefineClass>

#<DefineFunctions>
def GUI(*_LiargVariablesList,**_KwargVariablesDict):

	if len(_LiargVariablesList)==0:

		#view
		SYS.GUIViewer=ViewerClass(**_KwargVariablesDict).view()

	else:

		#call
		SYS.GUIViewer.MeteoredConcurrentDDPClientVariable.call(*_LiargVariablesList)
SYS.GUI=GUI
#</DefineFunctions>