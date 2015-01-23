

<!--
FrozenIsBool False
-->

#Closer

##Doc
----


>
> The Closer
>

----

<small>
View the Closer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Closer.ipynb)
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


The Closer
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Interfacers.Filer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineDoStrsList>
DoStrsList=["Closer","Close","Closing","Closed"]
#<DefineDoStrsList>

#<DefineClass>
@DecorationClass()
class CloserClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                                                                ]

        def default_init(self,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_close(self):

                #close
                self.FiledFileVariable.close()

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Closer sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Interfacers/Closer"
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
from ShareYourSystem.Standards.Interfacers import Closer

#Definition of an instance Closer and make it find the current dir
MyCloser=Closer.CloserClass().file('MyFile.txt','w').close()

#Definition the AttestedStr
SYS._attest(
    [
        'MyCloser is '+SYS._str(
            MyCloser,
            **{
                'RepresentingAlineaIsBool':False
            }
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyCloser is < (CloserClass), 4540266064>
   /{
   /  '<New><Instance>IdInt' : 4540266064
   /}

*****End of the Attest *****



```

