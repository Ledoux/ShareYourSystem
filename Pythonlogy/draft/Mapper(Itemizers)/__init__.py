# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>

A Mapper instance maps an apply and so "grinds" a MappingArgDictsList 
to a method.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Itemizers.Applyier"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class MapperClass(BaseClass):
		
	#Definition
	RepresentingKeyStrsList=[
							'MappingApplyMethodStr',
							'MappingArgDictsList',
							'MappedVariablesList'
						]

	def default_init(self,
				_MappingApplyMethodStr="", 		
				_MappingArgDictsList=None, 		
				_MappedVariablesList=None, 		
				**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_map(self):
		""" """

		#debug
		'''
		self.debug(
					('self.',self,[
									'MappingMethodStr',
									'MappingArgDictsList'
								])
			)
		'''

		"""
		map(
				lambda 
				self.Mapp
				self.MappingVariablesList
			)
		"""

#</DefineClass>
