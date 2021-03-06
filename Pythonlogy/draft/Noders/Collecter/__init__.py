# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Collecter instances

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Parenter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors import Doer
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CollecterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[	
									'CollectingCollectionStr',
									'CollectingNodeKeyStr',
									'CollectingNodeVariable',
									'CollectedGetStr',
									'CollectedSuffixStr',
									'CollectedSetTagStr'
								]

	def default_init(self,
						_CollectingCollectionStr="",
						_CollectingNodeKeyStr="",
						_CollectingNodeVariable=None,
						_CollectedGetStr="",
						_CollectedSuffixStr="",
						_CollectedSetTagStr="",
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_collect(self):
		
		#debug
		'''
		self.debug(('self.',self,[
						'CollectingNodeVariable',
						'CollectingCollectionStr',
						'CollectingNodeKeyStr',
					]))
		'''
		
		#Set
		self.CollectedGetStr=Noder.NodingPrefixGetStr+self.CollectingCollectionStr+Noder.NodingSuffixGetStr

		#Add a typing suffix Str
		if hasattr(self.CollectingNodeVariable.__class__,'NameStr'):
			self.CollectedSuffixStr=self.CollectingNodeVariable.__class__.NameStr  
		else:
			CollectedTypeStr=type(self.CollectingNodeVariable).__name__
			self.CollectedSuffixStr=CollectedTypeStr[0].upper()+CollectedTypeStr[1:]

		#set
		self.CollectedSetTagStr=self.CollectedGetStr+self.CollectingNodeKeyStr+self.CollectedSuffixStr

		#debug
		'''
		self.debug(('self.',self,['CollectedSetTagStr']))
		'''
		
		#node
		self[self.CollectedSetTagStr]=self.CollectingNodeVariable

#</DefineClass>

