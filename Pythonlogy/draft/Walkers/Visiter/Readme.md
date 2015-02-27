

<!--
FrozenIsBool False
-->

#Visiter

##Doc
----


>
> A Visiter
>
>

----

<small>
View the Visiter notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Visiter.ipynb)
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


A Visiter

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Walkers.Cumulater"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

from ShareYourSystem.Standards.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class VisiterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'VisitingCollectionStrsList',
'VisitingBeforeUpdateList',
'VisitingAfterUpdateList'
                                                                ]

        def default_init(self,
                                _VisitingCollectionStrsList=None,
                                _VisitingBeforeUpdateList=None,
                                _VisitingAfterUpdateList=None,
                                **_KwargVariablesDict
                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_visit(self):

                #Walk inside the group in order to parent
                self.walk(
                                        {
'BeforeUpdateList':self.VisitingBeforeUpdateList,
'AfterUpdateList':self.VisitingAfterUpdateList,
                                                'GatherVariablesList':map(
                                                                lambda
__NodeCollectionStr:
Noder.NodingPrefixGetStr+__NodeCollectionStr+Noder.NodingSuffixGetStr,
self.VisitingCollectionStrsList
                                                        )
                                        }
                                )


#</DefineClass>

```

<small>
View the Visiter sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Walkers/Visiter"
target="_blank">Github</a>
</small>



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Walkers import Cumulater,Visiter

#Definition a Visiter instance that is grouped
MyVisiter=Visiter.VisiterClass().update(
    [
        (
            '<Visitome>FirstChildVisiter',
            Visiter.VisiterClass().update(
                [
                    (
                        '<Collectome>GrandChildCumulater',
                        Cumulater.CumulaterClass()
                    )
                ]
            )
        ),
        (
            '<Visitome>SecondChildVisiter',
            Visiter.VisiterClass()
        )
    ]
)

#Walk inside the group in order to parent
MyVisiter.visit(['Visitome','Collectome'],[('TagStr','Je suis passe par la')])

#Definition the AttestedStr
SYS._attest(
    [
        'MyVisiter is '+SYS._str(
        MyVisiter,
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

MyVisiter is < (VisiterClass), 4556651600>
   /{
   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<New><Instance>IdInt' : 4556651600
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopVisiter
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TagStr' : Je suis passe par la
   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildVisiter' : < (VisiterClass), 4555499408>
   /   /   /{
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildCumulater' : < (CumulaterClass), 4555499216>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdInt' : 4555499216
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Collectome
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildCumulater
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(VisiterClass), 4555499408>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4537423976>
   /   /   /   /   /  '<New><Instance>TagStr' : Je suis passe par la
   /   /   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>CumulatedVariablesList' : None
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4555499408
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildVisiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (VisiterClass),
4556651600>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4537424568>
   /   /   /  '<New><Instance>TagStr' : Je suis passe par la
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>VisitingAfterUpdateList' : None
   /   /   /  '<Spe><Class>VisitingBeforeUpdateList' : None
   /   /   /  '<Spe><Class>VisitingCollectionStrsList' : None
   /   /   /}
   /   /  'SecondChildVisiter' : < (VisiterClass), 4555499664>
   /   /   /{
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdInt' : 4555499664
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildVisiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (VisiterClass),
4556651600>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4537424568>
   /   /   /  '<New><Instance>TagStr' : Je suis passe par la
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>VisitingAfterUpdateList' : None
   /   /   /  '<Spe><Class>VisitingBeforeUpdateList' : None
   /   /   /  '<Spe><Class>VisitingCollectionStrsList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>VisitingAfterUpdateList' : []
   /  '<Spe><Instance>VisitingBeforeUpdateList' :
   /   /[
   /   /  0 : ('TagStr', 'Je suis passe par la')
   /   /]
   /  '<Spe><Instance>VisitingCollectionStrsList' : ['Visitome', 'Collectome']
   /}

*****End of the Attest *****



```

