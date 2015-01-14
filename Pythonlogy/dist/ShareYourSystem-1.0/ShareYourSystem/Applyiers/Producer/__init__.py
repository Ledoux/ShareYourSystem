# -*- coding: utf-8 -*-
"""

<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Producer instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Pusher"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ProducerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[	
									'ProducingCollectionKeyStrsList',
									'ProducingPushClass',
									'ProducingUpdateVariable',
									'ProducedPushList'
								]

	def default_init(self,
						_ProducingCollectionKeyStrsList=None,
						_ProducingPushClass=Noder.NoderClass,
						_ProducingUpdateVariable=None,
						_ProducedPushList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_produce(self):
		
		#set
		self.ProducedPushList=map(
									lambda __ProducingCollectionKeyStr:
									[
										__ProducingCollectionKeyStr,
										self.ProducingPushClass().update(
											self.ProducingUpdateVariable
										)
									],
									self.ProducingCollectionKeyStrsList
								)

		#debug
		'''
		self.debug(('self.',self,['ProducedPushList']))
		'''
		
		#push
		self.push(
					_StoreListsList=self.ProducedPushList
				)

		#Return self
		#return self

#</DefineClass>

