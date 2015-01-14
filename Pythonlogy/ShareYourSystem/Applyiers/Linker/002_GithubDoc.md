
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


An Linker maps a point

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Updater"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class LinkerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'LinkingPointListsList'
							]

	def default_init(self,
				_LinkingPointListsList=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_link(self):
		""" """

		#debug
		'''
		self.debug(('self.',self,['LinkingPointListsList']))
		'''

		#Apply
		self.map('point',map(
								lambda __LinkingPointList:
								{'LiargVariablesList':__LinkingPointList},
								self.LinkingPointListsList
							)
		)

		#Return
		#return self

#</DefineClass>



```

<small>
View the Linker sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem/Applyiers/Linker)
</small>

