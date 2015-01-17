
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


An Adder maps an append
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Instancer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class AdderClass(BaseClass):
	
	#Definition 
	RepresentingKeyStrsList=[
									#'AddingVariablesList'
								]

	def default_init(self,
						_AddingVariablesList=None, 
						**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Argumenter.ArgumenterClass(**{'ArgumentingDoStr':'Add'})
	def __add__(self,_VariablesList):
		"""Apply the append to the <_AddingVariablesList>"""

		#Call the add method
		self.add(_VariablesList)

		#Return 
		return self

	def do_add(self):
		"""Apply the append to the <_AddingVariablesList>"""

		#debug
		'''
		self.debug(('self.',self,['AddingVariablesList']))
		'''

		#Apply	
		self.map('append',map(
									lambda __AddingVariable:
									{'LiargVariablesList':[__AddingVariable]},
									self.AddingVariablesList
								)
				)

#</DefineClass>

```

<small>
View the Adder sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Noders/Adder" target="_blank">Github</a>
</small>

