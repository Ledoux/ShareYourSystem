

<!--
FrozenIsBool False
-->

View the Producer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Applyiers/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Noder
from ShareYourSystem.Applyiers import Producer

#produce
MyProducer=Producer.ProducerClass().produce(
        ['First','Second'],
        Noder.NoderClass,
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

MyProducer is < (ProducerClass), 4550184336>
   /{
   /  '<New><Instance>IdInt' : 4550184336
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopProducer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>NodomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstNoder' : < (NoderClass), 4550226448>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550226448
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4550184336>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550019472>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /  'SecondNoder' : < (NoderClass), 4550226640>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550226640
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Nodome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondNoder
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4550184336>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550019472>
   /   /   /  '<Spe><Class>NodedCollectionIndexInt' : -1
   /   /   /  '<Spe><Class>NodedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>NodedCollectionStr' :
   /   /   /  '<Spe><Class>NodedKeyStr' :
   /   /   /  '<Spe><Class>NodingCollectionStr' :
   /   /   /}
   /   /}
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (NoderClass), 4550226448>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (NoderClass), 4550226640>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Noder.NoderClass'>
   /  '<Spe><Instance>ProducingUpdateVariable' :
   /   /{
   /   /  'MyInt' : 0
   /   /}
   /}

*****End of the Attest *****



```

