
#Initiator


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Initiator is a trivial module... It just helps for defining directly in the
__dict__ of an instance of the InitiatorClass some attributes given by the items
setted in the _KwargVariablesDict from the __init__ method.





<!--
FrozenIsBool False
-->

View the Initiator sources on [Github](https://github.com/Ledoux/ShareYourSystem
/tree/master/ShareYourSystem/Objects/Installer)




<!---
FrozenIsBool True
-->

##Example



```python

"""
FrozenIsBool True
"""

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Objects import Initiator

#Definition of an Initiator instance
MyInitiator=Initiator.InitiatorClass()
MyInitiator.GettingInt=1

#Definition the AttestedStr
SYS._attest(
    [
        'MyInitiator is '+SYS._str(MyInitiator)
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyInitiator is <ShareYourSystem.Standards.Objects.Initiator.InitiatorClass object at
0x10f8ff090>

*****End of the Attest *****



```

