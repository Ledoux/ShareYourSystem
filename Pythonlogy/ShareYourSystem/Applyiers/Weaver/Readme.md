

<!--
FrozenIsBool False
-->

View the Weaver sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Applyiers/Installer)




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

MyWeaver is < (WeaverClass), 4549774928>
   /{
   /  '<New><Instance>0Pointer' : < (PointerClass), 4549919504>
   /   /{
   /   /  '<New><Instance>IdInt' : 4549919504
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>1Pointer' : < (PointerClass), 4549919568>
   /   /{
   /   /  '<New><Instance>IdInt' : 4549919568
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>2Pointer' : < (PointerClass), 4549919632>
   /   /{
   /   /  '<New><Instance>IdInt' : 4549919632
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>IdInt' : 4549774928
   /  '<Spe><Instance>WeavingInteractTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : ['0Pointer', '2Pointer']
   /   /   /  1 : 0-2Pointer
   /   /   /  2 : < (PointerClass), 4549919696>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4549919696
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
   /   /   /  2 : < (PointerClass), 4549919824>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4549919824
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
   /   /   /  2 : < (PointerClass), 4549919760>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4549919760
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

