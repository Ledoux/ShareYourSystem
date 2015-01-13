
#Conditioner


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Conditioner





<!--
FrozenIsBool False
-->

View the Conditioner sources on [Github](https://github.com/Ledoux/ShareYourSyst
em/tree/master/ShareYourSystem/Objects/Installer)




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
from ShareYourSystem.Objects import Conditioner

#Definition of an instance Conditioner and make it print hello
MyConditioner=Conditioner.ConditionerClass(**{
        'ConditioningGetBoolFunction':lambda
_TestVariable,_AttestVariable:_TestVariable==_AttestVariable,
        'ConditioningAttestVariable':2
    })
MyConditioner.condition(3).ConditionedIsBool

#Definition the AttestedStr
SYS._attest(
                    [
                        'MyConditioner.condition(3).ConditionedIsBool is '+str(
                            MyConditioner.condition(3).ConditionedIsBool),
                        'MyConditioner.condition(2).ConditionedIsBool is '+str(
                            MyConditioner.condition(2).ConditionedIsBool)
                    ]
                )

#Print



```


```console
>>>


*****Start of the Attest *****

MyConditioner.condition(3).ConditionedIsBool is False

------

MyConditioner.condition(2).ConditionedIsBool is True

*****End of the Attest *****



```

