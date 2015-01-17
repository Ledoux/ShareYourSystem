
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


The Filer is a quick object for opening a FiledFileVariable and safely using (read,write) 
it depending on the FiledModeStr.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Objects.Packager"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
#</ImportSpecificModules>

#<DefineLocals>
FilingOrderStr='_'
#</DefineLocals>

#<DefineClass>
@DecorationClass()
class FilerClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'FilingKeyStr',
								'FilingModeStr',
								'FiledPathStr',
								'FiledFileVariable'
							]


	def default_init(self,
						_FilingKeyStr="",
						_FilingModeStr='r',
						_FiledPathStr="",
						_FiledFileVariable=None,
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	#@Argumenter.ArgumenterClass()
	def do_file(self,**_KwargVariablesDict):

		#Call the folder method before
		self.folder()

		#debug
		'''
		self.debug(('self.',self,['FolderingPathStr']))
		'''

		#set the FiledPathStr
		if self.FolderingPathStr[-1]!='/':
			self.FolderingPathStr=self.FolderingPathStr+'/'
		self.FiledPathStr=self.FolderingPathStr+self.FilingKeyStr

		#debug
		'''
		self.debug(('self.',self,['FilingKeyStr','FiledPathStr','FilingModeStr']))
		'''

		#Close before if we chaneg the mode
		if self.FiledFileVariable!=None:

			#Check
			if self.FiledFileVariable==self.FiledPathStr:

				#Return if it is the same mode already
				if self.FiledFileVariable.mode==self.FilingModeStr:
					return self

				#Check
				if self.FiledFileVariable.mode!='c':
					if ('w' in self.FilingModeStr and self.FiledFileVariable.mode=='r'
						) or ('r'==self.FilingModeStr and 'w' in self.FiledFileVariable.mode):
						self.FiledFileVariable.close()

			else:

				#Close
				self.FiledFileVariable.close()



		#Open the self.FilePointer
		if self.FilingModeStr=='r' and os.path.isfile(self.FiledPathStr):

			#debug
			'''
			self.debug('Open the file for reading !')
			'''

			#Open
			self.FiledFileVariable=open(self.FiledPathStr,self.FilingModeStr)

		else:

			#debug
			'''
			self.debug('Open the file for writing !')
			'''

			#Open
			self.FiledFileVariable=open(self.FiledPathStr,self.FilingModeStr)

		#Return self
		#return self
	
#</DefineClass>


```

<small>
View the Filer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tree/master/Pythonlogy/ShareYourSystem/Interfacers/Filer" target="_blank">Github</a>
</small>

