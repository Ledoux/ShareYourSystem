

<!--
FrozenIsBool False
-->

View the Attributer sources on [Github](https://github.com/Ledoux/ShareYourSyste
m/tree/master/ShareYourSystem/Itemizers/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Attributer

#Definition a Attributer and set with the __setitem__
MyAttributer=Attributer.AttributerClass().__setitem__('Attr_MyInt',0)

#Definition the AttestedStr
SYS._attest(
    [
    'MyAttributer is '+SYS._str(
            MyAttributer,
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

MyAttributer is < (AttributerClass), 4348011856>
   /{
   /  '<New><Instance>IdInt' : 4348011856
   /  '<New><Instance>MyInt' : 0
   /  '<Spe><Instance>AttributedSetKeyStr' : MyInt
   /  '<Spe><Instance>AttributingKeyStr' : Attr_MyInt
   /  '<Spe><Instance>AttributingValueVariable' : 0
   /}

*****End of the Attest *****



```

