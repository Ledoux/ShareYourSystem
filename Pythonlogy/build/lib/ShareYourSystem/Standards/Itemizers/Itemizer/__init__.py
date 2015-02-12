# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


An Itemizer...

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Pymongoer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
ItemizingMapPrefixStr="map_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ItemizerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
								'ItemizingKeyVariable',
								'ItemizedKeyVariable'
							]

	def default_init(self,
						_ItemizingKeyVariable=None,
						_ItemizingValueVariable=None,
						**_KwargVariablesDict
					):	

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_itemize(self):

		'''
		if type(self.ItemizingKeyVariable)==str:

			try:
				self.ItemizedValueVariable=getattr(self,)

		if 
		'''

		self.__class__.Inspected


#</DefineClass>


