
#Defaultor


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Defaultor is a crucial module for understanding how we can manage high-
computer-performance of many instanciations without making the memory crashes.
For an Instance that is setted by default, this latter will find its attributes
in the class __dict__. Once the instance has setted in its __dict__ a special
value it will stop to look at the class level. There is for now no distinction
of get,set for mutable or non mutable variable.





<!---
FrozenIsBool True
-->

##Example

We define here a FooClass with some attributes. Here is the difference for a
default instance
DefaultFoo that takes its values from the FooClass.__dict__ and a special one
that sets in its __dict__

```python
#ImportModules
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Standards.Objects import Initiator
from ShareYourSystem.Standards.Classors import Defaultor

#Definition a FooClass decorated by the DefaultorClass
@Defaultor.DefaultorClass()
class FooClass(Initiator.InitiatorClass):

        def default_init(self,
                                                Int,
                                                _MyFloat=1.,
                                                _MyList=[],
                                                _MyInt={
'DefaultingSetType':int
                                                                }
                                ):

                #Definition an attribute
                self.MyStr='I am a Foo with MyFloat equal to
'+str(self.MyFloat)+' and Int equal to '+str(Int)

#Definition a default instance that will take its values from the default classed
attributes
DefaultFoo=FooClass(3)

#Definition a special instance that sets in its __dict__
SpecialFoo=FooClass(3,_MyList=['hello'],**{'MyInt':3})

#Definition the AttestedStr
AttestingStrsList=[
                'What are you saying DefaultFoo ?',
                'DefaultFoo.__dict__ is '+str(DefaultFoo.__dict__),
                'DefaultFoo.MyFloat is '+str(DefaultFoo.MyFloat),
                'DefaultFoo.MyList is '+str(DefaultFoo.MyList),
                'DefaultFoo.MyInt is '+str(DefaultFoo.MyInt),
                'What are you saying SpecialFoo ?',
                'SpecialFoo.__dict__ is '+str(SpecialFoo.__dict__),
                'SpecialFoo.MyFloat is '+str(SpecialFoo.MyFloat),
                'SpecialFoo.MyList is '+str(SpecialFoo.MyList),
                'DefaultFoo.MyInt is '+str(SpecialFoo.MyInt)
        ]

#Change a classed attribute
FooClass.MyFloat=5

#Add
AttestingStrsList+=[
                'After reset at the level of the class',
                'DefaultFoo.MyFloat is '+str(DefaultFoo.MyFloat),
                'SpecialFoo.MyFloat is '+str(SpecialFoo.MyFloat),
        ]

#Definition
SYS._attest(AttestingStrsList)

#Print


```


```console
>>>


*****Start of the Attest *****

What are you saying DefaultFoo ?

------

DefaultFoo.__dict__ is {'MyStr': 'I am a Foo with MyFloat equal to 1.0 and
Int equal to 3'}

------

DefaultFoo.MyFloat is 1.0

------

DefaultFoo.MyList is []

------

DefaultFoo.MyInt is 0

------

What are you saying SpecialFoo ?

------

SpecialFoo.__dict__ is {'MyList': ['hello'], 'MyInt': 3, 'MyStr': 'I am a Foo
with MyFloat equal to 1.0 and Int equal to 3'}

------

SpecialFoo.MyFloat is 1.0

------

SpecialFoo.MyList is ['hello']

------

DefaultFoo.MyInt is 3

------

After reset at the level of the class

------

DefaultFoo.MyFloat is 5

------

SpecialFoo.MyFloat is 5

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the DefaultorClass are :



<!---
FrozenIsBool True
-->

##Example

We define here a FooClass with some attributes. Here is the difference for a
default instance
DefaultFoo that takes its values from the FooClass.__dict__ and a special one
that sets in its __dict__

```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Classors import Defaultor

#Definition the AttestedStr
SYS._attest(
        [
                'Nothing Special'
        ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

Nothing Special

*****End of the Attest *****




```


```python



#ImportModules
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Standards.Classors import Defaultor

#Definition the AttestedStr
SYS._attest(
        [
                Defaultor.DefaultorClass()
        ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

<ShareYourSystem.Standards.Classors.Defaultor.DefaultorClass object at 0x108d0e750>

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the instances

A default call of an instance gives :

