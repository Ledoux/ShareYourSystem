

<!--
FrozenIsBool False
-->

#Loader

##Doc
----


>
> The Loader is a quick object to load from a FiledHardVariable a
LoadedReadVariable
>
>

----

<small>
View the Loader notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Loader.ipynb)
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


The Loader is a quick object to load from a FiledHardVariable a
LoadedReadVariable

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Closer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
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
'FiledHardVariable'
                                                                ]

        def default_init(self,
                                                _LoadingFormatStr='txt',
                                                _LoadedReadVariable=None,
                                                _FiledHardVariable=None,
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

                        #Read the FiledHardVariable
                        self.LoadedReadVariable=self.FiledHardVariable.read()

                elif self.LoadingFormatStr=='json':

                        #Use the json decoder
self.LoadedReadVariable=json.load(self.FiledHardVariable)

                elif self.LoadingFormatStr=='yaml':

                        #Use the json decoder
self.LoadedReadVariable=yaml.load(self.FiledHardVariable)

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Loader sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Interfacers/Loader"
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
from ShareYourSystem.Standards.Interfacers import Loader

#Definition of an instance Loader and make it find the current dir
MyLoader=Loader.LoaderClass().file('MyFile.txt','w')
MyLoader.FiledHardVariable.write('hello')
MyLoader.FiledHardVariable.close()
MyLoader.load()

#Definition the AttestedStr
SYS._attest(
    [
        'MyLoader is '+SYS._str(MyLoader,
            **{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyLoader is < (LoaderClass), 4540264912>
   /{
   /  '<New><Instance>IdInt' : 4540264912
   /  '<Spe><Class>LoadingFormatStr' : txt
   /  '<Spe><Instance>LoadedReadVariable' : hello
   /}

*****End of the Attest *****



```

