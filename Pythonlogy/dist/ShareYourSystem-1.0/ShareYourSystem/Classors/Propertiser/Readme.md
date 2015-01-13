
#Propertiser


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Propertiser is an augmented Defaultor because it will set defaults
attributes possibly in properties for the new-style decorated classes. This can
set objects with high controlling features thanks to the binding





<!---
FrozenIsBool True
-->

##Example

Going back to the Doer cell when we invented a very minimalist Maker.
We now define its MakingMyFloat as a property that can be then defined as
a "binding" attribute thanks to the setMakingMyFloat method definition,
that will be linked to the fset attribute of the property object.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Propertiser
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass decorated by the PropertiserClass
@Propertiser.PropertiserClass()
class MakerClass(Initiator.InitiatorClass):

    def default_init(self,
            _MakingMyFloat={
                            'DefaultingSetType':property,
                            'PropertizingInitVariable':3.,
                            'PropertizingDocStr':'I am doing the thing here'
                            },
            _MakingMyList=[],
            _MakingMyInt={'DefaultingSetType':int},
            _MadeMyInt=0
        ):
        pass

    #Definition a binding function
    def setMakingMyFloat(self,_SettingValueVariable):

        #Print
        #print('I am going to make the job directly !')

        #set the value of the "hidden" property variable
        self._MakingMyFloat=_SettingValueVariable

        #Bind with MadeInt setting
        self.MadeMyInt=int(self._MakingMyFloat)

#Definition a default instance
DefaultMaker=MakerClass()

#Definition a special instance
SpecialMaker=MakerClass(_MakingMyFloat=5)

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.PropertizedDefaultTuplesList is
'+Representer.represent(MakerClass.PropertizedDefaultTuplesList),
        'What are you saying DefaultMaker ?',
        'DefaultMaker.__dict__ is '+str(DefaultMaker.__dict__),
        'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
        'DefaultMaker.MadeMyInt is '+str(DefaultMaker.MadeMyInt),
        'What are you saying SpecialMaker ?',
        'SpecialMaker.__dict__ is '+str(SpecialMaker.__dict__),
        'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
        'SpecialMaker.MadeMyInt is '+str(SpecialMaker.MadeMyInt),
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

MakerClass.PropertizedDefaultTuplesList is
   /[
   /  0 :
   /   /(
   /   /  0 : MakingMyFloat
   /   /  1 : <property object at 0x105fa8c58>
   /   /)
   /]

------

What are you saying DefaultMaker ?

------

DefaultMaker.__dict__ is {}

------

DefaultMaker.MakingMyFloat is 3.0

------

DefaultMaker.MadeMyInt is 0

------

What are you saying SpecialMaker ?

------

SpecialMaker.__dict__ is {'MadeMyInt': 5, '_MakingMyFloat': 5}

------

SpecialMaker.MakingMyFloat is 5

------

SpecialMaker.MadeMyInt is 5

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the PropertiserClass are :


```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Propertiser

#Definition the AttestedStr
SYS._attest(
    [
        'DefaultAttributeItemTuplesList is '+SYS._str(
            Propertiser.PropertiserClass.DefaultAttributeItemTuplesList,
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
from ShareYourSystem.Classors import Propertiser

#Definition the AttestedStr
SYS._attest(
    [
        Propertiser.PropertiserClass()
    ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

<ShareYourSystem.Classors.Propertiser.PropertiserClass object at 0x106417750>

*****End of the Attest *****




```

