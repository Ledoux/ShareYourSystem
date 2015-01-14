

<!--
FrozenIsBool False
-->

View the Applyier sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Applyiers/Installer)




<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive
special attributes from the decorating ClassorClass,
specially the NameStr, that should be the ClassStr
without the TypeStr in the end.

```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Applyier

#Definition an applyier instance
MyApplyier=Applyier.ApplyierClass()

#Apply just a set... (even if we can do shorter !)
MyApplyier.apply(
    '__setitem__',
    {'LiargVariablesList':['MyStr','Hello']}
)

#Apply an apply is possible
MyApplyier.apply(
    '__setitem__',
    {'LiargVariablesList':[
            '__setitem__',
            {
                'LiargVariablesList':
                ['MyNotLostStr','ben he']
            }
        ]
    }
)

#Definition the AttestedStr
SYS._attest(
    [
    'MyApplyier is '+SYS._str(
            MyApplyier,
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

MyApplyier is < (ApplyierClass), 4549605008>
   /{
   /  '<New><Instance>IdInt' : 4549605008
   /  '<New><Instance>MyNotLostStr' : ben he
   /  '<New><Instance>MyStr' : Hello
   /}

*****End of the Attest *****



```

