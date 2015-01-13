

<!--
FrozenIsBool False
-->

#Scriptbooker

----------------------- ------------------------------------



@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Installer directs a readme call in a ShareYourSystem directory.



----------------------------------------------------------------


View the Scriptbooker sources on [Github](https://github.com/Ledoux/ShareYourSys
tem/tree/master/ShareYourSystem.Guiders.Informer)




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
from ShareYourSystem.Guiders import Scriptbooker

#Definition of a Scriptbooker
MyScriptbooker=Scriptbooker.ScriptbookerClass().scriptbook(
        **{
            'FolderingPathStr':
            SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Objects/Object',
            'GuidingBookStr':'Doc'
        }
).scriptbook(**{
            'FolderingPathStr':
SYS.LocalShareYourSystemFolderPathStr+'/ShareYourSystem/Interfacers/Filer',
        }
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyScriptbooker is '+SYS._str(
                MyScriptbooker,
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


*****Start of the Attest *****

MyScriptbooker is < (ScriptbookerClass), 4466232912>
   /{
   /  '<New><Instance>IdStr' : 4466232912
   /  '<New><Instance>ScriptbookedSortDict' :
   /   /{
   /   /  'ExampleDoc.md' : 00_ExampleDoc.md
   /   /  'ExampleDoc.py' : 01_ExampleDoc.py
   /   /  'GithubDoc.md' : 001_GithubDoc.md
   /   /}
   /  '<Spe><Class>ScriptbookingGuideTuplesList' :
   /   /[
   /   /  0 : ('001', 'Github', 'Markdown')
   /   /]
   /  '<Spe><Instance>ScriptbookedFileKeyStrsList' : ['001_GithubDoc.md',
'00_ExampleDoc.md', '01_ExampleDoc.py']
   /  '<Spe><Instance>ScriptbookedNewGuideTuplesList' : []
   /  '<Spe><Instance>ScriptbookedOldGuideTuplesList' :
   /   /[
   /   /  0 : ['001', 'Github', 'Markdown', 'GithubDoc.md']
   /   /]
   /}

*****End of the Attest *****



```

