

<!--
FrozenIsBool False
-->

#Cumulater

##Doc
----


>
> A Cumulater pick and
>
>

----

<small>
View the Cumulater notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Cumulater.ipynb)
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


A Cumulater pick and

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Walkers.Walker"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy

#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CumulaterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'CumulatedVariablesList'
                                                        ]

        def default_init(self,
                                _CumulatedVariablesList=None,
                                **_KwargVariablesDict):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_cumulate(self):

                #debug
                '''
                self.debug(('self.',self,[
'WalkingSocketDict',
'WalkedTopOrderedDict'
                                                                ]))
                '''

                #Init
                if 'CumulateVariablesList' not in self.WalkedTopOrderedDict:
                        self.WalkedTopOrderedDict['CumulateVariablesList']=[]


                #debug
                '''
                self.debug(
                                        ('self.',self,[
'ConcludingConditionTuplesList',
                                                        ])
                                )
                '''

                #Check
                self.WalkedTopOrderedDict['CumulateVariablesList'].append(
                        self.filter('/').FilteredVariablesList
                )

                #debug
                '''
                self.debug(('self.',self,['FilteredVariablesList']))
                '''

                #set
                if self.WalkingSocketDict['TopVariable']==self:
self.CumulatedVariablesList=self.WalkedTopOrderedDict['CumulateVariablesList']
                        #self.CumulatedVariablesList=copy.copy(self.WalkedTopOrd
eredDict['CumulateVariablesList'])


#</DefineClass>

```

<small>
View the Cumulater sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Walkers/Cumulater"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Cumulater
import operator

#Definition a Filter instance that is grouped
MyCumulater=Cumulater.CumulaterClass().update(
        [
            (
                '<Filterome>FirstChildCumulater',
                Cumulater.CumulaterClass().update(
                    [
                        (
                            '<Filterome>GrandChildFilter',
                            Cumulater.CumulaterClass()
                        )
                    ]
                )
            ),
            (
                '<Filterome>SecondChildFilter',
                Cumulater.CumulaterClass()
            ),
            (
                '<Filterome>ThirdChildFilter',
                Cumulater.CumulaterClass()
            )
        ]
    )

#Walk inside the group in order to parent
MyCumulater.walk(
            {
                'BeforeUpdateList':
                [
                    (
                        'ConcludingConditionTuplesList',[
                            (
                                'NodeIndexInt',
                                lambda _TestInt,_AttestInt:
                                    operator.lt(_TestInt,_AttestInt) and
operator.lt(-1,_TestInt)
                                    if _TestInt!=None else False,
                                2
                            )
                        ]
                    ),
                    (
                        'PickingKeyVariablesList',['NodeKeyStr']
                    ),
                    ('cumulate',{'LiargVariablesList':[]})
                ],
                'GatherVariablesList':['<Filterome>']
            }
        )

#Definition the AttestedStr
SYS._attest(
    [
        'MyCumulater is '+SYS._str(
        MyCumulater,
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

MyCumulater is < (CumulaterClass), 4556651472>
   /{
   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildCumulater' : < (CumulaterClass), 4556651536>
   /   /   /{
   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildFilter' : < (CumulaterClass), 4556968016>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdInt' : 4556968016
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildFilter
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(CumulaterClass), 4556651536>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4557648840>
   /   /   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4556651536
   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildCumulater
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CumulaterClass),
4556651472>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557511944>
   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /}
   /   /  'SecondChildFilter' : < (CumulaterClass), 4557708880>
   /   /   /{
   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4557708880
   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildFilter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CumulaterClass),
4556651472>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557511944>
   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /}
   /   /  'ThirdChildFilter' : < (CumulaterClass), 4555039056>
   /   /   /{
   /   /   /  '<New><Instance>FilteromeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4555039056
   /   /   /  '<New><Instance>NodeCollectionStr' : Filterome
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : ThirdChildFilter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CumulaterClass),
4556651472>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557511944>
   /   /   /  '<Spe><Instance>CumulatedVariablesList' : []
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4556651472
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopCumulater
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Instance>CumulatedVariablesList' :
   /   /[
   /   /  0 : []
   /   /  1 : ['FirstChildCumulater']
   /   /  2 : ['GrandChildFilter']
   /   /  3 : ['SecondChildFilter']
   /   /  4 : []
   /   /]
   /}

*****End of the Attest *****



```

