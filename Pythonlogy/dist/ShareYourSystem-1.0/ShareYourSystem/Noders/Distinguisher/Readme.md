

<!--
FrozenIsBool False
-->

#Distinguisher

##Doc
----


>
> A Distinguisher is a bit the opposite of a Commander, it updates
> for every child nodes with a distinguished tuples list.
>
>

----

<small>
View the Distinguisher notebook on [NbViewer](http://nbviewer.ipython.org/url/sh
areyoursystem.ouvaton.org/Distinguisher.ipynb)
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


A Distinguisher is a bit the opposite of a Commander, it updates
for every child nodes with a distinguished tuples list.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Adder"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Noders import Noder
#</ImportSpecificModules>

#<DefineLocals>
DistinguishingPrefixStr="Dis_"
#</DefineLocals

#<DefineClass>
@DecorationClass()
class DistinguisherClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'DistinguishingNodeStr',
'DistinguishingUpdatesList',
'DistinguishedCollectionOrderedDict'
                                                        ]

        def default_init(self,
                                _DistinguishingNodeStr="",
                                _DistinguishingUpdatesList=None,
                                _DistinguishedCollectionOrderedDict=None,
                                **_KwargVariablesDict
                                ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def mimic_set(self):
                """ """

                #debug
                '''
self.debug(('self.',self,['SettingKeyVariable','SettingValueVariable']))
                '''

                #Definition
                OutputDict={'HookingIsBool':True}

                #Deep set
                if self.SettingKeyVariable.startswith(DistinguishingPrefixStr):

                        #debug
                        '''
                        self.debug('We are going to distinguish')
                        '''


                        #set arguments
self.DistinguishingNodeStr=Noder.NodingSuffixGetStr.join(
                                        (
                                                Noder.NodingPrefixGetStr.join(
self.SettingKeyVariable.split(
Noder.NodingPrefixGetStr
                                                        )[1:]
                                                )
                                        ).split(Noder.NodingSuffixGetStr)[:-1]
                                )

                        self.DistinguishingUpdatesList=self.SettingValueVariable

                        #debug
                        '''
                        self.debug(('self.',self,[
                                        'DistinguishingNodeStr',
                                        'DistinguishingUpdatesList'
                                        ]))
                        '''

                        #distinguish
                        self.distinguish()

                        #Stop the setting
                        OutputDict["HookingIsBool"]=False
                        #<Hook>return OutputDict

                #Call the parent get method
                if OutputDict['HookingIsBool']:
                        BaseClass.set(self)

        def do_distinguish(self):
                """ """

                #Check
                if self.DistinguishingNodeStr!="":

                        #debug
                        '''
                        self.debug(('self.',self,['DistinguishingNodeStr']))
                        '''

                        #get
                        self.DistinguishedCollectionOrderedDict=getattr(
                                self,
self.DistinguishingNodeStr+'CollectionOrderedDict'
                        )

                        #Map the distinguished updates
                        map(
                                lambda __NodeVariable,__UpdateTuplesList:
                                __NodeVariable.update(__UpdateTuplesList),
self.DistinguishedCollectionOrderedDict.values(),
                                self.DistinguishingUpdatesList
                        )

#</DefineClass>

```

<small>
View the Distinguisher sources on <a href="https://github.com/Ledoux/ShareYourSy
stem/tree/master/Pythonlogy/ShareYourSystem/Noders/Distinguisher"
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
from ShareYourSystem.Noders import Distinguisher
import copy

#Definition a tree of Distinguishers.
MyDistinguisher=Distinguisher.DistinguisherClass().__add__(
    [
        Distinguisher.DistinguisherClass().update(
            [
                ('NodeCollectionStr','Tree'),
                ('NodeKeyStr',str(Int1))
            ]
        ) for Int1 in xrange(2)
    ]
)

#distinguish
MyDistinguisher.distinguish("Tree",[
                                        [('MyStr',"hello")],
                                        [('MyInt',0)]
                                    ])

#distinguish through setting
MyDistinguisher.__setitem__(
    "Dis_<Tree>",
    [
        [('MyOtherStr',"bonjour")],
        [('MyOtherInt',1)]
    ]
)

#Definition the AttestedStr
SYS._attest(
    [
        'MyDistinguisher is '+SYS._str(
        MyDistinguisher,
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
Documenter/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopDistinguisher')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Tree
                                            self.AppendedNodeKeyStr is 0

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
Documenter/__init__.py do_inform | inform.py <module>
                                            ////////////////////////////////

                                            l.138 :
                                            *****
                                            I am with [('NodeKeyStr',
'TopDistinguisher')]
                                            *****
                                            self.AppendedNodeCollectionStr is
Tree
                                            self.AppendedNodeKeyStr is 1

                                            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyDistinguisher is < (DistinguisherClass), 4555575888>
   /{
   /  '<New><Instance>IdInt' : 4555575888
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopDistinguisher
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>TreeCollectionOrderedDict' :
   /   /{
   /   /  '0' : < (DistinguisherClass), 4556355728>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556355728
   /   /   /  '<New><Instance>MyOtherStr' : bonjour
   /   /   /  '<New><Instance>MyStr' : hello
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : 0
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(DistinguisherClass), 4555575888>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4537207184>
   /   /   /  '<Spe><Class>DistinguishedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>DistinguishingNodeStr' :
   /   /   /  '<Spe><Class>DistinguishingUpdatesList' : None
   /   /   /}
   /   /  '1' : < (DistinguisherClass), 4556354960>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556354960
   /   /   /  '<New><Instance>MyInt' : 0
   /   /   /  '<New><Instance>MyOtherInt' : 1
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 1
   /   /   /  '<New><Instance>NodeKeyStr' : 1
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}<
(DistinguisherClass), 4555575888>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4537207184>
   /   /   /  '<Spe><Class>DistinguishedCollectionOrderedDict' : None
   /   /   /  '<Spe><Class>DistinguishingNodeStr' :
   /   /   /  '<Spe><Class>DistinguishingUpdatesList' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>DistinguishedCollectionOrderedDict' : {...}<
(OrderedDict), 4537207184>
   /  '<Spe><Instance>DistinguishingNodeStr' : Tree
   /  '<Spe><Instance>DistinguishingUpdatesList' :
   /   /[
   /   /  0 :
   /   /   /[
   /   /   /  0 : ('MyOtherStr', 'bonjour')
   /   /   /]
   /   /  1 :
   /   /   /[
   /   /   /  0 : ('MyOtherInt', 1)
   /   /   /]
   /   /]
   /}

*****End of the Attest *****



```

