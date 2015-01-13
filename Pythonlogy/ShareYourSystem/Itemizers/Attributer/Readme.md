
#Attributer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Attributer instance has a __setitem__ method for setting things in the
<InstanceVariable>.__dict__ This is helpful for setting mutable variables in the
instance different from the one setted at the level of the class





<!--
FrozenIsBool False
-->

View the Attributer sources on [Github](https://github.com/Ledoux/ShareYourSyste
m/tree/master/ShareYourSystem/Itemizers/Installer)



```python

#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Itemizers import Attributer

#Definition a Attributer and set with the __setitem__
MyAttributer=Attributer.AttributerClass().__setitem__('Attr_MyInt',0)

#Definition the AttestedStr
SYS._attest(
    [
    'MyAttributer is '+SYS._str(
            MyAttributer,
            **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
            }
        )

    ]
)

#Print



```


```console
>>>
Doer l.132 : DoerStr is Itemizer
DoStr is Itemize
DoMethodStr is itemize
DoingStr is Itemizing
DoneStr is Itemized

Doer l.132 : DoerStr is Getter
DoStr is Get
DoMethodStr is get
DoingStr is Getting
DoneStr is Getted

Doer l.132 : DoerStr is Setter
DoStr is Set
DoMethodStr is set
DoingStr is Setting
DoneStr is Setted

Doer l.132 : DoerStr is Deleter
DoStr is Delete
DoMethodStr is delete
DoingStr is Deleting
DoneStr is Deleted

Doer l.132 : DoerStr is Attributer
DoStr is Attribute
DoMethodStr is attribute
DoingStr is Attributing
DoneStr is Attributed



*****Start of the Attest *****

MyAttributer is < (AttributerClass), 4465141392>
   /{
   /  '<New><Instance>IdString' : 4465141392
   /  '<New><Instance>MyInt' : 0
   /  '<Spe><Instance>AttributedSetKeyStr' : MyInt
   /  '<Spe><Instance>AttributingKeyStr' : Attr_MyInt
   /  '<Spe><Instance>AttributingValueVariable' : 0
   /}

*****End of the Attest *****



```

