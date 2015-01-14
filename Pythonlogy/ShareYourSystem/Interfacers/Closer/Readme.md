

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
BaseModuleStr="ShareYourSystem.Interfacers.Filer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
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
View the Closer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Interfacers/Closer)
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
from ShareYourSystem.Interfacers import Closer

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

MyCloser is < (CloserClass), 4391203408>
   /{
   /  '<New><Instance>IdInt' : 4391203408
   /}

*****End of the Attest *****



```

