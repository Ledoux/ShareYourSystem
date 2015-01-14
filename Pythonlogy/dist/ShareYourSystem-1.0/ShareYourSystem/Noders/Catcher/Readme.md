
#Catcher
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



Catcher instances





<!--
FrozenIsBool False
-->

View the Catcher sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Noders/Installer)



```python

#ImportModules
import ShareYourSystem as SYS

from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Noders import Catcher

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
            ['First','Second'],
            Catcher.CatcherClass,
            **{'CollectingCollectionStr':"Pointome"}
        )

#point
MyProducer['<Pointome>FirstCatcher'].catch(
        '/NodePointDeriveNoder/<Pointome>SecondCatcher',
        **{
            'CollectingCollectionStr':'Relatome',
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

                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
////////////////////////////////
Doer/__init__.py do
                                                                    From
<string> superDo_debug | Catcher/__init__.py do_catch | Doer/__init__.py do |
<string> superDo_catch | Watcher/__init__.py watch | <string>
watch_superDo_catch | <string> <module> | <string> <module> | site-
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
[('NodeKeyStr', 'FirstCatcher')]
                                                                    *****
self.CollectingCollectionStr is Relatome

                                                                    xxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyProducer is < (ProducerClass), 4557088592>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdStr' : 4557088592
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PointomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstCatcher' : < (CatcherClass), 4557132112>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>IdStr' : 4557132112
   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstCatcher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4557088592>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557084480>
   /   /   /  '<New><Instance>RelatomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'SecondCatcherPointer' : < (PointerClass), 4557089808>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdStr' : 4557089808
   /   /   /   /   /  '<New><Instance>PointVariable' : < (CatcherClass),
4557133520>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>IdStr' : 4557133520
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondCatcher
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(ProducerClass), 4557088592>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4557084480>
   /   /   /   /   /   /  '<Spe><Class>CatchedGetVariable' : None
   /   /   /   /   /   /  '<Spe><Class>CatchingCollectionStr' :
   /   /   /   /   /   /  '<Spe><Class>CatchingDefaultNodeKeyStrBool' : True
   /   /   /   /   /   /  '<Spe><Class>CatchingGetVariable' :
   /   /   /   /   /   /  '<Spe><Class>CatchingDerivePointerClass' : <class
'ShareYourSystem.Itemizers.Pointer.PointerClass'>
   /   /   /   /   /   /  '<Spe><Class>CatchingNodeKeyStr' :
   /   /   /   /   /   /  '<Spe><Class>CatchingPointBackBool' : False
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Class>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(CatcherClass), 4557133520>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(CatcherClass), 4557133520>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>CatchingDefaultNodeKeyStrBool' : True
   /   /   /  '<Spe><Class>CatchingDerivePointerClass' : {...}< (type), 140533540739184>
   /   /   /  '<Spe><Class>CatchingNodeKeyStr' :
   /   /   /  '<Spe><Class>CatchingPointBackBool' : False
   /   /   /  '<Spe><Instance>CatchedGetVariable' : {...}< (CatcherClass),
4557133520>
   /   /   /  '<Spe><Instance>CatchingCollectionStr' : Relatome
   /   /   /  '<Spe><Instance>CatchingGetVariable' :
/NodePointDeriveNoder/<Pointome>SecondCatcher
   /   /   /}
   /   /  'SecondCatcher' : {...}< (CatcherClass), 4557133520>
   /   /}
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (CatcherClass), 4557132112>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (CatcherClass), 4557133520>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingUpdateVariable' :
   /   /{
   /   /}
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Catcher.CatcherClass'>
   /}

*****End of the Attest *****



```

