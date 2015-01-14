

<!--
FrozenIsBool False
-->

View the Pather sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Itemizers/Installer)




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
from ShareYourSystem.Itemizers import Pather

#Explicit expression
MyPather=Pather.PatherClass().__setitem__('MyStr','I am the parent')
MyPather.__setitem__('ChildPather',Pather.PatherClass())

#set with a deep short Str
MyPather.__setitem__(
    '/ChildPather/MyStr',
    'I am the child'
)

#set with a deep deep short Str
MyPather.__setitem__(
    '/ChildPather/GrandChildPather',
    Pather.PatherClass()
)

#set with a deep short Str
MyPather.__setitem__(
    '/OtherChildPather',
    Pather.PatherClass().__setitem__('MyInt',3)
)

#set with a deep short Str
MyPather.__setitem__(
    '/OtherChildPather',
    Pather.PatherClass().__setitem__('MyInt',4)
)

#'/' gets the self
MyPather.__setitem__(
    '/SelfPather',
    MyPather['/']
)


#Definition the AttestedStr
SYS._attest(
[
    'MyPather is '+SYS._str(
            MyPather,
            **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
            }
        ),
    'MyPather[\'/ChildPather\'] is '+SYS._str(
            MyPather['/ChildPather'],
            **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
            }
        ),
    'MyPather[\'/ChildPather/GrandChildPather\'] is '+SYS._str(
            MyPather['/ChildPather/GrandChildPather'],
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

MyPather is < (PatherClass), 4348105488>
   /{
   /  '<New><Instance>ChildPather' : < (PatherClass), 4348191824>
   /   /{
   /   /  '<New><Instance>GrandChildPather' : < (PatherClass), 4348191888>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4348191888
   /   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /   /  '<Spe><Class>PathingKeyStr' :
   /   /   /}
   /   /  '<New><Instance>IdInt' : 4348191824
   /   /  '<New><Instance>MyStr' : I am the child
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>IdInt' : 4348105488
   /  '<New><Instance>MyStr' : I am the parent
   /  '<New><Instance>OtherChildPather' : < (PatherClass), 4348192016>
   /   /{
   /   /  '<New><Instance>IdInt' : 4348192016
   /   /  '<New><Instance>MyInt' : 4
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>SelfPather' : {...}< (PatherClass), 4348105488>
   /  '<Spe><Instance>PathedChildKeyStr' : /GrandChildPather
   /  '<Spe><Instance>PathedGetKeyStr' : SelfPather
   /  '<Spe><Instance>PathedKeyStrsList' : ['', 'SelfPather']
   /  '<Spe><Instance>PathingKeyStr' : /SelfPather
   /}

------

MyPather['/ChildPather'] is < (PatherClass), 4348191824>
   /{
   /  '<New><Instance>GrandChildPather' : < (PatherClass), 4348191888>
   /   /{
   /   /  '<New><Instance>IdInt' : 4348191888
   /   /  '<Spe><Class>PathedChildKeyStr' :
   /   /  '<Spe><Class>PathedGetKeyStr' :
   /   /  '<Spe><Class>PathedKeyStrsList' : None
   /   /  '<Spe><Class>PathingKeyStr' :
   /   /}
   /  '<New><Instance>IdInt' : 4348191824
   /  '<New><Instance>MyStr' : I am the child
   /  '<Spe><Class>PathedChildKeyStr' :
   /  '<Spe><Class>PathedGetKeyStr' :
   /  '<Spe><Class>PathedKeyStrsList' : None
   /  '<Spe><Class>PathingKeyStr' :
   /}

------

MyPather['/ChildPather/GrandChildPather'] is < (PatherClass), 4348191888>
   /{
   /  '<New><Instance>IdInt' : 4348191888
   /  '<Spe><Class>PathedChildKeyStr' :
   /  '<Spe><Class>PathedGetKeyStr' :
   /  '<Spe><Class>PathedKeyStrsList' : None
   /  '<Spe><Class>PathingKeyStr' :
   /}

*****End of the Attest *****



```

