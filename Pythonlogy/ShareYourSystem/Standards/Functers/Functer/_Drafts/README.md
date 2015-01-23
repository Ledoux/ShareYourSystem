
#Functer




<!---
FrozenIsBool True
-->

##Example

For this non directly very useful Module we just define a decorated FooClass
for which the Functer decoration by default call the decorated method...

```python
#ImportModules
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Functers import Functer

#Definition a derived second Class
class FooClass():

    @Functer.FuncterClass()
    def printSomething(self,**_KwargVariablesDict):
        print('Something !')

    #Functers can be cumulated
    @Functer.FuncterClass()
    @Functer.FuncterClass()
    def printOtherthing(self,**_KwargVariablesDict):
        print('An Other Thing ?')

#Definition an instance
MyFoo=FooClass()

#Do just a test of the basic FirstClass method printSomething
MyFoo.printSomething()

#Do just a test of the basic FirstClass method printSomething
MyFoo.printOtherthing()


```


```console
>>>
Something !
An Other Thing ?


```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the FuncterClass are :


```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Functers import Functer

#Definition the AttestedStr
SYS._attest(
    [
        'DefaultAttributeItemTuplesList is '+SYS._str(
            Functer.FuncterClass.DefaultAttributeItemTuplesList,
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
from ShareYourSystem.Standards.Classors import Attester
from ShareYourSystem.Functers import Functer

#Definition the AttestedStr
SYS._attest(
    [
        Functer.FuncterClass()
    ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

< (FuncterClass), 4445764880>
   /{
   /  '<Base><Class>PrintingVariable' : None
   /  '<New><Instance>FunctedClass' : None
   /  '<New><Instance>FunctedFunction' : None
   /  '<New><Instance>FunctedIsBool' : False
   /  '<New><Instance>FunctedModuleStr' :
   /  '<New><Instance>FunctingFunction' : None
   /}

*****End of the Attest *****




```

