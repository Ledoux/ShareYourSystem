
#Adder
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Adder maps an append



<!--
FrozenIsBool False
-->

View the Adder sources on [Github](https://github.com/Ledoux/ShareYourSystem/tre
e/master/ShareYourSystem/Noders/Installer)




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
from ShareYourSystem.Noders import Adder

#Definition an Tree instance
MyAdder=Adder.AdderClass()+[
    [
        ('NodeCollectionStr','Tree'),
        ('NodeKeyStr','MyTuplesList'),
        ('MyStr','Hello')
    ],
    {
        'NodeCollectionStr':'Tree',
        'NodeKeyStr':'MyDict',
        'MyOtherStr':'Bonjour'
    },
    Adder.AdderClass().update(
            [
                ('NodeCollectionStr','Tree'),
                ('NodeKeyStr','MyChildAppender')
            ]
        )
]

#Definition the AttestedStr
SYS._attest(
    [
        'MyAdder is '+SYS._str(
        MyAdder,
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
Doer l.132 : DoerStr is Itemizer
DoStr is Itemize
DoMethodStr is itemize
DoingStr is Itemizing
DoneStr is Itemized

Doer l.132 : DoerStr is Getter
DoStr is Get
DoMethodStr is get
DoingStr is Getting
DoneStr is Getted

Doer l.132 : DoerStr is Setter
DoStr is Set
DoMethodStr is set
DoingStr is Setting
DoneStr is Setted

Doer l.132 : DoerStr is Deleter
DoStr is Delete
DoMethodStr is delete
DoingStr is Deleting
DoneStr is Deleted

Doer l.132 : DoerStr is Attributer
DoStr is Attribute
DoMethodStr is attribute
DoingStr is Attributing
DoneStr is Attributed

Doer l.132 : DoerStr is Restricter
DoStr is Restrict
DoMethodStr is restrict
DoingStr is Restricting
DoneStr is Restricted

Doer l.132 : DoerStr is Pather
DoStr is Path
DoMethodStr is path
DoingStr is Pathing
DoneStr is Pathed

Doer l.132 : DoerStr is Sharer
DoStr is Share
DoMethodStr is share
DoingStr is Sharing
DoneStr is Shared

Doer l.132 : DoerStr is Executer
DoStr is Execute
DoMethodStr is execute
DoingStr is Executing
DoneStr is Executed

Doer l.132 : DoerStr is Pointer
DoStr is Point
DoMethodStr is point
DoingStr is Pointing
DoneStr is Pointed

Doer l.132 : DoerStr is Applyier
DoStr is Apply
DoMethodStr is apply
DoingStr is Applying
DoneStr is Applied

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
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Tree
self.AppendedNodeKeyStr is MyTuplesList

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
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Tree
self.AppendedNodeKeyStr is MyDict

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
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Tree
self.AppendedNodeKeyStr is MyChildAppender

                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyAdder is < (AdderClass), 4556130896>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdStr' : 4556130896
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'MyTuplesList' :
   /   /   /[
   /   /   /  0 : ('NodeCollectionStr', 'Tree')
   /   /   /  1 : ('NodeKeyStr', 'MyTuplesList')
   /   /   /  2 : ('MyStr', 'Hello')
   /   /   /]
   /   /  'MyDict' :
   /   /   /{
   /   /   /  'MyOtherStr' : Bonjour
   /   /   /  'NodeCollectionStr' : Tree
   /   /   /  'NodeKeyStr' : MyDict
   /   /   /}
   /   /  'MyChildAppender' : < (AdderClass), 4556808528>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdStr' : 4556808528
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : MyChildAppender
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (AdderClass),
4556130896>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556800672>
   /   /   /}
   /   /}
   /}

*****End of the Attest *****



```

