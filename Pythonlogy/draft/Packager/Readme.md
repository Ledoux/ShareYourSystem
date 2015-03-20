

<!--
FrozenIsBool False
-->

#Packager

##Doc
----


>
> The Packager is an Object that helps to get a module in the SYS framework
>
>

----

<small>
View the Packager notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Packager.ipynb)
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


The Packager is an Object that helps to get a module in the SYS framework

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Folderer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
import importlib
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class PackagerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'PackagingModuleVariable',
'PackagedModuleStr',
'PackagedModuleVariable',
'PackagedInstallFolderPathStr',
'PackagedLocalFolderPathStr'
                                                        ]

        def default_init(self,
                                                _PackagingModuleVariable=None,
                                                _PackagedModuleStr="",
                                                _PackagedModuleVariable=None,
_PackagedInstallFolderPathStr="",
                                                _PackagedLocalFolderPathStr="",
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_package(self):

                #debug
                '''
                self.debug(('self.',self,
                                                [
'PackagingModuleVariable'
                                                ]))
                '''

                #Check
                if type(self.PackagingModuleVariable) in SYS.StrTypesList:
                        self.PackagedModuleStr=self.PackagingModuleVariable
                else:
                        self.PackagedModuleVariable=self.PackagingModuleVariable
self.PackagedModuleStr=self.PackagingModuleVariable.__name__

                #Check for a module
                if self.PackagedModuleVariable==None or
self.PackagedModuleStr!=self.PackagedModuleVariable.__name__:

                        #Check
                        if self.PackagedModuleStr!="":

                                #Import the module if not already
                                if self.PackagedModuleStr not in sys.modules:
importlib.import_module(self.PackagedModuleStr)

                                #set with sys
self.PackagedModuleVariable=sys.modules[self.PackagedModuleStr]

                #set
                if self.PackagedModuleVariable!=None:

                        #set
                        self.PackagedInstallFolderPathStr='/'.join(
self.PackagedModuleVariable.__file__.split('/')[:-1]
                        )+'/'

                        #set
                        self.PackagedLocalFolderPathStr=SYS.PythonlogyLocalFolde
rPathStr+self.PackagedModuleVariable.__name__.replace(
                                '.','/')+'/'

                        #debug
                        '''
                        self.debug(('self.',self,[
                                'PackagedInstallFolderPathStr',
                                'PackagedLocalFolderPathStr'
                                ]))
                        '''

                        #Hook
                        self.folder(self.PackagedLocalFolderPathStr)

                #Return
                #return self

#</DefineClass>


```

<small>
View the Packager sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Objects/Packager"
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
from ShareYourSystem.Standards.Objects import Packager

#Definition of a Packager instance and module
MyPackager=Packager.PackagerClass().package(
    'ShareYourSystem.Standards.Interfacers.Printer'
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyPackager'+SYS._str(MyPackager)
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyPackager< (PackagerClass), 4537117456>
   /{
   /  '<New><Instance>IdInt' : 4537117456
   /  '<Spe><Instance>PackagedInstallFolderPathStr' : /usr/local/lib/python2.7
/site-packages/ShareYourSystem/Objects/Printer/
   /  '<Spe><Instance>PackagedLocalFolderPathStr' : /Users/ledoux/Documents/Shar
eYourSystem/Pythonlogy/ShareYourSystem/Objects/Printer/
   /  '<Spe><Instance>PackagedModuleStr' : ShareYourSystem.Standards.Interfacers.Printer
   /  '<Spe><Instance>PackagedModuleVariable' : <module
'ShareYourSystem.Standards.Interfacers.Printer' from '/usr/local/lib/python2.7/site-
packages/ShareYourSystem/Objects/Printer/__init__.pyc'>
   /  '<Spe><Instance>PackagingModuleVariable' : ShareYourSystem.Standards.Interfacers.Printer
   /}

*****End of the Attest *****



```

