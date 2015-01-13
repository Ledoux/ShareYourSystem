
#Classor


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



In the ShareYourSystem convention, building a module provide a ModuleStr like
"ShareYourSystem.Objects.Installer" and we call NameStr the end of this
Str, "Installer" here for the cell. In most of the module definitions
provided in this framework, one Module definition is asssociated with one Class
definition taking the \_\_name\_\_ as the \<NameStr\>\<ClassTypeStr\>
(InstallerClass in that cell). The Classor Module defines the ClassorClass
class, which is the deepest parent class in the framework for decorating another
class. For each decorated class, it just sets up the NameStr in it and also a
KeyStrsList for accumulating the new KeyStrs from other attributes that
can be provided by other decorating Classes.





<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive special attributes
from the decorating ClassorClass specially the NameStr, that should be the
ClassStr without the TypeStr in the end.

```python
#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Classors import Classor

#Definition a FooClass decorated by the ClassorClass
@Classor.ClassorClass()
class FooClass():
        pass

#Definition the AttestedStr
SYS._attest(
        [
                'FooClass.KeyStrsList is '+str(FooClass.KeyStrsList),
                'FooClass.NameStr is '+FooClass.NameStr,
                'FooClass.ClassorPointer is '+str(FooClass.ClassorPointer)
        ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

FooClass.KeyStrsList is ['NameStr', 'ClassorPointer']

------

FooClass.NameStr is Foo

------

FooClass.ClassorPointer is <ShareYourSystem.Classors.Classor.ClassorClass object
at 0x1073c2810>

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the ClassorClass are :


```python


#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Classors import Classor

#Definition the AttestedStr
SYS._attest(
        [
                'Classor sets its own NameStr :
'+Classor.ClassorClass.NameStr
        ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

Classor sets its own NameStr : Classor

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
from ShareYourSystem.Classors import Classor

#Definition the AttestedStr
SYS._attest(
        [
                Classor.ClassorClass()
        ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

<ShareYourSystem.Classors.Classor.ClassorClass object at 0x10bdd3750>

*****End of the Attest *****




```

