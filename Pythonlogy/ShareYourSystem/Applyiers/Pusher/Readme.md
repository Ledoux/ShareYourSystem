
#Pusher
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



Pusher instances





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

MyPusher is < (PusherClass), 4365177616>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4365177616
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PushomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildPusher' : < (PusherClass), 4365116880>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4365116880
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NodeCollectionStr' : Pushome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildPusher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PusherClass),
4365177616>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365456624>
   /   /   /  '<Spe><Class>PushingStoreListsList' : None
   /   /   /}
   /   /  'SecondChildPusher' : < (PusherClass), 4365116240>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4365116240
   /   /   /  '<New><Instance>NodeCollectionStr' : Pushome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildPusher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (PusherClass),
4365177616>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365456624>
   /   /   /  '<Spe><Class>PushingStoreListsList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>PushingStoreListsList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : FirstChild
   /   /   /  1 : {...}< (PusherClass), 4365116880>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : SecondChild
   /   /   /  1 : {...}< (PusherClass), 4365116240>
   /   /   /]
   /   /]
   /}

*****End of the Attest *****



```

