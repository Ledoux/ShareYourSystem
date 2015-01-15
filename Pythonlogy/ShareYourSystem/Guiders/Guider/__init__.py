# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Guider write templated .py or .md files for explaining how
work a certain Module

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Interfacers.Deployer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import inspect
import os
import sys
#</ImportSpecificModules>

#<DefineFunctions>
ScriptStrAndExtensionStrTuplesList=[
	('Latex','.tex'),
	('Markdown','.md'),
	('Python','.py'),
]
#</DefineFunctions>

#<DefineLocals>

GuidingDocumentMarkdownTextStr='''
<!--
FrozenIsBool False
-->

#<NameStr>

##Doc
----

<ModuleDocStr>

----

<small>
View the <NameStr> notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyoursystem.ouvaton.org/<NameStr>.ipynb)
</small>

'''

GuidingGithubMarkdownTextStr='''
<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
<CodeStr>
```

<small>
View the <NameStr> sources on [Github]('''+SYS.GithubMasterUrlStr+'''/Pythonlogy/<GithubPathStr>)
</small>

'''

GuidingOuvatonMarkdownTextStr='''
<!--
FrozenIsBool False
-->

##Concept and SubModules family

<script type="text/javascript">

	var HrefStr=window.location.href;
	//alert(window.location.href)

	if(HrefStr == "'''+SYS.OuvatonUrlStr+'''/<NameStr>/"){

	    //alert('Ouvaton')
	    document.write("from ")
	    document.write("'''+SYS.OuvatonUrlStr+''' ")
	    document.write("<iframe width=\\"725\\" height=\\"300\\" src=\\"")
	    document.write("'''+SYS.OuvatonUrlStr+'''")
	    document.write("/<NameStr>.php\\"></iframe>")
	}
	else{

	    //alert('Local')
	    document.write("from ")
	    document.write("'''+SYS.OuvatonLocalFolderPathStr+''' ")
	    document.write("<iframe width=\\"725\\" height=\\"300\\" src=\\"")
	    document.write("'''+SYS.OuvatonLocalFolderPathStr+'''")
	    document.write("<NameStr>.html\\"></iframe>")
	}

</script>

<small>
View the <NameStr> concept on [ Ouvaton ]('''+SYS.OuvatonUrlStr+'''/<NameStr>.php)
</small>

'''

GuidingClassMarkdownTextStr='''
<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the <NameStr>Class are :
'''

GuidingClassCodeTextStr='''
#FrozenIsBool False

#ImportModules
import ShareYourSystem as SYS
from <ParentModuleStr> import <NameStr>
		
#Definition the AttestedStr
SYS._attest(
	[
		'DefaultAttributeItemTuplesList is '+SYS._str(
			<NameStr>.<NameStr>Class.DefaultAttributeItemTuplesList,
			**{'RepresentingAlineaIsBool':False}
		)
	]
) 

#Print

'''

GuidingInstanceMarkdownTextStr='''
<!--
FrozenIsBool False
-->

##More Descriptions at the level of the instances

A default call of an instance gives :
'''

GuidingInstanceCodeTextStr='''
#FrozenIsBool False

#ImportModules
from ShareYourSystem.Classors import Attester
from <ParentModuleStr> import <NameStr>
		
#Definition the AttestedStr
SYS._attest(
	[
		<NameStr>.<NameStr>Class()
	]
) 

#Print


'''
GuidingSortStr='_'
#</DefineLocals>


#<DefineClass>
@DecorationClass()
class GuiderClass(BaseClass):
	
	#Definition
	RepresentingKeyStrsList=[
								'GuidingIndexStr',
								'GuidingPageStr',
								'GuidingBookStr',
								'GuidingScriptStr',
								'GuidedIndexStr'
							]
						
	def default_init(self,
						_GuidingIndexStr="",
						_GuidingPageStr="",
						_GuidingBookStr="",
						_GuidingScriptStr="",
						_GuidedIndexStr="",
						**_KwargVariablesDict
					):

		#Call the parent __init__ method
		BaseClass.__init__(self,**_KwargVariablesDict)

	def do_guide(self):
		
		#Check
		if self.PackagingModuleVariable!=None:

			#Check
			if self.GuidingPageStr!="":

				if self.GuidingIndexStr=="":

					#Definition
					IndexesList=map(
							int,
							map(
									lambda __KeyStr:
									__KeyStr.split(
									GuidingSortStr
									)[0],
								self.GuidedDict.values()
								)
						)

					#Definition the last index of Guide
					IndexInt=max(IndexesList) if len(IndexesList)>0 else -1

					#Define
					self.GuidingIndexStr="%02d"%(IndexInt+1)+GuidingSortStr

			#debug
			'''
			self.debug(('self.',self,['PackagedLocalFolderPathStr']))
			'''
			
			#Write a new file
			self.file(
						self.GuidingIndexStr+GuidingSortStr+self.GuidingPageStr+self.GuidingBookStr+(
									dict(
						ScriptStrAndExtensionStrTuplesList
						)
							)[self.GuidingScriptStr],
						'wt'
					)

			#Check
			if self.FiledFileVariable.mode=='wt':

				#Definition
				GuidingTextStrKeyStr='Guiding'+self.GuidingPageStr+self.GuidingScriptStr+'TextStr'

				#debug
				'''
				print('self.FiledFileVariable is ',self.FiledFileVariable)
				print('')
				'''

				#Definition
				GuidedTextStr=globals()[GuidingTextStrKeyStr]

				#debug
				'''
				print('GuidedTextStr is ',GuidedTextStr)
				print('')
				'''

				#Replace
				GuidedTextStr=GuidedTextStr.replace(
											'<NameStr>',
											self.FolderedNameStr
											)

				#debug
				'''
				print('GuidedTextStr is ',GuidedTextStr)
				print('')
				'''
						
				#Replace
				if self.FolderedNameStr=="ShareYourSystem":
					GuidedTextStr=GuidedTextStr.replace(
						"from <ParentModuleStr> ",""
					)
				else:
					GuidedTextStr=GuidedTextStr.replace(
							"<ParentModuleStr>",
							self.FolderedParentModuleStr
						).replace(
							"<GithubPathStr>",
							self.PackagedModuleStr.replace('.','/')
						).replace(
							"<ModuleDocStr>",
							sys.modules[
								self.PackagedModuleStr
							].__doc__.split('</DefineSource>\n'
								)[-1].replace(
								'\n','\n> '
							)
						).replace(
							"<CodeStr>",
							inspect.getsource(
								sys.modules[
									self.PackagedModuleStr
								]
							)
						)

				#debug
				'''
				print('Guider l.194')
				print('self.FiledPathStr is',self.FiledPathStr)
				print('')
				'''

				#Write
				self.write(GuidedTextStr,**{'LoadingFormatStr':'txt'})

				#Close
				self.FiledFileVariable.close()
		
#</DefineClass>

