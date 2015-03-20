
#Object


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Object defines the first class for augmenting new-style object classes





<!--
FrozenIsBool False
-->

View the Object sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Objects/Installer)




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
from ShareYourSystem.Standards.Objects import Object

#Definition a Getter
MyObject=Object.ObjectClass()

#Definition the AttestedStr
SYS._attest(
    [
        'MyObject is '+SYS._str(
            MyObject,
        **{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyObject is <ShareYourSystem.Standards.Objects.Object.ObjectClass object at 0x10f910350>

*****End of the Attest *****



```

