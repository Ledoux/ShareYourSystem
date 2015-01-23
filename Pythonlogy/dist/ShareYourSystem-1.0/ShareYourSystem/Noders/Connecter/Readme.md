

<!--
FrozenIsBool False
-->

#Connecter

##Doc
----


> Connecter instances catch grasped variables and makes an attention also on it.
>
>

----

<small>
View the Connecter notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Connecter.ipynb)
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

Connecter instances catch grasped variables and makes an attention also on it.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Mobilizer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class ConnecterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'ConnectingGraspClueVariablesList',
'ConnectedCatchDerivePointersList'
                                                        ]

        def default_init(self,
_ConnectingGraspClueVariablesList=None,
_ConnectedCatchDerivePointersList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_connect(self):

                #debug
                '''
                self.debug(('self.',self,['ConnectingGraspClueVariablesList']))
                '''

                #catch
                self.ConnectedCatchDerivePointersList=map(
                                lambda __ConnectingGraspVariable:
                                self.grasp(
                                                __ConnectingGraspVariable
                                        ).catch(
                                        ).attention(
                                        ).GraspedAnswerVariable,
                                self.ConnectingGraspClueVariablesList
                        )

#</DefineClass>

```

<small>
View the Connecter sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Noders/Connecter"
target="_blank">Github</a>
</small>





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
MyProducer['<Connectome>FirstConnecter'].connect(
    [
        '/NodePointDeriveNoder/<Connectome>SecondConnecter',
        SYS.GraspDictClass(**{'MyInt':0,'HintVariable':MyProducer['<Connectome>F
irstConnecter']})
    ],
    **{
        'CatchingCollectionStr':"PostRelatome",
        'AttentioningCollectionStr':"PreRelatome",
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

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        ////////////////////////////////
                        Attentioner/__init__.py do_attention
                        From Attentioner/__init__.py do_attention |
Connecter/__init__.py do_connect | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Documenter/__init__.py do_inform | inform.py <module>
                        ////////////////////////////////

                        l.60 :
                        *****
                        I am with [('NodeKeyStr', 'FirstConnecter')]
                        *****
                        self.AttentioningCollectionStr is PreRelatome
                        self.GraspingClueVariable is
/NodePointDeriveNoder/<Connectome>SecondConnecter

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                        ////////////////////////////////
                        Attentioner/__init__.py do_attention
                        From Attentioner/__init__.py do_attention |
Connecter/__init__.py do_connect | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Documenter/__init__.py do_inform | inform.py <module>
                        ////////////////////////////////

                        l.60 :
                        *****
                        I am with [('NodeKeyStr', 'FirstConnecter')]
                        *****
                        self.AttentioningCollectionStr is PreRelatome
                        self.GraspingClueVariable is GraspDictClass([('MyInt',
0), ('HintVariable', < (ConnecterClass), 4555535376>
                           /{
                           /  '<New><Instance>IdInt' : 4555535376
                           /  '<New><Instance>NodeCollectionStr' : Connectome
                           /  '<New><Instance>NodeIndexInt' : 0
                           /  '<New><Instance>NodeKeyStr' : FirstConnecter
                           /  '<New><Instance>NodePointDeriveNoder' : <
(ProducerClass), 4555535312>
                           /   /{
                           /   /
'<New><Instance>ConnectomeCollectionOrderedDict' :
                           /   /   /{
                           /   /   /  'FirstConnecter' : < (ConnecterClass),
4555535376>
                           /   /   /   /{
                           /   /   /   /  '<New><Instance>IdInt' : 4555535376
                           /   /   /   /  '<New><Instance>NodeCollectionStr' :
Connectome
                           /   /   /   /  '<New><Instance>NodeIndexInt' : 0
                           /   /   /   /  '<New><Instance>NodeKeyStr' :
FirstConnecter
                           /   /   /   /  '<New><Instance>NodePointDeriveNoder'
: {...}< (ProducerClass), 4555535312>
                           /   /   /   /  '<New><Instance>NodePointOrderedDict'
: {...}< (OrderedDict), 4555735416>
                           /   /   /   /
'<New><Instance>PostRelatomeCollectionOrderedDict' :
                           /   /   /   /   /{
                           /   /   /   /   /
'_NodePointDeriveNoder_<Connectome>SecondConnecterPointer' : < (PointerClass),
4555684304>
                           /   /   /   /   /   /{
                           /   /   /   /   /   /  '<New><Instance>IdInt' :
4555684304
                           /   /   /   /   /   /  '<New><Instance>CatchToPointVariable'
: < (ConnecterClass), 4555683216>
                           /   /   /   /   /   /   /{
                           /   /   /   /   /   /   /  '<New><Instance>IdInt' :
4555683216
                           /   /   /   /   /   /   /
'<New><Instance>NodeCollectionStr' : Connectome
                           /   /   /   /   /   /   /
'<New><Instance>NodeIndexInt' : 1
                           /   /   /   /   /   /   /
'<New><Instance>NodeKeyStr' : SecondConnecter
                           /   /   /   /   /   /   /
'<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass), 4555535312>
                           /   /   /   /   /   /   /
'<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict), 4555735416>
                           /   /   /   /   /   /   /
'<New><Instance>PreRelatomeCollectionOrderedDict' :
                           /   /   /   /   /   /   /   /{
                           /   /   /   /   /   /   /   /
'SecondConnecter>TopProducer<FirstConnecterPointer' : < (PointerClass),
4555685072>
                           /   /   /   /   /   /   /   /   /{
                           /   /   /   /   /   /   /   /   /
'<New><Instance>IdInt' : 4555685072
                           /   /   /   /   /   /   /   /   /
'<New><Instance>CatchToPointVariable' : {...}< (ConnecterClass), 4555535376>
                           /   /   /   /   /   /   /   /   /
'<Spe><Class>PointedBackSetStr' :
                           /   /   /   /   /   /   /   /   /
'<Spe><Class>PointedPathBackVariable' :
                           /   /   /   /   /   /   /   /   /
'<Spe><Instance>PointedGetVariable' : {...}< (ConnecterClass), 4555535376>
                           /   /   /   /   /   /   /   /   /
'<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
                           /   /   /   /   /   /   /   /   /
'<Spe><Instance>PointingBackSetStr' :
                           /   /   /   /   /   /   /   /   /
'<Spe><Instance>PointingGetVariable' : {...}< (ConnecterClass), 4555535376>
                           /   /   /   /   /   /   /   /   /
'<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
                           /   /   /   /   /   /   /   /   /}
                           /   /   /   /   /   /   /   /}
                           /   /   /   /   /   /   /
'<New><Instance>WatchParentWithParenterBool' : True
                           /   /   /   /   /   /   /
'<Spe><Class>ConnectedCatchDerivePointersList' : None
                           /   /   /   /   /   /   /
'<Spe><Class>ConnectingGraspClueVariablesList' : None
                           /   /   /   /   /   /   /}
                           /   /   /   /   /   /
'<Spe><Class>PointedBackSetStr' :
                           /   /   /   /   /   /
'<Spe><Class>PointedPathBackVariable' :
                           /   /   /   /   /   /
'<Spe><Instance>PointedGetVariable' : {...}< (ConnecterClass), 4555683216>
                           /   /   /   /   /   /
'<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
                           /   /   /   /   /   /
'<Spe><Instance>PointingBackSetStr' :
                           /   /   /   /   /   /
'<Spe><Instance>PointingGetVariable' : {...}< (ConnecterClass), 4555683216>
                           /   /   /   /   /   /
'<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
                           /   /   /   /   /   /}
                           /   /   /   /   /
'FirstConnecter>TopProducer<FirstConnecterPointer' : < (PointerClass),
4555684560>
                           /   /   /   /   /   /{
                           /   /   /   /   /   /  '<New><Instance>HintVariable'
: {...}< (ConnecterClass), 4555535376>
                           /   /   /   /   /   /  '<New><Instance>IdInt' :
4555684560
                           /   /   /   /   /   /  '<New><Instance>MyInt' : 0
                           /   /   /   /   /   /  '<New><Instance>CatchToPointVariable'
: {...}< (ConnecterClass), 4555535376>
                           /   /   /   /   /   /
'<Spe><Class>PointedBackSetStr' :
                           /   /   /   /   /   /
'<Spe><Class>PointedPathBackVariable' :
                           /   /   /   /   /   /
'<Spe><Instance>PointedGetVariable' : {...}< (ConnecterClass), 4555535376>
                           /   /   /   /   /   /
'<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
                           /   /   /   /   /   /
'<Spe><Instance>PointingBackSetStr' :
                           /   /   /   /   /   /
'<Spe><Instance>PointingGetVariable' : {...}< (ConnecterClass), 4555535376>
                           /   /   /   /   /   /
'<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
                           /   /   /   /   /   /}
                           /   /   /   /   /}
                           /   /   /   /
'<New><Instance>WatchParentWithParenterBool' : True
                           /   /   /   /
'<Spe><Instance>ConnectedCatchDerivePointersList' : []
                           /   /   /   /
'<Spe><Instance>ConnectingGraspClueVariablesList' :
                           /   /   /   /   /[
                           /   /   /   /   /  0 :
/NodePointDeriveNoder/<Connectome>SecondConnecter
                           /   /   /   /   /  1 : {...}< (GraspDictClass),
4555735120>
                           /   /   /   /   /]
                           /   /   /   /}
                           /   /   /  'SecondConnecter' : {...}<
(ConnecterClass), 4555683216>
                           /   /   /}
                           /   /  '<New><Instance>IdInt' : 4555535312
                           /   /  '<New><Instance>NodeCollectionStr' : Globals
                           /   /  '<New><Instance>NodeIndexInt' : -1
                           /   /  '<New><Instance>NodeKeyStr' : TopProducer
                           /   /  '<New><Instance>NodePointDeriveNoder' : None
                           /   /  '<New><Instance>NodePointOrderedDict' : None
                           /   /  '<New><Instance>WatchParentWithParenterBool' :
True
                           /   /  '<Spe><Class>ProducingUpdateVariable' : None
                           /   /  '<Spe><Instance>ProducedPushList' :
                           /   /   /[
                           /   /   /  0 :
                           /   /   /   /[
                           /   /   /   /  0 : First
                           /   /   /   /  1 : {...}< (ConnecterClass),
4555535376>
                           /   /   /   /]
                           /   /   /  1 :
                           /   /   /   /[
                           /   /   /   /  0 : Second
                           /   /   /   /  1 : {...}< (ConnecterClass),
4555683216>
                           /   /   /   /]
                           /   /   /]
                           /   /
'<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
                           /   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Connecter.ConnecterClass'>
                           /   /}
                           /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4555735416>
                           /  '<New><Instance>PostRelatomeCollectionOrderedDict'
: {...}< (OrderedDict), 4555736008>
                           /  '<New><Instance>WatchParentWithParenterBool' :
True
                           /  '<Spe><Instance>ConnectedCatchDerivePointersList' :
{...}< (list), 4555696536>
                           /  '<Spe><Instance>ConnectingGraspClueVariablesList'
: {...}< (list), 4555751936>
                           /})])

                        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyProducer is < (ProducerClass), 4555535312>
   /{
   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstConnecter' : < (ConnecterClass), 4555535376>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555535376
   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstConnecter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4555535312>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555735416>
   /   /   /  '<New><Instance>PostRelatomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  '_NodePointDeriveNoder_<Connectome>SecondConnecterPointer' : <
(PointerClass), 4555684304>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4555684304
   /   /   /   /   /  '<New><Instance>CatchToPointVariable' : < (ConnecterClass),
4555683216>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>IdInt' : 4555683216
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondConnecter
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(ProducerClass), 4555535312>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4555735416>
   /   /   /   /   /   /  '<New><Instance>PreRelatomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /
'SecondConnecter>TopProducer<FirstConnecterPointer' : < (PointerClass),
4555685072>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdInt' : 4555685072
   /   /   /   /   /   /   /   /  '<New><Instance>CatchToPointVariable' : {...}<
(ConnecterClass), 4555535376>
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4555535376>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' :
CatchToPointVariable
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4555535376>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' :
CatchToPointVariable
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>ConnectedCatchDerivePointersList' : None
   /   /   /   /   /   /  '<Spe><Class>ConnectingGraspClueVariablesList' : None
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4555683216>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4555683216>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /   /   /}
   /   /   /   /  'FirstConnecter>TopProducer<FirstConnecterPointer' : <
(PointerClass), 4555684560>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>HintVariable' : {...}< (ConnecterClass),
4555535376>
   /   /   /   /   /  '<New><Instance>IdInt' : 4555684560
   /   /   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /   /   /  '<New><Instance>CatchToPointVariable' : {...}< (ConnecterClass),
4555535376>
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4555535376>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4555535376>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>PreRelatomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'FirstConnecter>TopProducer<FirstConnecterPointer' : <
(PointerClass), 4555684816>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>HintVariable' : {...}< (ConnecterClass),
4555535376>
   /   /   /   /   /  '<New><Instance>IdInt' : 4555684816
   /   /   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /   /   /  '<New><Instance>CatchToPointVariable' : {...}< (ConnecterClass),
4555535376>
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4555535376>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4555535376>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Instance>ConnectedCatchDerivePointersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (ConnecterClass), 4555683216>
   /   /   /   /  1 : {...}< (ConnecterClass), 4555535376>
   /   /   /   /]
   /   /   /  '<Spe><Instance>ConnectingGraspClueVariablesList' :
   /   /   /   /[
   /   /   /   /  0 : /NodePointDeriveNoder/<Connectome>SecondConnecter
   /   /   /   /  1 : GraspDictClass([('MyInt', 0), ('HintVariable', <
(ConnecterClass), 4555535376>
   /{
   /  '<New><Instance>IdInt' : 4555535376
   /  '<New><Instance>NodeCollectionStr' : Connectome
   /  '<New><Instance>NodeIndexInt' : 0
   /  '<New><Instance>NodeKeyStr' : FirstConnecter
   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4555535312>
   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict), 4555735416>
   /  '<New><Instance>PostRelatomeCollectionOrderedDict' : {...}< (OrderedDict),
4555736008>
   /  '<New><Instance>PreRelatomeCollectionOrderedDict' : {...}< (OrderedDict),
4555735712>
   /  '<New><Instance>WatchParentWithParenterBool' : True
   /  '<Spe><Instance>ConnectedCatchDerivePointersList' : {...}< (list), 4555689784>
   /  '<Spe><Instance>ConnectingGraspClueVariablesList' : {...}< (list),
4555751936>
   /})])
   /   /   /   /]
   /   /   /}
   /   /  'SecondConnecter' : {...}< (ConnecterClass), 4555683216>
   /   /}
   /  '<New><Instance>IdInt' : 4555535312
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopProducer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>ProducingUpdateVariable' : None
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (ConnecterClass), 4555535376>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (ConnecterClass), 4555683216>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Connecter.ConnecterClass'>
   /}

*****End of the Attest *****



```

