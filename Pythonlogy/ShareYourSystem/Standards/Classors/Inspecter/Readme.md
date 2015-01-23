

<!--
FrozenIsBool False
-->

#Inspecter

##Doc
----


>
> An Inspecter decorates a class by giving it an InspectedArgumentDict that is
> an inspection of all defined methods.
>

----

<small>
View the Inspecter notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Inspecter.ipynb)
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


An Inspecter decorates a class by giving it an InspectedArgumentDict that is
an inspection of all defined methods.
"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Classors.Propertiser"
DecorationModuleStr=BaseModuleStr
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import inspect
#</ImportSpecificModules>

#<DefineFunction>
def getInspectedUnboundMethodsListWithClass(_Class):
        return SYS._filter(
                        lambda __AttributeVariable:
                        type(__AttributeVariable).__name__=="function",
                        _Class.__dict__.values()
                        )
#<DefineFunction>

#<DefineClass>
@DecorationClass()
class InspecterClass(BaseClass):

        def default_init(self,**_KwargVariablesDict):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent init method
                BaseClass.__call__(self,_Class)

                #Inspect
                self.inspect()

                #Return _Class
                return _Class

        def do_inspect(self):

                #Alias
                InspectedClass=self.DoClass

                #Debug
                '''
                print('InspectedClass is ',InspectedClass)
                print('')
                '''

                #Get the Args
                InspectedClass.InspectedArgumentDict=dict(
                                                                map(
                                                                        lambda
__Function:
                                                                        (
__Function.__name__,
SYS.getArgumentDictWithFunction(__Function)
                                                                        ),
getInspectedUnboundMethodsListWithClass(InspectedClass)
                                                                )
                                                        )

                #Add to the KeyStrsList
                InspectedClass.KeyStrsList+=[
'InspectedArgumentDict',
                                                                ]

#</Define_Class>


```

<small>
View the Inspecter sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Classors/Inspecter"
target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive special attributes
from the decorating ClassorClass specially the NameStr, that should be the
ClassStr without the TypeStr in the end.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Standards.Classors import Inspecter,Attester
from ShareYourSystem.Standards.Objects import Initiator

#Definition a FooClass decorated by the ClassorClass
@Inspecter.InspecterClass()
class MakerClass(Initiator.InitiatorClass):
    def make(self,
            _MakingStr,
            _MakingInt=0,
            **_KwargVariablesDict
        ):
        self.__class__.__bases__[0].__init__(self,**_KwargVariablesDict)

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.InspectedArgumentDict is
'+SYS._str(MakerClass.InspectedArgumentDict)
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MakerClass.InspectedArgumentDict is
   /{
   /  'callAllMro' :
   /   /{
   /   /  'DefaultIndexInt' : 2
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable', '_MethodStr']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' : _LiargVariablesList
   /   /}
   /  'callDo' :
   /   /{
   /   /  'DefaultIndexInt' : 1
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable']
   /   /  'KwargVariablesDictKeyStr' :
   /   /  'LiargVariablesListKeyStr' :
   /   /}
   /  'getClass' :
   /   /{
   /   /  'DefaultIndexInt' : 1
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /  '_ClassVariable' : None
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable', '_ClassVariable']
   /   /  'KwargVariablesDictKeyStr' :
   /   /  'LiargVariablesListKeyStr' :
   /   /}
   /  'setDefault' :
   /   /{
   /   /  'DefaultIndexInt' : 2
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /  '_AttributeKeyStrsList' : None
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable', '_ClassVariable',
'_AttributeKeyStrsList']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' :
   /   /}
   /  'setDefaultMutable' :
   /   /{
   /   /  'DefaultIndexInt' : 2
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /  '_AttributeKeyStrsList' : None
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable', '_ClassVariable',
'_AttributeKeyStrsList']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' :
   /   /}
   /  'setDo' :
   /   /{
   /   /  'DefaultIndexInt' : 1
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /  '_DoClassVariable' : None
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable', '_DoClassVariable']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' :
   /   /}
   /  'setDoing' :
   /   /{
   /   /  'DefaultIndexInt' : 1
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /  '_DoClassVariable' : None
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable', '_DoClassVariable']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' :
   /   /}
   /  'setDone' :
   /   /{
   /   /  'DefaultIndexInt' : 1
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /  '_DoClassVariable' : None
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable', '_DoClassVariable']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' :
   /   /}
   /  'superDefault_init' :
   /   /{
   /   /  'DefaultIndexInt' : 1
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' : _LiargVariablesList
   /   /}
   /  'superDo_make' :
   /   /{
   /   /  'DefaultIndexInt' : 1
   /   /  'DefaultOrderedDict' :
   /   /   /{
   /   /   /}
   /   /  'InputKeyStrsList' : ['_InstanceVariable']
   /   /  'KwargVariablesDictKeyStr' : _KwargVariablesDict
   /   /  'LiargVariablesListKeyStr' : _LiargVariablesList
   /   /}
   /}

*****End of the Attest *****



```

