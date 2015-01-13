
#Structurer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Structurer is the last level of class that helps for building hierarchic
structures. For a certain <StructuringNodeStr> it walks to group everybody in
the hfd5.





<!--
FrozenIsBool False
-->

View the Structurer sources on [Github](https://github.com/Ledoux/ShareYourSyste
m/tree/master/ShareYourSystem/Noders/Installer)




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
from ShareYourSystem.Noders import Structurer

#Definition a "graph" structure
MyStructurer=Structurer.StructurerClass().update(
    [
        (
            '<Graph>FirstChildStructurer',
            Structurer.StructurerClass().update(
            [
                ('<Graph>GrandChildStructurer',
                Structurer.StructurerClass())
            ])
        ),
        (
            '<Graph>SecondChildStructurer',
            Structurer.StructurerClass().update(
            [
                ('<Tree>OtherGrandChildStructurer',
                Structurer.StructurerClass())
            ])
        )
    ]
).structure(['Graph','Tree']).hdfclose()

#Definition the AttestedStr
SYS._attest(
    [
        'MyStructurer is '+SYS._str(
        MyStructurer,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        ),
        'MyStructurer.hdfview().HdformatedStr is
'+MyStructurer.hdfview().HdformatedStr
    ]
)

#Print



```


```console
>>>
Doer l.132 : DoerStr is Structurer
DoStr is Structure
DoMethodStr is structure
DoingStr is Structuring
DoneStr is Structured

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

MyStructurer is < (StructurerClass), 4570208400>
   /{
   /  '<New><Instance>ApplyingIsBool' : False
   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildStructurer' : < (StructurerClass), 4570318544>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildStructurer' : < (StructurerClass), 4570317840>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdStr' : 4570317840
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Graph
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildStructurer
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(StructurerClass), 4570318544>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4570323344>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : []
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdStr' : 4570318544
   /   /   /  '<New><Instance>NodeCollectionStr' : Graph
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildStructurer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4570208400>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570323936>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : {...}< (list),
4570202408>
   /   /   /}
   /   /  'SecondChildStructurer' : < (StructurerClass), 4570210256>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdStr' : 4570210256
   /   /   /  '<New><Instance>NodeCollectionStr' : Graph
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildStructurer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4570208400>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570323936>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'OtherGrandChildStructurer' : < (StructurerClass), 4570320016>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdStr' : 4570320016
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : OtherGrandChildStructurer
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(StructurerClass), 4570210256>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4570323640>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : {...}<
(list), 4570202408>
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : {...}< (list),
4570202408>
   /   /   /}
   /   /}
   /  '<New><Instance>IdStr' : 4570208400
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>StructuringBeforeUpdateList' : []
   /  '<Spe><Instance>StructuringNodeCollectionStrsList' : ['Graph', 'Tree']
   /}

------

MyStructurer.hdfview().HdformatedStr is /                        Group
/FirstChildStructurer    Group
/FirstChildStructurer/GrandChildStructurer Group
/SecondChildStructurer   Group
/SecondChildStructurer/OtherGrandChildStructurer Group


*****End of the Attest *****



```

