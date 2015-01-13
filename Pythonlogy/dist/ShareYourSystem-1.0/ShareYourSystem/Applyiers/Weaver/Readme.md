
#Weaver
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Weaver





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
Doer l.132 : DoerStr is Weaver
DoStr is Weave
DoMethodStr is weave
DoingStr is Weaving
DoneStr is Weaved



*****Start of the Attest *****

MyWeaver is < (WeaverClass), 4365118928>
   /{
   /  '<New><Instance>0Pointer' : < (PointerClass), 4365085328>
   /   /{
   /   /  '<New><Instance>IdString' : 4365085328
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>1Pointer' : < (PointerClass), 4365485648>
   /   /{
   /   /  '<New><Instance>IdString' : 4365485648
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>2Pointer' : < (PointerClass), 4365488016>
   /   /{
   /   /  '<New><Instance>IdString' : 4365488016
   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /}
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4365118928
   /  '<Spe><Instance>WeavingInteractTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : ['0Pointer', '2Pointer']
   /   /   /  1 : 0-2Pointer
   /   /   /  2 : < (PointerClass), 4364535632>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdString' : 4364535632
   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /   /   /}
   /   /   /)
   /   /  1 :
   /   /   /(
   /   /   /  0 : ['1Pointer', '0Pointer']
   /   /   /  1 : 1-0Pointer
   /   /   /  2 : < (PointerClass), 4365115472>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdString' : 4365115472
   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /   /   /}
   /   /   /)
   /   /  2 :
   /   /   /(
   /   /   /  0 : ['2Pointer', '1Pointer']
   /   /   /  1 : 2-1Pointer
   /   /   /  2 : < (PointerClass), 4365492880>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdString' : 4365492880
   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /  '<Spe><Class>PointedGetVariable' : None
   /   /   /   /  '<Spe><Class>PointedLocalSetStr' :
   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /   /  '<Spe><Class>PointingGetVariable' : None
   /   /   /   /  '<Spe><Class>PointingSetPathStr' :
   /   /   /   /}
   /   /   /)
   /   /]
   /}

*****End of the Attest *****



```

