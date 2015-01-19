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
BaseModuleStr="ShareYourSystem.Databasers.Flusher"
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
									'ScanningRangeTuplesList',
									'ScannedGetKeyStrsList',
									'ScannedValueVariablesTuplesList',
									'ScannedRetrieveListsList'
								]

	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':BaseClass.__init__}]})
	def default_init(self,
						_ScanningRangeTuplesList=None,
						_ScanningDatabaseKeyStr="",
						_ScannedGetKeyStrsList=None,
						_ScannedValueVariablesTuplesList=None,
						_ScannedRetrieveListsList=None,
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

			#set the ScannedGettingStrsList
			self.ScannedGetKeyStrsList=SYS.unzip(
				self.ScanningRangeTuplesList,[0]
			)

			#Scan the values of this model
			self.ScannedValueVariablesTuplesList=list(
											itertools.product(*SYS.unzip(
											self.ScanningRangeTuplesList,[1]
											)
										)
									)

			#Check
			if self.ScanningDatabaseKeyStr=="":
				self.ScanningDatabaseKeyStr=self.NodedDatabaseKeyStr

			#debug
			self.debug(('self.',self,[
				'ScanningDatabaseKeyStr',
				'ScannedGetKeyStrsList',
				'ScannedValueVariablesTuplesList']))
			
			#map an update and a store for each combination
			self.ScannedRetrieveListsList=map(
					lambda __ScannedValueVariablesTuple:
					getattr(
						self.NodedDatabaseParentPointer.update(
							zip(
								self.ScannedGetKeyStrsList, 
								__ScannedValueVariablesTuple
							)
						).setDoneVariables(),'NodedDatabaseOrderedDict'
						)[self.ScanningDatabaseKeyStr].flush().pick(['TabledInt','RowedIndexInt']),
					self.ScannedValueVariablesTuplesList
				)

		#Return self
		#return self

