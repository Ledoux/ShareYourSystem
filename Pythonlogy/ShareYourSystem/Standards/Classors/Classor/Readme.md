

<!--
FrozenIsBool False
-->

#Classor

##Doc
----


>
> The Classor Module defines the ClassorClass
> class, which is the deepest parent class in the framework for decorating
another class. For each decorated class,
> it just sets up the NameStr in it and also a KeyStrsList for accumulating the
new KeyStrs from
> other attributes that can be provided by other decorating Classes.
>
>

----

<small>
View the Classor notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Classor.ipynb)
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
import json

#Definition a FooClass decorated by the ClassorClass
@SYS.ClassorClass()
class FooClass(object):
    pass

#print
print('FooClass.__dict__ is ')
print(
    json.dumps(
        dict(
            zip(
                FooClass.__dict__.keys(),
                map(
                    str,
                    FooClass.__dict__.values()
                )
            )
        ),
        indent=2
    )
)

```


```console
>>>
FooClass.__dict__ is
{
  "ConceptModuleStr": "",
  "__module__": "__builtin__",
  "getClass": "<function getClass at 0x10dc8b5f0>",
  "DeriveClassor": "<ShareYourSystem.Standards.Classors.Classor.ClassorClass
object at 0x10eda1850>",
  "SelfClass": "<class 'FooClass'>",
  "MroClassesDict": "{'FooClass': <class 'FooClass'>, 'object': <type
'object'>}",
  "MroClassesList": "(<class 'FooClass'>, <type 'object'>)",
  "Module": "<module '__builtin__' (built-in)>",
  "__doc__": "None",
  "InspectMethodDict": "MethodDict([('callAllMro', <unbound method
FooClass.callAllMro>), ('getClass', <unbound method FooClass.getClass>)])",
  "KeyStrsList": "['ConceptModuleStr', 'DeriveClassor', 'SelfClass',
'MroClassesDict', 'MroClassesList', 'Module', 'InspectMethodDict', 'NameStr',
'InspectInspectDict', 'KeyStrsList']",
  "__dict__": "<attribute '__dict__' of 'FooClass' objects>",
  "NameStr": "Foo",
  "InspectInspectDict": "{'getClass': InspectDict([('DefaultIndexInt', 1),
('InputKeyStrsList', ['_InstanceVariable', '_ClassVariable']),
('LiargVariablesListKeyStr', ''), ('KwargVariablesSetTagStr', ''),
('DefaultOrderedDict', OrderedDict([('_ClassVariable', None)])),
('FunctionNameStr', 'getClass')]), 'callAllMro':
InspectDict([('DefaultIndexInt', 2), ('InputKeyStrsList', ['_InstanceVariable',
'_MethodStr']), ('LiargVariablesListKeyStr', '_LiargVariablesList'),
('KwargVariablesSetTagStr', '_KwargVariablesDict'), ('DefaultOrderedDict',
OrderedDict()), ('FunctionNameStr', 'callAllMro')])}",
  "__weakref__": "<attribute '__weakref__' of 'FooClass' objects>",
  "callAllMro": "<function callAllMro at 0x10dc8b668>"
}

```



<!--
FrozenIsBool False
-->

Classor gives information to the base classes that derive classes exists


```python

#ImportModules
import ShareYourSystem as SYS

#Definition of a MakerClass decorated by a DoerClass instance
@SYS.ClassorClass()
class MakerClass(object):
    pass

#Definition of a derived BuilderClass decorated by a Deriver
@SYS.ClassorClass()
class BuilderClass(MakerClass):
    pass

#Print
#print('MakerClass.DerivedClassesList is '+str(MakerClass.DerivedClassesList))

#Definition the AttestedStr
print('MakerClass.DeriveClassesList is '+str(MakerClass.DeriveClassesList))



```


```console
>>>
MakerClass.DeriveClassesList is [<class 'BuilderClass'>]

```



<!---
FrozenIsBool True
-->

We can inspect a classor decorated class

```python
#ImportModules
import ShareYourSystem as SYS

#define
@SYS.ClassorClass()
class MakerClass(object):

    def default_init(self,
            _MakingMyStr,
            _MakingMyInt=0,
            **_KwargVariablesDict
        ):
        object.__init__(self,**_KwargVariablesDict)

    def do_make(self):

        #str
        self.MadeMyStr=str(self.MakingMyStr)

#print
print('MakerClass.InspectInspectDict is ')
print(SYS.indent(
        MakerClass.InspectInspectDict
    )
)




