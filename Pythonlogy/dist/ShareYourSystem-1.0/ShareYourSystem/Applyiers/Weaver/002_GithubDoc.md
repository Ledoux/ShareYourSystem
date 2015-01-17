
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


A Weaver

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Linker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class WeaverClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'WeavingInteractTuplesList'
								]

	def default_init(self,
				_WeavingInteractTuplesList=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_weave(self):
		""" """

		#debug
		'''
		self.debug("self.UpdatingItemVariable is "+Representer.represent(
			self.UpdatingItemVariable,**{'RepresentingAlineaIsBool':False}))
		'''

		#Apply
		self.map('interact',map(
									lambda __WeavingInteractTuple:
									{'LiargVariablesList':__WeavingInteractTuple},
									self.WeavingInteractTuplesList
								)
		)

		#Return
		#return self
#</DefineClass>


```

<small>
View the Weaver sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Applyiers/Weaver" target="_blank">Github</a>
</small>

