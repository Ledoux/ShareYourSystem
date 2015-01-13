
#Caller


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Caller is an Object that helps to get an make call a function/method.





<!--
FrozenIsBool False
-->

View the Caller sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
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
from ShareYourSystem.Objects import Caller

#Definition of a Caller instance
MyCaller=Caller.CallerClass()

#Call the _print from the Rep
MyCaller.call(
    _FunctionStr='represent',
    **{
        'PackagingModuleVariableStr':'ShareYourSystem.Classors.Representer',
    }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyCaller is '+SYS._str(
        MyCaller,
        **{
            'RepresentingBaseKeyStrsListBool':False
        }
        )
    ]
)

#Print



```


```console
>>>
Doer l.132 : DoerStr is Caller
DoStr is Call
DoMethodStr is call
DoingStr is Calling
DoneStr is Called



*****Start of the Attest *****

MyCaller is < (CallerClass), 4556059536>
   /{
   /  '<New><Instance>IdString' : 4556059536
   /  '<Spe><Class>CallingClass' : None
   /  '<Spe><Class>CallingClassStr' :
   /  '<Spe><Class>CallingInstanceVariable' : None
   /  '<Spe><Class>CallingMethod' : None
   /  '<Spe><Class>CallingMethodStr' :
   /  '<Spe><Instance>CallingFunctionStr' : represent
   /  '<Spe><Instance>CallingVariable' : <function Watcher@represent at
0x10f75dd70>
   /}

*****End of the Attest *****



```

