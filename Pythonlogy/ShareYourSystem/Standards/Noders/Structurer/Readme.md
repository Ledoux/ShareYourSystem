

<!--
FrozenIsBool False
-->

#Structurer

##Doc
----


>
> A Structurer is the last level of class that helps for building
> hierarchic structures. For a certain <StructuringNodeStr> it walks to group
> everybody in the hfd5.
>
>

----

<small>
View the Structurer notebook on [NbViewer](http://nbviewer.ipython.org/url/share
yoursystem.ouvaton.org/Structurer.ipynb)
</small>




<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Structurer is the last level of class that helps for building
hierarchic structures. For a certain <StructuringNodeStr> it walks to group
everybody in the hfd5.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Noders.Grouper"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class StructurerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'StructuringNodeCollectionStrsList',
'StructuringBeforeUpdateList'
                                                                ]

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':
BaseClass.__init__}]})
        def default_init(self,
_StructuringNodeCollectionStrsList=[],
_StructuringBeforeUpdateList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingMethodStr'
:'hdformat'}]})
        def do_structure(self):

                #debug
                '''
                self.debug(('self.',self,['ParentingNodeStr']))
                '''

                #<NotHook>
                #hdformat first
                self.hdformat()
                #</NotHook>

                """
                print([
('parent',{'LiargVariablesList':[self.ParentingNodeStr]}),
('group',{'LiargVariablesList':[]})
]+self.StructuringBeforeUpdateList)
                """

                #Walk while parentizing and grouping
                self.walk(
                                        {
                                                'BeforeUpdateList':
                                                [
('parent',{'LiargVariablesList':[]}),
('group',{'LiargVariablesList':[]})
]+self.StructuringBeforeUpdateList,
                                                'GatherVariablesList':map(
                                                                lambda
__StructuringNodeCollectionStr:
                                                                Noder.NodingPref
ixGetStr+__StructuringNodeCollectionStr+Noder.NodingSuffixGetStr,
self.StructuringNodeCollectionStrsList
                                                        )
                                        }
                                )

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Structurer sources on <a href="https://github.com/Ledoux/ShareYourSyste
m/tree/master/Pythonlogy/ShareYourSystem/Noders/Structurer"
target="_blank">Github</a>
</small>




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
from ShareYourSystem.Standards.Noders import Structurer

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
        'MyStructurer.hdfview().HdformatedConsoleStr is
'+MyStructurer.hdfview().HdformatedConsoleStr
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyStructurer is < (StructurerClass), 4555635664>
   /{
   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildStructurer' : < (StructurerClass), 4555535184>
   /   /   /{
   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildStructurer' : < (StructurerClass), 4555535440>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdInt' : 4555535440
   /   /   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Graph
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildStructurer
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(StructurerClass), 4555535184>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4557178688>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : []
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4555535184
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Graph
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildStructurer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4555635664>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557179280>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : {...}< (list),
4556259696>
   /   /   /}
   /   /  'SecondChildStructurer' : < (StructurerClass), 4555537808>
   /   /   /{
   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4555537808
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Graph
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildStructurer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4555635664>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557179280>
   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'OtherGrandChildStructurer' : < (StructurerClass), 4555538000>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>GraphCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdInt' : 4555538000
   /   /   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : OtherGrandChildStructurer
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(StructurerClass), 4555537808>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4557178984>
   /   /   /   /   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : {...}<
(list), 4556259696>
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /   /   /  '<Spe><Class>StructuringNodeCollectionStrsList' : {...}< (list),
4556259696>
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4555635664
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopStructurer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>StructuringBeforeUpdateList' : []
   /  '<Spe><Instance>StructuringNodeCollectionStrsList' : ['Graph', 'Tree']
   /}

------

MyStructurer.hdfview().HdformatedConsoleStr is /                        Group
/TopStructurer           Group
/TopStructurer/FirstChildStructurer Group
/TopStructurer/FirstChildStructurer/GrandChildStructurer Group
/TopStructurer/SecondChildStructurer Group
/TopStructurer/SecondChildStructurer/OtherGrandChildStructurer Group
/xx0xxThingsFindoerTable Dataset {3/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,1], MyStr="guten tag"},
        (2) {RowInt=2, MyInt=1, MyIntsList=[0,0,0], MyStr="bonjour"}
/xx0xxThingsInserterTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[2,4,6], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,0], MyStr="hello"}
/xx0xxThingsRecovererTable Dataset {3/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,1], MyStr="guten tag"},
        (2) {RowInt=2, MyInt=1, MyIntsList=[0,0,0], MyStr="bonjour"}
/xx0xxThingsRetrieverTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[2,4,6], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,0], MyStr="guten tag"}
/xx0xxThingsRowerTable   Dataset {0/Inf}
    Data:

/xx0xxThingsTablerTable  Dataset {0/Inf}
    Data:

/xx0xx__UnitsInt_3__ThingsMergerTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0,1], MyStr="hello"},
        (1) {RowInt=1, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"}
/xx0xx__UnitsInt_3__ThingsShaperTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0,1], MyStr="hello"},
        (1) {RowInt=1, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"}
/xx1xx__UnitsInt_2__ThingsMergerTable Dataset {1/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0], MyStr=""}
/xx1xx__UnitsInt_2__ThingsShaperTable Dataset {1/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0], MyStr=""}


*****End of the Attest *****



```

