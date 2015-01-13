
#Coupler
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Coupler





<!--
FrozenIsBool False
-->

View the Coupler sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Noders/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Noders import Coupler

#store
MyCoupler=Coupler.CouplerClass().collect(
        'Couplome',
        'FirstChild',
        Coupler.CouplerClass()
).collect(
        'Couplome',
        'SecondChild',
        Coupler.CouplerClass()
)

#couple
MyCoupler['<Couplome>SecondChildCoupler'].couple(
            'Relatome',
            '/NodePointDeriveNoder/<Couplome>FirstChildCoupler'
    )

#Return
SYS._attest(
    [
    'MyCoupler is '+SYS._str(
            MyCoupler,
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
Doer l.132 : DoerStr is Coupler
DoStr is Couple
DoMethodStr is couple
DoingStr is Coupling
DoneStr is Coupled



*****Start of the Attest *****

MyCoupler is < (CouplerClass), 4557283024>
   /{
   /  '<New><Instance>CouplomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildCoupler' : < (CouplerClass), 4557281872>
   /   /   /{
   /   /   /  '<New><Instance>IdStr' : 4557281872
   /   /   /  '<New><Instance>NodeCollectionStr' : Relatome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildCoupler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : < (CouplerClass),
4557281488>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdStr' : 4557281488
   /   /   /   /  '<New><Instance>NodeCollectionStr' : Couplome
   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildCoupler
   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CouplerClass),
4557283024>
   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557306552>
   /   /   /   /  '<New><Instance>RelatomeCollectionOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /  'FirstChildCoupler' : {...}< (CouplerClass), 4557281872>
   /   /   /   /   /}
   /   /   /   /  '<Spe><Instance>CoupledGetStr' : <Relatome>
   /   /   /   /  '<Spe><Instance>CouplingGetStr' :
/NodePointDeriveNoder/<Couplome>FirstChildCoupler
   /   /   /   /  '<Spe><Instance>CouplingNodeStr' : Relatome
   /   /   /   /}
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4557306848>
   /   /   /  '<Spe><Class>CoupledGetStr' :
   /   /   /  '<Spe><Class>CouplingGetStr' :
   /   /   /  '<Spe><Class>CouplingNodeStr' :
   /   /   /}
   /   /  'SecondChildCoupler' : {...}< (CouplerClass), 4557281488>
   /   /}
   /  '<New><Instance>IdStr' : 4557283024
   /  '<New><Instance>NodeCollectionStr' : Global
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' :
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>CoupledGetStr' :
   /  '<Spe><Class>CouplingGetStr' :
   /  '<Spe><Class>CouplingNodeStr' :
   /}

*****End of the Attest *****



```

