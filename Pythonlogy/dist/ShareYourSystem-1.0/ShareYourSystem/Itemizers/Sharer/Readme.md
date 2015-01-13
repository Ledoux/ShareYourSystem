
#Sharer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



A Sharer can set attributes at the level of the class





<!--
FrozenIsBool False
-->

View the Sharer sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Itemizers/Installer)




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
from ShareYourSystem.Itemizers import Sharer

#Explicit expression
MySharer=Sharer.SharerClass().__setitem__(
    '__class__.MyStr',
    'I am setted at the level of the class'
)

#Return
SYS._attest(
    [

        'MySharer is '+SYS._str(
                MySharer,
                **{
                'RepresentingBaseKeyStrsListBool':False
                }
            ),
        'MySharer.__class__.MyStr is '+MySharer.__class__.MyStr,
        'MySharer["__class__.MyStr"] is '+MySharer['__class__.MyStr'],
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MySharer is < (SharerClass), 4465477264>
   /{
   /  '<New><Class>MyStr' : I am setted at the level of the class
   /  '<New><Instance>IdString' : 4465477264
   /  '<Spe><Instance>SharedClassDict' :
   /   /{
   /   /}
   /  '<Spe><Instance>SharedSetKeyStr' : MyStr
   /  '<Spe><Instance>SharingKeyStr' : __class__.MyStr
   /  '<Spe><Instance>SharingValueVariable' : I am setted at the level of the
class
   /}

------

MySharer.__class__.MyStr is I am setted at the level of the class

------

MySharer["__class__.MyStr"] is I am setted at the level of the class

*****End of the Attest *****



```

