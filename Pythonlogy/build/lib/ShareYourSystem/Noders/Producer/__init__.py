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
BaseModuleStr="ShareYourSystem.Noders.Collecter"
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
									'ProducingNodeKeyStrsList',
									'ProducingDeriveNoderClass',
									'ProducingUpdateVariable',
									'ProducedDeriveNodersList'
								]

	def default_init(self,
						_ProducingCollectionStr="",
						_ProducingNodeKeyStrsList=None,
						_ProducingDeriveNoderClass=Noder.NoderClass,
						_ProducingUpdateVariable=None,
						_ProducedDeriveNodersList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_produce(self):
		
		#debug
		'''
		self.debug(('self.',self,[
						'ProducingNodeKeyStrsList',
						'ProducingDeriveNoderClass',
						'ProducingUpdateVariable'
					]))
		'''

		#set
		self.ProducedDeriveNodersList=map(
									lambda __ProducingCollectionKeyStr:
									self.ProducingDeriveNoderClass().update(
										self.ProducingUpdateVariable
									),
									self.ProducingNodeKeyStrsList
								)

		#debug
		'''
		self.debug(('self.',self,['ProducedDeriveNodersList']))
		'''
		
		#map a collect
		map(
				lambda __ProducingNodeKeyStr,__ProducedDeriveNoder:
				self.collect(
					self.ProducingCollectionStr,
					__ProducingNodeKeyStr,
					__ProducedDeriveNoder
				),
				self.ProducingNodeKeyStrsList,
				self.ProducedDeriveNodersList
			)

#</DefineClass>

