

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
from ShareYourSystem.Itemizers import Grasper

#Explicit expression
MyGrasper=Grasper.GrasperClass().__setitem__(
    'ChildGrasper',
    Grasper.GrasperClass().__setitem__('MyStr',"hello")
)

#Return
SYS._attest(
    [
        "MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable is "+
        str(
            MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable
            ),
        "MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable is "+
        str(
            MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable
            ),
        "MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyS
tr'})).GraspedAnswerVariable is "+
        str(
MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})
            ).GraspedAnswerVariable),
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyGrasper.grasp('/ChildGrasper/MyStr').GraspedAnswerVariable is hello

------

MyGrasper.grasp(MyGrasper.ChildGrasper).GraspedAnswerVariable is <
(GrasperClass), 4348193680>
   /{
   /  '<New><Instance>IdInt' : 4348193680
   /  '<New><Instance>MyStr' : hello
   /  '<Spe><Class>GraspedAnswerVariable' : None
   /  '<Spe><Class>GraspedClueVariableType' : None
   /  '<Spe><Class>GraspingClueVariable' : None
   /}

------

MyGrasper.grasp(SYS.GraspDictClass(**{'HintVariable':'/ChildGrasper/MyStr'})).Gr
aspedAnswerVariable is hello

*****End of the Attest *****



```

