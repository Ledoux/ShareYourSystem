# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Scanner instances helps for doing and flushing rows from
a range of modeling values
 
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Modelers.Scanner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

import itertools
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ExplorerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ExploringStatTuplesList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_ExploringStatTuplesList=None
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_scan(self):

		#<NotHook>
		#table first
		self.table()
		#</NotHook>

		#Check
		if len(self.ScanningRangeTuplesList)==0:

			#just flush
			self.flush()

		else:


		#Return self
		#return self

