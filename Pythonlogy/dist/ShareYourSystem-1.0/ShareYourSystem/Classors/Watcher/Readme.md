

<!--
FrozenIsBool False
-->

#Watcher

##Doc
----


>
> The Watcher
>
>

----

<small>
View the Watcher notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Watcher.ipynb)
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


The Watcher

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Binder"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
import copy
from ShareYourSystem.Classors import Doer,Observer,Representer
Binder=BaseModule
#</ImportSpecificModules>

#<DefineLocals>
WatchingPrefixKeyStr="Watch"
#</DefineLocals>

#<SetRepresent>
def getIsBoolWithItemTupleAndPrefixStr(_ItemTuple,_PrefixStr):

        #Debug
        '''
        print('Watcher l 35')
        print('_ItemTuple is ',_ItemTuple)
        print('_PrefixStr is ',_PrefixStr)
        print('')
        '''

        #Return
        return _ItemTuple[0].split('>')[-1].startswith(_PrefixStr)
OldRepresentFunction=copy.copy(Representer.represent)
def represent(_Variable,**_KwargVariablesDict):
        return OldRepresentFunction(
                _Variable,
                **dict(
                        _KwargVariablesDict,
                        **{
                                'RepresentingNotConcludeTuplesList':
                                [
(getIsBoolWithItemTupleAndPrefixStr,'_Watch'),
(getIsBoolWithItemTupleAndPrefixStr,'Watch')
                                ]
                        }
                )
        )
represent.__name__="Watcher@represent"
Representer.represent=represent
#</SetRepresent>

