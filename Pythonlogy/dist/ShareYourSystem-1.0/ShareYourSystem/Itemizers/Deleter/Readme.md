
#Deleter
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Deleter has a __delitem__ method for deleting things in the
<InstanceVariable>.__dict__





<!--
FrozenIsBool False
-->

View the Deleter sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Itemizers/Installer)




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
from ShareYourSystem.Itemizers import Deleter

#Definition a Deleter
MyDeleter=Deleter.DeleterClass().__setitem__('MyInt',0).__delitem__('MyInt')

#Definition the AttestedStr
SYS._attest(
    [
    'MyDeleter is '+SYS._str(
            MyDeleter,
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

MyDeleter is < (DeleterClass), 4465249680>
   /{
   /  '<New><Instance>IdString' : 4465249680
   /}

*****End of the Attest *****



```

