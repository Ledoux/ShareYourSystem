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
BaseModuleStr="ShareYourSystem.Standards.Noders.Grouper"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class StructurerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'StructuringNodeCollectionStrsList',
								'StructuringBeforeUpdateList'
							]

	def default_init(self,
						_StructuringNodeCollectionStrsList=None,
						_StructuringBeforeUpdateList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_structure(self):

		#debug
		'''
		self.debug(('self.',self,['ParentingNodeStr']))
		'''
		
		#<NotHook>
		#hdformat first
		self.hdformat()
		#</NotHook>

		#Walk while parentizing and grouping
		self.walk(
					{
						'BeforeUpdateList':
						[
							(
								'parent',
								SYS.ApplyDictClass(
									{
									'LiargVariablesList':[
										['HdformatedFileVariable']
										]
									}
								)
							),
							(
								'group',
								SYS.ApplyDictClass()
							)
						]+self.StructuringBeforeUpdateList,
						'GatherVariablesList':map(
								lambda __StructuringNodeCollectionStr:
								Noder.NodingPrefixGetStr+__StructuringNodeCollectionStr+Noder.NodingSuffixGetStr,
								self.StructuringNodeCollectionStrsList
							)
					}
				)

#</DefineClass>
