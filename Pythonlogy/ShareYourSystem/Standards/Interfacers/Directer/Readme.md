

<!--
FrozenIsBool False
-->

#Directer

##Doc
----


>
> The Directer is a walker through the folders of the harddrive,
> assuring a call of _DirectingCallbackFunction at each level.
>
>

----

<small>
View the Directer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Directer.ipynb)
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


The Directer is a walker through the folders of the harddrive,
assuring a call of _DirectingCallbackFunction at each level.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Killer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import os
from ShareYourSystem.Functers import Argumenter
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class DirecterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'DirectingCallbackFunction',
'DirectingLiargVariablesList',
'DirectingFilterFunctionPointer'
                                                                ]

        def default_init(self,
                                                _DirectingCallbackFunction=None,
_DirectingLiargVariablesList=None,
_DirectingFilterFunctionPointer=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Argumenter.ArgumenterClass()
        def do_direct(self):

                #Call the folder method before
                self.folder()

                #debug
                '''
                print('Directer l.62')
                print('self.FolderingPathStr is ',self.FolderingPathStr)
                print('')
                '''

                #Definition the call back function if not already
                if self.DirectingCallbackFunction==None:

                        #Definition a test function
                        def
test(_LiargVariablesList,_FolderPathStr,_DirKeyStrsList):
                                pass
print(_LiargVariablesList,_FolderPathStr,_DirKeyStrsList)

                        #set
                        self.DirectingCallbackFunction=test

                '''
                #Call the function
                try:
                        self.DirectingCallbackFunction(
self.DirectingLiargVariablesList,
self.FolderingPathStr,
self.FolderedDirKeyStrsList,
**_KwargVariablesDict
                                                                )
                except:
                        self.DirectingCallbackFunction(
self.DirectingLiargVariablesList,
self.FolderingPathStr,
self.FolderedDirKeyStrsList
                                                                )
                '''

                #Walk with os
                os.path.walk(
                                                self.FolderingPathStr,
                                                self.DirectingCallbackFunction,
                                                self.DirectingLiargVariablesList
                                        )

                """
                #Do it Manually

                #Call the function
                try:
                        self.DirectingCallbackFunction(
self.DirectingLiargVariablesList,
self.FolderingPathStr,
self.FolderedDirKeyStrsList,
**_KwargVariablesDict
                                                                )
                except:
                        self.DirectingCallbackFunction(
self.DirectingLiargVariablesList,
self.FolderingPathStr,
self.FolderedDirKeyStrsList
                                                                )

                #Filter the folders to walk
                DirectedFolderKeyStrsList=SYS._filter(
                                                lambda __FolderedDirKeyStr:
os.path.isdir(self.FolderingPathStr+__FolderedDirKeyStr),
                                                self.FolderedDirKeyStrsList
                        )

                #debug
                '''
                print('After first filter DirectedFolderKeyStrsList is
',DirectedFolderKeyStrsList)
                print('')
                '''

                #Filter again maybe
                if self.DirectingFilterFunctionPointer!=None:
                        DirectedFolderKeyStrsList=SYS._filter(
                                                lambda __DirectedFolderKeyStr:
self.DirectingFilterFunctionPointer(
self,__DirectedFolderKeyStr),
                                                DirectedFolderKeyStrsList
                        )

                #debug
                '''
                print('After second DirectedFolderKeyStrsList is
',DirectedFolderKeyStrsList)
                print('')
                '''

                #Map a recursive direct
                '''
                map(
                                lambda __DirectedFolderKeyStr:
                                self.__class__().direct(
self.DirectingCallbackFunction,
self.DirectingLiargVariablesList,
                                                                **{
'FolderingPathStr':
self.FolderingPathStr+__DirectedFolderKeyStr+'/'
                                                                }
                                                        ),
                                DirectedFolderKeyStrsList
                        )
                '''

                """

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Directer sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Interfacers/Directer"
target="_blank">Github</a>
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
from ShareYourSystem.Standards.Interfacers import Directer
import os

#Definition an instance
MyDirecter=Directer.DirecterClass()

#Direct for displaying folders
'''
MyDirecter.direct(
            lambda _LiargVariablesList,_FolderPathStr,_FileKeyStrsList:
            Representer._print(_LiargVariablesList[0]+_FolderPathStr),
            ["_FolderPathStr is "],
            **{'FolderingPathStr':'/'.join(SYS.__file__.split('/')[:-1])}
        )
'''

#Delete things
def delete(_LiargVariablesList,_FolderPathStr,_FileKeyStrsList):
    #os.popen('rm -r '+_FolderPathStr+'/Attests/')
    os.popen('rm '+_FolderPathStr+'/02_ClassCell.md')
    os.popen('rm '+_FolderPathStr+'/03_ClassCell.py')
    os.popen('rm '+_FolderPathStr+'/04_InstanceCell.md')
    os.popen('rm '+_FolderPathStr+'/05_InstanceCell.py')
def move(_LiargVariablesList,_FolderPathStr,_FileKeyStrsList):
    os.popen('mv '+_FolderPathStr+'/00_ExampleCell.md
'+_FolderPathStr+'/00_ExampleDoc.md')
    os.popen('mv '+_FolderPathStr+'/01_ExampleCell.py
'+_FolderPathStr+'/01_ExampleDoc.py')

MyDirecter=Directer.DirecterClass().direct(
            delete,
            [],
            **{
                'FolderingPathStr':
SYS.ShareYourSystemLocalFolderPathStr+'/ShareYourSystem/Guiders/'
            }
        )

#Definition the AttestedStr
SYS._attest(
    [
        'MyDirecter is '+SYS._str(
                MyDirecter,
                **{
                'RepresentingBaseKeyStrsListBool':False
                }
            )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyDirecter is < (DirecterClass), 4554248848>
   /{
   /  '<New><Instance>IdInt' : 4554248848
   /  '<Spe><Class>DirectingFilterFunctionPointer' : None
   /  '<Spe><Instance>DirectingCallbackFunction' : <function delete at
0x10f733c08>
   /  '<Spe><Instance>DirectingLiargVariablesList' : []
   /}

*****End of the Attest *****



```

