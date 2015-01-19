

<!--
FrozenIsBool False
-->

#Networker

##Doc
----


>
> A Networker
>
>

----

<small>
View the Networker notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Networker.ipynb)
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


A Networker

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Connecter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':["network"]})
class NetworkerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'NetworkedDeriveConnectersList',
'NetworkedConnectionTuplesList'
                                                                ]

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'CallingVariable':
BaseClass.__init__}]})
        def default_init(self,
_NetworkingSuffixStr="Connectome",
                                                _NetworkingCatchStr="Post",
                                                _NetworkingAttentionStr="Pre",
_NetworkedDeriveConnectersList=None,
_NetworkedConnectionTuplesList=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

                #map
                map(
                                lambda __KeyStr:
                                self.__setattr__(
                                                __KeyStr,
                                                ""
                                        ),
                                map(
                                                lambda __TagStr:
                                                'Newtork'+__TagStr+'Str',
['Collection','Catch','Attention']
                                        )
                        )

        def do_network(self):

                #recruit first
                if self.VisitingCollectionStrsList==None:
self.VisitingCollectionStrsList=[self.CollectingCollectionStr]

                #debug
                '''
                self.debug(('self.',self,['VisitingCollectionStrsList']))
                '''

                #recruit
                self.recruit()
self.NetworkedDeriveConnectersList=self.RecruitedFlatCumulateVariablesList

                #debug
                '''
                self.debug(('self.',self,['NetworkedDeriveConnectersList']))
                '''

                #map a connect
                self.NetworkedConnectionTuplesList=map(
                                lambda __NodedDeriveConnecter:
                                (
                                        __NodedDeriveConnecter,
                                        __NodedDeriveConnecter.connect(
                                                **{
'CatchingCollectionStr':self.NetworkingCatchStr+self.NetworkingSuffixStr,
'AttentioningCollectionStr':self.NetworkingAttentionStr+self.NetworkingSuffixStr
                                                }
                                        ).update(
                                                [
('NetworkCollectionStr',self.NetworkingSuffixStr),
('NetworkCatchStr',self.NetworkingCatchStr),
('NetworkAttentionStr',self.NetworkingAttentionStr)
                                                ]
                                        ).pick(
                                                [
'ConnectedAttentionDeriveConnectersList',
'ConnectedDerivePointersList'
                                                ]
                                        )
                                ),
                                self.NetworkedDeriveConnectersList
                )
#</DefineClass>

```

<small>
View the Networker sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Noders/Networker"
target="_blank">Github</a>
</small>



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
                ('ConnectingGraspClueVariablesList',
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
).network(
    **{
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

                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                            ////////////////////////////////
                            Attentioner/__init__.py do_attention
                            From Attentioner/__init__.py do_attention |
Connecter/__init__.py do_connect | Networker/__init__.py do_network | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Notebooker/__init__.py
do_notebook | Documenter/__init__.py do_inform | inform.py <module>
                            ////////////////////////////////

                            l.60 :
                            *****
                            I am with [('NodeKeyStr', 'FirstConnecter')]
                            *****
                            self.AttentioningCollectionStr is PreConnectome
                            self.GraspingClueVariable is
/NodePointDeriveNoder/<Connectome>SecondConnecter

                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyNetworker is < (NetworkerClass), 4555534992>
   /{
   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstConnecter' : < (ConnecterClass), 4555682512>
   /   /   /{
   /   /   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4555682512
   /   /   /  '<New><Instance>NetworkAttentionStr' : Pre
   /   /   /  '<New><Instance>NetworkCatchStr' : Post
   /   /   /  '<New><Instance>NetworkCollectionStr' : Connectome
   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstConnecter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (NetworkerClass),
4555534992>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555945200>
   /   /   /  '<New><Instance>PostConnectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  '_NodePointDeriveNoder_<Connectome>SecondConnecterPointer' : <
(PointerClass), 4555899792>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4555899792
   /   /   /   /   /  '<New><Instance>CatchToPointVariable' : < (ConnecterClass),
4555899088>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ConnectomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>IdInt' : 4555899088
   /   /   /   /   /   /  '<New><Instance>NetworkAttentionStr' : Pre
   /   /   /   /   /   /  '<New><Instance>NetworkCatchStr' : Post
   /   /   /   /   /   /  '<New><Instance>NetworkCollectionStr' : Connectome
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Connectome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondConnecter
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(NetworkerClass), 4555534992>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4555945200>
   /   /   /   /   /   /  '<New><Instance>PreConnectomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /
'SecondConnecter>TopNetworker<FirstConnecterPointer' : < (PointerClass),
4555901072>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdInt' : 4555901072
   /   /   /   /   /   /   /   /  '<New><Instance>CatchToPointVariable' : {...}<
(ConnecterClass), 4555682512>
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4555682512>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' :
CatchToPointVariable
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4555682512>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' :
CatchToPointVariable
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>TagStr' : Networked
   /   /   /   /   /   /  '<Spe><Instance>ConnectedDerivePointersList' : []
   /   /   /   /   /   /  '<Spe><Instance>ConnectingGraspClueVariablesList' : []
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(ConnecterClass), 4555899088>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(ConnecterClass), 4555899088>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>TagStr' : Networked
   /   /   /  '<Spe><Instance>ConnectedDerivePointersList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (ConnecterClass), 4555899088>
   /   /   /   /]
   /   /   /  '<Spe><Instance>ConnectingGraspClueVariablesList' :
['/NodePointDeriveNoder/<Connectome>SecondConnecter']
   /   /   /}
   /   /  'SecondConnecter' : {...}< (ConnecterClass), 4555899088>
   /   /}
   /  '<New><Instance>IdInt' : 4555534992
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopNetworker
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Instance>NetworkedConnectionTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : {...}< (ConnecterClass), 4555682512>
   /   /   /  1 :
   /   /   /   /[
   /   /   /   /  0 : None
   /   /   /   /  1 : {...}< (list), 4555922248>
   /   /   /   /]
   /   /   /)
   /   /  1 :
   /   /   /(
   /   /   /  0 : {...}< (ConnecterClass), 4555899088>
   /   /   /  1 :
   /   /   /   /[
   /   /   /   /  0 : None
   /   /   /   /  1 : {...}< (list), 4555696536>
   /   /   /   /]
   /   /   /)
   /   /]
   /  '<Spe><Instance>NetworkedDeriveConnectersList' :
   /   /[
   /   /  0 : {...}< (ConnecterClass), 4555682512>
   /   /  1 : {...}< (ConnecterClass), 4555899088>
   /   /]
   /}

*****End of the Attest *****



```

