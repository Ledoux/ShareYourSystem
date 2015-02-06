# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Viewer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from IPython.display import HTML,display
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ViewerClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
								'ViewingConditionVariable',
								'ViewingQueryVariable',
								'ViewedCollectionStrsList',
								'ViewedConsoleStr'
							]

	def default_init(self, 
						_ViewingConditionVariable=None,
						_ViewingQueryVariable=None,
						_ViewedCollectionStrsList=None,
						_ViewedConsoleStr="",
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_view(self):

		#Init
		self.ViewedConsoleStr=""

		#Check
		if hasattr(self,'hdfview'):
			
			#hdfview
			self.hdfview()

			#
			self.ViewedConsoleStr+="Associated Hdf file :\n"
			self.ViewedConsoleStr+=self.HdformatedConsoleStr

		#Check
		if self.PymongoneDatabaseVariable!=None:
			
			#Check
			if self.ViewingConditionVariable==None:
				self.ViewingConditionVariable={}

			#map
			self.ViewedCollectionStrsList=map(
					lambda __CollectionTuple:
					__CollectionTuple[0]+' : \n'+SYS._str(
						list(
							__CollectionTuple[1].find(
									self.ViewingConditionVariable[__CollectionTuple[0]]
									if __CollectionTuple[0] in self.ViewingConditionVariable
									else {},
									self.ViewingQueryVariable[__CollectionTuple[0]]
									if __CollectionTuple[0] in self.ViewingQueryVariable
									else {}
								)
						)
					),
					self.PymongoneDatabaseVariable.__dict__.items()
				)

			self.ViewedConsoleStr+="Associated Mongo db :\n"
			self.ViewedConsoleStr=""




#</DefineClass>
