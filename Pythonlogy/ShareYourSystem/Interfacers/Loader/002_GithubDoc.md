
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


The Loader is a quick object to load from a FiledFileVariable a LoadedReadVariable

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Interfacers.Closer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import json
import yaml
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class LoaderClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'LoadingFormatStr',
									'LoadedReadVariable',
									'FiledFileVariable'
								]

	def default_init(self,
						_LoadingFormatStr='txt',
						_LoadedReadVariable=None,
						_FiledFileVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_load(self,**_KwargVariablesDict):

		#debug
		'''
		self.debug(('self.',self,['LoadingFormatStr']))
		'''

		#file first
		self.file(_ModeStr='r')

		#Check
		if self.LoadingFormatStr=='txt':

			#Read the FiledFileVariable
			self.LoadedReadVariable=self.FiledFileVariable.read()

		elif self.LoadingFormatStr=='json':

			#Use the json decoder
			self.LoadedReadVariable=json.load(self.FiledFileVariable)

		elif self.LoadingFormatStr=='yaml':

			#Use the json decoder
			self.LoadedReadVariable=yaml.load(self.FiledFileVariable)

		#Return self
		#return self
	
#</DefineClass>


```

<small>
View the Loader sources on [Github](https://github.com/Ledoux/ShareYourSystem/tree/master/ShareYourSystem/Interfacers/Loader)
</small>