#<DefineFunctions>
def watch(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

        #Debug
        '''
        print('l 67')
        print('In the watch function ')
        print('_KwargVariablesDict is ')
        print(_KwargVariablesDict)
        print('')
        '''

        """
        #alias
        FuncDict=_InstanceVariable.__class__.watch.__dict__

        #Debug
        '''
        print('l 79')
        print('In the watch function ')
        print('FuncDict is ')
        print(FuncDict)
        print('')
        '''
        """

        #Set in the _InstanceVariable
        _InstanceVariable.__setattr__(
                        _KwargVariablesDict['WatchDoBoolKeyStr'],
                        True
                )

        #get the wrapped method
        WrapUnboundMethod=getattr(
                getattr(
                        SYS,
                        _KwargVariablesDict['BindDoClassStr']
                ),
                _KwargVariablesDict['BindObserveWrapMethodStr']
        )

        #del
        map(
                        lambda __KeyStr:
                        _KwargVariablesDict.__delitem__(__KeyStr),
['BindObserveWrapMethodStr','BindDoClassStr','WatchDoBoolKeyStr']
                )

        #Call
        return WrapUnboundMethod(
                _InstanceVariable,
                *_LiargVariablesList,
                **_KwargVariablesDict
        )

#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class WatcherClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                'WatchingIsBool',
                'WatchedDoBoolKeyStr',
                'WatchedDecorationMethodStr'
        ]

        def default_init(self,
                                                _WatchingIsBool=False,
                                                _WatchedDoBoolKeyStr="",
                                                _WatchedDecorationMethodStr="",
                                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent method
                Observer.ObserverClass.__bases__[0].__call__(self,_Class)

                #Watch
                self.watch()

                #Return
                return _Class

        def do_watch(self):

                #Check
                if self.WatchingIsBool:

                        #Debug
                        '''
                        print('l 133 Watcher')
                        print('self.ObservingWrapMethodStr is
'+self.ObservingWrapMethodStr)
                        print('')
                        '''

                        #Keep the old value
                        self.WatchedWrapMethodStr=self.ObservingWrapMethodStr

                        #observe first
                        self.observe(
                                                        True
                                                )

                        #Debug
                        '''
                        print('l 171 Watcher')
                        print('self.ObservedWrapMethodStr is
',self.ObservedWrapMethodStr)
                        '''

                        #Check
                        if self.ObservedWrapMethodStr.startswith(
                                watch.__name__+Binder.BindingDecorationSuffixStr
                        )==False:

                                #Debug
                                '''
                                print('l 173 this is a new watch method')
                                print('')
                                '''

                                #Define
                                WatchedDoMethodStr=self.WatchedWrapMethodStr
WatchedDoStr=WatchedDoMethodStr[0].upper()+WatchedDoMethodStr[1:]
self.WatchedDoBoolKeyStr=WatchingPrefixKeyStr+WatchedDoStr
self.WatchedDoBoolKeyStr+='With'+self.DoClass.NameStr
                                self.WatchedDoBoolKeyStr+='Bool'

                                WatchedIsInitBool=True
                                if hasattr(self.DoClass,'ResetDoBoolKeyStr'):
                                        if
self.WatchedDoBoolKeyStr!=self.DoClass.ResetDoBoolKeyStr:
                                                WatchedIsInitBool=False
                                if WatchedIsInitBool:
                                        #WARNING this cancels the reset property
binding before
                                        #Set already in the class
                                        setattr(
                                                        self.DoClass,
self.WatchedDoBoolKeyStr,
                                                        False
                                                )

                                #Debug
                                '''
                                print('l 145 Watcher')
                                print('WatchedDoMethodStr is
',WatchedDoMethodStr)
                                print('WatchedDoStr is ',WatchedDoStr)
                                print('self.WatchedDoBoolKeyStr is
',self.WatchedDoBoolKeyStr)
                                print('')
                                '''

                                #first bind
                                self.bind(
                                                        True,
                                                        watch,
                                                        "",
                                                        watch.__name__,
[('WatchDoBoolKeyStr',self.WatchedDoBoolKeyStr)],
**{'ObservingWrapMethodStr':self.ObservedWrapMethodStr}
                                                )

                                #set
self.WatchedDecorationMethodStr=self.BindedDecorationMethodStr

                                #Now make the amalgam
                                setattr(
                                                self.DoClass,
                                                WatchedDoMethodStr,
self.BindedDecorationUnboundMethod
                                        )

                        else:

                                #set
self.WatchedDecorationMethodStr=self.ObservedWrapMethodStr

#</DefineClass>

```

<small>
View the Watcher sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Classors/Watcher"
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
from ShareYourSystem.Classors import Watcher
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass with decorated make by a Watcher
@Watcher.WatcherClass(**{
    'WatchingIsBool':True,
    #'ObservingWrapMethodStr':'do_make'
    #'ObservingWrapMethodStr':'superDo_make'
    'ObservingWrapMethodStr':'make'
    })
class MakerClass(Initiator.InitiatorClass):

    #Definition
    RepresentingKeyStrsList=[
                                'MakingMyFloat',
                                'MadeMyInt'
                            ]

    def default_init(self,
                _MakingMyFloat=1.,
                _MadeMyInt=0
                ):
        Initiator.InitiatorClass.__init__(self)

    def do_make(self):

        #print
        print('self.MakingMyFloat is '+str(self.MakingMyFloat))
        print('self.MadeMyInt is '+str(self.MadeMyInt))
        print('')

        #Cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition a MakerClass with decorated make by a Watcher
@Watcher.WatcherClass(**{
    'WatchingIsBool':True,
    #'ObservingWrapMethodStr':'do_make'
    #'ObservingWrapMethodStr':'superDo_make'
    'ObservingWrapMethodStr':'make'
    })
class BuilderClass(MakerClass):

    #Definition
    RepresentingKeyStrsList=[
                            ]

    def default_init(self,
                ):
        MakerClass.__init__(self)

    def do_buid(self):
        pass

#Definition an instance
MyBuilder=MakerClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder)

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder)

#Definition the AttestedStr
SYS._attest(
    [
        'BuilderClass.make is '+str(BuilderClass.make),
        'MyBuilder is '+SYS._str(
            MyBuilder,**{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print


```


```console
>>>
Before make, MyBuilder is
< (MakerClass), 4539273424>
   /{
   /  '<New><Instance>IdInt' : 4539273424
   /  '<Spe><Class>MadeMyInt' : 0
   /  '<Spe><Class>MakingMyFloat' : 1.0
   /}
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyBuilder is
< (MakerClass), 4539273424>
   /{
   /  '<New><Instance>IdInt' : 4539273424
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}


*****Start of the Attest *****

BuilderClass.make is <unbound method BuilderClass.watch_superDo_make>

------

MyBuilder is < (MakerClass), 4539273424>
   /{
   /  '<New><Instance>IdInt' : 4539273424
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}

*****End of the Attest *****



```

