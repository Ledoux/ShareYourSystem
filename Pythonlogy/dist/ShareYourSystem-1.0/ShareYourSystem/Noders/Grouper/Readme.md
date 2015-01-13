
#Grouper
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Grouper establishes a group of parenting nodes for which each level is setted
in equivalent hdf5 structure.





<!--
FrozenIsBool False
-->

View the Grouper sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
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
from ShareYourSystem.Noders import Grouper

#Definition a structure of Grouper
MyGrouper=Grouper.GrouperClass().hdformat().update(
    [
        (
            '<Tree>FirstChildGrouper',
            Grouper.GrouperClass().update(
                [
                    ('<Tree>GrandChildGrouper',
                    Grouper.GrouperClass())
                ]
            )
        ),
        (
            '<Tree>SecondChildGrouper',
            Grouper.GrouperClass()
        )
    ]
)

#Walk to set the same structure in the hdf5
MyGrouper.walk(
        {
                'BeforeUpdateList':
                [
                    ('parent',{'LiargVariablesList':['Tree']}),
                    ('group',{'LiargVariablesList':[]})
                ],
                'GatherVariablesList':['<Tree>']
        }
).hdfclose()

#Definition the AttestedStr
SYS._attest(
    [
        'MyGrouper is '+SYS._str(
        MyGrouper,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
            }
        ),
        'MyGrouper.hdfview().HdformatedStr is
'+MyGrouper.hdfview().HdformatedStr
    ]
)

#Print



```


```console
>>>
Doer l.132 : DoerStr is Networker
DoStr is Network
DoMethodStr is network
DoingStr is Networking
DoneStr is Networked

Doer l.132 : DoerStr is Grouper
DoStr is Group
DoMethodStr is group
DoingStr is Grouping
DoneStr is Grouped

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

MyGrouper is < (GrouperClass), 4556363600>
   /{
   /  '<New><Instance>ApplyingIsBool' : False
   /  '<New><Instance>IdStr' : 4556363600
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildGrouper' : < (GrouperClass), 4567709584>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /  '<New><Instance>IdStr' : 4567709584
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildGrouper
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (GrouperClass),
4556363600>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4567798432>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildGrouper' : < (GrouperClass), 4567771792>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /   /   /  '<New><Instance>IdStr' : 4567771792
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildGrouper
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(GrouperClass), 4567709584>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4567798136>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>GroupedInt' : -1
   /   /   /   /   /  '<Spe><Class>GroupedKeyStr' :
   /   /   /   /   /  '<Spe><Class>GroupedParentVariable' : None
   /   /   /   /   /  '<Spe><Instance>GroupedDeriveParentersList' : []
   /   /   /   /   /  '<Spe><Instance>GroupedPathStr' :
/FirstChildGrouper/GrandChildGrouper
   /   /   /   /   /  '<Spe><Instance>GroupedPathStrsList' : []
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>GroupedInt' : -1
   /   /   /  '<Spe><Class>GroupedKeyStr' :
   /   /   /  '<Spe><Class>GroupedParentVariable' : None
   /   /   /  '<Spe><Instance>GroupedDeriveParentersList' : []
   /   /   /  '<Spe><Instance>GroupedPathStr' : /FirstChildGrouper
   /   /   /  '<Spe><Instance>GroupedPathStrsList' : []
   /   /   /}
   /   /  'SecondChildGrouper' : < (GrouperClass), 4567772752>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /  '<New><Instance>IdStr' : 4567772752
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildGrouper
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (GrouperClass),
4556363600>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4567798432>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>GroupedInt' : -1
   /   /   /  '<Spe><Class>GroupedKeyStr' :
   /   /   /  '<Spe><Class>GroupedParentVariable' : None
   /   /   /  '<Spe><Instance>GroupedDeriveParentersList' : []
   /   /   /  '<Spe><Instance>GroupedPathStr' : /SecondChildGrouper
   /   /   /  '<Spe><Instance>GroupedPathStrsList' : []
   /   /   /}
   /   /}
   /  '<Spe><Class>GroupedInt' : -1
   /  '<Spe><Class>GroupedKeyStr' :
   /  '<Spe><Class>GroupedParentVariable' : None
   /  '<Spe><Instance>GroupedDeriveParentersList' : []
   /  '<Spe><Instance>GroupedPathStr' : /
   /  '<Spe><Instance>GroupedPathStrsList' : []
   /}

------

MyGrouper.hdfview().HdformatedStr is /                        Group
/FirstChildGrouper       Group
/FirstChildGrouper/GrandChildGrouper Group
/SecondChildGrouper      Group


*****End of the Attest *****



```

