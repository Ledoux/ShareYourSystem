

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
from ShareYourSystem.Classors import Inspecter,Attester
from ShareYourSystem.Objects import Initiator

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

