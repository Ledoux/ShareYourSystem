
#Storer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



Storer instances





<!--
FrozenIsBool False
-->

View the Storer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Noders/Installer)



```python

#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Noders import Noder,Storer

#Definition of an instance
MyStorer=Storer.StorerClass().collect(
    'Nodome',
    'First',
    Noder.NoderClass()
).collect(
    'Nodome',
    'Second',
    Noder.NoderClass()
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyStorer is '+SYS._str(
        MyStorer,
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

MyStorer is < (StorerClass), 4567894352>
   /{
   /  '<New><Instance>IdStr' : 4567894352
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>NodomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstNoder' : < (NoderClass), 4567707792>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4567707792
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StorerClass),
4567894352>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570225928>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /  'SecondNoder' : < (NoderClass), 4570220240>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4570220240
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StorerClass),
4567894352>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570225928>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /}
   /  '<Spe><Instance>StoredGetStr' : <Nodome>
   /  '<Spe><Instance>StoredSuffixStr' : Noder
   /  '<Spe><Instance>CollectingCollectionStr' : Nodome
   /  '<Spe><Instance>CollectingNodeKeyStr' : Second
   /  '<Spe><Instance>CollectingNodeVariable' : {...}< (NoderClass), 4570220240>
   /}

*****End of the Attest *****



```

