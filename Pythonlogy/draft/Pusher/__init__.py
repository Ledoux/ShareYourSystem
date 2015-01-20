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
								'PushingCollectionStr',
								'PushingStoreListsList'
							]

	def default_init(self,
						_PushingCollectionStr="",
						_PushingStoreListsList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_push(self):
		
		#debug
		'''
		self.debug(('self.',self,[
								'PushingCollectionStrs',
								'PushingStoreListsList'
							]))
		'''
		
		#map a collect
		map(
			lambda __PushingStoreList:
			self.collect(
				self.PushingCollectionStr,
				*__PushingStoreList
			),
			self.PushingStoreListsList
		)
#</DefineClass>

