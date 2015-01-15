
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


A Picker maps a __getitem__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Mapper"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'DoingGetBool':True})
class PickerClass(BaseClass):
	
	def default_init(self,
				_PickingGetKeyVariablesList=None,
				_PickedGetValueVariablesList=None,
				**_KwargVariablesDict
				):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_pick(self):
		"""Map the __getitem__ to the <_GettingVariablesList>"""

		#debug
		'''
		self.debug(('self.',self,['PickingGetKeyVariablesList']))
		'''

		#Apply __getitem__
		self.map('__getitem__',map(
									lambda __PickingKeyVariable:
									{'LiargVariablesList':[__PickingKeyVariable]},
									self.PickingGetKeyVariablesList
								)
					)

		#link with AppliedMappedVariablesList
		self.PickedGetValueVariablesList=self.MappedVariablesList

		#debug
		'''
		self.debug(('self.',self,['PickedGetValueVariablesList']))
		'''
		
		#Return AppliedVariablesList
		return self.PickedGetValueVariablesList
#</DefineClass>

```

<small>
View the Picker sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem/Applyiers/Picker)
</small>

