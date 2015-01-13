
#Tester


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Tester helps for defining asserts between attested Strs stored in the
Attests Folder and new calls of the attest functions. Thanks here to a wrap of
the unitest python module : https://docs.python.org/2/library/unittest.html





<!---
FrozenIsBool True
-->

##Example

The Incrementer from the previous Attester Module is now tested from its
corresponding attesting function
attest_increment. Here a test_increment method is implicitely defined in a
unittest class and when we call
the test method, a unittest.run is done.

```python
#ImportModules
import os
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Initiator
from ShareYourSystem.Classors import Tester

#Definition a module like a class and an attest function
AttestingFunctionStrsList=['attest_increment']
def attest_increment():
    Incrementer=IncrementerClass()
    Incrementer.increment()
    return Incrementer.IncrementingInt

#Definition a decorated Incrementer
@Tester.TesterClass()
class IncrementerClass(Initiator.InitiatorClass):
    def default_init(self):
        self.IncrementingInt=0
    def increment(self):
        self.IncrementingInt+=1

#Attest and test
attest();test()

```


```console
>>>

###########################################

AttestedStr is :
1

TestedStr is :
1



```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the TesterClass are :


```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Tester

#Definition the AttestedStr
SYS._attest(
    [
        'DefaultAttributeItemTuplesList is '+SYS._str(
            Tester.TesterClass.DefaultAttributeItemTuplesList,
            **{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

DefaultAttributeItemTuplesList is []

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the instances

A default call of an instance gives :


```python



#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Classors import Tester

#Definition the AttestedStr
SYS._attest(
    [
        Tester.TesterClass()
    ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

< (TesterClass), 4441734416>
   /{
   /  '<New><Instance>NameStr' : Tester
   /}

*****End of the Attest *****




```

