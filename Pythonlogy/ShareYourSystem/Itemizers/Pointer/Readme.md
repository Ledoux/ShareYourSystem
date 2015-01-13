
#Pointer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Pointer





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
Doer l.132 : DoerStr is Pointer
DoStr is Point
DoMethodStr is point
DoingStr is Pointing
DoneStr is Pointed



*****Start of the Attest *****

MyPointer is < (PointerClass), 4465425168>
   /{
   /  '<New><Instance>ChildPather' : < (PatherClass), 4465287632>
   /   /{
   /   /  '<New><Instance>GrandChildPather' : < (PatherClass), 4465476176>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4465476176
   /   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /   /  '<Spe><Class>PathingKeyStr' :
   /   /   /}
   /   /  '<New><Instance>GrandChildPather/GrandParentPointer' : {...}<
(PointerClass), 4465425168>
   /   /  '<New><Instance>IdString' : 4465287632
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>IdString' : 4465425168
   /  '<Spe><Class>PointedBackSetStr' :
   /  '<Spe><Class>PointedPathBackVariable' :
   /  '<Spe><Class>PointingBackSetKeyStr' :
   /  '<Spe><Instance>PointedGetVariable' : {...}< (PointerClass), 4465425168>
   /  '<Spe><Instance>PointedLocalSetStr' : GrandParentPointer
   /  '<Spe><Instance>PointingGetVariable' : /
   /  '<Spe><Instance>PointingSetPathStr' :
/ChildPather/GrandChildPather/GrandParentPointer
   /}

*****End of the Attest *****



```

