
#Databaser
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Databaser rises to the DatabaserClass. This latter is the deepest class for
instancing Variables able to store values in hierarchic tables. Here, as a first
step, the database method helps to set the <DatabasingKeyStr> in the __dict__





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
from ShareYourSystem.Objects import Databaser

#Definition a Getter
MyDatabaser=Databaser.DatabaserClass().database('Parameters')

#Definition the AttestedStr
SYS._attest(
    [
        'MyDatabaser is '+SYS._str(
        MyDatabaser,
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


*****Start of the Attest *****

MyDatabaser is < (DatabaserClass), 4333452176>
   /{
   /  '<New><Class>SwitchedClassDatabaseBool' : True
   /  '<New><Class>SwitchingDatabaseBool' : False
   /  '<New><Instance>SwitchingDatabaseBool' : True
   /  '<Spe><Instance>DatabasedSuffixStr' : ParametersModel
   /  '<Spe><Instance>DatabasingKeyStr' : Parameters
   /}

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the DatabaserClass are :


```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Databaser

#Definition the AttestedStr
SYS._attest(
    [
        'DefaultAttributeItemTuplesList is '+SYS._str(
            Databaser.DatabaserClass.DefaultAttributeItemTuplesList,
            **{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

DefaultAttributeItemTuplesList is
   /[
   /  0 : ('DatabasingKeyStr', '')
   /  1 : ('DatabasedSuffixStr', '')
   /]

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
from ShareYourSystem.Objects import Databaser

#Definition the AttestedStr
SYS._attest(
    [
        Databaser.DatabaserClass()
    ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

< (DatabaserClass), 4575017936>
   /{
   /  '<Spe><Class>DatabasedSuffixStr' :
   /  '<Spe><Class>DatabasingKeyStr' :
   /}

*****End of the Attest *****




```

