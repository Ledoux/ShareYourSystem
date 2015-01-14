
#Updater
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Updater maps a __setitem__





<!--
FrozenIsBool False
-->

View the Updater sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Applyiers/Installer)




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
from ShareYourSystem.Applyiers import Updater

#Update several things
MyUpdater=Updater.UpdaterClass().update([
        ('MyInt',0),
        ('MyFloat',0.2)
    ]
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyUpdater is '+SYS._str(
        MyUpdater,
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

MyUpdater is < (UpdaterClass), 4365085904>
   /{
   /  '<New><Instance>ApplyingIsBool' : True
   /  '<New><Instance>IdString' : 4365085904
   /  '<New><Instance>MyFloat' : 0.2
   /  '<New><Instance>MyInt' : 0
   /  '<Spe><Instance>UpdatingItemVariable' :
   /   /[
   /   /  0 : ('MyInt', 0)
   /   /  1 : ('MyFloat', 0.2)
   /   /]
   /}

*****End of the Attest *****



```

