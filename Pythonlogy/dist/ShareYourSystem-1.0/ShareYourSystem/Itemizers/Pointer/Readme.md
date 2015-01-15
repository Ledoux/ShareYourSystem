

<!--
FrozenIsBool False
-->

View the Pointer sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Itemizers/Installer)




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
from ShareYourSystem.Itemizers import Pather,Pointer

#Explicit expression
MyPointer=Pointer.PointerClass().__setitem__(
        'ChildPather',
        Pather.PatherClass().__setitem__(
            'GrandChildPather',
            Pather.PatherClass()
        )
    ).point(
            '/',
            '/ChildPather/GrandChildPather/GrandParentPointer'
    )

#Return
SYS._attest(
    [
    'MyPointer is '+SYS._str(
            MyPointer,
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

MyPointer is < (PointerClass), 4348453840>
   /{
   /  '<New><Instance>ChildPather' : < (PatherClass), 4348481808>
   /   /{
   /   /  '<New><Instance>GrandChildPather' : < (PatherClass), 4348481872>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4348481872
   /   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /   /  '<Spe><Class>PathingKeyStr' :
   /   /   /}
   /   /  '<New><Instance>GrandChildPather/GrandParentPointer' : {...}<
(PointerClass), 4348453840>
   /   /  '<New><Instance>IdInt' : 4348481808
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>IdInt' : 4348453840
   /  '<Spe><Class>PointedBackSetStr' :
   /  '<Spe><Class>PointedPathBackVariable' :
   /  '<Spe><Class>PointingBackSetStr' :
   /  '<Spe><Instance>PointedGetVariable' : {...}< (PointerClass), 4348453840>
   /  '<Spe><Instance>PointedLocalSetStr' : GrandParentPointer
   /  '<Spe><Instance>PointingGetVariable' : /
   /  '<Spe><Instance>PointingSetPathStr' :
/ChildPather/GrandChildPather/GrandParentPointer
   /}

*****End of the Attest *****



```

