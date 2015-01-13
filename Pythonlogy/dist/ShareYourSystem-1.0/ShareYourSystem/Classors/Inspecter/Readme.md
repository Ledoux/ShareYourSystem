
#Inspecter


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Inspecter decorates a class by giving it an InspectedArgumentDict that is an
inspection of all defined methods.



<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive special attributes
from the decorating ClassorClass specially the NameStr, that should be the
ClassStr without the TypeStr in the end.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Inspecter

#Definition a FooClass decorated by the ClassorClass
@Inspecter.InspecterClass()
class MakerClass():
    def make(self,_MakingStr,_MakingInt=0,*_LiargVariablesList,**_KwargVariab
lesDict):
        pass

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.InspectedArgumentDict is
'+Representer.represent(MakerClass.InspectedArgumentDict)
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

MakerClass.InspectedArgumentDict is
   /{
   /  'make' :
   /   /{
   /   /  'DefaultIndexInt' : 2
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /  '_MakingInt' : 0
   /   /   /}
   /   /  'InputKeyStrsList' : ['self', '_MakingStr', '_MakingInt']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' : _LiargVariablesList
   /   /}
   /}

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the InspecterClass are :


```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Inspecter

#Definition the AttestedStr
SYS._attest(
    [
        'DefaultAttributeItemTuplesList is '+SYS._str(
            Inspecter.InspecterClass.DefaultAttributeItemTuplesList,
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
from ShareYourSystem import Classors

#Definition the AttestedStr
SYS._attest(
    [
        Classors.ClassorsClass()
    ]
)

#Print




```


```console
>>>


```

