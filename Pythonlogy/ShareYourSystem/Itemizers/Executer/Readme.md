
#Executer
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



An Executer can exec commands with the six.exec_ function



<!--
FrozenIsBool False
-->

View the Executer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Itemizers/Installer)




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
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Itemizers import Executer

#Definition and update with an exec Str
MyExecuter=Executer.ExecuterClass()

MySecondInt=MyExecuter.__setitem__(
    'MySecondInt',
    'Exec_self.SettingValueVariable=1+1'
).MySecondInt

#Exec is also possible in a getting
GettedValueVariable=MyExecuter['Exec_self.GettedValueVariable=self.MySecondInt-1
']

#Definition the AttestedStr
SYS._attest(
    [
        'MySecondInt is  '+str(MySecondInt),
        'GettedValueVariable is '+str(GettedValueVariable)
    ]
)

#Print



```


```console
>>>
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



*****Start of the Attest *****

MySecondInt is  2

------

GettedValueVariable is None

*****End of the Attest *****



```

