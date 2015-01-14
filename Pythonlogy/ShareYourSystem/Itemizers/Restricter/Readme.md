

<!--
FrozenIsBool False
-->

View the Restricter sources on [Github](https://github.com/Ledoux/ShareYourSyste
m/tree/master/ShareYourSystem/Itemizers/Installer)




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
from ShareYourSystem.Itemizers import Restricter

#Explicit expression
MyRestricter=Restricter.RestricterClass(**{'RestrictingIsBool':True})
MyRestricter.ResettedStr="Hello"
MyRestricter.__setitem__('ResettedStr',"Bonjour")
MyRestricter.__setitem__('NotsettedFloat',1.)

#Return
SYS._attest(
    [
    'MyRestricter is '+SYS._str(
            MyRestricter,
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

MyRestricter is < (RestricterClass), 4347887312>
   /{
   /  '<New><Instance>IdInt' : 4347887312
   /  '<New><Instance>ResettedStr' : Bonjour
   /  '<Spe><Instance>RestrictedSetIsBool' : True
   /  '<Spe><Instance>RestrictingIsBool' : True
   /  '<Spe><Instance>RestrictingKeyStr' : NotsettedFloat
   /}

*****End of the Attest *****



```

