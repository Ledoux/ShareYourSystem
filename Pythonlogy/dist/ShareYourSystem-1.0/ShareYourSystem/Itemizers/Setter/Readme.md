

<!--
FrozenIsBool False
-->

View the Setter sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
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
from ShareYourSystem.Itemizers import Setter

#Definition a Setter and set with the __setitem__
MySetter=Setter.SetterClass().__setitem__('MyInt',0)

#Definition the AttestedStr
SYS._attest(
    [
    'MySetter is '+SYS._str(
            MySetter,
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

MySetter is < (SetterClass), 4347770064>
   /{
   /  '<New><Instance>IdInt' : 4347770064
   /  '<New><Instance>MyInt' : 0
   /  '<Spe><Instance>SettingKeyVariable' : MyInt
   /  '<Spe><Instance>SettingValueVariable' : 0
   /}

*****End of the Attest *****



```

