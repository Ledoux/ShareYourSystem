
#Commander
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Commander gather Variables to set them with an UpdateList. The command process
can be AllSetsForEach (ie a map of the update succesively for each) or a
EachSetForAll (ie each set is a map of each).





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
        'EachSetForAll',
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
Doer l.132 : DoerStr is Mapper
DoStr is Map
DoMethodStr is map
DoingStr is Mapping
DoneStr is Mapped

Doer l.132 : DoerStr is Picker
DoStr is Pick
DoMethodStr is pick
DoingStr is Picking
DoneStr is Pick

Doer l.132 : DoerStr is Gatherer
DoStr is Gather
DoMethodStr is gather
DoingStr is Gathering
DoneStr is Gathered

Doer l.132 : DoerStr is Updater
DoStr is Update
DoMethodStr is update
DoingStr is Updating
DoneStr is Updated

Doer l.132 : DoerStr is Filterer
DoStr is Filter
DoMethodStr is filter
DoingStr is Filtering
DoneStr is Filterer

Doer l.132 : DoerStr is Noder
DoStr is Node
DoMethodStr is node
DoingStr is Noding
DoneStr is Noded

Doer l.132 : DoerStr is Appender
DoStr is Append
DoMethodStr is append
DoingStr is Appending
DoneStr is Appended

Doer l.132 : DoerStr is Instancer
DoStr is Instance
DoMethodStr is instance
DoingStr is Instancing
DoneStr is Instanced

Doer l.132 : DoerStr is Adder
DoStr is Add
DoMethodStr is add
DoingStr is Adding
DoneStr is Added

Doer l.132 : DoerStr is Distinguisher
DoStr is Distinguish
DoMethodStr is distinguish
DoingStr is Distinguishing
DoneStr is Distinguished

Doer l.132 : DoerStr is Parenter
DoStr is Parent
DoMethodStr is parent
DoingStr is Parenting
DoneStr is Parented

Doer l.132 : DoerStr is Storer
DoStr is Store
DoMethodStr is store
DoingStr is Storing
DoneStr is Stored

Doer l.132 : DoerStr is Pusher
DoStr is Push
DoMethodStr is push
DoingStr is Pushing
DoneStr is Pushed

Doer l.132 : DoerStr is Producer
DoStr is Produce
DoMethodStr is produce
DoingStr is Producing
DoneStr is Produced

Doer l.132 : DoerStr is Catcher
DoStr is Catch
DoMethodStr is catch
DoingStr is Catching
DoneStr is Catched

Doer l.132 : DoerStr is Commander
DoStr is Command
DoMethodStr is command
DoingStr is Commanding
DoneStr is Commanded


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | Appender/__init__.py do_append | Doer/__init__.py do | <string>
superDo_append | Watcher/__init__.py watch | <string> watch_superDo_append |
Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic | <string>
superMimic_watch_superDo_append | Applyier/__init__.py do_apply |
Doer/__init__.py do | <string> superDo_apply | Watcher/__init__.py watch |
<string> watch_superDo_apply | Mapper/__init__.py do_map | Doer/__init__.py do |
<string> superDo_map | Watcher/__init__.py watch | <string> watch_superDo_map |
Adder/__init__.py do_add | Doer/__init__.py do | <string> superDo_add |
Watcher/__init__.py watch | <string> watch_superDo_add | Adder/__init__.py
__add__ | <string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | Installer/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Commandome
self.AppendedNodeKeyStr is 0

                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | Appender/__init__.py do_append | Doer/__init__.py do | <string>
superDo_append | Watcher/__init__.py watch | <string> watch_superDo_append |
Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic | <string>
superMimic_watch_superDo_append | Applyier/__init__.py do_apply |
Doer/__init__.py do | <string> superDo_apply | Watcher/__init__.py watch |
<string> watch_superDo_apply | Mapper/__init__.py do_map | Doer/__init__.py do |
<string> superDo_map | Watcher/__init__.py watch | <string> watch_superDo_map |
Adder/__init__.py do_add | Doer/__init__.py do | <string> superDo_add |
Watcher/__init__.py watch | <string> watch_superDo_add | Adder/__init__.py
__add__ | <string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | Installer/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Commandome
self.AppendedNodeKeyStr is 1

                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | Appender/__init__.py do_append | Doer/__init__.py do | <string>
