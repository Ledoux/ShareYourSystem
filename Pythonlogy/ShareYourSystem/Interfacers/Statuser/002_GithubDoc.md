
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


The Statuser

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Interfacers.Processer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class StatuserClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'StatusingProcessStr',
									'StatusedSnapshotStr',
									'StatusedLineStrsList',
									'StatusedIdStrsList'
								]

	def default_init(self,
						_StatusingProcessStr="",
						_StatusedSnapshotStr="",
						_StatusedLineStrsList=None,
						_StatusedIdStrsList=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)
	
	def do_status(self):

		#Check
		if self.StatusingProcessStr!="":

			#call
			self.StatusedSnapshotStr=self.process(
				"ps -ef | grep "+self.StatusingProcessStr
			).ProcessedBashStr

			#debug
			'''
			self.debug(('self.',self,['StatusedSnapshotStr']))
			'''

			#map
			self.StatusedLineStrsList=SYS._filter(
					lambda __LineStr:
					SYS.PythonPathStr in __LineStr,
					self.StatusedSnapshotStr.split('\n')
				)

			#debug
			'''
			self.debug(('self.',self,['StatusedLineStrsList']))
			'''

			#call
			self.StatusedIdStrsList=map(
				lambda __LineStr:
				__LineStr.split()[1],
				self.StatusedLineStrsList	
			)

			#debug
			'''
			self.debug(('self.',self,['StatusedIdStrsList']))
			'''

		#Return self
		#return self

#</DefineClass>

```

<small>
View the Statuser sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Interfacers/Statuser)
</small>

