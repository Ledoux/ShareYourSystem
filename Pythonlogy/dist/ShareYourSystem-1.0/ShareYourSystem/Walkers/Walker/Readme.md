
#Walker
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Parenter completes the list of grand-parent nodes that a child node could
have. It is a recursive top-down set of the pointers and the pathStrs.





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
from ShareYourSystem.Walkers import Walker

#Definition a Walker instance with a noded tree
MyWalker=Walker.WalkerClass().update(
    [
        (
            '<Tree>FirstChildWalker',
            Walker.WalkerClass().update(
                [
                    (
                        '<Tree>GrandChildWalker',
                        Walker.WalkerClass()
                    )
                ]
            )
        ),
        (
            '<Tree>SecondChildWalker',
            Walker.WalkerClass()
        )
    ]
)

#Walk inside the Tree in order to parent again because the tree was not yet
completely setted when it was done
MyWalker.walk(
            {
                'BeforeUpdateList':
                [
                    ('SwitchingParentBool',False),
                    ('parent',{'LiargVariablesList':['Tree']})
                ],
                'GatherVariablesList':['<Tree>']
            }
        )


#Definition the AttestedStr
SYS._attest(
    [
        'MyWalker is '+SYS._str(
        MyWalker,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':['ParentedDeriveParentersList']
        }
        )
    ]
)

#Print



```


```console
>>>
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

MyWalker is < (WalkerClass), 4559108688>
   /{
   /  '<New><Instance>ApplyingIsBool' : False
   /  '<New><Instance>IdString' : 4559108688
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>SwitchingParentBool' : False
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildWalker' : < (WalkerClass), 4559108560>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /  '<New><Instance>IdString' : 4559108560
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildWalker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (WalkerClass),
4559108688>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559207096>
   /   /   /  '<New><Instance>SwitchingParentBool' : False
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildWalker' : < (WalkerClass), 4559108496>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /   /   /  '<New><Instance>IdString' : 4559108496
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildWalker
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(WalkerClass), 4559108560>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559206800>
   /   /   /   /   /  '<New><Instance>SwitchingParentBool' : False
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /   /   /[
   /   /   /   /   /   /  0 : {...}< (WalkerClass), 4559108560>
   /   /   /   /   /   /  1 : {...}< (WalkerClass), 4559108688>
   /   /   /   /   /   /]
   /   /   /   /   /  '<Spe><Instance>WalkingSocketDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /  'BeforeUpdateList' :
   /   /   /   /   /   /   /[
   /   /   /   /   /   /   /  0 :
   /   /   /   /   /   /   /   /(
   /   /   /   /   /   /   /   /  0 : SwitchingParentBool
   /   /   /   /   /   /   /   /  1 : False
   /   /   /   /   /   /   /   /)
   /   /   /   /   /   /   /  1 :
   /   /   /   /   /   /   /   /(
   /   /   /   /   /   /   /   /  0 : parent
   /   /   /   /   /   /   /   /  1 :
   /   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /   /  'LiargVariablesList' : ['Tree']
   /   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /   /)
   /   /   /   /   /   /   /]
   /   /   /   /   /   /  'GatherVariablesList' : ['<Tree>']
   /   /   /   /   /   /  'IdStr' : 4559267272
   /   /   /   /   /   /  'TopVariable' : {...}< (WalkerClass), 4559108688>
   /   /   /   /   /   /}
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (WalkerClass), 4559108688>
   /   /   /   /]
   /   /   /  '<Spe><Instance>WalkingSocketDict' : {...}< (dict), 4559267272>
   /   /   /}
   /   /  'SecondChildWalker' : < (WalkerClass), 4559108752>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : False
   /   /   /  '<New><Instance>IdString' : 4559108752
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildWalker
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (WalkerClass),
4559108688>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559207096>
   /   /   /  '<New><Instance>SwitchingParentBool' : False
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (WalkerClass), 4559108688>
   /   /   /   /]
   /   /   /  '<Spe><Instance>WalkingSocketDict' : {...}< (dict), 4559267272>
   /   /   /}
   /   /}
   /  '<Spe><Instance>ParentedDeriveParentersList' : []
   /  '<Spe><Instance>WalkingSocketDict' : {...}< (dict), 4559267272>
   /}

*****End of the Attest *****



```

