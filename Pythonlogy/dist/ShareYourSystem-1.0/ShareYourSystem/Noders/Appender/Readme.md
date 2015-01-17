

<!--
FrozenIsBool False
-->

#Appender

##Doc
----


>
> An Appender append by doing a set in a NodedOrderedDict thanks to the
<AppendedNodeCollectionStr><AppendedNodeKeyStr>
>
>

----

<small>
View the Appender notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Appender.ipynb)
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


An Appender append by doing a set in a NodedOrderedDict thanks to the
<AppendedNodeCollectionStr><AppendedNodeKeyStr>

"""


#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Noders.Noder"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections

from ShareYourSystem.Applyiers import Updater
Noder=BaseModule
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class AppenderClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'AppendingCollectionVariable',
'AppendedNodeCollectionStr',
'AppendedNodeKeyStr'
                                                                ]

        def default_init(self,
_AppendingCollectionVariable=None,
                                                _AppendedNodeCollectionStr="",
                                                _AppendedNodeKeyStr="",
                                                **_KwargVariablesDict
                                        ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_append(self):
                """ """

                #debug
                '''
                self.debug('self.AppendingCollectionVariable is
'+str(self.AppendingCollectionVariable))
                '''

                #TuplesList Case
                if SYS.getIsTuplesListBool(self.AppendingCollectionVariable):

                        #debug
                        '''
                        self.debug('This is a tuples list')
                        '''

                        #Definition the KeyStrsList
AppendedKeyStrsList=SYS.unzip(self.AppendingCollectionVariable,[0])

                        #Look for an AppendingNodeCollectionStr
                        try:
NodeCollectionStrIndexInt=AppendedKeyStrsList.index(
                                        "NodeCollectionStr"
                                )
self.AppendedNodeCollectionStr=self.AppendingCollectionVariable[
                                        NodeCollectionStrIndexInt
                                ][1]

                                '''
#self.AppendedKeyStrKeyStr='Noded'+self.AppendedNodeCollectionStr+'KeyStr'
                                try:
AppendedKeyStrIndexInt=AppendedKeyStrsList.index(
                                                self.AppendedKeyStrKeyStr
                                        )
self.AppendedKeyStr=self.AppendingCollectionVariable[KeyStrIndexInt][1]
                                except:
                                        pass
                                '''
                                NodeKeyStrIndexInt=AppendedKeyStrsList.index(
                                        "NodeKeyStr"
                                )
self.AppendedNodeKeyStr=self.AppendingCollectionVariable[
                                        NodeKeyStrIndexInt
                                ][1]

                        except:
                                pass

                else:

                        #Objects Case
                        if "AppenderClass" in map(
                                                        lambda __Class:
                                                        __Class.__name__,
type(self.AppendingCollectionVariable).__mro__
                                                        ):

                                #debug
                                '''
                                self.debug('This is a derived object from an
Appender')
                                '''

                                #set
AppendedDict=self.AppendingCollectionVariable.__dict__

                        #dict Case
                        elif type(self.AppendingCollectionVariable) in
[dict,collections.OrderedDict]:
                                AppendedDict=self.AppendingCollectionVariable

                        try:

                                #set
self.AppendedNodeCollectionStr=AppendedDict["NodeCollectionStr"]
                                self.AppendedNodeKeyStr=AppendedDict[
                                                'NodeKeyStr'
                                ]

                        except:
                                pass

                #Init the SettingVariable and Add the NodifyingStr
                AppendedSettingKeyVariable=Noder.NodingPrefixGetStr+self.Appende
dNodeCollectionStr+Noder.NodingSuffixGetStr+self.AppendedNodeKeyStr

                #debug
                self.debug([
                                                ('self.',self,[
        'AppendedNodeCollectionStr',
        'AppendedNodeKeyStr'
])
                                        ]
                                )

                #Then set
                if
AppendedSettingKeyVariable!=Noder.NodingPrefixGetStr+Noder.NodingSuffixGetStr:
                        self.__setitem__(
AppendedSettingKeyVariable,
self.AppendingCollectionVariable
                                                        )

                #Return self
                #return self

#</DefineClass>

```

<small>
View the Appender sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Noders/Appender"
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
from ShareYourSystem.Noders import Appender

#Append with a TuplesList
MyAppender=Appender.AppenderClass().append([
                                    ('NodeCollectionStr','Tree'),
                                    ('NodeKeyStr','MyTuplesList'),
                                    ('MyStr','Hello')
                                ]
                            )

#Append with a dict
MyAppender.append({
                    'NodeCollectionStr':'Tree',
                    'NodeKeyStr':'MyDict',
                    'MyOtherStr':'Bonjour'
                    }
                )

#Append with an instance
MyAppender.append(
                    Appender.AppenderClass().update(
                        [
                            ('NodeCollectionStr','Tree'),
                            ('NodeKeyStr','MyAppender')
                        ]
                    )
                )

#Definition the AttestedStr
SYS._attest(
    [
        'MyAppender is '+SYS._str(
        MyAppender,
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

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    ////////////////////////////////
                    Appender/__init__.py do_append
                    From Appender/__init__.py do_append | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                    ////////////////////////////////

                    l.138 :
                    *****
                    I am with [('NodeKeyStr', 'TopAppender')]
                    *****
                    self.AppendedNodeCollectionStr is Tree
                    self.AppendedNodeKeyStr is MyTuplesList

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    ////////////////////////////////
                    Appender/__init__.py do_append
                    From Appender/__init__.py do_append | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                    ////////////////////////////////

                    l.138 :
                    *****
                    I am with [('NodeKeyStr', 'TopAppender')]
                    *****
                    self.AppendedNodeCollectionStr is Tree
                    self.AppendedNodeKeyStr is MyDict

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                    ////////////////////////////////
                    Appender/__init__.py do_append
                    From Appender/__init__.py do_append | site-packages/six.py
exec_ | Celler/__init__.py do_cell | Notebooker/__init__.py do_notebook |
Informer/__init__.py do_inform | inform.py <module>
                    ////////////////////////////////

                    l.138 :
                    *****
                    I am with [('NodeKeyStr', 'TopAppender')]
                    *****
                    self.AppendedNodeCollectionStr is Tree
                    self.AppendedNodeKeyStr is MyAppender

                    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyAppender is < (AppenderClass), 4556357392>
   /{
   /  '<New><Instance>IdInt' : 4556357392
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopAppender
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
   /   /  'MyAppender' : < (AppenderClass), 4556355536>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556355536
   /   /   /  '<New><Instance>NodeCollectionStr' : Tree
   /   /   /  '<New><Instance>NodeIndexInt' : 2
   /   /   /  '<New><Instance>NodeKeyStr' : MyAppender
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (AppenderClass),
4556357392>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4556379080>
   /   /   /  '<Spe><Class>AppendedNodeCollectionStr' :
   /   /   /  '<Spe><Class>AppendedNodeKeyStr' :
   /   /   /  '<Spe><Class>AppendingCollectionVariable' : None
   /   /   /}
   /   /}
   /  '<Spe><Instance>AppendedNodeCollectionStr' : Tree
   /  '<Spe><Instance>AppendedNodeKeyStr' : MyAppender
   /  '<Spe><Instance>AppendingCollectionVariable' : {...}< (AppenderClass),
4556355536>
   /}

*****End of the Attest *****



```

