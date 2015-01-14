

<!--
FrozenIsBool False
-->

View the Commander sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem/Applyiers/Installer)




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
from ShareYourSystem.Applyiers import Commander
import copy

#Definition a structure of Commanders.
MyFirstCommander=Commander.CommanderClass().__add__(
    [
        Commander.CommanderClass().update(
            [
                ('NodeCollectionStr','Commandome'),
                ('NodeKeyStr',str(Int1))
            ]) for Int1 in xrange(2)
    ]
)

#Definition a structure of Commanders.
MySecondCommander=Commander.CommanderClass().__add__(
    [
        Commander.CommanderClass().update(
            [
                ('NodeCollectionStr','Commandome'),
                ('NodeKeyStr',str(Int1))
            ]) for Int1 in xrange(2)
    ]
)


#Definition an CommandingUpdateList to be commanded
CommandingUpdateList=[
    (
        'MyCountingInt',
        ';'.join([
'Exec_self.SettingValueVariable=self.__class__.MyCountingInt',
                    'self.__class__.MyCountingInt+=1'
                ])
    ),
    (
        'MyCountingInt',
        ';'.join([
'Exec_self.SettingValueVariable=self.__class__.MyCountingInt',
                    'self.__class__.MyCountingInt+=1'
                ])
    )
]

#Definition GatheringVariablesList
GatheringVariablesList=[
        ['/'],
        '<Commandome>'
]

#Now command with a AllSetsForEach protocol
MyFirstCommander.execute('self.__class__.MyCountingInt=0').command(
        _UpdateList=CommandingUpdateList,
        **{
            'GatheringVariablesList': GatheringVariablesList
            }
        )

#Command with a EachSetForAll protocol
MySecondCommander.execute('self.__class__.MyCountingInt=0').command(
        CommandingUpdateList,
        _OrderStr='EachSetForAll',
        **{
            'GatheringVariablesList': GatheringVariablesList
        }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyFirstCommander is '+SYS._str(
        MyFirstCommander,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        ),
        'MySecondCommander is '+SYS._str(
        MySecondCommander,
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

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Appender/__init__.py do_append
                                            From Appender/__init__.py do_append
| Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic |
Applyier/__init__.py do_apply | Mapper/__init__.py do_map | Adder/__init__.py
do_add | Adder/__init__.py __add__ | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopCommander')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Commandome
                                            self.AppendedNodeKeyStr is 0

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Appender/__init__.py do_append
                                            From Appender/__init__.py do_append
| Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic |
Applyier/__init__.py do_apply | Mapper/__init__.py do_map | Adder/__init__.py
do_add | Adder/__init__.py __add__ | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopCommander')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Commandome
                                            self.AppendedNodeKeyStr is 1

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Appender/__init__.py do_append
                                            From Appender/__init__.py do_append
| Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic |
Applyier/__init__.py do_apply | Mapper/__init__.py do_map | Adder/__init__.py
do_add | Adder/__init__.py __add__ | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopCommander')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Commandome
                                            self.AppendedNodeKeyStr is 0

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Appender/__init__.py do_append
                                            From Appender/__init__.py do_append
| Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic |
Applyier/__init__.py do_apply | Mapper/__init__.py do_map | Adder/__init__.py
do_add | Adder/__init__.py __add__ | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopCommander')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Commandome
                                            self.AppendedNodeKeyStr is 1

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyFirstCommander is < (CommanderClass), 4550228176>
   /{
   /  '<New><Instance>CommandomeCollectionOrderedDict' :
   /   /{
   /   /  '0' : < (CommanderClass), 4550240656>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550240656
   /   /   /  '<New><Instance>MyCountingInt' : 3
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : 0
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4550228176>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550296224>
   /   /   /  '<Spe><Class>CommandingGatherIsBool' : True
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /  '1' : < (CommanderClass), 4550240784>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550240784
   /   /   /  '<New><Instance>MyCountingInt' : 5
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : 1
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4550228176>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550296224>
   /   /   /  '<Spe><Class>CommandingGatherIsBool' : True
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4550228176
   /  '<New><Instance>MyCountingInt' : 1
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopCommander
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>CommandingGatherIsBool' : True
   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /}

------

MySecondCommander is < (CommanderClass), 4550241104>
   /{
   /  '<New><Instance>CommandomeCollectionOrderedDict' :
   /   /{
   /   /  '0' : < (CommanderClass), 4550242064>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550242064
   /   /   /  '<New><Instance>MyCountingInt' : 4
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : 0
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4550241104>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550296520>
   /   /   /  '<Spe><Class>CommandingGatherIsBool' : True
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /  '1' : < (CommanderClass), 4550241616>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4550241616
   /   /   /  '<New><Instance>MyCountingInt' : 5
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : 1
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4550241104>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4550296520>
   /   /   /  '<Spe><Class>CommandingGatherIsBool' : True
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4550241104
   /  '<New><Instance>MyCountingInt' : 3
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopCommander
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>CommandingGatherIsBool' : True
   /  '<Spe><Instance>CommandingOrderStr' : EachSetForAll
   /}

*****End of the Attest *****



```

