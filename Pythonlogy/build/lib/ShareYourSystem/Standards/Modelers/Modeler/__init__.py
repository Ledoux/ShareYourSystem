# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Modeler rises to the ModelerClass. This latter is the deepest class for instancing
Variables able to store values in hierarchic tables. Here, as a first step,
the database method helps to set the <ModelingKeyStr> in the __dict__

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
@DecorationClass(**{'ClassingSwitchMethodStrsList':['model']})
class ModelerClass(
						BaseClass
				):

	#Definition
	RepresentingKeyStrsList=[
								'ModeledSuffixStr',
								'ModeledCollectionStr',
								'ModeledSuffixStr',
								'ModeledPointDeriveControllerVariable'
							]

	def default_init(self,
					_ModelingKeyStr="",
					_ModeledCollectionStr="",
					_ModeledSuffixStr="",
					_ModeledPointDeriveControllerVariable=None,
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_model(self):

		#set
		if hasattr(self,'NodeKeyStr'):
			self.ModelingKeyStr=self.NodeKeyStr
			self.ModeledCollectionStr=self.NodeCollectionStr

		#set
		self.ModeledSuffixStr=self.ModelingKeyStr+'Model'

		#Check
		if hasattr(self,'NodePointDeriveNoder'):

			#debug
			'''
			self.debug(
				[
					#('self.',self,['NodePointDeriveNoder']),
					str(self.point)
				]
			)
			'''
			
			#point
			self.point(
				self.NodePointDeriveNoder,
				'ModeledPointDeriveControllerVariable'
			)

#</DefineClass>