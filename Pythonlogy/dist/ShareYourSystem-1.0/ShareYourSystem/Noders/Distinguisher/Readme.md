
#Distinguisher
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Distinguisher is a bit the opposite of a Commander, it updates for every child
nodes with a distinguished tuples list.





<!--
FrozenIsBool False
-->

View the Distinguisher sources on [Github](https://github.com/Ledoux/ShareYourSy
stem/tree/master/ShareYourSystem/Noders/Installer)




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
from ShareYourSystem.Noders import Distinguisher
import copy

#Definition a tree of Distinguishers.
MyDistinguisher=Distinguisher.DistinguisherClass().__add__(
    [
        Distinguisher.DistinguisherClass().update(
            [
                ('NodeCollectionStr','Tree'),
                ('NodeKeyStr',str(Int1))
            ]
        ) for Int1 in xrange(2)
    ]
)

#distinguish
MyDistinguisher.distinguish("Tree",[
                                        [('MyStr',"hello")],
                                        [('MyInt',0)]
                                    ])

#distinguish through setting
MyDistinguisher.__setitem__("Dis_<Tree>",[
                                        [('MyOtherStr',"bonjour")],
                                        [('MyOtherInt',1)]
                                    ])

#Definition the AttestedStr
SYS._attest(
    [
        'MyDistinguisher is '+SYS._str(
        MyDistinguisher,
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
<string> watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                                l.180 :
                                                                *****
                                                                I am with
[('NodeKeyStr', '')]
                                                                *****
self.AppendedNodeCollectionStr is Tree
self.AppendedNodeKeyStr is 1

                                                                xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyDistinguisher is < (DistinguisherClass), 4557299088>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdStr' : 4557299088
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  '0' : < (DistinguisherClass), 4557281168>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdStr' : 4557281168
   /   /   /  '<New><Instance>MyOtherStr' : bonjour
   /   /   /  '<New><Instance>MyStr' : hello
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : 0
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(DistinguisherClass), 4557299088>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557307144>
   /   /   /  '<Spe><Class>DistinguishingNodeStr' :
   /   /   /  '<Spe><Class>DistinguishingUpdatesList' : None
   /   /   /}
   /   /  '1' : < (DistinguisherClass), 4557299600>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdStr' : 4557299600
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>MyOtherInt' : 1
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : 1
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(DistinguisherClass), 4557299088>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557307144>
   /   /   /  '<Spe><Class>DistinguishingNodeStr' :
   /   /   /  '<Spe><Class>DistinguishingUpdatesList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>DistinguishingNodeStr' : Tree
   /  '<Spe><Instance>DistinguishingUpdatesList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : ('MyOtherStr', 'bonjour')
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : ('MyOtherInt', 1)
   /   /   /]
   /   /]
   /}

*****End of the Attest *****



```