```


```console
>>>
MakerClass.InspectInspectDict is
{
  "default_init": "InspectDict([('DefaultIndexInt', 2), ('InputKeyStrsList',
['self', '_MakingMyStr', '_MakingMyInt']), ('LiargVariablesListKeyStr', ''),
('KwargVariablesSetTagStr', '_KwargVariablesDict'), ('DefaultOrderedDict',
OrderedDict([('_MakingMyInt', 0)])), ('FunctionNameStr', 'default_init')])",
  "getClass": "InspectDict([('DefaultIndexInt', 1), ('InputKeyStrsList',
['_InstanceVariable', '_ClassVariable']), ('LiargVariablesListKeyStr', ''),
('KwargVariablesSetTagStr', ''), ('DefaultOrderedDict',
OrderedDict([('_ClassVariable', None)])), ('FunctionNameStr', 'getClass')])",
  "callAllMro": "InspectDict([('DefaultIndexInt', 2), ('InputKeyStrsList',
['_InstanceVariable', '_MethodStr']), ('LiargVariablesListKeyStr',
'_LiargVariablesList'), ('KwargVariablesSetTagStr', '_KwargVariablesDict'),
('DefaultOrderedDict', OrderedDict()), ('FunctionNameStr', 'callAllMro')])",
  "do_make": "InspectDict([('DefaultIndexInt', 1), ('InputKeyStrsList',
['self']), ('LiargVariablesListKeyStr', ''), ('KwargVariablesSetTagStr', ''),
('DefaultOrderedDict', OrderedDict()), ('FunctionNameStr', 'do_make')])"
}

