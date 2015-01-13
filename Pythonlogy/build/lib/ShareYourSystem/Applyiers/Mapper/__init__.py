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
BaseModuleStr="ShareYourSystem.Applyiers.Applyier"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Functers import Argumenter
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

	#<DefineDoMethods>
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

		#Link to the apply features
		if hasattr(self,self.MappingApplyMethodStr):

			#set the AppliedMethod
			self.AppliedMethod=getattr(self,self.MappingApplyMethodStr)

			#set that it is ok
			self.ApplyingIsBool=True

			#debug
			'''
			self.debug(
						('self.',self,[
										'AppliedMethod'
									])
				)
			'''

			#Map the apply
			self.MappedVariablesList=map(
					lambda __MappingArgDict:
					self.apply(
								self.MappingApplyMethodStr,
								__MappingArgDict
							).AppliedOutputVariable,
					self.MappingArgDictsList
				)

		#Return self
		#return self

#</DefineClass>
