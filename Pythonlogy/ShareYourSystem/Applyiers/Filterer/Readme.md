
#Filterer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Filterer pick and





<!--
FrozenIsBool False
-->

View the Filterer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Applyiers/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Filterer
import operator

#Definition a Filter instance that is grouped
MyFilterer=Filterer.FiltererClass().update(
    [
        ('NodeIndexInt',1),
        ('NodeKeyStr','MyFilterer'),
        (
            'ConcludingConditionTuplesList',[
                        (
                            'NodeIndexInt',
                            lambda _TestInt,_AttestInt:
                                operator.lt(_TestInt,_AttestInt)
                                if _TestInt!=None else False,
                            2
                        )
                    ]
                ),
        (
            'PickingGetKeyVariablesList',['NodeKeyStr']
        )
    ]
).filter('/')


#Definition the AttestedStr
SYS._attest(
    [
        'MyFilterer is '+SYS._str(
        MyFilterer,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        )
    ]
)



```


```console
>>>


*****Start of the Attest *****

MyFilterer is < (FiltererClass), 4364535504>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4364535504
   /  '<New><Instance>NodeIndexInt' : 1
   /  '<New><Instance>NodeKeyStr' : MyFilterer
   /  '<Spe><Instance>FilteredGetVariable' : {...}< (FiltererClass), 4364535504>
   /  '<Spe><Instance>FilteredVariablesList' : ['MyFilterer']
   /  '<Spe><Instance>FilteringGetVariable' : /
   /}

*****End of the Attest *****



```

