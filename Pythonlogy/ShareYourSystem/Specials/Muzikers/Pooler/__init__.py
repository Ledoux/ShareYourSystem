# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Pooler...

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Controller"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import itertools
from ShareYourSystem.Functers import Argumenter,Hooker,Switcher
#</ImportSpecificModules>


#<DefineClass>
@DecorationClass()
class PoolerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'PoolingSubsetLengthInt',
									'PoolingSetLengthInt',
									'PooledIntsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_PoolingSubsetLengthInt=0,
						_PoolingSetLengthInt=0,
						_PooledIntsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	@Argumenter.ArgumenterClass()
	def pool(self,_SubsetLengthInt=None,_SetLengthInt=None,**_KwargVariablesDict):

		#debug
		self.debug(('self.',self,[
									'PoolingSubsetLengthInt',
									'PoolingSetLengthInt'
								]))

		#Combine
		self.PooledIntsList=list(
			itertools.combinations(
				xrange(self.PoolingSetLengthInt),
				self.PoolingSubsetLengthInt
			)
		)
		
		#debug
		'''
		self.debug(('self.',self,['PooledIntsList']))
		'''

		#Return self
		return self

#</DefineClass>
