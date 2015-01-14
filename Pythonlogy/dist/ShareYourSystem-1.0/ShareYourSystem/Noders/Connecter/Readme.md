
#Connecter
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



Connecters...





<!--
FrozenIsBool False
-->

View the Connecter sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem/Noders/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Connecter

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
            ['First','Second'],
            Connecter.ConnecterClass,
            **{'CollectingCollectionStr':"Connectome"}
        )

#connect
MyProducer['<Connectome>FirstConnecter'].connect(**{
        'CatchingCollectionStr':"PostRelatome",
        'AttentioningCollectionStr':"PreRelatome",
        'ConnectingAttentionGetStrsList':[
            '/NodePointDeriveNoder/<Connectome>SecondConnecter'
        ],
        'ConnectingCatchGetStrsList':[
            '/NodePointDeriveNoder/<Connectome>SecondConnecter'
        ],
    }
)


#Definition the AttestedStr
SYS._attest(
    [
        'MyProducer is '+SYS._str(
        MyProducer,
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
Doer l.132 : DoerStr is Commander
DoStr is Command
DoMethodStr is command
DoingStr is Commanding
DoneStr is Commanded

Doer l.132 : DoerStr is Walker
DoStr is Walk
DoMethodStr is walk
DoingStr is Walking
DoneStr is Walked

Doer l.132 : DoerStr is Cumulater
DoStr is Cumulate
DoMethodStr is cumulate
DoingStr is Cumulating
DoneStr is Cumulated

Doer l.132 : DoerStr is Visiter
DoStr is Visit
DoMethodStr is visit
DoingStr is Visiting
DoneStr is Visited

Doer l.132 : DoerStr is Recruiter
DoStr is Recruit
DoMethodStr is recruit
DoingStr is Recruiting
DoneStr is Recruit

Doer l.132 : DoerStr is Mobilizer
DoStr is Mobilize
DoMethodStr is mobilize
DoingStr is Mobilizing
DoneStr is Mobilized

Doer l.132 : DoerStr is Connecter
DoStr is Connect
DoMethodStr is connect
DoingStr is Connecting
DoneStr is Connected


                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                            ////////////////////////////////
                            Doer/__init__.py do
                            From <string> superDo_debug | Catcher/__init__.py
do_catch | Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py
watch | <string> watch_superDo_catch | Attentioner/__init__.py do_attention |
Doer/__init__.py do | <string> superDo_attention | Watcher/__init__.py watch |
<string> watch_superDo_attention | Connecter/__init__.py do_connect |
Doer/__init__.py do | <string> superDo_connect | Watcher/__init__.py watch |
<string> watch_superDo_connect | <string> <module> | <string> <module> | site-
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
                            I am with [('NodeKeyStr', 'FirstConnecter')]
                            *****
                            self.CollectingCollectionStr is

                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                            ////////////////////////////////
                            Doer/__init__.py do
                            From <string> superDo_debug | Catcher/__init__.py
do_catch | Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py
watch | <string> watch_superDo_catch | Attentioner/__init__.py do_attention |
Doer/__init__.py do | <string> superDo_attention | Watcher/__init__.py watch |
<string> watch_superDo_attention | Connecter/__init__.py do_connect |
Doer/__init__.py do | <string> superDo_connect | Watcher/__init__.py watch |
<string> watch_superDo_connect | <string> <module> | <string> <module> | site-
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
                            I am with [('NodeKeyStr', 'SecondConnecter')]
                            *****
                            self.CollectingCollectionStr is PreRelatome

                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx
        ////////////////////////////////
        Doer/__init__.py do
        From <string> superDo_debug | Catcher/__init__.py do_catch |
Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py watch |
<string> watch_superDo_catch | Connecter/__init__.py do_connect |
Doer/__init__.py do | <string> superDo_connect | Watcher/__init__.py watch |
<string> watch_superDo_connect | <string> <module> | <string> <module> | site-
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
        I am with [('NodeKeyStr', 'FirstConnecter')]
        *****
        self.CollectingCollectionStr is PostRelatome

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyProducer is < (ProducerClass), 4557090384>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstConnecter' : < (ConnecterClass), 4557092816>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdStr' : 4557092816
   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstConnecter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4557090384>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557237216>
   /   /   /  '<New><Instance>PostRelatomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'SecondConnecterPointer' : < (PointerClass), 4557092880>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdStr' : 4557092880
   /   /   /   /   /  '<New><Instance>PointVariable' : < (ConnecterClass),
4557093264>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>IdStr' : 4557093264
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondConnecter
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(ProducerClass), 4557090384>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4557237216>
   /   /   /   /   /   /  '<New><Instance>PreRelatomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /  'FirstConnecterPointer' : < (PointerClass),
4557281296>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdStr' : 4557281296
   /   /   /   /   /   /   /   /  '<New><Instance>PointVariable' : {...}<
(ConnecterClass), 4557092816>
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4557092816>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' :
PointVariable
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4557092816>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' :
PointVariable
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>ConnectedAttentionDeriveConnectersList' :
None
   /   /   /   /   /   /  '<Spe><Class>ConnectedDerivePointersList' :
None
   /   /   /   /   /   /  '<Spe><Class>ConnectingAttentionGetStrsList' : None
   /   /   /   /   /   /  '<Spe><Class>ConnectingCatchGetStrsList' : None
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4557093264>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4557093264>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Instance>ConnectedAttentionDeriveConnectersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (ConnecterClass), 4557092816>
   /   /   /   /]
   /   /   /  '<Spe><Instance>ConnectedDerivePointersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (ConnecterClass), 4557092816>
   /   /   /   /]
   /   /   /  '<Spe><Instance>ConnectingAttentionGetStrsList' :
['/NodePointDeriveNoder/<Connectome>SecondConnecter']
   /   /   /  '<Spe><Instance>ConnectingCatchGetStrsList' :
['/NodePointDeriveNoder/<Connectome>SecondConnecter']
   /   /   /}
   /   /  'SecondConnecter' : {...}< (ConnecterClass), 4557093264>
   /   /}
   /  '<New><Instance>IdStr' : 4557090384
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (ConnecterClass), 4557092816>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (ConnecterClass), 4557093264>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingInitiateDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Connecter.ConnecterClass'>
   /}

*****End of the Attest *****



```

