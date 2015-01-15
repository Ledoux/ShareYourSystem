
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


An Updater maps a __setitem__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Gatherer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class UpdaterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'UpdatingItemVariable'
							]

	def default_init(self,
				_UpdatingItemVariable=None,
				**_KwargVariablesDict):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_update(self):
		""" """

		#debug
		'''
		self.debug("self.UpdatingItemVariable is "+Representer.represent(
			self.UpdatingItemVariable,**{'RepresentingAlineaIsBool':False}))
		'''
		
		#Apply
		self.map('__setitem__',map(
									lambda __UpdatingItemTuple:
									{'LiargVariablesList':__UpdatingItemTuple},
									self.UpdatingItemVariable.items()
									if hasattr(self.UpdatingItemVariable,'items')
									else (self.UpdatingItemVariable 
										if self.UpdatingItemVariable !=None
										else []
									)
								)
		)

		#Return
		#return self
#</DefineClass>

```

<small>
View the Updater sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem/Applyiers/Updater)
</small>

