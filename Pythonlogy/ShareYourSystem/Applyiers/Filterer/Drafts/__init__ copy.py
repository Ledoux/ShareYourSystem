# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Filterer pick and 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Walker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections

#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class FiltererClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'FilteredVariablesList'
								]

	def default_init(self,
				_FilteredVariablesList=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_filter(self):
			
		#debug
		'''
		self.debug(('self.',self,[
									'WalkingSocketDict',
									'WalkedTopOrderedDict'
								]))
		'''

		#Init
		if 'FilterVariablesList' not in self.WalkedTopOrderedDict:
			self.WalkedTopOrderedDict['FilterVariablesList']=[]

		#Check
		if self.conclude(
			self,
			self.WalkingSocketDict['ConcludeConditionTuplesList']
		).ConcludedIsBool:

			#debug
			'''
			self.debug(
					(
						'self.',self,[
										'ConcludedConditionIsBoolsList',
									]+SYS.unzip(
										self.WalkingSocketDict[
										'ConcludeConditionTuplesList'],[0]
									)
					)
				)
			'''

			#Pick
			self.WalkedTopOrderedDict['FilterVariablesList'].append(
				self.pick(
							self.WalkingSocketDict['PickVariablesList']
						)
			)

		#set
		if self.WalkingSocketDict['TopVariable']==self:
			self.FilteredVariablesList=self.WalkedTopOrderedDict['FilterVariablesList']
			#self.FilteredVariablesList=copy.copy(self.WalkedTopOrderedDict['FilterVariablesList'])
		

#</DefineClass>
