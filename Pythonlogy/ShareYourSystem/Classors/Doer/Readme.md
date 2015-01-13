
#Doer


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Doer defines a huge family of classes in this framework, that are going to
be decorated by the DoerClass. Staying on the idea, that one module should
associate one class, now a decorated class by a Doer should have a NameStr
that is a DoStr and express also method a method with the name
<DoStr>[0].lower()+<DoStr>[1:] All the attributes that are controlling
this method process are <DoingStr><MiddleStr><TypeStr> and all the ones
resetted during the method are <DoneStr><MiddleStr><TypeStr>. This
helps a lot for defining a fisrt level of objects that are acting like input-
output controllers.





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
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Initiator
from ShareYourSystem.Classors import Doer

#Definition a MakerClass decorated by the DefaultorClass
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):

    def default_init(self,
                _MakingMyFloat=1.,
                _MakingMyList=[],
                _MakingMyInt={'DefaultingSetType':int},
                _MadeMyInt=0):

        #Definition an attribute
        self.MakeStr="I am a Maker with "+str(self.MakingMyFloat)

    def make():
        self.MadeInt=int(self.MakingMyFloat)

#Definition a default instance
DefaultMaker=MakerClass()

#Definition a special instance
SpecialMaker=MakerClass(_MakingMyList=['hello'],**{'MakingMyInt':3})

#Definition the AttestedStr
AttestingStrsList=[
    'MakerClass has some special attributes',
    'MakerClass.DoingAttributeVariablesOrderedDict is
'+str(MakerClass.DoingAttributeVariablesOrderedDict),
    'MakerClass.DoneAttributeVariablesOrderedDict is
'+str(MakerClass.DoneAttributeVariablesOrderedDict),
    'MakerClass.MakingMyFloat is '+str(MakerClass.MakingMyFloat),
    'MakerClass.MakingMyList is '+str(MakerClass.MakingMyList),
    'MakerClass.MadeMyInt is '+str(MakerClass.MadeMyInt),
    'What are you saying DefaultMaker ?',
    'DefaultMaker.__dict__ is '+str(DefaultMaker.__dict__),
    'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
    'DefaultMaker.MakingMyList is '+str(DefaultMaker.MakingMyList),
    'DefaultMaker.MakingMyInt is '+str(DefaultMaker.MakingMyInt),
    'What are you saying SpecialMaker ?',
    'SpecialMaker.__dict__ is '+str(SpecialMaker.__dict__),
    'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
    'SpecialMaker.MakingMyList is '+str(SpecialMaker.MakingMyList),
    'DefaultMaker.MakingMyInt is '+str(SpecialMaker.MakingMyInt)
]

#Change a classed attribute
MakerClass.MakingMyFloat=5

#Add
AttestingStrsList+=[
        'After reset at the level of the class',
        'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
        'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
    ]

#Definition
SYS._attest(AttestingStrsList)

#Print


```


```console
>>>


```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the DoerClass are :



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
from ShareYourSystem.Classors import Defaultor

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
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Classors import Defaultor

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

<ShareYourSystem.Classors.Defaultor.DefaultorClass object at 0x1088d3750>

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the instances

A default call of an instance gives :

