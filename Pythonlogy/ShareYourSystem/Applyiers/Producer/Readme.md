
#Producer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



Producer instances





<!--
FrozenIsBool False
-->

View the Producer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Applyiers/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Storer
from ShareYourSystem.Applyiers import Producer

#produce
MyProducer=Producer.ProducerClass().produce(
        ['First','Second'],
        Storer.StorerClass,
        {'MyInt':0},
        **{'CollectingCollectionStr':'Nodome'}
    )

#Definition the AttestedStr
SYS._attest(
    [
        'MyProducer is '+SYS._str(
        MyProducer,
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

MyProducer is < (ProducerClass), 4365385552>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4365385552
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>NodomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstStorer' : < (StorerClass), 4364535504>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4364535504
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstStorer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4365385552>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365152336>
   /   /   /  '<Spe><Class>StoredGetStr' :
   /   /   /  '<Spe><Class>StoredSuffixStr' :
   /   /   /  '<Spe><Class>CollectingCollectionStr' :
   /   /   /  '<Spe><Class>CollectingNodeKeyStr' :
   /   /   /  '<Spe><Class>CollectingNodeVariable' : None
   /   /   /}
   /   /  'SecondStorer' : < (StorerClass), 4364535440>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4364535440
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondStorer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4365385552>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365152336>
   /   /   /  '<Spe><Class>StoredGetStr' :
   /   /   /  '<Spe><Class>StoredSuffixStr' :
   /   /   /  '<Spe><Class>CollectingCollectionStr' :
   /   /   /  '<Spe><Class>CollectingNodeKeyStr' :
   /   /   /  '<Spe><Class>CollectingNodeVariable' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (StorerClass), 4364535504>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (StorerClass), 4364535440>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingInitiateDict' :
   /   /{
   /   /  'MyInt' : 0
   /   /}
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Storer.StorerClass'>
   /}

*****End of the Attest *****



```

