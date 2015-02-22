

<!--
FrozenIsBool False
-->

View the Concluder sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem/Objects/Markdowner)



```python

#ImportModules
import operator
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Objects import Concluder

#Definition of an instance Concluder and make it print hello
MyConcluder=Concluder.ConcluderClass().conclude(
    {'MyColorStr':'Black','MySuperInt':6},
    [
        ('MyColorStr',operator.eq,"Black"),
        ('MySuperInt',operator.gt,3),
        (1,operator.eq,1)
    ]
)

#Definition the AttestedStr
SYS._attest(
                    [
                        'MyConcluder is '+SYS._str(
                        MyConcluder,
                        **{
                            'RepresentingBaseKeyStrsListBool':False,
                            'RepresentingAlineaIsBool':False
                            }
                        ),
                    ]
                )

#Print






```


```console
>>>


*****Start of the Attest *****

MyConcluder is < (ConcluderClass), 4523890576>
   /{
   /  '<New><Instance>IdStr' : 4523890576
   /  '<Spe><Instance>ConcludedConditionIsBoolsList' :
   /   /[
   /   /  0 : True
   /   /  1 : True
   /   /  2 : True
   /   /]
   /  '<Spe><Instance>ConcludedIsBool' : True
   /  '<Spe><Instance>ConcludingConditionVariable' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : MyColorStr
   /   /   /  1 : <built-in function eq>
   /   /   /  2 : Black
   /   /   /)
   /   /  1 :
   /   /   /(
   /   /   /  0 : MySuperInt
   /   /   /  1 : <built-in function gt>
   /   /   /  2 : 3
   /   /   /)
   /   /  2 :
   /   /   /(
   /   /   /  0 : 1
   /   /   /  1 : {...}< (builtin_function_or_method), 4510259176>
   /   /   /  2 : 1
   /   /   /)
   /   /]
   /  '<Spe><Instance>ConcludingTestVariable' :
   /   /{
   /   /  'MyColorStr' : Black
   /   /  'MySuperInt' : 6
   /   /}
   /}

*****End of the Attest *****



```

