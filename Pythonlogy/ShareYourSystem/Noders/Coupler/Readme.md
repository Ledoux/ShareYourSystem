

<!--
FrozenIsBool False
-->

#Coupler

##Doc
----


>
> A Coupler
>
>

----

<small>
View the Coupler notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Coupler.ipynb)
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


A Coupler

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Attentioner"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>

from ShareYourSystem.Itemizers import Pather
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class CouplerClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'CouplingNodeStr',
'CouplingGetStr',
                                                                'CoupledGetStr'
                                                        ]

        def default_init(self,
                                                _CouplingNodeStr="",
                                                _CouplingGetStr="",
                                                _CoupledGetStr="",
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_couple(self):

                #debug
                '''
                self.debug(('self.',self,[
'CouplingNodeStr',
'CouplingGetStr',
'PointingBackBool'
                                                                ]))
                '''

                #set
                self.CoupledGetStr=Noder.NodingPrefixGetStr+self.CouplingNodeStr
+Noder.NodingSuffixGetStr
self.PointingSetPathStr=self.CoupledGetStr+self.CouplingGetStr.split(
                                                Noder.NodingSuffixGetStr
                                        )[-1]

                #debug
                '''
self.debug(('self.',self,['CoupledGetStr','PointingSetPathStr']))
                '''

                #point
                self.point(
                                        self.CouplingGetStr,
                                        self.PointingSetPathStr
                                )

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Coupler sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Noders/Coupler" target="_blank">Github</a>
</small>



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


*****Start of the Attest *****

MyCoupler is < (CouplerClass), 4555634704>
   /{
   /  '<New><Instance>CouplomeCollectionOrderedDict' :
   /   /{
   /   /  'FirstChildCoupler' : < (CouplerClass), 4555634256>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555634256
   /   /   /  '<New><Instance>NodeCollectionStr' : Relatome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : FirstChildCoupler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : < (CouplerClass),
4555535248>
   /   /   /   /{
   /   /   /   /  '<New><Instance>IdInt' : 4555535248
   /   /   /   /  '<New><Instance>NodeCollectionStr' : Couplome
   /   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /   /  '<New><Instance>NodeKeyStr' : SecondChildCoupler
   /   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (CouplerClass),
4555634704>
   /   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555707336>
   /   /   /   /  '<New><Instance>RelatomeCollectionOrderedDict' :
   /   /   /   /   /{
   /   /   /   /   /  'FirstChildCoupler' : {...}< (CouplerClass), 4555634256>
   /   /   /   /   /}
   /   /   /   /  '<Spe><Instance>CoupledGetStr' : <Relatome>
   /   /   /   /  '<Spe><Instance>CouplingGetStr' :
/NodePointDeriveNoder/<Couplome>FirstChildCoupler
   /   /   /   /  '<Spe><Instance>CouplingNodeStr' : Relatome
   /   /   /   /}
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4555707632>
   /   /   /  '<Spe><Class>CoupledGetStr' :
   /   /   /  '<Spe><Class>CouplingGetStr' :
   /   /   /  '<Spe><Class>CouplingNodeStr' :
   /   /   /}
   /   /  'SecondChildCoupler' : {...}< (CouplerClass), 4555535248>
   /   /}
   /  '<New><Instance>IdInt' : 4555634704
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopCoupler
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>CoupledGetStr' :
   /  '<Spe><Class>CouplingGetStr' :
   /  '<Spe><Class>CouplingNodeStr' :
   /}

*****End of the Attest *****



```

