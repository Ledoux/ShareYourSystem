
#Parenter
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Parenter completes the list of grand-parent nodes that a child node could
have. It acts only at one level.





<!--
FrozenIsBool False
-->

View the Parenter sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Noders/Installer)




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
from ShareYourSystem.Noders import Parenter

#Short expression and set in the appended manner
MyParenter=Parenter.ParenterClass().__setitem__(
    '<Tree>ChildParenter',
    Parenter.ParenterClass().__setitem__(
        '<Tree>GrandChildParenter',
        Parenter.ParenterClass()
    )
)

#Parent for the children
#MyParenter['<Tree>ChildParenter'].parent('Tree')
MyParenter['<Tree>ChildParenter']['<Tree>GrandChildParenter'].parent()

#Definition the AttestedStr
SYS._attest(
    [
        'MyParenter is '+SYS._str(
        MyParenter,
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

MyParenter is < (ParenterClass), 4570207184>
   /{
   /  '<New><Instance>IdStr' : 4570207184
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'ChildParenter' : < (ParenterClass), 4567892688>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4567892688
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ChildParenter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ParenterClass),
4570207184>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4570171200>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildParenter' : < (ParenterClass), 4570208784>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdStr' : 4570208784
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildParenter
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(ParenterClass), 4567892688>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4570170904>
   /   /   /   /   /  '<Spe><Class>ParentingWalkBool' : True
   /   /   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /   /   /[
   /   /   /   /   /   /  0 : {...}< (ParenterClass), 4567892688>
   /   /   /   /   /   /  1 : {...}< (ParenterClass), 4570207184>
   /   /   /   /   /   /]
   /   /   /   /   /  '<Spe><Instance>ParentedNodeCollectionStrsList' : ['', '']
   /   /   /   /   /  '<Spe><Instance>ParentedPathStr' : /ChildParenter
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>ParentingWalkBool' : True
   /   /   /  '<Spe><Instance>ParentedDeriveParentersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (ParenterClass), 4570207184>
   /   /   /   /]
   /   /   /  '<Spe><Instance>ParentedNodeCollectionStrsList' : ['']
   /   /   /  '<Spe><Instance>ParentedPathStr' :
   /   /   /}
   /   /}
   /  '<Spe><Class>ParentedPathStr' :
   /  '<Spe><Class>ParentingWalkBool' : True
   /  '<Spe><Instance>ParentedDeriveParentersList' : []
   /  '<Spe><Instance>ParentedNodeCollectionStrsList' : []
   /}

*****End of the Attest *****



```

