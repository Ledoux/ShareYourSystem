

<!--
FrozenIsBool False
-->

#Guider

##Doc
----


>
> The Guider write templated .py or .md files for explaining how
> work a certain Module
>
>

----

<small>
View the Guider notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Guider.ipynb)
</small>




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


The Guider write templated .py or .md files for explaining how
work a certain Module

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Deployer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
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
View the <NameStr> notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/<NameStr>.ipynb)
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
View the <NameStr> sources on <a
href="'''+SYS.GithubMasterUrlStr+'''/Pythonlogy/<GithubPathStr>"
target="_blank">Github</a>
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
            document.write("'''+SYS.OuvatonUrlStr+'''/slides/ ")
            document.write("<iframe width=\\"725\\" height=\\"300\\" src=\\"")
            document.write("'''+SYS.OuvatonUrlStr+'''")
            document.write("/slides/<NameStr>.php\\"></iframe>")
        }
        else if(HrefStr == "http://127.0.0.1:8000/LibraryReference/<NameStr>/"){

        //alert('Localhost')
        document.write("from ")
        document.write("localhost mkdocs but direct to ouvaton")
        document.write("<iframe width=\\"725\\" height=\\"300\\" src=\\"")
        document.write("'''+SYS.OuvatonUrlStr+'''")
        document.write("/slides/<NameStr>.php\\"></iframe>")
    }
    else
    {

        //alert('Local')
            document.write("from ")
            document.write("'''+SYS.OuvatonLocalFolderPathStr+''' ")
            document.write("<iframe width=\\"725\\" height=\\"300\\" src=\\"")
            document.write("'''+SYS.OuvatonLocalFolderPathStr+'''")
            document.write("<NameStr>.html\\"></iframe>")

    }

</script>

<small>
View the <NameStr> concept on <a
href="'''+SYS.OuvatonUrlStr+'''/slides/<NameStr>.php"
target="_blank">Ouvaton</a>
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
from ShareYourSystem.Standards.Classors import Attester
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
                                                                        lambda
__KeyStr:
__KeyStr.split(
GuidingSortStr
                                                                        )[0],
self.GuidedDict.values()
                                                                )
                                                )

                                        #Definition the last index of Guide
                                        IndexInt=max(IndexesList) if
len(IndexesList)>0 else -1

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
                                GuidingTextStrKeyStr='Guiding'+self.GuidingPageS
tr+self.GuidingScriptStr+'TextStr'

                                #debug
                                '''
                                print('self.FiledFileVariable is
',self.FiledFileVariable)
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


```

<small>
View the Guider sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Guiders/Guider" target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive
special attributes from the decorating ClassorClass,
specially the NameStr, that should be the ClassStr
without the TypeStr in the end.

```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Guiders import Guider
from ShareYourSystem.Standards.Objects import Concluder

#Definition an instance
MyGuider=Guider.GuiderClass(
    ).package(
        Concluder
    ).guide(
        '001','Github','Doc','Markdown',
    )

#Definition the AttestedStr
SYS._attest(
    [
        'MyGuider is '+str(
            SYS._str(
                MyGuider,
                **{
                'RepresentingBaseKeyStrsListBool':False
                }
            )
        )
    ]
)


```


```console
>>>


*****Start of the Attest *****

MyGuider is < (GuiderClass), 4538290832>
   /{
   /  '<New><Instance>IdInt' : 4538290832
   /  '<Spe><Class>GuidedIndexStr' :
   /  '<Spe><Instance>GuidingBookStr' : Doc
   /  '<Spe><Instance>GuidingIndexStr' : 001
   /  '<Spe><Instance>GuidingPageStr' : Github
   /  '<Spe><Instance>GuidingScriptStr' : Markdown
   /}

*****End of the Attest *****



```