```



<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

<small>
View the Classor sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Standards/Classors/Classor"
target="_blank">Github</a>
</small>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Classor Module defines the ClassorClass
class, which is the deepest parent class in the framework for decorating another
class. For each decorated class,
it just sets up the NameStr in it and also a KeyStrsList for accumulating the
new KeyStrs from
other attributes that can be provided by other decorating Classes.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
#</DefineAugmentation>

#<ImportSpecificModules>
import sys
#</ImportSpecificModules>

#<DefineLocals>
ClassDecorationStr="Cls@"
LocalModuleFolderPathStrAndModuleStrTuplesList=[]
#</DefineLocals>

#<DefineLocals>
def getClass(_InstanceVariable,_ClassVariable=None):

        #Debug
        '''
        print('Classor l 35')
        print('_ClassVariable is ')
        print(_ClassVariable)
        print('')
        '''

        #Check
        if type(_ClassVariable) in SYS.StrTypesList:
                if _ClassVariable=="":
                        return _InstanceVariable.__class__
                else:
                        return
getattr(SYS,SYS.getClassStrWithNameStr(_ClassVariable))
        elif _ClassVariable==None:
                return _InstanceVariable.__class__
        else:
                return _ClassVariable

def callAllMro(_InstanceVariable,_MethodStr,*_LiargVariablesList,**_KwargVariabl
esDict):

        #map
        map(
                        lambda __MroClass:
                        getattr(
                                _InstanceVariable,
                                _MethodStr
                        )(__MroClass,*_LiargVariablesList,**_KwargVariablesDict)
                        if hasattr(__MroClass,_MethodStr)
                        else None,
                        _InstanceVariable.__class__.__mro__
                )

        #Debug
        '''
        print('Classor l 50 ')
        print('_InstanceVariable is ',_InstanceVariable)
        print('')
        '''

        #return
        return _InstanceVariable
#</DefineLocals>

#<DefineClass>
class ClassorClass(object):

        #set the Local NameStr
        NameStr="Classor"

        def default_init(self,**_KwargVariablesDict):

                #set the NameStr
                self.NameStr=SYS.getNameStrWithClassStr(self.__class__.__name__)

                #Map the update
                map(
                                lambda __ItemTuple:
                                self.__setattr__(__ItemTuple[0],__ItemTuple[1])
                                #If we want to not set the items setted during
hooks and that are not specified...
                                if hasattr(self,__ItemTuple[0]) else None
                                ,_KwargVariablesDict.iteritems()
                        )

                #call the base method
                object.__init__(self)

        def __call__(self,_Class):


                #/###################/#
                # Set the NameStr, Module, SelfClass...
                #

                #get
                self.Module=sys.modules[_Class.__module__]

                #debug
                '''
                print('Classor l.53 __call__ method')
                print('_Class is ',_Class)
                print('')
                '''

                #set in the class the classed Strs
                _Class.NameStr=SYS.getNameStrWithClassStr(_Class.__name__)

                #Give a Pointer to the Hooker
                setattr(_Class,'DeriveClassor',self)

                #set to the SYS the module
                if len(SYS.NameStrsList)==0:
setattr(SYS,self.NameStr,sys.modules[self.__class__.__module__])
                        setattr(SYS,self.__class__.__name__,self.__class__)
                        SYS.NameStrsList.append(self.NameStr)
                setattr(SYS,_Class.NameStr,self.Module)
                setattr(SYS,_Class.__name__,_Class)
                SYS.NameStrsList.append(_Class.NameStr)

                #get the module and set it to the class
                _Class.Module=self.Module
                _Class.Module.LocalFolderPathStr=SYS.PythonlogyLocalFolderPathSt
r+self.Module.__name__.replace(
                        '.','/')+'/'

                #set a pointer to itself
                _Class.SelfClass=_Class
                _Class.MroClassesList=_Class.__mro__
                _Class.MroClassesDict=dict(
                        map(
                                lambda __Class:
                                (__Class.__name__,__Class),
                                _Class.__mro__
                        )
                )

                #Check
                if hasattr(_Class,'callAllMro')==False:
                        setattr(
                                        _Class,
                                        callAllMro.__name__,
                                        callAllMro
                                )
                        setattr(
                                        _Class,
                                        getClass.__name__,
                                        getClass
                                )

                #add in LocalModuleFolderPathStrAndModuleStrTuplesList
                global LocalModuleFolderPathStrAndModuleStrTuplesList
                LocalModuleFolderPathStrAndModuleStrTuplesList.append(
                        (
                                _Class.Module.LocalFolderPathStr,
                                _Class.Module.__name__
                        )
                )

                #/###################/#
                # Give ref to the concept module
                #

                #append
ConceptModuleStr='.'.join(_Class.Module.__name__.split('.')[:-1])
                if hasattr(_Class,"ConceptModuleStr")==False or
_Class.ConceptModuleStr!=ConceptModuleStr:

                        #set
                        _Class.ConceptModuleStr=ConceptModuleStr

                        #append
                        LocalModuleFolderPathStrAndModuleStrTuplesList.append(
                                        (
SYS.PythonlogyLocalFolderPathStr+ConceptModuleStr.replace('.','/')+'/',
                                                ConceptModuleStr
                                        )
                                )

                #/###################/#
                # Alert the base method that a derive object exists
                #

                #set
                if len(_Class.__bases__)>0:

                        #set the DerivedBaseClas
                        FirstBaseClass=_Class.__bases__[0]

                        #Debug
                        '''
                        print('l. 183 Classor')
                        print('We can set derived bases for the base')
                        print('FirstBaseClass is ',FirstBaseClass)
                        print('')
                        '''

                        #Append to the parent class
                        if hasattr(FirstBaseClass,'DeriveClassesList'):
                                FirstBaseClass.DeriveClassesList.append(_Class)
                        elif FirstBaseClass!=object:
                                FirstBaseClass.DeriveClassesList=[_Class]

                #/###################/#
                # Inspect the methods
                #

                #Get the Methods
                _Class.InspectMethodDict=SYS.MethodDict(_Class)

                #dict
                _Class.InspectInspectDict=dict(
                        map(
                                        lambda __MethodItemTuple:
                                        (
                                                __MethodItemTuple[0],
                                                SYS.InspectDict(
                                                        __MethodItemTuple[1]
                                                )
                                        ),
                                        _Class.InspectMethodDict.items()
                                )
                        )

                #/###################/#
                # set the KeyStrsList
                #

                #set the KeyStrsList
_Class.KeyStrsList=SYS.getKeyStrsListWithClass(_Class)+['KeyStrsList']

                #/###################/#
                # alias
                #

                self.WrapClass=_Class

                #Return
                return _Class

        def setMethod(self,_KeyStr,_ValueMethod):

                #/################/#
                # Set in the class but also in the inspect dict
                #

                #set
                setattr(
                                self.WrapClass,
                                _KeyStr,
                                _ValueMethod
                        )

                #set
                self.WrapClass.InspectMethodDict[_KeyStr]=_ValueMethod

                #dict
                self.WrapClass.InspectInspectDict[_KeyStr]=SYS.InspectDict(
                                                        _ValueMethod
                                                )

#</DefineClass>

#give to SYS
SYS.LocalModuleFolderPathStrAndModuleStrTuplesList=LocalModuleFolderPathStrAndMo
duleStrTuplesList
SYS.ClassorClass=ClassorClass
SYS.Classor=sys.modules[ClassorClass.__module__]

```


