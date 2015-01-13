
#Networker
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Networker





<!--
FrozenIsBool False
-->

View the Networker sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem/Noders/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Connecter,Networker
import operator

#Definition of a brian structure
MyNetworker=Networker.NetworkerClass(
    ).push(
[
    (
        'First',
        Connecter.ConnecterClass().update(
            [
                ('ConnectingCatchGetStrsList',
                    [
                        '/NodePointDeriveNoder/<Connectome>SecondConnecter'
                    ]
                ),
                ('ConnectingAttentionGetStrsList',
                    [
                        '/NodePointDeriveNoder/<Connectome>SecondConnecter'
                    ]
                ),
                ('TagStr','Networked')
            ]
        )
    ),
    (
        'Second',
        Connecter.ConnecterClass().__setitem__(
            'TagStr',
            'Networked'
        )
    )
],
    **{
        'CollectingCollectionStr':'Connectome'
    }
).network(**{
                'RecruitingConcludeConditionTuplesList':[
                    ('__class__.NameStr',operator.eq,'Connecter')
                ]
            }
        )

#Definition the AttestedStr
SYS._attest(
    [
        'MyNetworker is '+SYS._str(
        MyNetworker,
        **{
            'RepresentingBaseKeyStrsList':False,
            'RepresentingAlineaIsBool':False
        }
        ),
    ]
)

#Print



```


```console
>>>
l 35
In the switch function
_KwargVariablesDict is
{'RecruitingConcludeConditionTuplesList': [('__class__.NameStr', <built-in
function eq>, 'Connecter')], 'BindObserveWrapMethodStr':
'watch_superDo_network', 'WatchDoBoolKeyStr': 'WatchNetworkWithNetworkerBool',
'BindDoClassStr': 'NetworkerClass'}


                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                        Doer/__init__.py do
                                                        From <string>
superDo_debug | Catcher/__init__.py do_catch | Doer/__init__.py do | <string>
superDo_catch | Watcher/__init__.py watch | <string> watch_superDo_catch |
Attentioner/__init__.py do_attention | Doer/__init__.py do | <string>
superDo_attention | Watcher/__init__.py watch | <string> watch_superDo_attention
| Connecter/__init__.py do_connect | Doer/__init__.py do | <string>
superDo_connect | Watcher/__init__.py watch | <string> watch_superDo_connect |
Networker/__init__.py do_network | Doer/__init__.py do | <string>
superDo_network | Watcher/__init__.py watch | <string> watch_superDo_network |
Switcher/__init__.py switch | <string> switch_watch_superDo_network | <string>
<module> | <string> <module> | site-packages/six.py exec_ | Celler/__init__.py
do_cell | Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py
watch | <string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                        l.180 :
                                                        *****
                                                        I am with
[('NodeKeyStr', 'FirstConnecter')]
                                                        *****
self.CollectingCollectionStr is

                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
                                                        Doer/__init__.py do
                                                        From <string>
superDo_debug | Catcher/__init__.py do_catch | Doer/__init__.py do | <string>
superDo_catch | Watcher/__init__.py watch | <string> watch_superDo_catch |
Attentioner/__init__.py do_attention | Doer/__init__.py do | <string>
superDo_attention | Watcher/__init__.py watch | <string> watch_superDo_attention
| Connecter/__init__.py do_connect | Doer/__init__.py do | <string>
superDo_connect | Watcher/__init__.py watch | <string> watch_superDo_connect |
Networker/__init__.py do_network | Doer/__init__.py do | <string>
superDo_network | Watcher/__init__.py watch | <string> watch_superDo_network |
Switcher/__init__.py switch | <string> switch_watch_superDo_network | <string>
<module> | <string> <module> | site-packages/six.py exec_ | Celler/__init__.py
do_cell | Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py
watch | <string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
////////////////////////////////

                                                        l.180 :
                                                        *****
                                                        I am with
[('NodeKeyStr', 'SecondConnecter')]
                                                        *****
self.CollectingCollectionStr is PostConnectome

                                                        xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                    ////////////////////////////////
                                    Doer/__init__.py do
                                    From <string> superDo_debug |
