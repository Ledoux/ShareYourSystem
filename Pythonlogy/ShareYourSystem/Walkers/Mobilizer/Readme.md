
#Mobilizer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Mobilizer




```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Visiter,Recruiter,Mobilizer
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
            'RecruitingConcludeConditionTuplesList':[('NodeIndexInt',lambda
_TestInt,_AttestInt:
                _TestInt!=None and operator.lt(_TestInt,_AttestInt),2)]
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

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx
        ////////////////////////////////
        Doer/__init__.py do
        From <string> superDo_debug | Catcher/__init__.py do_catch |
Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py watch |
<string> watch_superDo_catch | Mobilizer/__init__.py do_mobilize |
Doer/__init__.py do | <string> superDo_mobilize | Watcher/__init__.py watch |
<string> watch_superDo_mobilize | <string> <module> | <string> <module> | site-
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
<string> watch_superDo_install | Installer/Install.py <module>
        ////////////////////////////////

        l.180 :
        *****
        I am with [('NodeKeyStr', '')]
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
<string> watch_superDo_catch | Mobilizer/__init__.py do_mobilize |
Doer/__init__.py do | <string> superDo_mobilize | Watcher/__init__.py watch |
<string> watch_superDo_mobilize | <string> <module> | <string> <module> | site-
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
<string> watch_superDo_install | Installer/Install.py <module>
        ////////////////////////////////

        l.180 :
        *****
        I am with [('NodeKeyStr', '')]
        *****
        self.CollectingCollectionStr is MobilizerFigurome

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx


        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx
        ////////////////////////////////
        Doer/__init__.py do
        From <string> superDo_debug | Catcher/__init__.py do_catch |
Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py watch |
<string> watch_superDo_catch | Mobilizer/__init__.py do_mobilize |
Doer/__init__.py do | <string> superDo_mobilize | Watcher/__init__.py watch |
<string> watch_superDo_mobilize | <string> <module> | <string> <module> | site-
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
<string> watch_superDo_install | Installer/Install.py <module>
        ////////////////////////////////

        l.180 :
        *****
        I am with [('NodeKeyStr', '')]
        *****
        self.CollectingCollectionStr is MobilizerFigurome

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx


        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx
        ////////////////////////////////
        Doer/__init__.py do
        From <string> superDo_debug | Catcher/__init__.py do_catch |
Doer/__init__.py do | <string> superDo_catch | Watcher/__init__.py watch |
<string> watch_superDo_catch | Mobilizer/__init__.py do_mobilize |
Doer/__init__.py do | <string> superDo_mobilize | Watcher/__init__.py watch |
<string> watch_superDo_mobilize | <string> <module> | <string> <module> | site-
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
<string> watch_superDo_install | Installer/Install.py <module>
        ////////////////////////////////

        l.180 :
        *****
        I am with [('NodeKeyStr', '')]
        *****
        self.CollectingCollectionStr is RecruiterFigurome

        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyMobilizer is < (MobilizerClass), 4558050512>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4558050512
   /  '<New><Instance>MobilizerFiguromeCollectionOrderedDict' :
   /   /{
   /   /  'Pointer' : < (PointerClass), 4559184272>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4559184272
   /   /   /  '<New><Instance>PointVariable' : {...}< (MobilizerClass),
4558050512>
   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}< (MobilizerClass),
4558050512>
   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}< (MobilizerClass),
4558050512>
   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /}
   /   /  'FirstChildMobilizerPointer' : < (PointerClass), 4559187280>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4559187280
   /   /   /  '<New><Instance>PointVariable' : < (MobilizerClass), 4558890064>
   /   /   /   /{
   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /  '<New><Instance>IdString' : 4558890064
   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /}
   /   /   /   /  '<New><Instance>NodeCollectionStr' : Mobilizome
   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildMobilizer
   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4558050512>
   /   /   /   /  '<New><Instance>NodePointOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /  'FirstChildMobilizer' : {...}< (MobilizerClass),
4558890064>
   /   /   /   /   /  'SecondChildMobilizer' : < (MobilizerClass), 4559067856>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>IdString' : 4559067856
   /   /   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Mobilizome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildMobilizer
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4558050512>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559174624>
   /   /   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>MobilizingNameStrsList' : None
   /   /   /   /   /   /}
   /   /   /   /   /  'ThirdChildMobilizer' : < (MobilizerClass), 4559065744>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>IdString' : 4559065744
   /   /   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Mobilizome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildMobilizer
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4558050512>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559174624>
   /   /   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>MobilizingNameStrsList' : None
   /   /   /   /   /   /}
   /   /   /   /   /}
   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /  'GrandChildRecruiter' : < (RecruiterClass), 4559179536>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>IdString' : 4559179536
   /   /   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Recruitome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildRecruiter
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4558890064>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559125472>
   /   /   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>RecruitedFlatCumulateVariablesList' :
None
   /   /   /   /   /   /  '<Spe><Class>RecruitingConcludeConditionTuplesList' :
None
   /   /   /   /   /   /}
   /   /   /   /   /  'FakeGrandChildVisiter' : < (VisiterClass), 4559175824>
   /   /   /   /   /   /{
   /   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /   /  '<New><Instance>IdString' : 4559175824
   /   /   /   /   /   /  '<New><Instance>MobilizomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Recruitome
   /   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /   /   /  '<New><Instance>NodeKeyStr' : FakeGrandChildVisiter
   /   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(MobilizerClass), 4558890064>
   /   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559125472>
   /   /   /   /   /   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /   /   /   /   /   /{
   /   /   /   /   /   /   /}
   /   /   /   /   /   /  '<Spe><Class>VisitingAfterUpdateList' : None
   /   /   /   /   /   /  '<Spe><Class>VisitingBeforeUpdateList' : None
   /   /   /   /   /   /  '<Spe><Class>VisitingCollectionStrsList' : None
   /   /   /   /   /   /}
   /   /   /   /   /}
   /   /   /   /  '<Spe><Class>MobilizingNameStrsList' : None
   /   /   /   /}
   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}< (MobilizerClass),
4558890064>
   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}< (MobilizerClass),
4558890064>
   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /}
   /   /  'SecondChildMobilizerPointer' : < (PointerClass), 4559068240>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4559068240
   /   /   /  '<New><Instance>PointVariable' : {...}< (MobilizerClass),
4559067856>
   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}< (MobilizerClass),
4559067856>
   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}< (MobilizerClass),
4559067856>
   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /}
   /   /}
   /  '<New><Instance>MobilizomeCollectionOrderedDict' : {...}< (OrderedDict),
4559174624>
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>RecruiterFiguromeCollectionOrderedDict' :
   /   /{
   /   /  'GrandChildRecruiterPointer' : < (PointerClass), 4559077200>
   /   /   /{
   /   /   /  '<New><Instance>IdString' : 4559077200
   /   /   /  '<New><Instance>PointVariable' : {...}< (RecruiterClass),
4559179536>
   /   /   /  '<Spe><Class>PointedBackSetStr' :
   /   /   /  '<Spe><Class>PointedPathBackVariable' :
   /   /   /  '<Spe><Class>PointingBackSetKeyStr' :
   /   /   /  '<Spe><Instance>PointedGetVariable' : {...}< (RecruiterClass),
4559179536>
   /   /   /  '<Spe><Instance>PointedLocalSetStr' : PointVariable
   /   /   /  '<Spe><Instance>PointingGetVariable' : {...}< (RecruiterClass),
4559179536>
   /   /   /  '<Spe><Instance>PointingSetPathStr' : PointVariable
   /   /   /}
   /   /}
   /  '<New><Instance>RecruitomeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>MobilizingNameStrsList' : ['Mobilizer', 'Recruiter']
   /}

*****End of the Attest *****



```

