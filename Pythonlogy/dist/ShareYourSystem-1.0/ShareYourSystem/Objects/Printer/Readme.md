
#Printer


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Printer is an object that can directly print Strs in the Representer
context.





<!--
FrozenIsBool False
-->

View the Printer sources on [Github](https://github.com/Ledoux/ShareYourSystem/t
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
from ShareYourSystem.Objects import Printer

#Definition of an instance Printer and make it print hello
MyPrinter=Printer.PrinterClass()._print('hello')

#Definition the AttestedStr
SYS._attest(
    [
        'MyPrinter is '+SYS._str(MyPrinter)
    ]
)

#Print



```


```console
>>>
hello


*****Start of the Attest *****

MyPrinter is < (PrinterClass), 4556129552>
   /{
   /  '<New><Instance>IdString' : 4556129552
   /  '<Spe><Instance>PrintingVariable' : hello
   /}

*****End of the Attest *****



```

