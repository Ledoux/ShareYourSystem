

<!--
FrozenIsBool False
-->

View the Pusher sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Applyiers/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Pusher

#push
MyPusher=Pusher.PusherClass().push(
    [
        [
            'FirstChild',
            Pusher.PusherClass().__setitem__('MyInt',0)
        ],
        [
            'SecondChild',
            Pusher.PusherClass()
        ]
    ],
    **{'CollectingCollectionStr':'Pushome'}
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyPusher is '+SYS._str(
        MyPusher,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        )
    ]
)



```


```console
>>>


*****Start of the Attest *****

MyPusher is < (PusherClass), 4549922128>
   /{
   /  '<New><Instance>IdInt' : 4549922128
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopPusher
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PushomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildPusher' : < (PusherClass), 4550182608>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550182608
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Pushome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildPusher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PusherClass),
4549922128>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550146744>
   /   /   /  '<Spe><Class>PushingStoreListsList' : None
   /   /   /}
   /   /  'SecondChildPusher' : < (PusherClass), 4550182736>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550182736
   /   /   /  '<New><Instance>NodeCollectionStr' : Pushome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildPusher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PusherClass),
4549922128>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550146744>
   /   /   /  '<Spe><Class>PushingStoreListsList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>PushingStoreListsList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : FirstChild
   /   /   /  1 : {...}< (PusherClass), 4550182608>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : SecondChild
   /   /   /  1 : {...}< (PusherClass), 4550182736>
   /   /   /]
   /   /]
   /}

*****End of the Attest *****



```

