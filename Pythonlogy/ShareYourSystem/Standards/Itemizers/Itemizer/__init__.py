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
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Hdformater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
ItemizingPrefixStr="Item_"
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class ItemizerClass(BaseClass):
	
	pass
	
	"""
	#Definition
	RepresentingKeyStrsList=[
									'ItemizingKeyVariable',
									'ItemizedKeyVariable'
								]

	#@SYS.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.init}]})
	def default_init(self,
						_ItemizingKeyVariable=None,
						_ItemizedKeyVariable=None,
						**_KwargVariablesDict
					):
		""" """		

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_itemize(self):

		#Check
		if self.ItemizingKeyVariable.startswith(ItemizingPrefixStr):

			#split
			self.ItemizedKeyVariable=ItemizingPrefixStr.join(
				self.ItemizingKeyVariable.split(
				ItemizingPrefixStr)[1:]
			)

			#debug
			self.debug(
						[
							'go to a getitem get',
							('self.',self,['ItemizingKeyVariable','ItemizedKeyVariable'])
						]
					)

			#return	__getitem__
			return self.__getitem__(self.ItemizedKeyVariable)

		else:

			#debug
			self.debug(
						[
							'classic object getattr...',
							('self.',self,['ItemizingKeyVariable'])
						]
					)

			#Return default getattr
			return object.__getattribute__(self,self.ItemizingKeyVariable)

	def __getattribute__(self,_KeyVariable):

		#Itemize
		return self.itemize(_KeyVariable)
	"""

#</DefineClass>


