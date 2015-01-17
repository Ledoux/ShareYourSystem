

<!--
FrozenIsBool False
-->

#Attentioner

##Doc
----


>
> Attentioner instances grasp a Variable and make inside a catch to the original
> instance
>
>

----

<small>
View the Attentioner notebook on [NbViewer](http://nbviewer.ipython.org/url/shar
eyoursystem.ouvaton.org/Attentioner.ipynb)
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


Attentioner instances grasp a Variable and make inside a catch to the original
instance

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Catcher"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Classors import Doer
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class AttentionerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'AttentioningCollectionStr'
                                                        ]

        def default_init(self,
                                                _AttentioningCollectionStr="",
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_attention(self):

                #debug
                '''
                self.debug(('self.',self,['CatchingCollectionStr']))
                '''

                #set
                if self.AttentioningCollectionStr=="":
self.AttentioningCollectionStr=self.CollectingCollectionStr

                #debug
                self.debug(
                                        ('self.',self,[
'AttentioningCollectionStr',
                                                        'GraspingClueVariable'
                                                        ])
                                )

                #poitn in the other way
                self.GraspedAnswerVariable.grasp(
                                self
                        ).catch(
                                self.AttentioningCollectionStr
                        )



#</DefineClass>


```

<small>
View the Attentioner sources on <a href="https://github.com/Ledoux/ShareYourSyst
em/tree/master/Pythonlogy/ShareYourSystem/Noders/Attentioner"
target="_blank">Github</a>
</small>



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
MyProducer['<Pointome>FirstAttentioner'].grasp(
        '/NodePointDeriveNoder/<Pointome>SecondAttentioner'
    ).attention(
        'BackRelatome'
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

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    ////////////////////////////////
                    Attentioner/__init__.py do_attention
                    From Attentioner/__init__.py do_attention | site-
packages/six.py exec_ | Celler/__init__.py do_cell | Notebooker/__init__.py
do_notebook | Informer/__init__.py do_inform | inform.py <module>
                    ////////////////////////////////

                    l.60 :
                    *****
                    I am with [('NodeKeyStr', 'FirstAttentioner')]
                    *****
                    self.AttentioningCollectionStr is BackRelatome
                    self.GraspingClueVariable is
/NodePointDeriveNoder/<Pointome>SecondAttentioner

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyProducer is < (ProducerClass), 4555536272>
   /{
   /  '<New><Instance>IdInt' : 4555536272
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopProducer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PointomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstAttentioner' : < (AttentionerClass), 4555633872>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555633872
   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstAttentioner
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4555536272>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556380560>
   /   /   /  '<Spe><Instance>AttentioningCollectionStr' : BackRelatome
   /   /   /}
   /   /  'SecondAttentioner' : < (AttentionerClass), 4555634960>
   /   /   /{
   /   /   /  '<New><Instance>BackRelatomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'SecondAttentioner>TopProducer<FirstAttentionerPointer' : <
(PointerClass), 4555635216>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4555635216
   /   /   /   /   /  '<New><Instance>PointVariable' : {...}<
(AttentionerClass), 4555633872>
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(AttentionerClass), 4555633872>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(AttentionerClass), 4555633872>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4555634960
   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondAttentioner
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4555536272>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556380560>
   /   /   /  '<Spe><Class>AttentioningCollectionStr' :
   /   /   /}
   /   /}
   /  '<Spe><Class>ProducingUpdateVariable' : None
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (AttentionerClass), 4555633872>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (AttentionerClass), 4555634960>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Noders.Attentioner.AttentionerClass'>
   /}

*****End of the Attest *****



```

