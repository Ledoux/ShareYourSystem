
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


A Settler 

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Coupler"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Itemizers import Pather
from ShareYourSystem.Applyiers import Linker
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['settle']})
class SettlerClass(
					BaseClass,
					Linker.LinkerClass
					):

	#Definition
	RepresentingKeyStrsList=[
								'SettlingParentBool',
								'SettlingLinkBool'
							]

	def default_init(self,
				_SettlingParentBool=False,
				_SettlingLinkBool=False,
				**_KwargVariablesDict):

		#Call the parent init method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Switcher.SwitcherClass()
	def do_settle(self):

		#debug
		'''
		self.debug('We settle here')
		'''
		
		#Parent first
		if self.SettlingParentBool:

			#debug
			'''
			self.debug('We parent here')
			'''

			#parent
			self.parent()

		#link
		if self.SettlingLinkBool:

			#debug
			'''
			self.debug('We link here')
			'''

			#link
			self.link()

		#Return self
		#return self

	#@Imitater.ImitaterClass()
	def mimic_set(self):

		#debug


		#Call the parent method
		OutputDict=BaseClass.set(self)

		#debug
		'''
		self.debug(('self.',self,[
									'SettingKeyVariable',
									'SettingValueVariable'
								]))
		'''

		#Check
		if self.SettingKeyVariable=='NodePointDeriveNoder' and self.SettingValueVariable!=None:

			#debug
			'''
			self.debug(('self.',self,['NodePointDeriveNoder']))
			'''
			
			#settle
			self.settle()

		#return 
		#return OutputDict
			
#</DefineClass>


```

<small>
View the Settler sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Noders/Settler" target="_blank">Github</a>
</small>

