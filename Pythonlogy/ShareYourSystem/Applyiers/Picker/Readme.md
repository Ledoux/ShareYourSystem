

<!--
FrozenIsBool False
-->

View the Picker sources on [Github](https://github.com/Ledoux/ShareYourSystem/tr
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
from ShareYourSystem.Applyiers import Picker

#Definition an Picker
MyPicker=Picker.PickerClass()

#set some items
map(
        lambda __ItemTuple:
        MyPicker.__setitem__(__ItemTuple[0],__ItemTuple[1]),
        [
            ('MyInt',0),
            ('MyPicker',Picker.PickerClass().__setitem__('MyStr',"hello")),
        ]
    )

#Map some gets
PickedVariablesList=MyPicker.pick(
    [
        #Get directly in the __dict__
        'MyInt',
        'MyPicker',
        #Get with a DeepShortStr
        '/MyPicker/MyStr'
    ]
)

#Definition the AttestedStr
SYS._attest(
    [
        'PickedVariablesList is '+SYS._str(
            PickedVariablesList
            ,**{
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

PickedVariablesList is
   /[
   /  0 : 0
   /  1 : < (PickerClass), 4549771856>
   /   /{
   /   /  '<New><Instance>IdInt' : 4549771856
   /   /  '<New><Instance>MyStr' : hello
   /   /}
   /  2 : hello
   /]

*****End of the Attest *****



```

