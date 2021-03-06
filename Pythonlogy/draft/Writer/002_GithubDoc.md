
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


The Writer is a quick object to write from a LoadedReadVariable.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Loader"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import json
import yaml
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class WriterClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
									'WritingStoreVariable',
									'WritingLoadBool'
								]

	def default_init(self,
						_WritingStoreVariable=None,
						_WritingLoadBool=False,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_write(self):

		#debug
		'''
		self.debug([
						('Before file'),
						('self.',self,[
									'FolderingPathStr',
								])
				])
		'''

		#file first
		self.file(_ModeStr='w')

		#debug
		'''
		self.debug([
						('After file'),
						('self.',self,[
									'FolderingPathStr',
									'WritingLoadBool'
								])
				])
		'''

		#Check
		if self.WritingLoadBool:
			self.WritingStoreVariable=self.LoadedReadVariable

		#debug
		'''
		self.debug(('self.',self,[
									'FiledHardVariable',
									'FolderingPathStr',
									'LoadingFormatStr',
									'WritingStoreVariable'
								]))
		'''

		#Check
		if self.LoadingFormatStr=='txt':

			#Read the FiledHardVariable
			self.FiledHardVariable.write(self.WritingStoreVariable)

		elif self.LoadingFormatStr=='json':

			#debug
			'''
			self.debug(
						[
							'we write in json...',
							'json.dumps(self.WritingStoreVariable,indent=2) is '+str(json.dumps(self.WritingStoreVariable,indent=2))
						]
				)
			'''
			
			#Use the json decoder
			self.FiledHardVariable.write(
				json.dumps(self.WritingStoreVariable,indent=2)
			)

		elif self.LoadingFormatStr=='yaml':

			#debug
			'''
			print('We yamelized !')
			print('self.FiledHardVariable is ',self.FiledHardVariable)
			print('self.WritingStoreVariable is ',self.WritingStoreVariable)
			print('')
			'''

			#Use the json decoder
			self.FiledHardVariable.write(
				yaml.dump(self.WritingStoreVariable,indent=2)
			)

		#Return self
		#return self
	
#</DefineClass>


```

<small>
View the Writer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Interfacers/Writer" target="_blank">Github</a>
</small>

