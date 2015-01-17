

<!--
FrozenIsBool False
-->

#Transmitter

##Doc
----


>
> A Transmitter
>
>

----

<small>
View the Transmitter notebook on [NbViewer](http://nbviewer.ipython.org/url/shar
eyoursystem.ouvaton.org/Transmitter.ipynb)
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


A Transmitter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Networker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Itemizers import Pather
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class TransmitterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'TransmittingUpdateList',
'TransmittingCollectionStrsList',
'TransmittedVariablesList',
'TransmittingSelfIsBool'
                                                        ]

        def default_init(self,
                        _TransmittingUpdateList=None,
                        _TransmittingCollectionStrsList=None,
                        _TransmittingSelfIsBool=True,
                        _TransmittedVariablesList=None,
                        **_KwargVariablesDict
                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_transmit(self):

                #debug
                '''
                self.debug(('self.',self,['TransmittingSelfIsBool']))
                '''

                #Check
                if self.TransmittingSelfIsBool:

                        #update
                        self.update(self.TransmittingUpdateList)

                #map
                self.TransmittedVariablesList=SYS.flat(
                        map(
                                lambda __TransmittingCollectionStr:
                                map(
                                        lambda __DeriveNoderPointer:
                                        __DeriveNoderPointer.PointVariable,
                                        getattr(
                                                self,
__TransmittingCollectionStr+'CollectionOrderedDict'
                                        ).values()
                                ) if
hasattr(self,__TransmittingCollectionStr+'CollectionOrderedDict')
                                else [],
                                self.TransmittingCollectionStrsList
                        )
                )

                #command
                self.command(
                                                self.TransmittingUpdateList,
                                                self.TransmittedVariablesList,
                                                _GatherIsBool=False
                                        )

                #Return self
                #return self

#</DefineClass>


```

<small>
View the Transmitter sources on <a href="https://github.com/Ledoux/ShareYourSyst
em/tree/master/Pythonlogy/ShareYourSystem/Noders/Transmitter"
target="_blank">Github</a>
</small>




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
from ShareYourSystem.Noders import Transmitter
import operator

#Definition of a brian structure
MyTransmitter=Transmitter.TransmitterClass(
    ).push(
[
    (
        'First',
        Transmitter.TransmitterClass().update(
            [
                ('ConnectingCatchGetStrsList',
                    [
                        '/NodePointDeriveNoder/<Transmitome>SecondTransmitter'
                    ]
                ),
                ('ConnectingGraspClueVariablesList',
                    [
                        '/NodePointDeriveNoder/<Transmitome>SecondTransmitter'
                    ]
                ),
                ('TagStr','Networked')
            ]
        )
    ),
    (
        'Second',
        Transmitter.TransmitterClass().__setitem__(
            'TagStr',
            'Networked'
        )
    )
],
    **{
        'CollectingCollectionStr':'Transmitome'
    }
).network(
    **{
                'RecruitingConcludeConditionTuplesList':[
                    ('__class__.NameStr',operator.eq,'Transmitter')
                ]
        }
)

#transmit
MyTransmitter['<Transmitome>FirstTransmitter'].transmit(
    [('MyInt',0)],
    ['PostConnectome']
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyTransmitter is '+SYS._str(
        MyTransmitter,
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

                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                            ////////////////////////////////
                            Attentioner/__init__.py do_attention
                            From Attentioner/__init__.py do_attention |
Connecter/__init__.py do_connect | Networker/__init__.py do_network | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Notebooker/__init__.py
do_notebook | Informer/__init__.py do_inform | inform.py <module>
                            ////////////////////////////////

                            l.60 :
                            *****
                            I am with [('NodeKeyStr', 'FirstTransmitter')]
                            *****
                            self.AttentioningCollectionStr is PreConnectome
                            self.GraspingClueVariable is
/NodePointDeriveNoder/<Transmitome>SecondTransmitter

                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyTransmitter is < (TransmitterClass), 4555900496>
   /{
   /  '<New><Instance>IdInt' : 4555900496
   /  '<New><Instance>NetworkAttentionStr' : Pre
   /  '<New><Instance>NetworkCatchStr' : Post
   /  '<New><Instance>NetworkCollectionStr' : Connectome
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopTransmitter
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TransmitomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstTransmitter' : < (TransmitterClass), 4556050768>
   /   /   /{
   /   /   /  '<New><Instance>ConnectingCatchGetStrsList' :
['/NodePointDeriveNoder/<Transmitome>SecondTransmitter']
   /   /   /  '<New><Instance>IdInt' : 4556050768
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>NetworkAttentionStr' : Pre
   /   /   /  '<New><Instance>NetworkCatchStr' : Post
   /   /   /  '<New><Instance>NetworkCollectionStr' : Connectome
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Transmitome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstTransmitter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (TransmitterClass),
4555900496>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555996424>
   /   /   /  '<New><Instance>PostConnectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  '_NodePointDeriveNoder_<Transmitome>SecondTransmitterPointer'
: < (PointerClass), 4556051600>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4556051600
   /   /   /   /   /  '<New><Instance>PointVariable' : < (TransmitterClass),
4556050960>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>IdInt' : 4556050960
   /   /   /   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /   /   /   /  '<New><Instance>NetworkAttentionStr' : Pre
   /   /   /   /   /   /  '<New><Instance>NetworkCatchStr' : Post
   /   /   /   /   /   /  '<New><Instance>NetworkCollectionStr' : Connectome
   /   /   /   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Transmitome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondTransmitter
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(TransmitterClass), 4555900496>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4555996424>
   /   /   /   /   /   /  '<New><Instance>PreConnectomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /
'SecondTransmitter>TopTransmitter<FirstTransmitterPointer' : < (PointerClass),
4556052560>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdInt' : 4556052560
   /   /   /   /   /   /   /   /  '<New><Instance>PointVariable' : {...}<
(TransmitterClass), 4556050768>
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(TransmitterClass), 4556050768>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' :
PointVariable
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(TransmitterClass), 4556050768>
   /   /   /   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' :
PointVariable
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>TagStr' : Networked
   /   /   /   /   /   /  '<New><Instance>TransmitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>TransmittedVariablesList' : None
   /   /   /   /   /   /  '<Spe><Class>TransmittingCollectionStrsList' : None
   /   /   /   /   /   /  '<Spe><Class>TransmittingSelfIsBool' : True
   /   /   /   /   /   /  '<Spe><Class>TransmittingUpdateList' : None
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(TransmitterClass), 4556050960>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(TransmitterClass), 4556050960>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>TagStr' : Networked
   /   /   /  '<New><Instance>TransmitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>TransmittingSelfIsBool' : True
   /   /   /  '<Spe><Instance>TransmittedVariablesList' :
   /   /   /   /[
   /   /   /   /  0 : {...}< (TransmitterClass), 4556050960>
   /   /   /   /]
   /   /   /  '<Spe><Instance>TransmittingCollectionStrsList' :
['PostConnectome']
   /   /   /  '<Spe><Instance>TransmittingUpdateList' :
   /   /   /   /[
   /   /   /   /  0 : ('MyInt', 0)
   /   /   /   /]
   /   /   /}
   /   /  'SecondTransmitter' : {...}< (TransmitterClass), 4556050960>
   /   /}
   /  '<Spe><Class>TransmittedVariablesList' : None
   /  '<Spe><Class>TransmittingCollectionStrsList' : None
   /  '<Spe><Class>TransmittingSelfIsBool' : True
   /  '<Spe><Class>TransmittingUpdateList' : None
   /}

*****End of the Attest *****



```

