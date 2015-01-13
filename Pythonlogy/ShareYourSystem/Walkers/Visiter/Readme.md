
#Visiter
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Visiter




```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Walkers import Cumulater,Visiter

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

MyVisiter is < (VisiterClass), 4559074768>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /{
   /   /}
   /  '<New><Instance>IdString' : 4559074768
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TagStr' : Je suis passe par la
   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildVisiter' : < (VisiterClass), 4558963408>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /  'GrandChildCumulater' : < (CumulaterClass), 4558962768>
   /   /   /   /   /{
   /   /   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<New><Instance>IdString' : 4558962768
   /   /   /   /   /  '<New><Instance>NodeCollectionStr' : Collectome
   /   /   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /   /   /  '<New><Instance>NodeKeyStr' : GrandChildCumulater
   /   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(VisiterClass), 4558963408>
   /   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}<
(OrderedDict), 4559296912>
   /   /   /   /   /  '<New><Instance>TagStr' : Je suis passe par la
   /   /   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /   /   /{
   /   /   /   /   /   /}
   /   /   /   /   /  '<Spe><Class>CumulatedVariablesList' : None
   /   /   /   /   /}
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4558963408
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildVisiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (VisiterClass),
4559074768>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559297504>
   /   /   /  '<New><Instance>TagStr' : Je suis passe par la
   /   /   /  '<New><Instance>VisitomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Class>VisitingAfterUpdateList' : None
   /   /   /  '<Spe><Class>VisitingBeforeUpdateList' : None
   /   /   /  '<Spe><Class>VisitingCollectionStrsList' : None
   /   /   /}
   /   /  'SecondChildVisiter' : < (VisiterClass), 4558890128>
   /   /   /{
   /   /   /  '<New><Instance>ApplyingIsBool' : True
   /   /   /  '<New><Instance>CollectomeCollectionOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<New><Instance>IdString' : 4558890128
   /   /   /  '<New><Instance>NodeCollectionStr' : Visitome
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildVisiter
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (VisiterClass),
4559074768>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4559297504>
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

