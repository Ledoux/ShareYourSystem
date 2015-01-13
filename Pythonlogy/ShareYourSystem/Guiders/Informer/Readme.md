

<!--
FrozenIsBool False
-->

#Informer

----------------------- ------------------------------------



@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Installer directs a readme call in a ShareYourSystem directory.



----------------------------------------------------------------


View the Informer sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem.Guiders.Informer)




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
from ShareYourSystem.Guiders import Informer

#Definition an Informer instance
MyInformer=Informer.InformerClass()

#Definition the AttestedStr
SYS._attest(
    [
        'MyInformer is '+SYS._str(
        MyInformer,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        )
    ]
)



```


```console
>>>


*****Start of the Attest *****

MyInformer is < (InformerClass), 4466183888>
   /{
   /  '<New><Instance>IdStr' : 4466183888
   /  '<Spe><Class>InformedConceptModule' : None
   /  '<Spe><Class>InformedModulePathStrsList' : None
   /  '<Spe><Class>InformedModulesList' : None
   /  '<Spe><Class>InformedNameStrsList' : None
   /  '<Spe><Class>InformingConceptFolderPathStr' :
   /  '<Spe><Class>InformingConceptIsBool' : True
   /  '<Spe><Class>InformingReadmeIsBool' : True
   /}

*****End of the Attest *****



```

