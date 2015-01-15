
<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
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
BaseModuleStr="ShareYourSystem.Itemizers.Pointer"
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
									'FilteringGetVariable',
									'FilteredGetVariable',
									'FilteredVariablesList'
								]

	def default_init(self,
				_FilteringGetVariable=None,
				_FilteredGetVariable=None,
				_FilteredVariablesList=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_filter(self):
			
		#debug
		'''
		self.debug(('self.',self,[
									'PickingGetKeyVariablesList',
									'ConcludingConditionTuplesList',
									'FilteringGetVariable'
								])
				)
		'''
		
		#Get
		if type(self.FilteringGetVariable) in SYS.StrTypesList:
			self.FilteredGetVariable=self[self.FilteringGetVariable]
		else:
			self.FilteredGetVariable=self.FilteringGetVariable

		#Check
		if self.conclude(self.FilteredGetVariable).ConcludedIsBool:

			#debug
			'''
			self.debug(
					(
						'self.',self,[
										'PickingGetKeyVariablesList',
										'ConcludedConditionIsBoolsList',
									]+SYS.unzip(
										self.ConcludingConditionTuplesList,[0]
									)
					)
				)
			'''

			#Pick
			self.FilteredVariablesList=self.pick()


#</DefineClass>

```

<small>
View the Filterer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem/Applyiers/Filterer)
</small>

