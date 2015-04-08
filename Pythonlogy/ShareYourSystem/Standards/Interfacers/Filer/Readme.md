

<!--
FrozenIsBool False
-->

#Filer

##Doc
----


>
> The Filer is a quick object for opening a FiledHardVariable and safely using
(read,write)
> it depending on the FiledModeStr.
>
>

----

<small>
View the Filer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyours
ystem.ouvaton.org/Filer.ipynb)
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


The Filer is a quick object for opening a FiledHardVariable and safely using
(read,write)
it depending on the FiledModeStr.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Objects.Packager"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
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
'FiledHardVariable'
                                                        ]


        def default_init(self,
                                                _FilingKeyStr="",
                                                _FilingModeStr='r',
                                                _FiledPathStr="",
                                                _FiledHardVariable=None,
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
                self.debug(('self.',self,['FolderingPathVariable']))
                '''

                #set the FiledPathStr
                if self.FolderingPathVariable[-1]!='/':
                        self.FolderingPathVariable=self.FolderingPathVariable+'/'
                self.FiledPathStr=self.FolderingPathVariable+self.FilingKeyStr

                #debug
                '''
self.debug(('self.',self,['FilingKeyStr','FiledPathStr','FilingModeStr']))
                '''

                #Close before if we chaneg the mode
                if self.FiledHardVariable!=None:

                        #Check
                        if self.FiledHardVariable==self.FiledPathStr:

                                #Return if it is the same mode already
                                if
self.FiledHardVariable.mode==self.FilingModeStr:
                                        return self

                                #Check
                                if self.FiledHardVariable.mode!='c':
                                        if ('w' in self.FilingModeStr and
self.FiledHardVariable.mode=='r'
                                                ) or ('r'==self.FilingModeStr
and 'w' in self.FiledHardVariable.mode):
                                                self.FiledHardVariable.close()

                        else:

                                #Close
                                self.FiledHardVariable.close()



                #Open the self.FilePointer
                if self.FilingModeStr=='r' and
os.path.isfile(self.FiledPathStr):

                        #debug
                        '''
                        self.debug('Open the file for reading !')
                        '''

                        #Open
self.FiledHardVariable=open(self.FiledPathStr,self.FilingModeStr)

                else:

                        #debug
                        '''
                        self.debug('Open the file for writing !')
                        '''

                        #Open
self.FiledHardVariable=open(self.FiledPathStr,self.FilingModeStr)

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Filer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tre
e/master/Pythonlogy/ShareYourSystem/Interfacers/Filer"
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
from ShareYourSystem.Standards.Interfacers import Filer

#Definition of an instance Filer and make it find the current dir
MyFiler=Filer.FilerClass().file('MyFile.txt','w',
    **{
    'FolderingPathVariable':
    Filer.LocalFolderPathStr
    }
)

#close
MyFiler.FiledHardVariable.close()

#Definition the AttestedStr
SYS._attest(
    [
        'MyFiler is '+SYS._str(MyFiler,
        **{'RepresentingAlineaIsBool':False})
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyFiler is < (FilerClass), 4540265936>
   /{
   /  '<New><Instance>IdInt' : 4540265936
   /  '<Spe><Instance>FiledHardVariable' : <closed file '/Users/ledoux/Documents
/ShareYourSystem/Pythonlogy/ShareYourSystem/Interfacers/Filer/MyFile.txt', mode
'w' at 0x10e66bed0>
   /  '<Spe><Instance>FiledPathStr' : /Users/ledoux/Documents/ShareYourSystem/Py
thonlogy/ShareYourSystem/Interfacers/Filer/MyFile.txt
   /  '<Spe><Instance>FilingKeyStr' : MyFile.txt
   /  '<Spe><Instance>FilingModeStr' : w
   /}

*****End of the Attest *****



```

