
#Settler
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Settler





<!--
FrozenIsBool False
-->

View the Settler sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Noders/Installer)




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
from ShareYourSystem.Noders import Settler

#Short expression and set in the appended manner
MySettler=Settler.SettlerClass().__setitem__(
    '<Settlome>ChildSettler',
    Settler.SettlerClass()
).update(
    [
        (
            '<Settlome>GrandFirstChildSettler',
            Settler.SettlerClass()
        ),
        (
            '<Settlome>GrandSecondChildSettler',
            Settler.SettlerClass(**{
                'SettlingParentBool':True,
                'SettlingLinkBool':True
                }
                ).__setitem__(
                'LinkingPointListsList',
                [
        ('/NodePointDeriveNoder/<Settlome>GrandFirstChildSettler','GrandFirstChi
ldSettler')
                ]
            )
        )
    ]
)



#Definition the AttestedStr
SYS._attest(
    [
        'MySettler is '+SYS._str(
        MySettler,
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
Doer l.132 : DoerStr is Linker
DoStr is Link
DoMethodStr is link
DoingStr is Linking
DoneStr is Linked

Doer l.132 : DoerStr is Settler
DoStr is Settle
DoMethodStr is settle
DoingStr is Settling
DoneStr is Settled

l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_settle', 'WatchDoBoolKeyStr':
'WatchSettleWithSettlerBool', 'BindDoClassStr': 'SettlerClass'}

l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_settle', 'WatchDoBoolKeyStr':
'WatchSettleWithSettlerBool', 'BindDoClassStr': 'SettlerClass'}

l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_settle', 'WatchDoBoolKeyStr':
'WatchSettleWithSettlerBool', 'BindDoClassStr': 'SettlerClass'}

l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_settle', 'WatchDoBoolKeyStr':
'WatchSettleWithSettlerBool', 'BindDoClassStr': 'SettlerClass'}

l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_settle', 'WatchDoBoolKeyStr':
'WatchSettleWithSettlerBool', 'BindDoClassStr': 'SettlerClass'}

l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_parent', 'WatchDoBoolKeyStr':
'WatchParentWithParenterBool', 'BindDoClassStr': 'ParenterClass'}

l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_parent', 'WatchDoBoolKeyStr':
'WatchParentWithParenterBool', 'BindDoClassStr': 'ParenterClass'}



*****Start of the Attest *****

MySettler is < (SettlerClass), 4570209680>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdStr' : 4570209680
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>SettlomeCollectionOrderedDict' :
   /   /{
   /   /  'ChildSettler' : < (SettlerClass), 4570209232>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4570209232
   /   /   /  '<New><Instance>NodeCollectionStr' : Settlome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ChildSettler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (SettlerClass),
4570209680>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570225632>
   /   /   /  '<Spe><Class>SettlingLinkBool' : False
   /   /   /  '<Spe><Class>SettlingParentBool' : False
   /   /   /}
   /   /  'GrandFirstChildSettler' : < (SettlerClass), 4567895056>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4567895056
   /   /   /  '<New><Instance>NodeCollectionStr' : Settlome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : GrandFirstChildSettler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (SettlerClass),
4570209680>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570225632>
   /   /   /  '<Spe><Class>SettlingLinkBool' : False
   /   /   /  '<Spe><Class>SettlingParentBool' : False
   /   /   /}
   /   /  'GrandSecondChildSettler' : < (SettlerClass), 4570208016>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>GrandFirstChildSettler' : {...}< (SettlerClass),
4567895056>
   /   /   /  '<New><Instance>IdStr' : 4570208016
   /   /   /  '<New><Instance>NodeCollectionStr' : Settlome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : GrandSecondChildSettler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (SettlerClass),
4570209680>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570225632>
   /   /   /  '<Spe><Instance>SettlingLinkBool' : True
   /   /   /  '<Spe><Instance>SettlingParentBool' : True
   /   /   /}
   /   /}
   /  '<Spe><Class>SettlingLinkBool' : False
   /  '<Spe><Class>SettlingParentBool' : False
   /}

*****End of the Attest *****



```

