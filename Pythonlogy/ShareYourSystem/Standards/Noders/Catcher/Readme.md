

<!--
FrozenIsBool False
-->

#Catcher

##Doc
----


> Catcher instances grasps a Variable, sets a Pointer on it that will be then
collected
>
>

----

<small>
View the Catcher notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Catcher.ipynb)
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

Catcher instances grasps a Variable, sets a Pointer on it that will be then
collected

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Producer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Itemizers import Pointer
from ShareYourSystem.Standards.Noders import Noder
import collections
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CatcherClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'CatchingCollectionStr',
'CatchingUpdateVariable',
'CatchingNodeKeyStr',
'CatchingDefaultNodeKeyStrBool',
'CatchingDerivePointerClass',
'CatchingPointBackSetStr',
'CatchedGraspVariable',
'CatchedNodeKeyStr',
'CatchedDerivePointerVariable'
                                                        ]

        def default_init(self,
                                                _CatchingCollectionStr="",
                                                _CatchingUpdateVariable=None,
                                                _CatchingNodeKeyStr="",
_CatchingDefaultNodeKeyStrBool=True,
_CatchingDerivePointerClass=Pointer.PointerClass,
                                                _CatchingPointBackSetStr="",
                                                _CatchedGraspVariable=None,
                                                _CatchedNodeKeyStr="",
                                                _CatchedDerivePointerVariable=None,
                                                **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_catch(self):

                #debug
                '''
                self.debug(
                                        ('self.',self,[
'CollectingCollectionStr',
'GraspingClueVariable'
                                                                ])
                                )
                '''

                #grasp
                '''
                self.grasp(
                        self.GraspingClueVariable
                )
                '''

                #link
                if type(self.GraspingClueVariable)==SYS.GraspDictClass:
                        self.CatchingUpdateVariable=self.GraspingClueVariable

                #Defaut set for the collection keyStr
                if self.CatchingDefaultNodeKeyStrBool:

                        #Check
                        CatchedGetStr=">UnknowPath<"
                        if type(self.GraspingClueVariable) in SYS.StrTypesList:

                                #set
                                CatchedGetStr=self.GraspingClueVariable

                        elif type(self.GraspingClueVariable)==SYS.GraspDictClass
and type(
                                self.GraspingClueVariable['HintVariable']) in
SYS.StrTypesList:

                                #set
CatchedGetStr=self.GraspingClueVariable['HintVariable']

                        elif hasattr(self.GraspedAnswerVariable,'parent'):

                                #Get the up
                                CatchedUpNodeKeyStrsList=(self.parent(
).ParentedPathStr+'/'+self.NodeKeyStr).split('/')
                                CatchedUpNodeKeyStrsList.reverse()
CatchedUpPathStr='/'.join(CatchedUpNodeKeyStrsList[:-1])

                                #Get the down
CatchedDownNodeKeyStrsList=(self.GraspedAnswerVariable.parent(
).ParentedPathStr+'/'+self.GraspedAnswerVariable.NodeKeyStr).split('/')
CatchedDownPathStr='/'.join(CatchedDownNodeKeyStrsList[1:])

                                #Get the top
                                CatchedTopStr=CatchedUpNodeKeyStrsList[-1]

                                if
CatchedUpNodeKeyStrsList[-1]==CatchedDownNodeKeyStrsList[0]:

                                        #set
CatchedGetStr=CatchedUpPathStr+'>'+CatchedTopStr+'<'+CatchedDownPathStr

                        #set
                        self.CatchedNodeKeyStr=CatchedGetStr

                else:

                        #Look for one
                        self.CatchedNodeKeyStr=self.CatchingNodeKeyStr

                #adapt the
                self.CatchedNodeKeyStr=self.CatchedNodeKeyStr.replace('/','_')

                #debug
                '''
                self.debug(
                                        ('self.',self,[
'CatchingCollectionStr',
'CatchedNodeKeyStr'
                                                                ])
                                        )
                '''

                #Check
                if self.CatchingCollectionStr=="":
                        self.CatchingCollectionStr=self.CollectingCollectionStr

                #init
                self.CatchedDerivePointerVariable=self.CatchingDerivePointerClass(
                        **{
'PointingBackSetStr':self.CatchingPointBackSetStr
                        }
                ).point(
                        self.GraspedAnswerVariable,
                        'CatchToPointVariable'
                )

                #debug
                '''
                self.debug(
                                        ('self.',self,[
'CatchedDerivePointerVariable'
                                                                ])
                                        )
                '''

                #collect and update
                self.collect(
                        self.CatchingCollectionStr,
                        self.CatchedNodeKeyStr,
                        self.CatchedDerivePointerVariable
                )

                #set
                self.CatchedDerivePointerVariable.update(
                        self.CatchingUpdateVariable
                )

#</DefineClass>


```

<small>
View the Catcher sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Noders/Catcher" target="_blank">Github</a>
</small>



##Example

With a point back

```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Producer
from ShareYourSystem.Standards.Noders import Catcher

#Definition of an instance
MyProducer=Producer.ProducerClass().produce(
            ['First','Second'],
            Catcher.CatcherClass,
            **{'CollectingCollectionStr':"Pointome"}
        )

#point
MyProducer['<Pointome>FirstCatcher'].grasp(
            '/NodePointDeriveNoder/<Pointome>SecondCatcher'
        ).catch(
            _PointBackSetStr='MyBackVariable',
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


*****Start of the Attest *****

MyProducer is < (ProducerClass), 4555633296>
   /{
   /  '<New><Instance>IdInt' : 4555633296
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopProducer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>PointomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstCatcher' : < (CatcherClass), 4555633168>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555633168
   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstCatcher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (ProducerClass),
4555633296>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556379968>
   /   /   /  '<New><Instance>RelatomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  '_NodePointDeriveNoder_<Pointome>SecondCatcherPointer' : <
(PointerClass), 4555634512>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>IdInt' : 4555634512
   /   /   /   /   /  '<New><Instance>CatchToPointVariable' : < (CatcherClass),
4555633488>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>IdInt' : 4555633488
   /   /   /   /   /   /  '<New><Instance>MyBackVariable' : {...}<
(PointerClass), 4555634512>
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Pointome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondCatcher
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(ProducerClass), 4555633296>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4556379968>
   /   /   /   /   /   /  '<Spe><Class>CatchedDerivePointerVariable' : None
   /   /   /   /   /   /  '<Spe><Class>CatchedGraspVariable' : None
   /   /   /   /   /   /  '<Spe><Class>CatchedNodeKeyStr' :
   /   /   /   /   /   /  '<Spe><Class>CatchingCollectionStr' :
   /   /   /   /   /   /  '<Spe><Class>CatchingDefaultNodeKeyStrBool' : True
   /   /   /   /   /   /  '<Spe><Class>CatchingDerivePointerClass' : <class
'ShareYourSystem.Standards.Itemizers.Pointer.PointerClass'>
   /   /   /   /   /   /  '<Spe><Class>CatchingNodeKeyStr' :
   /   /   /   /   /   /  '<Spe><Class>CatchingPointBackSetStr' :
   /   /   /   /   /   /  '<Spe><Class>CatchingUpdateVariable' : None
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}<
(CatcherClass), 4555633488>
   /   /   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /   /   /  '<Spe><Instance>PointedPathBackVariable' : {...}<
(PointerClass), 4555634512>
   /   /   /   /   /  '<Spe><Instance>PointingBackSetStr' : MyBackVariable
   /   /   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}<
(CatcherClass), 4555633488>
   /   /   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<Spe><Class>CatchedGraspVariable' : None
   /   /   /  '<Spe><Class>CatchingDefaultNodeKeyStrBool' : True
   /   /   /  '<Spe><Class>CatchingDerivePointerClass' : {...}< (type),
140476488083952>
   /   /   /  '<Spe><Class>CatchingNodeKeyStr' :
   /   /   /  '<Spe><Class>CatchingUpdateVariable' : None
   /   /   /  '<Spe><Instance>CatchedDerivePointerVariable' : {...}< (PointerClass),
4555634512>
   /   /   /  '<Spe><Instance>CatchedNodeKeyStr' :
_NodePointDeriveNoder_<Pointome>SecondCatcher
   /   /   /  '<Spe><Instance>CatchingCollectionStr' : Relatome
   /   /   /  '<Spe><Instance>CatchingPointBackSetStr' : MyBackVariable
   /   /   /}
   /   /  'SecondCatcher' : {...}< (CatcherClass), 4555633488>
   /   /}
   /  '<Spe><Class>ProducingUpdateVariable' : None
   /  '<Spe><Instance>ProducedPushList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : First
   /   /   /  1 : {...}< (CatcherClass), 4555633168>
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : Second
   /   /   /  1 : {...}< (CatcherClass), 4555633488>
   /   /   /]
   /   /]
   /  '<Spe><Instance>ProducingCollectionKeyStrsList' : ['First', 'Second']
   /  '<Spe><Instance>ProducingPushClass' : <class
'ShareYourSystem.Standards.Noders.Catcher.CatcherClass'>
   /}

*****End of the Attest *****



```

