

<!--
FrozenIsBool False
-->

View the Updater sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Applyiers/Installer)




<!---
FrozenIsBool True
-->

##Example

Update is possible with a TuplesList or a Dict (and OrderedDict)

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Applyiers import Updater

#Update several things
MyUpdater=Updater.UpdaterClass(
    ).update(
        [
            ('MyInt',0),
            ('MyFloat',0.2)
        ]
    ).update(
        {
            'MyStr':"hello"
        }
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

MyUpdater is < (UpdaterClass), 4549672528>
   /{
   /  '<New><Instance>IdInt' : 4549672528
   /  '<New><Instance>MyFloat' : 0.2
   /  '<New><Instance>MyInt' : 0
   /  '<New><Instance>MyStr' : hello
   /  '<Spe><Instance>UpdatingItemVariable' :
   /   /{
   /   /  'MyStr' : hello
   /   /}
   /}

*****End of the Attest *****



```

