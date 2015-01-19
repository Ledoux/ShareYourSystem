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
BaseModuleStr="ShareYourSystem.Meteorers.Boxer"
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
								'ViewingHeightInt',
								'ViewedHTMLVariable'
							]

	def default_init(self, 
						_ViewingWidthInt=800,
						_ViewingHeightInt=400,
						_ViewingUrlStr="",
						_ViewedHtmlStr="",
						_ViewedHTMLVariable=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_view(self):
		
		#Check
		if self.ViewingUrlStr=="":
			self.ViewingUrlStr=self.MeteoredUrlStr

		#Init
		self.ViewedHtmlStr=""

		#display
		self.ViewedHtmlStr+="<h1>Client-side</h1><iframe id=\"Client\" width=\""+str(self.ViewingWidthInt
				)+"\" height=\""+str(self.ViewingHeightInt
				)+"\" src=\""+self.ViewingUrlStr+"\" frameborder=\"1\"></iframe>"

		#debug
		'''
		self.debug(('self.',self,[
									'ViewingUrlStr',
									'ViewingHeightInt',
									'ViewingWidthInt',
									'ViewedHtmlStr'
								]))
		'''

		#Html
		self.ViewedHTMLVariable=HTML(self.ViewedHtmlStr)
		
		#display
		display(self.ViewedHTMLVariable)

#</DefineClass>

#<DefineFunctions>
def setGUI(
			_ViewWidthInt=None,
			_ViewHeigthInt=None,
			*_LiargVariablesList,
			**_KwargVariablesDict
		):

	#Set inputs
	if _ViewWidthInt!=None:
		_KwargVariablesDict.update({'ViewingWidthInt':_ViewWidthInt})
	if _ViewHeigthInt!=None:
		_KwargVariablesDict.update({'ViewingHeigthInt':_ViewHeigthInt})

	#Check
	if len(_LiargVariablesList)==0:

		#view
		SYS.GUIViewer=ViewerClass(**_KwargVariablesDict).meteor().view()

	else:

		#call
		SYS.GUIViewer.MeteoredConcurrentDDPClientVariable.call(*_LiargVariablesList)
SYS.setGUI=setGUI
#</DefineFunctions>