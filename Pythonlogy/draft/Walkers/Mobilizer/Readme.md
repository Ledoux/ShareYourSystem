

<!--
FrozenIsBool False
-->

#Mobilizer

##Doc
----


>
> A Mobilizer
>
>

----

<small>
View the Mobilizer notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Mobilizer.ipynb)
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


A Mobilizer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Walkers.Recruiter"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Standards.Classors import Deriver
from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineFunctions>
def getMobilizedIsBoolWithParentClassAndDeriveClassesList(
        _ParentClass,_DeriveClassesList):

        #Debug
        '''
        print('Mobilizer l.37')
        print('_ParentClass is ',_ParentClass)
        print('_DeriveClassesList is ',_DeriveClassesList)
        print('')
        '''

        #Return
        return any(
                                map(
                                        lambda __DeriveClass:
Deriver.getIsDerivedBoolWithParentClassAndDeriveClass(
                                                _ParentClass,
                                                __DeriveClass
                                        ),
                                        _DeriveClassesList
                                )
                        )


#<DefineFunctions>

#<DefineClass>
@DecorationClass()
class MobilizerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'MobilizingNameStrsList'
                                                                ]

        def default_init(self,
                                _MobilizingNameStrsList=None,
                                _MobilizingCollectionSuffixStr="Figurome",
                                _MobilizedAttestClassesList=None,
                                **_KwargVariablesDict
                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_mobilize(self):

                #Check
                if self.VisitingCollectionStrsList==None:
                        self.VisitingCollectionStrsList=[
                                self.CollectingCollectionStr
                        ]

                #map
                self.MobilizedAttestClassesList=map(
                        SYS.getClassWithNameStr,
                        self.MobilizingNameStrsList
                )

                #debug
                '''
                self.debug(('self.',self,['MobilizedAttestClassesList']))
                '''

                #append
                self.RecruitingConcludeConditionVariable.append(
                                (
                                        '__class__',
getMobilizedIsBoolWithParentClassAndDeriveClassesList,
                                        self.MobilizedAttestClassesList
                                )
                        )

                #debug
                '''
self.debug(('self.',self,['RecruitingConcludeConditionVariable']))
                '''

                #recruit
                self.recruit()

                #debug
                '''
self.debug(('self.',self,['RecruitedFlatCumulateVariablesList']))
                '''

                #Split the different names into different collections
                map(
                                lambda __RecruitedFlatCollectVariable:
                                self.grasp(
                                                __RecruitedFlatCollectVariable
                                        ).catch(
                                                __RecruitedFlatCollectVariable._
_class__.NameStr+self.MobilizingCollectionSuffixStr,
                                        ),
                                self.RecruitedFlatCumulateVariablesList
                        )
#</DefineClass>

```

<small>
View the Mobilizer sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Walkers/Mobilizer"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Walkers import Visiter,Recruiter,Mobilizer
import operator

#Definition a Mobilizer instance that is grouped
MyMobilizer=Mobilizer.MobilizerClass().update(
    [
        (
            '<Mobilizome>FirstChildMobilizer',
            Mobilizer.MobilizerClass().update(
                [
                    (
                        '<Recruitome>GrandChildRecruiter',
                        Recruiter.RecruiterClass()
                    ),
                    (
                        '<Recruitome>FakeGrandChildVisiter',
                        Visiter.VisiterClass()
                    )
                ]
            )
        ),
        (
            '<Mobilizome>SecondChildMobilizer',
            Mobilizer.MobilizerClass()
        ),
        (
            '<Mobilizome>ThirdChildMobilizer',
            Mobilizer.MobilizerClass()
        )
    ]
)

#Walk inside the group in order to parent
MyMobilizer.mobilize(
    [
        'Mobilizer','Recruiter'
    ],
    **{
            'VisitingCollectionStrsList':['Mobilizome','Recruitome'],
            'RecruitingConcludeConditionVariable':[
            ('NodeIndexInt',lambda _TestInt,_AttestInt:
                _TestInt!=None and operator.lt(_TestInt,_AttestInt),2)
            ]
    }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyMobilizer is '+SYS._str(
        MyMobilizer,
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

MyMobilizer is < (MobilizerClass), 4556651536>
   /{
   /  '<New><Instance>IdInt' : 4556651536
   /  '<New><Instance>MobilizerFiguromeCollectionOrderedDict' :
   /   /{
   /   /  'TopMobilizer><TopMobilizerPointer' : < (PointerClass), 4555536912>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555536912
   /   /   /  '<New><Instance>CatchToPointVariable' : {...}< (MobilizerClass),
4556651536>
   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}< (MobilizerClass),
4556651536>
   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}< (MobilizerClass),
4556651536>
   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /}
   /   /  '>UnknowPath<Pointer' : < (PointerClass), 4559654096>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4559654096
   /   /   /  '<New><Instance>CatchToPointVariable' : < (MobilizerClass), 4555535760>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4555535760
   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /}
   /   /   /   /  '<New><Instance>NodeCollectionStr' : Mobilizome
   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildMobilizer
   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4556651536>
   /   /   /   /  '<New><Instance>NodePointOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /  'FirstChildMobilizer' : < (MobilizerClass), 4556971024>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>IdInt' : 4556971024
   /   /   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Mobilizome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildMobilizer
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4556651536>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559683664>
   /   /   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /  'GrandChildRecruiter' : < (RecruiterClass),
4555536784>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdInt' : 4555536784
   /   /   /   /   /   /   /   /
'<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' :
Recruitome
   /   /   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' :
GrandChildRecruiter
   /   /   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4556971024>
   /   /   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4555558448>
   /   /   /   /   /   /   /   /
'<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /   /
'<Spe><Class>RecruitedFlatCumulateVariablesList' : None
   /   /   /   /   /   /   /   /
'<Spe><Class>RecruitingConcludeConditionVariable' : None
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /  'FakeGrandChildVisiter' : < (VisiterClass),
4555536720>
   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /  '<New><Instance>IdInt' : 4555536720
   /   /   /   /   /   /   /   /
'<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' :
Recruitome
   /   /   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' :
FakeGrandChildVisiter
   /   /   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4556971024>
   /   /   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4555558448>
   /   /   /   /   /   /   /   /
'<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /   /  '<Spe><Class>VisitingAfterUpdateList' : None
   /   /   /   /   /   /   /   /  '<Spe><Class>VisitingBeforeUpdateList' : None
   /   /   /   /   /   /   /   /  '<Spe><Class>VisitingCollectionStrsList' :
None
   /   /   /   /   /   /   /   /}
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>MobilizingNameStrsList' : None
   /   /   /   /   /   /}
   /   /   /   /   /  'SecondChildMobilizer' : {...}< (MobilizerClass),
4555535760>
   /   /   /   /   /  'ThirdChildMobilizer' : < (MobilizerClass), 4559653008>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>IdInt' : 4559653008
   /   /   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Mobilizome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildMobilizer
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4556651536>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559683664>
   /   /   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>MobilizingNameStrsList' : None
   /   /   /   /   /   /}
   /   /   /   /   /}
   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /}
   /   /   /   /  '<Spe><Class>MobilizingNameStrsList' : None
   /   /   /   /}
   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}< (MobilizerClass),
4555535760>
   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}< (MobilizerClass),
4555535760>
   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /}
   /   /}
   /  '<New><Instance>MobilizomeCollectionOrderedDict' : {...}< (OrderedDict),
4559683664>
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopMobilizer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>RecruiterFiguromeCollectionOrderedDict' :
   /   /{
   /   /  '>UnknowPath<Pointer' : < (PointerClass), 4555537232>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555537232
   /   /   /  '<New><Instance>CatchToPointVariable' : {...}< (RecruiterClass),
4555536784>
   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}< (RecruiterClass),
4555536784>
   /   /   /  '<Spe><Instance>PointedLocalSetStr' : CatchToPointVariable
   /   /   /  '<Spe><Instance>PointingBackSetStr' :
   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}< (RecruiterClass),
4555536784>
   /   /   /  '<Spe><Instance>PointingSetPathStr' : CatchToPointVariable
   /   /   /}
   /   /}
   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>MobilizingNameStrsList' : ['Mobilizer', 'Recruiter']
   /}

*****End of the Attest *****



```

