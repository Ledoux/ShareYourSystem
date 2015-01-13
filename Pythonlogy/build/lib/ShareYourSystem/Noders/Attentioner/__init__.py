# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Attentioner instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Catcher"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Classors import Doer
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class AttentionerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'AttentioningCollectionStr'
							]

	def default_init(self,
						_AttentioningCollectionStr="",
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_attention(self):
		
		#debug
		'''
		self.debug(('self.',self,['CatchingCollectionStr']))
		'''
		
		#catch first
		self.catch()

		#set
		if self.AttentioningCollectionStr=="":
			self.AttentioningCollectionStr=self.CollectingCollectionStr

		#debug
		'''
		self.debug(
					('self.',self,[
							'AttentioningCollectionStr',
							'CatchedGetVariable'
							])
				)
		'''
		
		#poitn in the other way
		self.CatchedGetVariable.catch(
			self,
			**{
				'CatchingCollectionStr':self.AttentioningCollectionStr
			}
		)	

#</DefineClass>

