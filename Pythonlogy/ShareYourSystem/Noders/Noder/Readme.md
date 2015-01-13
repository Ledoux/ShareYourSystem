
#Noder
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Noder defines Child ordered dicts with <DoStr> as KeyStr. The items inside are
automatically setted with Noded<DoStr><TypeStr> and have a Pointer to the parent
InstanceVariable. This is the beginning for buiding high arborescent and
(possibly circular) structures of objects.





<!--
FrozenIsBool False
-->

View the Noder sources on [Github](https://github.com/Ledoux/ShareYourSystem/tre
e/master/ShareYourSystem/Noders/Installer)




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
from ShareYourSystem.Noders import Noder

#Definition of a Noder instance
MyNoder=Noder.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Nodome>FirstChildNoder']=Noder.NoderClass()

#Short expression for setting in the appended manner a structured object
MyNoder['<Nodome>SecondChildNoder']=Noder.NoderClass()

#Definition the AttestedStr
SYS._attest(
    [
        'MyNoder is '+SYS._str(
                MyNoder,
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

MyNoder is < (NoderClass), 4567892624>
   /{
   /  '<New><Instance>IdStr' : 4567892624
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>NodomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildNoder' : < (NoderClass), 4567894672>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4567894672
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (NoderClass),
4567892624>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570170608>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /  'SecondChildNoder' : < (NoderClass), 4567895504>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4567895504
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (NoderClass),
4567892624>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570170608>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /}
   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /  '<Spe><Class>NodedCollectionStr' :
   /  '<Spe><Class>NodedKeyStr' :
   /  '<Spe><Instance>NodedCollectionOrderedDict' : {...}< (OrderedDict),
4570170608>
   /  '<Spe><Instance>NodingCollectionStr' : Nodome
   /}

*****End of the Attest *****



```

