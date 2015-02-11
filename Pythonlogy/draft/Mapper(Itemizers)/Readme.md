

<!--
FrozenIsBool False
-->

#Mapper

##Doc
----


> A Mapper instance maps an apply and so "grinds" a MappingArgDictsList
> to a method.
>
>

----

<small>
View the Mapper notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Mapper.ipynb)
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

A Mapper instance maps an apply and so "grinds" a MappingArgDictsList
to a method.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Applyiers.Applyier"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
from ShareYourSystem.Functers import Argumenter
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class MapperClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'MappingApplyMethodStr',
'MappingArgDictsList',
'MappedVariablesList'
                                                                ]

        def default_init(self,
                                _MappingApplyMethodStr="",
                                _MappingArgDictsList=None,
                                _MappedVariablesList=None,
                                **_KwargVariablesDict
                                ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #<DefineDoMethods>
        def do_map(self):
                """ """

                #debug
                '''
                self.debug(
                                        ('self.',self,[
'MappingMethodStr',
'MappingArgDictsList'
                                                                ])
                        )
                '''

                #Link to the apply features
                if hasattr(self,self.MappingApplyMethodStr):

                        #set the AppliedMethod
self.AppliedMethod=getattr(self,self.MappingApplyMethodStr)

                        #set that it is ok
                        self.ApplyingIsBool=True

                        #debug
                        '''
                        self.debug(
                                                ('self.',self,[
'AppliedMethod'
                                                                        ])
                                )
                        '''

                        #Map the apply
                        self.MappedVariablesList=map(
                                        lambda __MappingArgDict:
                                        self.apply(
self.MappingApplyMethodStr,
                                                                __MappingArgDict
                                                        ).AppliedOutputVariable,
                                        self.MappingArgDictsList
                                )

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Mapper sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Applyiers/Mapper"
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

MyMapper is < (MapperClass), 4554250512>
   /{
   /  '<New><Instance>IdInt' : 4554250512
   /  '<New><Instance>MyFloat' : 0.1
   /  '<New><Instance>MyInt' : 0
   /  '<New><Instance>MyNotLostStr' : ben he
   /  '<New><Instance>MyStr' : Hello
   /  '<New><Instance>MyThirdStr' : GutenTag
   /  '<Spe><Instance>MappedVariablesList' :
   /   /[
   /   /  0 : {...}< (MapperClass), 4554250512>
   /   /  1 : {...}< (MapperClass), 4554250512>
   /   /  2 : {...}< (MapperClass), 4554250512>
   /   /  3 : {...}< (MapperClass), 4554250512>
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

