

<!--
FrozenIsBool False
-->

#Guider

----------------------- ------------------------------------



@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Installer directs a readme call in a ShareYourSystem directory.



----------------------------------------------------------------


View the Guider sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem.Guiders.Informer)




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
from ShareYourSystem.Guiders import Guider
from ShareYourSystem.Objects import Concluder

#Definition an instance
MyGuider=Guider.GuiderClass().guide(
    '001','Github','Doc','Markdown'
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyGuider is '+str(
            SYS._str(
                MyGuider,
                **{
                'RepresentingBaseKeyStrsListBool':False
                }
            )
        )
    ]
)

```


```console
>>>


*****Start of the Attest *****

MyGuider is < (GuiderClass), 4466183440>
   /{
   /  '<New><Instance>IdStr' : 4466183440
   /  '<Spe><Class>GuidedIndexStr' :
   /  '<Spe><Instance>GuidingBookStr' : Doc
   /  '<Spe><Instance>GuidingIndexStr' : 001
   /  '<Spe><Instance>GuidingPageStr' : Github
   /  '<Spe><Instance>GuidingScriptStr' : Markdown
   /}

*****End of the Attest *****



```

