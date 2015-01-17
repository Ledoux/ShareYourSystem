
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


The Conditioner

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Debugger"
DecorationModuleStr="ShareYourSystem.Classors.Representer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Representer=DecorationModule
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConditionerClass(BaseClass):

	#Definition
	RepresentingKeyStrsList=[
									'ConditioningTestVariable',
									'ConditioningGetBoolFunction',
									'ConditionedIsBool'
								]
	
	def default_init(self,
						_ConditioningTestVariable=None,
						_ConditioningGetBoolFunction=None,
						_ConditioningAttestVariable=None,
						_ConditionedIsBool=True,
						**_KwargVariablesDict
					):
		
		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	#<DefineDoMethod>	
	def do_condition(self):

		#debug
		'''
		self.debug(('self.',self,[
									'ConditioningTestVariable',
									'ConditioningAttestVariable'
								]))
		'''
		
		#call
		self.ConditionedIsBool=self.ConditioningGetBoolFunction(
			self.ConditioningTestVariable,
			self.ConditioningAttestVariable
		)

		#debug
		'''
		self.debug(('self.',self,['ConditionedIsBool']))
		'''
		
#</DefineClass>


```

<small>
View the Conditioner sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Objects/Conditioner" target="_blank">Github</a>
</small>

