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
BaseModuleStr="ShareYourSystem.Standards.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ViewerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
			'ViewingKeyStr',
			'ViewedCollectionStr',
			'ViewedPointDeriveControllerVariable',
		]

	def default_init(self, 
						_ViewingKeyStr="",
						_ViewedCollectionStr="",
						_ViewedPointDeriveControllerVariable=None,
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_view(self):

		#set
		if hasattr(self,'NodeKeyStr'):
			self.ViewingKeyStr=self.NodeKeyStr
			self.ViewedCollectionStr=self.NodeCollectionStr

		#Check
		if hasattr(self,'NodePointDeriveNoder'):

			#debug
			self.debug(
				[
					#('self.',self,['NodePointDeriveNoder']),
					str(self.point)
				]
			)

			#point
			self.point(
				self.NodePointDeriveNoder,
				'ViewedPointDeriveControllerVariable'
			)

#</DefineClass>
