

<!--
FrozenIsBool False
-->

View the Getter sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Itemizers/Installer)




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
from ShareYourSystem.Itemizers import Getter

#Definition a Getter
MyGetter=Getter.GetterClass()
MyGetter.MyInt=1

#Definition the AttestedStr
SYS._attest(
    [
        'Get the MyInt returns '+str(MyGetter['MyInt']),
        'Get the MyStr returns '+str(MyGetter['MyStr'])
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

Get the MyInt returns 1

------

Get the MyStr returns None

*****End of the Attest *****



```

