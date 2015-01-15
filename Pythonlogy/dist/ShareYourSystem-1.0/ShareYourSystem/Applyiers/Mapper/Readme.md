

<!--
FrozenIsBool False
-->

View the Mapper sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
ee/master/ShareYourSystem/Applyiers/Installer)




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
from ShareYourSystem.Applyiers import Mapper

#Definition a Getter
MyMapper=Mapper.MapperClass().map(
    '__setitem__',
    [
        {'LiargVariablesList':['MyStr',"Hello"]},
        {'LiargVariablesList':['MyThirdStr',"GutenTag"]},
        {'LiargVariablesList':['map',
                                        {
                                            'LiargVariablesList':
                                            [
                                                '__setitem__',
                                                [
                                                    {
                                                        'LiargVariablesList':
                                                        ['MyInt',0]
                                                    },
                                                    {
                                                        'LiargVariablesList':
                                                        ['MyFloat',0.1]
                                                    }
                                                ]
                                            ]
                                        }

                            ]},
        {'LiargVariablesList':['MyNotLostStr',"ben he"]},
    ]
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyMapper is '+SYS._str(
        MyMapper,
        **{
            'RepresentingBaseKeyStrsListBool':False
        }
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyMapper is < (MapperClass), 4549669392>
   /{
   /  '<New><Instance>IdInt' : 4549669392
   /  '<New><Instance>MyFloat' : 0.1
   /  '<New><Instance>MyInt' : 0
   /  '<New><Instance>MyNotLostStr' : ben he
   /  '<New><Instance>MyStr' : Hello
   /  '<New><Instance>MyThirdStr' : GutenTag
   /  '<Spe><Instance>MappedVariablesList' :
   /   /[
   /   /  0 : {...}< (MapperClass), 4549669392>
   /   /  1 : {...}< (MapperClass), 4549669392>
   /   /  2 : {...}< (MapperClass), 4549669392>
   /   /  3 : {...}< (MapperClass), 4549669392>
   /   /]
   /  '<Spe><Instance>MappingApplyMethodStr' : __setitem__
   /  '<Spe><Instance>MappingArgDictsList' :
   /   /[
   /   /  0 :
   /   /   /{
   /   /   /  'LiargVariablesList' : ['MyInt', 0]
   /   /   /}
   /   /  1 :
   /   /   /{
   /   /   /  'LiargVariablesList' : ['MyFloat', 0.1]
   /   /   /}
   /   /]
   /}

*****End of the Attest *****



```

