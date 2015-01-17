

<!--
FrozenIsBool False
-->

#Weaver

##Doc
----


>
> A Weaver
>
>

----

<small>
View the Weaver notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Weaver.ipynb)
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


A Weaver

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Linker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class WeaverClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'WeavingInteractTuplesList'
                                                                ]

        def default_init(self,
                                _WeavingInteractTuplesList=None,
                                **_KwargVariablesDict):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_weave(self):
                """ """

                #debug
                '''
                self.debug("self.UpdatingItemVariable is
"+Representer.represent(
self.UpdatingItemVariable,**{'RepresentingAlineaIsBool':False}))
                '''

                #Apply
                self.map('interact',map(
                                                                        lambda
__WeavingInteractTuple:
{'LiargVariablesList':__WeavingInteractTuple},
self.WeavingInteractTuplesList
                                                                )
                )

                #Return
                #return self
#</DefineClass>


```

<small>
View the Weaver sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Applyiers/Weaver"
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
from ShareYourSystem.Itemizers import Pointer
from ShareYourSystem.Applyiers import Weaver

#Update several things
MyWeaver=Weaver.WeaverClass().update(
    map(
            lambda __Int:
            (
                str(__Int)+'Pointer',
                Pointer.PointerClass()
            ),
            xrange(3)
        )
).weave(
        map(
                lambda __Int:
                (
                    [
                        str(__Int)+'Pointer',
                        str(__Int-1)+'Pointer',
                    ],
                    str(__Int)+'-'+str(__Int-1)+'Pointer',
                    Pointer.PointerClass()
                )
                if __Int>0
                else
                (
                    [
                        str(0)+'Pointer',
                        str(2)+'Pointer',
                    ],
                    str(0)+'-'+str(2)+'Pointer',
                    Pointer.PointerClass()
                ),
                xrange(3)
            )
        )

#Definition the AttestedStr
SYS._attest(
    [
        'MyWeaver is '+SYS._str(
        MyWeaver,
        **{
            'RepresentingBaseKeyStrsListBool':False,
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

MyWeaver is < (WeaverClass), 4554324496>
   /{
   /  '<New><Instance>0Pointer' : < (PointerClass), 4554325712>
   /   /{
   /   /  '<New><Instance>IdInt' : 4554325712
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>1Pointer' : < (PointerClass), 4554325776>
   /   /{
   /   /  '<New><Instance>IdInt' : 4554325776
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>2Pointer' : < (PointerClass), 4554325840>
   /   /{
   /   /  '<New><Instance>IdInt' : 4554325840
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>IdInt' : 4554324496
   /  '<Spe><Instance>WeavingInteractTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : ['0Pointer', '2Pointer']
   /   /   /  1 : 0-2Pointer
   /   /   /  2 : < (PointerClass), 4554325904>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4554325904
   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /   /   /}
   /   /   /)
   /   /  1 :
   /   /   /(
   /   /   /  0 : ['1Pointer', '0Pointer']
   /   /   /  1 : 1-0Pointer
   /   /   /  2 : < (PointerClass), 4554325968>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4554325968
   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /   /   /}
   /   /   /)
   /   /  2 :
   /   /   /(
   /   /   /  0 : ['2Pointer', '1Pointer']
   /   /   /  1 : 2-1Pointer
   /   /   /  2 : < (PointerClass), 4555337808>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4555337808
   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /   /   /}
   /   /   /)
   /   /]
   /}

*****End of the Attest *****



```

