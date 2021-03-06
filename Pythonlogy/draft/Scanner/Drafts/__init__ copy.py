# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


Scanner instances helps for doing and storing a list of results
given a grid of values for the parameters
 
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Storer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

import itertools
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ScannerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'ScanningGridTuplesList',
									'ScannedGetKeyStrsList',
									'ScannedValueVariablesTuplesList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_ScanningGridTuplesList=None,
						_ScannedGetKeyStrsList=None,
						_ScannedValueVariablesTuplesList=None,
						**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_scan(self):

		#set the ScannedGettingStrsList
		self.ScannedGetKeyStrsList=SYS.unzip(
			self.ScanningGridTuplesList,[0]
		)

		#Scan the values of this model
		self.ScannedValueVariablesTuplesList=list(
										itertools.product(*SYS.unzip(
										self.ScanningGridTuplesList,[1]
										)
									)
								)

		#debug
		self.debug(('self.',self,['ScannedGetKeyStrsList','ScannedValueVariablesTuplesList']))

		#map an update and a store for each combination
		map(
				lambda __ScannedValueVariablesTuple:
				self.update(
						zip(
							self.ScannedGetKeyStrsList, 
							__ScannedValueVariablesTuple
						)
				).setDoneVariables().collect(),
				self.ScannedValueVariablesTuplesList
			)

		#Return self
		#return self

