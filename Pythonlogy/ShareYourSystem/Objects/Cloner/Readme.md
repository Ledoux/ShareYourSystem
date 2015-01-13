
#Cloner


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Cloner





<!--
FrozenIsBool False
-->

View the Cloner sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Objects/Installer)




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
from ShareYourSystem.Objects import Cloner

#Definition of an instance Cloner
MyCloner=Cloner.ClonerClass()
MyCloner.MyInt=1

#clone
MyFirstCloner=MyCloner.clone()
MyFirstCloner.MyInt=2

#Definition the AttestedStr
SYS._attest(
                    [
                        'MyCloner is '+SYS._str(MyCloner),
                        'MyFirstCloner is '+SYS._str(MyFirstCloner)
                    ]
                )

#Print



```


```console
>>>
Doer l.132 : DoerStr is Cloner
DoStr is Clone
DoMethodStr is clone
DoingStr is Cloning
DoneStr is Cloned

('CloningNotCopyKeyStringsList', [])
('MyInt', 1)
('ClonedItemTuplesList', [])
('CloningIdsDict', {})
('IdString', 4556060240)
('_WatchCloneWithClonerBool', True)


*****Start of the Attest *****

MyCloner is < (ClonerClass), 4556060240>
   /{
   /  '<New><Instance>IdString' : 4556060240
   /  '<New><Instance>MyInt' : 1
   /  '<Spe><Class>CloningResetBool' : False
   /  '<Spe><Instance>ClonedCopyVariable' : < (ClonerClass), 4556062608>
   /   /{
   /   /  '<New><Instance>IdString' : 4556060240
   /   /  '<New><Instance>MyInt' : 2
   /   /  '<Spe><Class>ClonedCopyVariable' : None
   /   /  '<Spe><Class>CloningResetBool' : False
   /   /  '<Spe><Instance>ClonedItemTuplesList' :
   /   /   /[
   /   /   /  0 :
   /   /   /   /(
   /   /   /   /  0 : CloningNotCopyKeyStringsList
   /   /   /   /  1 : []
   /   /   /   /)
   /   /   /  1 : ('MyInt', 1)
   /   /   /  2 :
   /   /   /   /(
   /   /   /   /  0 : ClonedItemTuplesList
   /   /   /   /  1 : []
   /   /   /   /)
   /   /   /  3 :
   /   /   /   /(
   /   /   /   /  0 : CloningIdsDict
   /   /   /   /  1 :
   /   /   /   /   /{
   /   /   /   /   /}
   /   /   /   /)
   /   /   /  4 : ('IdString', 4556060240)
   /   /   /  5 :
   /   /   /   /(
   /   /   /   /  0 : _WatchCloneWithClonerBool
   /   /   /   /  1 : True
   /   /   /   /)
   /   /   /]
   /   /  '<Spe><Instance>CloningIdsDict' : {...}< (dict), 4556155432>
   /   /  '<Spe><Instance>CloningNotCopyKeyStringsList' : {...}< (list),
4555996912>
   /   /}
   /  '<Spe><Instance>ClonedItemTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : CloningNotCopyKeyStringsList
   /   /   /  1 : []
   /   /   /)
   /   /  1 : {...}< (tuple), 4555685472>
   /   /  2 :
   /   /   /(
   /   /   /  0 : ClonedItemTuplesList
   /   /   /  1 : []
   /   /   /)
   /   /  3 :
   /   /   /(
   /   /   /  0 : CloningIdsDict
   /   /   /  1 :
   /   /   /   /{
   /   /   /   /}
   /   /   /)
   /   /  4 : {...}< (tuple), 4555709616>
   /   /  5 : {...}< (tuple), 4555708248>
   /   /]
   /  '<Spe><Instance>CloningIdsDict' : {...}< (dict), 4556156552>
   /  '<Spe><Instance>CloningNotCopyKeyStringsList' : {...}< (list), 4555993240>
   /}

------

MyFirstCloner is < (ClonerClass), 4556062608>
   /{
   /  '<New><Instance>IdString' : 4556060240
   /  '<New><Instance>MyInt' : 2
   /  '<Spe><Class>ClonedCopyVariable' : None
   /  '<Spe><Class>CloningResetBool' : False
   /  '<Spe><Instance>ClonedItemTuplesList' :
   /   /[
   /   /  0 :
   /   /   /(
   /   /   /  0 : CloningNotCopyKeyStringsList
   /   /   /  1 : []
   /   /   /)
   /   /  1 : ('MyInt', 1)
   /   /  2 :
   /   /   /(
   /   /   /  0 : ClonedItemTuplesList
   /   /   /  1 : []
   /   /   /)
   /   /  3 :
   /   /   /(
   /   /   /  0 : CloningIdsDict
   /   /   /  1 :
   /   /   /   /{
   /   /   /   /}
   /   /   /)
   /   /  4 : ('IdString', 4556060240)
   /   /  5 :
   /   /   /(
   /   /   /  0 : _WatchCloneWithClonerBool
   /   /   /  1 : True
   /   /   /)
   /   /]
   /  '<Spe><Instance>CloningIdsDict' : {...}< (dict), 4556155432>
   /  '<Spe><Instance>CloningNotCopyKeyStringsList' : {...}< (list), 4555996912>
   /}

*****End of the Attest *****



```

