

<!--
FrozenIsBool False
-->

#Writer

##Doc
----


>
> The Writer is a quick object to write from a LoadedReadVariable.
>
>

----

<small>
View the Writer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Writer.ipynb)
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


The Writer is a quick object to write from a LoadedReadVariable.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Interfacers.Loader"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
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
'FiledFileVariable',
'FolderingPathStr',
'LoadingFormatStr',
'WritingStoreVariable'
                                                                ]))
                '''

                #Check
                if self.LoadingFormatStr=='txt':

                        #Read the FiledFileVariable
                        self.FiledFileVariable.write(self.WritingStoreVariable)

                elif self.LoadingFormatStr=='json':

                        #debug
                        '''
                        self.debug(
                                                [
                                                        'we write in json...',
'json.dumps(self.WritingStoreVariable,indent=2) is
'+str(json.dumps(self.WritingStoreVariable,indent=2))
                                                ]
                                )
                        '''

                        #Use the json decoder
                        self.FiledFileVariable.write(
                                json.dumps(self.WritingStoreVariable,indent=2)
                        )

                elif self.LoadingFormatStr=='yaml':

                        #debug
                        '''
                        print('We yamelized !')
                        print('self.FiledFileVariable is
',self.FiledFileVariable)
                        print('self.WritingStoreVariable is
',self.WritingStoreVariable)
                        print('')
                        '''

                        #Use the json decoder
                        self.FiledFileVariable.write(
                                yaml.dump(self.WritingStoreVariable,indent=2)
                        )

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Writer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Interfacers/Writer)
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
from ShareYourSystem.Interfacers import Writer

#Definition of an instance Writer and make it find the current dir
MyWriter=Writer.WriterClass().write("hello",**{
    'FolderingPathStr':Writer.LocalFolderPathStr,
    'FilingKeyStr':'MyFile.txt',
    'FilingModeStr':'w'
    }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyWriter is '+SYS._str(MyWriter)
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyWriter is < (WriterClass), 4391205328>
   /{
   /  '<New><Instance>IdInt' : 4391205328
   /  '<Spe><Class>WritingLoadBool' : False
   /  '<Spe><Instance>WritingStoreVariable' : hello
   /}

*****End of the Attest *****



```

