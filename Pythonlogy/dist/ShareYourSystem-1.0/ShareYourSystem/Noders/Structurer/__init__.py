# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Structurer is the last level of class that helps for building
hierarchic structures. For a certain <StructuringNodeStr> it walks to group
everybody in the hfd5.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Grouper"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class StructurerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'StructuringNodeCollectionStrsList',
									'StructuringBeforeUpdateList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_StructuringNodeCollectionStrsList=[],
						_StructuringBeforeUpdateList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':'hdformat'}]})
	def do_structure(self):

		#debug
		'''
		self.debug(('self.',self,['ParentingNodeStr']))
		'''
		
		#<NotHook>
		#hdformat first
		self.hdformat()
		#</NotHook>

		"""
		print([
							('parent',{'LiargVariablesList':[self.ParentingNodeStr]}),
							('group',{'LiargVariablesList':[]})
						]+self.StructuringBeforeUpdateList)
		"""

		#Walk while parentizing and grouping
		self.walk(
					{
						'BeforeUpdateList':
						[
							('parent',{'LiargVariablesList':[]}),
							('group',{'LiargVariablesList':[]})
						]+self.StructuringBeforeUpdateList,
						'GatherVariablesList':map(
								lambda __StructuringNodeCollectionStr:
								Noder.NodingPrefixGetStr+__StructuringNodeCollectionStr+Noder.NodingSuffixGetStr,
								self.StructuringNodeCollectionStrsList
							)
					}
				)

		#Return self
		#return self

#</DefineClass>
