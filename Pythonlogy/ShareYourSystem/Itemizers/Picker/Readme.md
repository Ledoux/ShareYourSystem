

<!--
FrozenIsBool False
-->

#Picker

##Doc
----


>
> A Picker maps a __getitem__
>
>

----

<small>
View the Picker notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Picker.ipynb)
</small>




<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


A Picker maps a __getitem__

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Mapper"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'DoingGetBool':True})
class PickerClass(BaseClass):

        def default_init(self,
                                _PickingKeyVariablesList=None,
                                _PickedValueVariablesList=None,
                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_pick(self):
                """Map the __getitem__ to the <_GettingVariablesList>"""

                #debug
                '''
                self.debug(('self.',self,['PickingKeyVariablesList']))
                '''

                #Apply __getitem__
                self.map('__getitem__',map(
                                                                        lambda
__PickingKeyVariable:
{'LiargVariablesList':[__PickingKeyVariable]},
self.PickingKeyVariablesList
                                                                )
                                        )

                #link with AppliedMappedVariablesList
                self.PickedValueVariablesList=self.MappedVariablesList

                #debug
                '''
                self.debug(('self.',self,['PickedValueVariablesList']))
                '''

                #Return AppliedVariablesList
                return self.PickedValueVariablesList
#</DefineClass>

```

<small>
View the Picker sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Applyiers/Picker"
target="_blank">Github</a>
</small>




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
   /  1 : < (PickerClass), 4555210256>
   /   /{
   /   /  '<New><Instance>IdInt' : 4555210256
   /   /  '<New><Instance>MyStr' : hello
   /   /}
   /  2 : hello
   /]

*****End of the Attest *****



```

