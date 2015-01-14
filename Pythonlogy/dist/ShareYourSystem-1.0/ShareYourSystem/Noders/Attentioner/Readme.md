
#Attentioner
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



Attentioner instances





<!--
FrozenIsBool False
-->

View the Attentioner sources on [Github](https://github.com/Ledoux/ShareYourSyst
em/tree/master/ShareYourSystem/Noders/Installer)



```python

#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Attentioner

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
            ['First','Second'],
            Attentioner.AttentionerClass,
            **{'CollectingCollectionStr':"Pointome"}
        )

#attention
MyProducer['<Pointome>FirstAttentioner'].attention(
        'BackRelatome',
        **{
'CatchingGetVariable':'/NodePointDeriveNoder/<Pointome>SecondAttentioner',
                'CatchingCollectionStr':'Relatome'
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

Doer l.132 : DoerStr is Attentioner
DoStr is Attention
DoMethodStr is attention
DoingStr is Attentioning
DoneStr is Attentioned


        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx
        ////////////////////////////////
        Doer/__init__.py do
        From <string> superDo_debug | Catcher/__init__.py do_catch |
Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py watch |
<string> watch_superDo_catch | Attentioner/__init__.py do_attention |
Doer/__init__.py do | <string> superDo_attention | Watcher/__init__.py watch |
<string> watch_superDo_attention | <string> <module> | <string> <module> | site-
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
        I am with [('NodeKeyStr', 'FirstAttentioner')]
        *****
        self.CollectingCollectionStr is

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx


        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx
        ////////////////////////////////
        Doer/__init__.py do
        From <string> superDo_debug | Catcher/__init__.py do_catch |
Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py watch |
<string> watch_superDo_catch | Attentioner/__init__.py do_attention |
Doer/__init__.py do | <string> superDo_attention | Watcher/__init__.py watch |
<string> watch_superDo_attention | <string> <module> | <string> <module> | site-
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
        I am with [('NodeKeyStr', 'SecondAttentioner')]
        *****
        self.CollectingCollectionStr is BackRelatome

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyProducer is < (ProducerClass), 4556931728>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdStr' : 4556931728
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PointomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstAttentioner' : < (AttentionerClass), 4557045392>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdStr' : 4557045392
   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstAttentioner
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4556931728>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557083592>
   /   /   /  '<New><Instance>RelatomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'SecondAttentionerPointer' : < (PointerClass), 4557088528>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdStr' : 4557088528
   /   /   /   /   /  '<New><Instance>PointVariable' : < (AttentionerClass),
4557087888>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>BackRelatomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /  'FirstAttentionerPointer' : < (PointerClass),
4556882128>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdStr' : 4556882128
   /   /   /   /   /   /   /   /  '<New><Instance>PointVariable' : {...}<
(AttentionerClass), 4557045392>
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(AttentionerClass), 4557045392>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' :
PointVariable
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(AttentionerClass), 4557045392>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' :
PointVariable
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>IdStr' : 4557087888
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondAttentioner
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(ProducerClass), 4556931728>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4557083592>
   /   /   /   /   /   /  '<Spe><Class>AttentioningCollectionStr' :
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(AttentionerClass), 4557087888>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(AttentionerClass), 4557087888>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Instance>AttentioningCollectionStr' : BackRelatome
   /   /   /}
   /   /  'SecondAttentioner' : {...}< (AttentionerClass), 4557087888>
   /   /}
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (AttentionerClass), 4557045392>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (AttentionerClass), 4557087888>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingInitiateDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Attentioner.AttentionerClass'>
   /}

*****End of the Attest *****



```

