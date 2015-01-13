# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Hierarchizer is a Joiner that can joins also with tables contained in noded objects

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Joiner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import tables

from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class HierarchizerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'HierarchizingNodeStr'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_HierarchizingNodeStr="Component",
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)


	#@Switcher.SwitcherClass()
	#@Argumenter.ArgumenterClass()
	#@Imitater.ImitaterClass()
	def mimic_table(self):

		#debug
		'''
		self.debug(('self.',self,[
									'HierarchizingNodeStr',
								]))
		'''

		#<NotHook>
		#database firstand hierarchy first
		self.database()
		#/<NotHook>

		#Check
		if self.HierarchizingNodeStr!="":

			#structure first in the parent pointer and then table
			if self.NodePointDeriveNoder!=None:

				#Check
				if self.HdformatedFileVariable==None:

					#debug
					'''
					self.debug(
							[
								'We have to structure first'
							]
						)
					self.NodePointDeriveNoder.debug(
							[
								'Storer speaking...'
							]
						)
					'''

					#structure by also tabling at the same time
					self.NodePointDeriveNoder.structure(
						**{
							'ParentingNodeStr':self.HierarchizingNodeStr
						}
					)
		
		#<NotHook>
		BaseClass.table(self)
		#</NotHook>

		#<NotHook>
		#Return self
		#return self
		#</NotHook>

#</DefineClass>