superDo_append | Watcher/__init__.py watch | <string> watch_superDo_append |
Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic | <string>
superMimic_watch_superDo_append | Applyier/__init__.py do_apply |
Doer/__init__.py do | <string> superDo_apply | Watcher/__init__.py watch |
<string> watch_superDo_apply | Mapper/__init__.py do_map | Doer/__init__.py do |
<string> superDo_map | Watcher/__init__.py watch | <string> watch_superDo_map |
Adder/__init__.py do_add | Doer/__init__.py do | <string> superDo_add |
Watcher/__init__.py watch | <string> watch_superDo_add | Adder/__init__.py
__add__ | <string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | Installer/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Commandome
self.AppendedNodeKeyStr is 0

                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                                Doer/__init__.py
do
                                                                From <string>
superDo_debug | Appender/__init__.py do_append | Doer/__init__.py do | <string>
superDo_append | Watcher/__init__.py watch | <string> watch_superDo_append |
Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic | <string>
superMimic_watch_superDo_append | Applyier/__init__.py do_apply |
Doer/__init__.py do | <string> superDo_apply | Watcher/__init__.py watch |
<string> watch_superDo_apply | Mapper/__init__.py do_map | Doer/__init__.py do |
<string> superDo_map | Watcher/__init__.py watch | <string> watch_superDo_map |
Adder/__init__.py do_add | Doer/__init__.py do | <string> superDo_add |
Watcher/__init__.py watch | <string> watch_superDo_add | Adder/__init__.py
__add__ | <string> <module> | <string> <module> | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Doer/__init__.py do | <string> superDo_cell |
Watcher/__init__.py watch | <string> watch_superDo_cell | Notebooker/__init__.py
do_notebook | Doer/__init__.py do | <string> superDo_notebook |
Watcher/__init__.py watch | <string> watch_superDo_notebook |
Readmer/__init__.py do_readme | Doer/__init__.py do | <string> superDo_readme |
Watcher/__init__.py watch | <string> watch_superDo_readme |
python2.7/posixpath.py walk | python2.7/posixpath.py walk | Directer/__init__.py
do_direct | Doer/__init__.py do | <string> superDo_direct | Watcher/__init__.py
watch | <string> watch_superDo_direct | Installer/__init__.py do_install |
Doer/__init__.py do | <string> superDo_install | Watcher/__init__.py watch |
<string> watch_superDo_install | Installer/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Commandome
self.AppendedNodeKeyStr is 1

                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyFirstCommander is < (CommanderClass), 4364536016>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>CommandomeCollectionOrderedDict' :
   /   /{
   /   /  '0' : < (CommanderClass), 4365084688>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4365084688
   /   /   /  '<New><Instance>MyCountingInt' : 3
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : 0
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4364536016>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365152336>
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /  '1' : < (CommanderClass), 4365086544>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4365086544
   /   /   /  '<New><Instance>MyCountingInt' : 5
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : 1
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4364536016>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365152336>
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /}
   /  '<New><Instance>IdString' : 4364536016
   /  '<New><Instance>MyCountingInt' : 1
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /}

------

MySecondCommander is < (CommanderClass), 4365118864>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>CommandomeCollectionOrderedDict' :
   /   /{
   /   /  '0' : < (CommanderClass), 4365116944>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4365116944
   /   /   /  '<New><Instance>MyCountingInt' : 4
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : 0
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4365118864>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365152632>
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /  '1' : < (CommanderClass), 4365115536>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdString' : 4365115536
   /   /   /  '<New><Instance>MyCountingInt' : 5
   /   /   /  '<New><Instance>NodeCollectionStr' : Commandome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : 1
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CommanderClass),
4365118864>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4365152632>
   /   /   /  '<Spe><Class>CommandingOrderStr' : AllSetsForEach
   /   /   /}
   /   /}
   /  '<New><Instance>IdString' : 4365118864
   /  '<New><Instance>MyCountingInt' : 3
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Instance>CommandingOrderStr' : EachSetForAll
   /}

*****End of the Attest *****



```

