

<!--
FrozenIsBool False
-->

#Filer

##Doc
----


>
> The Filer is a quick object for opening a FiledFileVariable and safely using
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


The Filer is a quick object for opening a FiledFileVariable and safely using
(read,write)
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
                                if
self.FiledFileVariable.mode==self.FilingModeStr:
                                        return self

                                #Check
                                if self.FiledFileVariable.mode!='c':
                                        if ('w' in self.FilingModeStr and
self.FiledFileVariable.mode=='r'
                                                ) or ('r'==self.FilingModeStr
and 'w' in self.FiledFileVariable.mode):
                                                self.FiledFileVariable.close()

                        else:

                                #Close
                                self.FiledFileVariable.close()



                #Open the self.FilePointer
                if self.FilingModeStr=='r' and
os.path.isfile(self.FiledPathStr):

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
View the Filer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tre
e/master/Pythonlogy/ShareYourSystem/Interfacers/Filer)
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
from ShareYourSystem.Interfacers import Filer

#Definition of an instance Filer and make it find the current dir
MyFiler=Filer.FilerClass().file('MyFile.txt','w',
    **{
    'FolderingPathStr':
    Filer.LocalFolderPathStr
    }
)

#close
MyFiler.FiledFileVariable.close()

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

MyFiler is < (FilerClass), 4511432592>
   /{
   /  '<New><Instance>IdInt' : 4511432592
   /  '<Spe><Instance>FiledFileVariable' : <closed file '/Users/ledoux/Documents
/ShareYourSystem/Pythonlogy/ShareYourSystem/Interfacers/Filer/MyFile.txt', mode
'w' at 0x10ce740c0>
   /  '<Spe><Instance>FiledPathStr' : /Users/ledoux/Documents/ShareYourSystem/Py
thonlogy/ShareYourSystem/Interfacers/Filer/MyFile.txt
   /  '<Spe><Instance>FilingKeyStr' : MyFile.txt
   /  '<Spe><Instance>FilingModeStr' : w
   /}

*****End of the Attest *****



```

