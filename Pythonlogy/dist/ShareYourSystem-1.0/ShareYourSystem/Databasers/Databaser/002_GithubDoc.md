
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


A Databaser rises to the DatabaserClass. This latter is the deepest class for instancing
Variables able to store values in hierarchic tables. Here, as a first step,
the database method helps to set the <DatabasingKeyStr> in the __dict__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Structurer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['database']})
class DatabaserClass(
						BaseClass
				):

	#Definition
	RepresentingKeyStrsList=[
								'DatabasedSuffixStr',
								'DatabasedCollectionStr',
								'DatabasedSuffixStr',
								'DatabasedPointDeriveStorerVariable'
							]

	def default_init(self,
					_DatabasingKeyStr="",
					_DatabasedCollectionStr="",
					_DatabasedSuffixStr="",
					_DatabasedPointDeriveStorerVariable=None,
					**_KwargVariablesDict
				):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
		
	def do_database(self):

		#set
		if hasattr(self,'NodeKeyStr'):
			self.DatabasingKeyStr=self.NodeKeyStr
			self.DatabasedCollectionStr=self.NodeCollectionStr

		#set
		self.DatabasedSuffixStr=self.DatabasingKeyStr+'Model'

		#
		if hasattr(self,'NodePointDeriveNoder'):
			self.point(
				self.NodePointDeriveNoder,
				'DatabasedPointDeriveStorerVariable'
			)

#</DefineClass>

```

<small>
View the Databaser sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Databasers/Databaser" target="_blank">Github</a>
</small>

