
#Moduler


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Moduler is an Object that helps to get a module in the SYS framework





<!--
FrozenIsBool False
-->

View the Moduler sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
ree/master/ShareYourSystem/Objects/Installer)




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
from ShareYourSystem.Objects import Moduler

#Definition of a Moduler instance and module
MyModuler=Moduler.ModulerClass().module('ShareYourSystem.Objects.Printer')

#Definition the AttestedStr
SYS._attest(
    [
        'MyModuler'+SYS._str(MyModuler)
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyModuler< (ModulerClass), 4556059280>
   /{
   /  '<New><Instance>IdString' : 4556059280
   /  '<Spe><Instance>PackagingModuleVariable' : <module
'ShareYourSystem.Objects.Printer' from '/Users/ledoux/Documents/ShareYourSystem/
ShareYourSystem/Objects/Printer/__init__.pyc'>
   /  '<Spe><Instance>PackagingModuleVariableStr' : ShareYourSystem.Objects.Printer
   /}

*****End of the Attest *****



```

