
#Applyier
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Applyier apply a function thanks to a ApplyingMethodStr and an
ApplyingArgDict. This property is going to be useful to begin to establish
mappping methods and commanding calls in deep structures.





<!--
FrozenIsBool False
-->

View the Applyier sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Applyiers/Installer)




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
from ShareYourSystem.Applyiers import Applyier

#Definition an applyier instance
MyApplyier=Applyier.ApplyierClass()

#Apply just a set... (even if we can do shorter !)
MyApplyier.apply(
    '__setitem__',
    {'LiargVariablesList':['MyStr','Hello']}
)

#Apply an apply is possible
MyApplyier.apply(
    '__setitem__',
    {'LiargVariablesList':[
            '__setitem__',
            {
                'LiargVariablesList':
                ['MyNotLostStr','ben he']
            }
        ]
    }
)

#Definition the AttestedStr
SYS._attest(
    [
    'MyApplyier is '+SYS._str(
            MyApplyier,
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

Doer l.132 : DoerStr is Restricter
DoStr is Restrict
DoMethodStr is restrict
DoingStr is Restricting
DoneStr is Restricted

Doer l.132 : DoerStr is Pather
DoStr is Path
DoMethodStr is path
DoingStr is Pathing
DoneStr is Pathed

Doer l.132 : DoerStr is Sharer
DoStr is Share
DoMethodStr is share
DoingStr is Sharing
DoneStr is Shared

Doer l.132 : DoerStr is Executer
DoStr is Execute
DoMethodStr is execute
DoingStr is Executing
DoneStr is Executed

Doer l.132 : DoerStr is Pointer
DoStr is Point
DoMethodStr is point
DoingStr is Pointing
DoneStr is Pointed

Doer l.132 : DoerStr is Applyier
DoStr is Apply
DoMethodStr is apply
DoingStr is Applying
DoneStr is Applied



*****Start of the Attest *****

MyApplyier is < (ApplyierClass), 4364297872>
   /{
   /  '<New><Instance>ApplyingIsBool' : False
   /  '<New><Instance>IdString' : 4364297872
   /  '<New><Instance>MyNotLostStr' : ben he
   /  '<New><Instance>MyStr' : Hello
   /}

*****End of the Attest *****



```

