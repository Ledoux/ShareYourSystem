# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

Connecter instances catch grasped variables and makes an attention also on it.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Mobilizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConnecterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'ConnectingGraspClueVariablesList',
								'ConnectedDerivePointersList'
							]

	def default_init(self,
						_ConnectingGraspClueVariablesList=None,
						_ConnectedDerivePointersList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_connect(self):	

		#debug
		'''
		self.debug(('self.',self,['ConnectingGraspClueVariablesList']))
		'''
		
		#catch
		self.ConnectedDerivePointersList=map(
				lambda __ConnectingGraspVariable:
				self.grasp(
						__ConnectingGraspVariable
					).catch(
					).attention(
					).GraspedAnswerVariable,
				self.ConnectingGraspClueVariablesList
			)

#</DefineClass>
