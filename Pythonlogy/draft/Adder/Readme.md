

<!--
FrozenIsBool False
-->

#Adder

##Doc
----


>
> An Adder maps an append
>

----

<small>
View the Adder notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyours
ystem.ouvaton.org/Adder.ipynb)
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


An Adder maps an append
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Instancer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class AdderClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
#'AddingVariablesList'
                                                                ]

        def default_init(self,
                                                _AddingVariablesList=None,
                                                **_KwargVariablesDict
                                ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Argumenter.ArgumenterClass(**{'ArgumentingDoStr':'Add'})
        def __add__(self,_VariablesList):
                """Apply the append to the <_AddingVariablesList>"""

                #Call the add method
                self.add(_VariablesList)

                #Return
                return self

        def do_add(self):
                """Apply the append to the <_AddingVariablesList>"""

                #debug
                '''
                self.debug(('self.',self,['AddingVariablesList']))
                '''

                #Apply
                self.map('append',map(
                                                                        lambda
__AddingVariable:
{'LiargVariablesList':[__AddingVariable]},
self.AddingVariablesList
                                                                )
                                )

#</DefineClass>

```

<small>
View the Adder sources on <a href="https://github.com/Ledoux/ShareYourSystem/tre
e/master/Pythonlogy/ShareYourSystem/Noders/Adder" target="_blank">Github</a>
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
from ShareYourSystem.Noders import Adder

#Definition an Tree instance
MyAdder=Adder.AdderClass()+[
    [
        ('NodeCollectionStr','Tree'),
        ('NodeKeyStr','MyTuplesList'),
        ('MyStr','Hello')
    ],
    {
        'NodeCollectionStr':'Tree',
        'NodeKeyStr':'MyDict',
        'MyOtherStr':'Bonjour'
    },
    Adder.AdderClass().update(
            [
                ('NodeCollectionStr','Tree'),
                ('NodeKeyStr','MyChildAppender')
            ]
        )
]

#Definition the AttestedStr
SYS._attest(
    [
        'MyAdder is '+SYS._str(
        MyAdder,
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

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Appender/__init__.py do_append
                                            From Appender/__init__.py do_append
| Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic |
Applyier/__init__.py do_apply | Mapper/__init__.py do_map | Adder/__init__.py
do_add | Adder/__init__.py __add__ | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopAdder')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Tree
                                            self.AppendedNodeKeyStr is
MyTuplesList

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Appender/__init__.py do_append
                                            From Appender/__init__.py do_append
| Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic |
Applyier/__init__.py do_apply | Mapper/__init__.py do_map | Adder/__init__.py
do_add | Adder/__init__.py __add__ | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopAdder')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Tree
                                            self.AppendedNodeKeyStr is MyDict

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                                            ////////////////////////////////
                                            Appender/__init__.py do_append
                                            From Appender/__init__.py do_append
| Instancer/__init__.py mimic_append | Mimicker/__init__.py mimic |
Applyier/__init__.py do_apply | Mapper/__init__.py do_map | Adder/__init__.py
do_add | Adder/__init__.py __add__ | site-packages/six.py exec_ |
Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopAdder')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Tree
                                            self.AppendedNodeKeyStr is
MyChildAppender

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyAdder is < (AdderClass), 4555575760>
   /{
   /  '<New><Instance>IdInt' : 4555575760
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopAdder
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  'MyTuplesList' :
   /   /   /[
   /   /   /  0 : ('NodeCollectionStr', 'Tree')
   /   /   /  1 : ('NodeKeyStr', 'MyTuplesList')
   /   /   /  2 : ('MyStr', 'Hello')
   /   /   /]
   /   /  'MyDict' :
   /   /   /{
   /   /   /  'MyOtherStr' : Bonjour
   /   /   /  'NodeCollectionStr' : Tree
   /   /   /  'NodeKeyStr' : MyDict
   /   /   /}
   /   /  'MyChildAppender' : < (AdderClass), 4555209680>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4555209680
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : MyChildAppender
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (AdderClass),
4555575760>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556378784>
   /   /   /}
   /   /}
   /}

*****End of the Attest *****



```

