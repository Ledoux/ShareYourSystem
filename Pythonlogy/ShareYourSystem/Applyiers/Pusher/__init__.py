# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Pusher instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Collecter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PusherClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[	
									'PushingStoreListsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_PushingStoreListsList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_push(self):
		
		#debug
		'''
		self.debug(('self.',self,['PushingStoreListsList']))
		'''
		
		#Apply __getitem__
		self.map('collect',map(
									lambda __PushingStoreList:
									{
										'LiargVariablesList':[],
										'KwargVariablesDict':
										{
											'CollectingNodeKeyStr':__PushingStoreList[0],
											'CollectingNodeVariable':__PushingStoreList[1],
										}
									},
									self.PushingStoreListsList
								)
					)
#</DefineClass>

