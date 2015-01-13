
#Parenter
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Parenter completes the list of grand-parent nodes that a child node could
have. It acts only at one level.





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
from ShareYourSystem.Objects import Parenter

#Short expression and set in the appended manner
MyParenter=Parenter.ParenterClass().__setitem__(
    '<Group>ChildNode',
    Parenter.ParenterClass().__setitem__(
        '<Group>GrandChildNode',
        Parenter.ParenterClass()
    )
)

#Parent for the children
MyParenter['<Group>ChildNode'].parent('Group')
MyParenter['<Group>ChildNode']['<Group>GrandChildNode'].parent('Group')

#Definition the AttestedStr
SYS._attest(
    [
        'MyParenter is '+SYS._str(
        MyParenter,
        **{
            'RepresentingBaseKeyStrsListBool':False
        }
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyParenter is < (ParenterClass), 4381805648>
   /{
   /  '<New><Instance>NodedGroupGrandParentPointersList' : []
   /  '<New><Instance>NodedGroupInt' : -1
   /  '<New><Instance>NodedGroupKeyStr' :
   /  '<New><Instance>NodedGroupOrderedDict' :
   /   /{
   /   /  'ChildNode' : < (ParenterClass), 4382860560>
   /   /   /{
   /   /   /  '<New><Instance>NodedGroupGrandParentKeyStrsList' : ['']
   /   /   /  '<New><Instance>NodedGroupGrandParentPointersList' : ['<
(ParenterClass), 4381805648>']
   /   /   /  '<New><Instance>NodedGroupInt' : 0
   /   /   /  '<New><Instance>NodedGroupKeyStr' : ChildNode
   /   /   /  '<New><Instance>NodedGroupOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildNode' : < (ParenterClass), 4382860752>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>NodedGroupGrandParentKeyStrsList' :
['ChildNode', '']
   /   /   /   /   /  '<New><Instance>NodedGroupGrandParentPointersList' : ['<
(ParenterClass), 4382860560>', '< (ParenterClass), 4381805648>']
   /   /   /   /   /  '<New><Instance>NodedGroupInt' : 0
   /   /   /   /   /  '<New><Instance>NodedGroupKeyStr' : GrandChildNode
   /   /   /   /   /  '<New><Instance>NodedGroupOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>NodedGroupParentPointer' : <
(ParenterClass), 4382860560>
   /   /   /   /   /  '<New><Instance>NodedGroupPathStr' :
/ChildNode/GrandChildNode
   /   /   /   /   /  '<New><Instance>NodedGroupPathStrsList' : ['',
'ChildNode', 'GrandChildNode']
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>NodedGroupParentPointer' : < (ParenterClass),
4381805648>
   /   /   /  '<New><Instance>NodedGroupPathStr' : /ChildNode
   /   /   /  '<New><Instance>NodedGroupPathStrsList' : ['', 'ChildNode']
   /   /   /}
   /   /}
   /  '<New><Instance>NodedGroupParentPointer' : < (NoneType), 4357211448>
   /}

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the ParenterClass are :


```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Parenter

#Definition the AttestedStr
SYS._attest(
    [
        'DefaultAttributeItemTuplesList is '+SYS._str(
            Parenter.ParenterClass.DefaultAttributeItemTuplesList,
            **{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

DefaultAttributeItemTuplesList is
   /[
   /  0 : ('ParentingNodeStr', '')
   /  1 :
   /   /(
   /   /  0 : ParentedDeriveNodersList
   /   /  1 : []
   /   /)
   /  2 : ('ParentedPathStr', '')
   /]

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the instances

A default call of an instance gives :


```python



#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Parenter

#Definition the AttestedStr
SYS._attest(
    [
        Parenter.ParenterClass()
    ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

< (ParenterClass), 4527459344>
   /{
   /}

*****End of the Attest *****




```

