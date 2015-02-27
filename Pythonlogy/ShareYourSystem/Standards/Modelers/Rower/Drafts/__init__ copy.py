# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Rower helps to set rowed lines in a Databaser from pointed attributes,
ready then to be inserted in a table.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Tabler"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
from ShareYourSystem.Functers import Hooker,Triggerer,Alerter
#</ImportSpecificModules>

#<DefineFunctions>
def getRowedDictsListWithTable(_Table):
	return map(
			lambda __Row:
			dict(
				zip(
					_Table.colnames,
					map(
						lambda __ColumnStr:
						__Row[__ColumnStr],
						_Table.colnames
					)
				)
			),
			_Table.iterrows()
		)
#</DefineFunctions>


#<DefineClass>
@DecorationClass()
class RowerClass(
					BaseClass
				):
	
	#Definition
	RepresentingKeyStrsList=[
									'RowedVariablePointer', 										
									'RowedNotIdentifiedGettingStrsList',																
									'RowedIdentifiedGettingStrsList',
									'RowedIdentifiedOrderedDict',
									'RowedNotIdentifiedOrderedDict'
								]

	def default_init(self,
					_RowedVariablePointer=None, 									
					_RowedNotIdentifiedGettingStrsList=[],					
					_RowedIdentifiedGettingStrsList=[],						
					_RowedIdentifiedOrderedDict=collections.OrderedDict(), 		
					_RowedNotIdentifiedOrderedDict=collections.OrderedDict(), 
					**_KwargVariablesDict
					):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	#@Alerter.AlerterClass()
	#@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr':"table"}]})
	def row(self,**_KwargVariablesDict):
		"""Call the Output<HookStr> methods and return self.OutputedPointer (self by default)"""
	
		#set the RowedVariablePointer as the NodedDatabaseParentPointer by default		
		if self.RowedVariablePointer==None and hasattr(self,'NodedDatabaseParentPointer'):
			self.RowedVariablePointer=self.NodedDatabaseParentPointer
			
		#Split the GettingStrs between the ones that identify and the other that not
		self.RowedNotIdentifiedGettingStrsList=filter(
					lambda __GettingStr:
					__GettingStr not in self.RowedIdentifiedGettingStrsList,
					SYS.unzip(
						self.ModelingDescriptionTuplesList,[0]
						)
				)

		self.RowedIdentifiedOrderedDict.update(
					zip(
						self.RowedIdentifiedGettingStrsList,
						self.RowedVariablePointer.pick(self.RowedIdentifiedGettingStrsList)
						)
				)

		self.RowedNotIdentifiedOrderedDict.update(
					zip(
						self.RowedNotIdentifiedGettingStrsList,
						self.RowedVariablePointer.pick(self.RowedNotIdentifiedGettingStrsList)
						)
				)

		#<NotHook>
		#table then
		self.table()
		#</NotHook>

		#<NotHook>
		#Return self
		return self
		#</NotHook>
		
#</DefineClass>
