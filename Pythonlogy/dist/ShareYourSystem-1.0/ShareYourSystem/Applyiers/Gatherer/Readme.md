

<!--
FrozenIsBool False
-->

View the Gatherer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
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
from ShareYourSystem.Applyiers import Gatherer

#Definition a Gatherer
MyGatherer=Gatherer.GathererClass().map('__setitem__',map(
        lambda __ItemTuple:
        {'LiargVariablesList':__ItemTuple},
        [
            ('MyInt',0),
            ('FirstChildGatherer',Gatherer.GathererClass().__setitem__(
                    'MyStr',
                    "bonjour"
                    )
            ),
            ('SecondChildGatherer',Gatherer.GathererClass().__setitem__(
                    'MyStr',
                    "hello"
                    )
            )
        ]
    )
)

#Map some gets
GatheredVariablesList=MyGatherer.gather(
                            [
                                ['MyInt'],
['/FirstChildGatherer/MyStr','/SecondChildGatherer/MyStr']
                            ]
                        )

#Definition the AttestedStr
SYS._attest(
    [
        'GatheredVariablesList is '+SYS._str(
            GatheredVariablesList
            ,**{
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

GatheredVariablesList is
   /[
   /  0 : ('MyInt', 0)
   /  1 : ('/FirstChildGatherer/MyStr', 'bonjour')
   /  2 : ('/SecondChildGatherer/MyStr', 'hello')
   /]

*****End of the Attest *****



```

