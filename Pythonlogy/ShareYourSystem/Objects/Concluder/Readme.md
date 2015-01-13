

<!--
FrozenIsBool False
-->

#Concluder

----


>
> @Date : Fri Nov 14 13:20:38 2014
>
> @Author : Erwan Ledoux
>
>
>
> The Nbconverter
>
>

----


View the Concluder sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem.Guiders.Nbconverter)




<!---
FrozenIsBool True
-->

##Example

Let's do a simple conclude call

```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Concluder
import operator

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

MyConcluder is < (ConcluderClass), 4570347216>
   /{
   /  '<New><Instance>IdStr' : 4570347216
   /  '<Spe><Instance>ConcludedConditionIsBoolsList' :
   /   /[
   /   /  0 : True
   /   /  1 : True
   /   /  2 : True
   /   /]
   /  '<Spe><Instance>ConcludedIsBool' : True
   /  '<Spe><Instance>ConcludingConditionTuplesList' :
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
   /   /   /  1 : {...}< (builtin_function_or_method), 4556741088>
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

