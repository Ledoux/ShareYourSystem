

<!--
FrozenIsBool False
-->

#Recruiter

##Doc
----


>
> A Recruiter
>
>

----

<small>
View the Recruiter notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Recruiter.ipynb)
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


A Recruiter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Visiter"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RecruiterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'RecruitingConcludeConditionTuplesList',
'RecruitedFlatCumulateVariablesList'
                                                                ]

        def default_init(self,
                                _RecruitingConcludeConditionTuplesList=None,
                                _RecruitedFlatCumulateVariablesList=None,
                                **_KwargVariablesDict
                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_recruit(self):

                #Check
                if type(self.VisitingBeforeUpdateList)!=list:
                        self.VisitingBeforeUpdateList=[]

                #add
                self.VisitingBeforeUpdateList+=[
                        (
                                'PickingGetKeyVariablesList',['/']
                        ),
                        (
                                'ConcludingConditionTuplesList',
                                self.RecruitingConcludeConditionTuplesList
                        ),
                        ('cumulate',{'LiargVariablesList':[]})
                ]

                #visit
                self.visit()

                #flat
                self.RecruitedFlatCumulateVariablesList=SYS.filterNone(SYS.flat(
                        self.CumulatedVariablesList
                        )
                )
#</DefineClass>

```

<small>
View the Recruiter sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Walkers/Recruiter"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Cumulater,Recruiter
import operator

#Definition a Recruiter instance that is grouped
MyRecruiter=Recruiter.RecruiterClass().update(
        [
            (
                '<Visitome>FirstChildRecruiter',
                Recruiter.RecruiterClass().update(
                    [
                        (
                            '<Collectome>GrandChildCumulater',
                            Cumulater.CumulaterClass()
                        )
                    ]
                )
            ),
            (
                '<Visitome>SecondChildRecruiter',
                Recruiter.RecruiterClass()
            ),
            (
                '<Visitome>ThirdChildRecruiter',
                Recruiter.RecruiterClass()
            )
        ]
    )

#Walk inside the group in order to parent
MyRecruiter.recruit(
    [
        (
            'NodeIndexInt',
            lambda
_TestIndexInt,_AttestIndexInt:operator.lt(_TestIndexInt,_AttestIndexInt)
            if _TestIndexInt!=None else False,
            2
        )
    ],
    **{'VisitingCollectionStrsList':['Visitome','Collectome']}
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyRecruiter is '+SYS._str(
        MyRecruiter,
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

MyRecruiter is < (RecruiterClass), 4555498384>
   /{
   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<New><Instance>IdInt' : 4555498384
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopRecruiter
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildRecruiter' : < (RecruiterClass), 4556356176>
   /   /   /{
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildCumulater' : < (CumulaterClass), 4557708048>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdInt' : 4557708048
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Collectome
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildCumulater
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(RecruiterClass), 4556356176>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4537423384>
   /   /   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4556356176
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildRecruiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RecruiterClass),
4555498384>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4537424272>
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>RecruitedFlatCumulateVariablesList' : None
   /   /   /  '<Spe><Class>RecruitingConcludeConditionTuplesList' : None
   /   /   /}
   /   /  'SecondChildRecruiter' : < (RecruiterClass), 4556968016>
   /   /   /{
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4556968016
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildRecruiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RecruiterClass),
4555498384>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4537424272>
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>RecruitedFlatCumulateVariablesList' : None
   /   /   /  '<Spe><Class>RecruitingConcludeConditionTuplesList' : None
   /   /   /}
   /   /  'ThirdChildRecruiter' : < (RecruiterClass), 4556968208>
   /   /   /{
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4556968208
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildRecruiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RecruiterClass),
4555498384>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4537424272>
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>RecruitedFlatCumulateVariablesList' : None
   /   /   /  '<Spe><Class>RecruitingConcludeConditionTuplesList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>RecruitedFlatCumulateVariablesList' :
   /   /[
   /   /  0 : {...}< (RecruiterClass), 4555498384>
   /   /  1 : {...}< (RecruiterClass), 4556356176>
   /   /  2 : {...}< (CumulaterClass), 4557708048>
   /   /  3 : {...}< (RecruiterClass), 4556968016>
   /   /]
   /  '<Spe><Instance>RecruitingConcludeConditionTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : NodeIndexInt
   /   /   /  1 : <function <lambda> at 0x10e8a5b90>
   /   /   /  2 : 2
   /   /   /)
   /   /]
   /}

*****End of the Attest *****



```

