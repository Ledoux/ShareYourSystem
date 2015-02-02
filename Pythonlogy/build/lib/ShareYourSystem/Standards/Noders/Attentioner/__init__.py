# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Attentioner instances grasp a Variable and make inside a catch to the original
instance

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Catcher"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors import Doer
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class AttentionerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'AttentioningCollectionStr',
								'AttentioningUpdateVariable'
							]

	def default_init(self,
						_AttentioningCollectionStr="",
						_AttentioningUpdateVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_attention(self):
		
		#debug
		'''
		self.debug(('self.',self,['AttentioningCollectionStr']))
		'''
		
		#debug
		'''
		self.debug(
					('self.',self,[
							'AttentioningCollectionStr',
							'GraspingClueVariable',
							'AttentioningUpdateVariable'
							])
				)
		'''
		
		#poitn in the other way
		self.GraspedAnswerVariable.grasp(
				self
			).catch(
				self.AttentioningCollectionStr,
				_CatchingUpdateVariable=self.AttentioningUpdateVariable
			)

		

#</DefineClass>

