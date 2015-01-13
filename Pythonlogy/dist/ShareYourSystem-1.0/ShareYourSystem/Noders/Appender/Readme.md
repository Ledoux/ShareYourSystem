
#Appender
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Appender append by doing a set in a NodedOrderedDict thanks to the
<AppendedNodeCollectionStr><AppendedNodeKeyStr>





<!--
FrozenIsBool False
-->

View the Appender sources on [Github](https://github.com/Ledoux/ShareYourSystem/
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
from ShareYourSystem.Noders import Appender

#Append with a TuplesList
MyAppender=Appender.AppenderClass().append([
                                    ('NodeCollectionStr','Tree'),
                                    ('NodeKeyStr','MyTuplesList'),
                                    ('MyStr','Hello')
                                ]
                            )

#Append with a dict
MyAppender.append({
                    'NodeCollectionStr':'Tree',
                    'NodeKeyStr':'MyDict',
                    'MyOtherStr':'Bonjour'
                    }
                )

#Append with an instance
MyAppender.append(
                    Appender.AppenderClass().update(
                        [
                            ('NodeCollectionStr','Tree'),
                            ('NodeKeyStr','MyAppender')
                        ]
                    )
                )

#Definition the AttestedStr
SYS._attest(
    [
        'MyAppender is '+SYS._str(
        MyAppender,
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

                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
Doer/__init__.py do
                                                                    From
<string> superDo_debug | Appender/__init__.py do_append | Doer/__init__.py do |
<string> superDo_append | Watcher/__init__.py watch | <string>
watch_superDo_append | <string> <module> | <string> <module> | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Doer/__init__.py do |
<string> superDo_cell | Watcher/__init__.py watch | <string> watch_superDo_cell
| Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
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

                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
Doer/__init__.py do
                                                                    From
<string> superDo_debug | Appender/__init__.py do_append | Doer/__init__.py do |
<string> superDo_append | Watcher/__init__.py watch | <string>
watch_superDo_append | <string> <module> | <string> <module> | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Doer/__init__.py do |
<string> superDo_cell | Watcher/__init__.py watch | <string> watch_superDo_cell
| Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
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

                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
Doer/__init__.py do
                                                                    From
<string> superDo_debug | Appender/__init__.py do_append | Doer/__init__.py do |
<string> superDo_append | Watcher/__init__.py watch | <string>
watch_superDo_append | <string> <module> | <string> <module> | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Doer/__init__.py do |
<string> superDo_cell | Watcher/__init__.py watch | <string> watch_superDo_cell
| Notebooker/__init__.py do_notebook | Doer/__init__.py do | <string>
superDo_notebook | Watcher/__init__.py watch | <string> watch_superDo_notebook |
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
self.AppendedNodeKeyStr is MyAppender

                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyAppender is < (AppenderClass), 4556812112>
   /{
   /  '<New><Instance>IdStr' : 4556812112
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
   /   /  'MyAppender' : < (AppenderClass), 4556811024>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdStr' : 4556811024
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : MyAppender
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (AppenderClass),
4556812112>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556800968>
   /   /   /  '<Spe><Class>AppendedNodeCollectionStr' :
   /   /   /  '<Spe><Class>AppendedNodeKeyStr' :
   /   /   /  '<Spe><Class>AppendingCollectionVariable' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>AppendedNodeCollectionStr' : Tree
   /  '<Spe><Instance>AppendedNodeKeyStr' : MyAppender
   /  '<Spe><Instance>AppendingCollectionVariable' : {...}< (AppenderClass),
4556811024>
   /}

*****End of the Attest *****



```