Catcher/__init__.py do_catch | Doer/__init__.py do | <string> superDo_catch |
Watcher/__init__.py watch | <string> watch_superDo_catch | Connecter/__init__.py
do_connect | Doer/__init__.py do | <string> superDo_connect |
Watcher/__init__.py watch | <string> watch_superDo_connect |
Networker/__init__.py do_network | Doer/__init__.py do | <string>
superDo_network | Watcher/__init__.py watch | <string> watch_superDo_network |
Switcher/__init__.py switch | <string> switch_watch_superDo_network | <string>
<module> | <string> <module> | site-packages/six.py exec_ | Celler/__init__.py
do_cell | Doer/__init__.py do | <string> superDo_cell | Watcher/__init__.py
watch | <string> watch_superDo_cell | Notebooker/__init__.py do_notebook |
Doer/__init__.py do | <string> superDo_notebook | Watcher/__init__.py watch |
<string> watch_superDo_notebook | Readmer/__init__.py do_readme |
Doer/__init__.py do | <string> superDo_readme | Watcher/__init__.py watch |
<string> watch_superDo_readme | python2.7/posixpath.py walk |
python2.7/posixpath.py walk | Directer/__init__.py do_direct | Doer/__init__.py
do | <string> superDo_direct | Watcher/__init__.py watch | <string>
watch_superDo_direct | Installer/__init__.py do_install | Doer/__init__.py do |
<string> superDo_install | Watcher/__init__.py watch | <string>
watch_superDo_install | ShareYourSystem/Install.py <module>
                                    ////////////////////////////////

                                    l.180 :
                                    *****
                                    I am with [('NodeKeyStr', 'FirstConnecter')]
                                    *****
                                    self.CollectingCollectionStr is PreConnectome

                                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyNetworker is < (NetworkerClass), 4567892048>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstConnecter' : < (ConnecterClass), 4567776144>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdStr' : 4567776144
   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstConnecter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (NetworkerClass),
4567892048>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4567800208>
   /   /   /  '<New><Instance>PreConnectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'SecondConnecterPointer' : < (PointerClass), 4567893776>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdStr' : 4567893776
   /   /   /   /   /  '<New><Instance>PointVariable' : < (ConnecterClass),
4567776208>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>IdStr' : 4567776208
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondConnecter
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(NetworkerClass), 4567892048>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4567800208>
   /   /   /   /   /   /  '<New><Instance>PostConnectomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /  'FirstConnecterPointer' : < (PointerClass),
4567893264>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdStr' : 4567893264
   /   /   /   /   /   /   /   /  '<New><Instance>PointVariable' : {...}<
(ConnecterClass), 4567776144>
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4567776144>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' :
PointVariable
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4567776144>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' :
PointVariable
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>TagStr' : Networked
   /   /   /   /   /   /  '<Spe><Instance>ConnectedAttentionDeriveConnectersList' :
[]
   /   /   /   /   /   /  '<Spe><Instance>ConnectedCatchDeriveConnectersList' :
[]
   /   /   /   /   /   /  '<Spe><Instance>ConnectingAttentionGetStrsList' : []
   /   /   /   /   /   /  '<Spe><Instance>ConnectingCatchGetStrsList' : []
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4567776208>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4567776208>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>TagStr' : Networked
   /   /   /  '<Spe><Instance>ConnectedAttentionDeriveConnectersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (ConnecterClass), 4567776144>
   /   /   /   /]
   /   /   /  '<Spe><Instance>ConnectedCatchDeriveConnectersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (ConnecterClass), 4567776144>
   /   /   /   /]
   /   /   /  '<Spe><Instance>ConnectingAttentionGetStrsList' :
['/NodePointDeriveNoder/<Connectome>SecondConnecter']
   /   /   /  '<Spe><Instance>ConnectingCatchGetStrsList' :
['/NodePointDeriveNoder/<Connectome>SecondConnecter']
   /   /   /}
   /   /  'SecondConnecter' : {...}< (ConnecterClass), 4567776208>
   /   /}
   /  '<New><Instance>IdStr' : 4567892048
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Instance>NetworkedConnectionTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : {...}< (ConnecterClass), 4567776144>
   /   /   /  1 :
   /   /   /   /[
   /   /   /   /  0 : {...}< (list), 4567866328>
   /   /   /   /  1 : {...}< (list), 4567898880>
   /   /   /   /]
   /   /   /)
   /   /  1 :
   /   /   /(
   /   /   /  0 : {...}< (ConnecterClass), 4567776208>
   /   /   /  1 :
   /   /   /   /[
   /   /   /   /  0 : {...}< (list), 4567867192>
   /   /   /   /  1 : {...}< (list), 4567833344>
   /   /   /   /]
   /   /   /)
   /   /]
   /  '<Spe><Instance>NetworkedDeriveConnectersList' :
   /   /[
   /   /  0 : {...}< (ConnecterClass), 4567776144>
   /   /  1 : {...}< (ConnecterClass), 4567776208>
   /   /]
   /}

*****End of the Attest *****



```

