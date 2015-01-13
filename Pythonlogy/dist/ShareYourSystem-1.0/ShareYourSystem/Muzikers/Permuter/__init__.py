# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Permuter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Controller"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import functools
import itertools
from ShareYourSystem.Functers import Argumenter,Hooker,Switcher
#</ImportSpecificModules>

#<DefineFunctions>
def getFlattenedListWithVariablesList(_VariablesList):
	return functools.reduce(
					lambda x,y:
						x+list(y) if type(y)==tuple 
						else list(x)+[y] if type(x) in [list,tuple] 
						else [x,y],_VariablesList
				)

def getPermutedIntsListWithCategoriesIntAndLengthInt(_CategoriesInt,_LengthInt):
	return functools.reduce(
					lambda x,y:
						map(
								lambda __IntOrTuple:
										getFlattenedListWithVariablesList(list(__IntOrTuple)) 
										if type(__IntOrTuple)==tuple
										else __IntOrTuple,
										itertools.product(x,y)
							),
						map(lambda Int:xrange(_LengthInt),xrange(_CategoriesInt))
				)
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class PermuterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'PermutingSubsetContentInt',
									'PermutingSetLengthInt',
									'PermutedIntsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_PermutingSubsetContentInt=0,
						_PermutingSetLengthInt=0,
						_PermutedIntsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	@Argumenter.ArgumenterClass()
	def permute(self,_SubsetContentInt=None,_SetLengthInt=None,**_KwargVariablesDict):

		#debug
		'''
		self.debug(('self.',self,['PermutingSetLengthInt','PermutingSubsetContentInt']))
		'''

		#Permute
		self.PermutedIntsList=getPermutedIntsListWithCategoriesIntAndLengthInt(
			self.PermutingSubsetContentInt,
			self.PermutingSetLengthInt
		)

		#Return self
		return self

#</DefineClass>
