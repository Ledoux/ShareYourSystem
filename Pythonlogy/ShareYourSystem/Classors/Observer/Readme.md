

<!--
FrozenIsBool False
-->

#Observer

##Doc
----


>
> Observer...
>
>

----

<small>
View the Observer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Observer.ipynb)
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


Observer...

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Tester"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import copy
import inspect
#</ImportSpecificModules>

#<DefineFunctions>
def observe(_InstanceVariable,**_KwargVariablesDict):
        return _InstanceVariable
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class ObserverClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                                                'ObservingIsBool',
                                                'ObservingWrapMethodStr',
                                                'ObservedWrapUnboundMethod',
                                                'ObservedWrapMethodStr'
        ]

        def default_init(self,
                                        _ObservingIsBool=False,
                                        _ObservingWrapMethodStr="",
                                        _ObservedWrapUnboundMethod=None,
                                        _ObservedWrapMethodStr="",
                                        **_KwargVariablesDict
                                ):

                #Call the init parent method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent init method
                BaseClass.__call__(self,_Class)

                #observe
                self.observe()

                #Return
                return _Class

        def do_observe(self):

                #Check
                if self.ObservingIsBool:

                        #Debug
                        '''
                        print('Observer l.75')
                        print('self.ObservingWrapMethodStr is')
                        print(self.ObservingWrapMethodStr)
                        print('')
                        '''

                        #Get
                        self.ObservedWrapUnboundMethod=getattr(
                                self.DoClass,
                                self.ObservingWrapMethodStr
                        ) if self.ObservingWrapMethodStr!="" else observe

                        #Debug
                        '''
                        print('Observer l 86')
                        print('self.ObservedWrapUnboundMethod is
',self.ObservedWrapUnboundMethod)
                        print('')
                        '''

                        #Define Check for not pointing a circular function...
                        if
self.ObservingWrapMethodStr!=self.ObservedWrapUnboundMethod.__name__:
self.ObservedWrapMethodStr=self.ObservedWrapUnboundMethod.__name__
                        else:
self.ObservedWrapMethodStr=self.ObservingWrapMethodStr

                        #Debug
                        '''
                        print('Observer l.85')
                        print('self.ObservingWrapMethodStr is')
                        print(self.ObservingWrapMethodStr)
                        print('')
                        '''

                        #Return self
                        #return self

#</DefineClass>


```

<small>
View the Observer sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Classors/Observer"
target="_blank">Github</a>
</small>




<!---
FrozenIsBool True
-->

##Example

For this non directly very useful Module we just define a decorated FooClass
for which the Functer decoration by default call the decorated method...

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Observer
from ShareYourSystem.Objects import Initiator
import operator

#Definition a MakerClass decorated by the ObserverClass
@Observer.ObserverClass(**{
    'ObservingIsBool':True,
    'ObservingWrapMethodStr':'make'
})
class MakerClass(Initiator.InitiatorClass):

    #Definition
    RepresentingKeyStrsList=[
                                'MakingMyFloat',
                                'MadeMyInt'
                            ]

    def default_init(self,
                    _MakingMyFloat=0.,
                    _MadeMyInt=0,
                    **_KwarVariablesDict
                ):
        self.__class__.__bases__[0].__init__(self,**_KwarVariablesDict)

    def do_make(self):

        #cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.make is '+str(MakerClass.make),
        'MakerClass.DeriveClassor.ObservingWrapMethodStr is '+str(
            MakerClass.DeriveClassor.ObservingWrapMethodStr),
        'MakerClass.DeriveClassor.ObservedWrapMethodStr is '+str(
            MakerClass.DeriveClassor.ObservedWrapMethodStr),
    ]
)

#Print





```


```console
>>>


*****Start of the Attest *****

MakerClass.make is <unbound method MakerClass.superDo_make>

------

MakerClass.DeriveClassor.ObservingWrapMethodStr is make

------

MakerClass.DeriveClassor.ObservedWrapMethodStr is superDo_make

*****End of the Attest *****



```

