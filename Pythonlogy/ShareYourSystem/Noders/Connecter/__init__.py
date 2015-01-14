# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Connecters...

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
								'ConnectingCatchVariablesList',
								'ConnectingAttentionVariablesList',
								'ConnectedAttentionDeriveConnectersList',
								'ConnectedCatchDeriveConnectersList'
							]

	def default_init(self,
						_ConnectingCatchVariablesList=None,
						_ConnectingAttentionVariablesList=None,
						_ConnectedAttentionDeriveConnectersList=None,
						_ConnectedCatchDeriveConnectersList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_connect(self):	

		#attention
		self.ConnectedCatchDeriveConnectersList=map(
				lambda __ConnectingAttentionGetStr:
				self.attention(**{
						'CatchingGetVariable':__ConnectingAttentionGetStr
					}
				).CatchedGetVariable,
				self.ConnectingAttentionGetStrsList
			)

		#catch
		self.ConnectedAttentionDeriveConnectersList=map(
				lambda __ConnectingCatchGetStr:
				self.catch(_GetVariable=__ConnectingCatchGetStr).CatchedGetVariable,
				self.ConnectingCatchGetStrsList
			)

#</DefineClass>
