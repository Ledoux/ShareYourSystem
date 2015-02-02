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
BaseModuleStr="ShareYourSystem.Standards.Walkers.Mobilizer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConnecterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'ConnectingGraspClueVariablesList',
								'ConnectingCatchCollectionStr',
								'ConnectingAttentionCollectionStr',
								'ConnectedCatchDerivePointersList',
								'ConnectedCatchKeyStrsList'
							]

	def default_init(self,
						_ConnectingGraspClueVariablesList=None,
						_ConnectingCatchCollectionStr="To",
						_ConnectingAttentionCollectionStr="From",
						_ConnectedCatchDerivePointersList=None,
						_ConnectedCatchKeyStrsList=None,
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
		self.ConnectedCatchDerivePointersList=map(
				lambda __ConnectingGraspVariable:
				copy.copy(
					self.grasp(
						__ConnectingGraspVariable
					).catch(
						self.ConnectingCatchCollectionStr
					).attention(
						self.ConnectingAttentionCollectionStr,
						__ConnectingGraspVariable['AttentionUpdateVariable'] 
						if 'AttentionUpdateVariable' in __ConnectingGraspVariable
						else {}
					).CatchedDerivePointerVariable
				),
				self.ConnectingGraspClueVariablesList
			)

		#map
		self.ConnectedCatchKeyStrsList=map(
				lambda __ConnectedDerivePointer:
				__ConnectedDerivePointer.CatchKeyStr,
				self.ConnectedCatchDerivePointersList
			)

		#debug
		'''
		self.debug(('self.',self,['ConnectedCatchKeyStrsList']))
		'''

#</DefineClass>
