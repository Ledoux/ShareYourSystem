
#Recruiter
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Recruiter




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

MyRecruiter is < (RecruiterClass), 4559068880>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<New><Instance>IdString' : 4559068880
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildRecruiter' : < (RecruiterClass), 4559177040>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildCumulater' : < (CumulaterClass), 4559179664>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdString' : 4559179664
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Collectome
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildCumulater
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(RecruiterClass), 4559177040>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559126064>
   /   /   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4559177040
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildRecruiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RecruiterClass),
4559068880>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559125768>
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>RecruitedFlatCumulateVariablesList' : None
   /   /   /  '<Spe><Class>RecruitingConcludeConditionTuplesList' : None
   /   /   /}
   /   /  'SecondChildRecruiter' : < (RecruiterClass), 4559176336>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4559176336
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildRecruiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RecruiterClass),
4559068880>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559125768>
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>RecruitedFlatCumulateVariablesList' : None
   /   /   /  '<Spe><Class>RecruitingConcludeConditionTuplesList' : None
   /   /   /}
   /   /  'ThirdChildRecruiter' : < (RecruiterClass), 4559176144>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4559176144
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildRecruiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (RecruiterClass),
4559068880>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559125768>
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>RecruitedFlatCumulateVariablesList' : None
   /   /   /  '<Spe><Class>RecruitingConcludeConditionTuplesList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>RecruitedFlatCumulateVariablesList' :
   /   /[
   /   /  0 : {...}< (RecruiterClass), 4559068880>
   /   /  1 : {...}< (RecruiterClass), 4559177040>
   /   /  2 : {...}< (CumulaterClass), 4559179664>
   /   /  3 : {...}< (RecruiterClass), 4559176336>
   /   /]
   /  '<Spe><Instance>RecruitingConcludeConditionTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : NodeIndexInt
   /   /   /  1 : <function <lambda> at 0x10fad7578>
   /   /   /  2 : 2
   /   /   /)
   /   /]
   /}

*****End of the Attest *****



```

