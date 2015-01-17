

<!--
FrozenIsBool False
-->

#Switcher

##Doc
----


>
> The Switcher
>
>

----

<small>
View the Switcher notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Switcher.ipynb)
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


The Switcher

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Watcher"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import operator
from ShareYourSystem.Classors import Doer,Observer
#</ImportSpecificModules>

#<DefineFunctions>
def setSwitch(_InstanceVariable,_ClassVariable=None,_DoStrsList=None):

        #Debug
        '''
        print('l 31 setSwitch')
        print('_DoStrsList is ',_DoStrsList)
        print('_InstanceVariable.__class__.NameStr is
',_InstanceVariable.__class__.NameStr)
        print('')
        '''

        #get
        SwitchClass=_InstanceVariable.getClass(_ClassVariable)

        #check
        if _DoStrsList==None:
                _DoStrsList=[SwitchClass.DoStr]

        #map
        map(
                        lambda __MethodStr:
                        _InstanceVariable.__setattr__(
'Watch'+__MethodStr+'With'+SwitchClass.NameStr+'Bool',
                                False
                        ),
                        _DoStrsList,
                )

        #return
        return _InstanceVariable

def switch(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

        #Debug
        '''
        print('l 51')
        print('In the switch function ')
        print('_KwargVariablesDict is ')
        print(_KwargVariablesDict)
        print('')
        '''

        """
        #alias
        FuncDict=switch.__dict__

        #Debug
        '''
        print('l 52')
        print('In the switch function ')
        print('FuncDict is ')
        print(FuncDict)
        print('')
        '''
        """

        #Check
        if hasattr(_InstanceVariable,_KwargVariablesDict['WatchDoBoolKeyStr']):

                #get
                WatchDoBool=getattr(
                                _InstanceVariable,
                                _KwargVariablesDict['WatchDoBoolKeyStr']
                                )

                #Switch
                if WatchDoBool:
                        return _InstanceVariable

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
class SwitcherClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                'SwitchingIsBool',
                'SwitchingWrapMethodStr'
        ]

        def default_init(self,
                                                _SwitchingIsBool=False,
                                                _SwitchingWrapMethodStr="",
                                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent method
                Observer.ObserverClass.__bases__[0].__call__(self,_Class)

                #reset
                self.switch()

                #Return
                return _Class

        def do_switch(self):

                #Check
                if self.SwitchingIsBool:

                        #Debug
                        '''
                        print('l 195 Switcher')
                        print('self.SwitchingWrapMethodStr is
'+self.SwitchingWrapMethodStr)
                        print('')
                        '''

                        #watch first
                        self.watch(
                                                True,
**{'ObservingWrapMethodStr':self.SwitchingWrapMethodStr}
                                        )

                        #Debug
                        '''
                        print('l 204 Switcher')
                        print('self.WatchedDecorationMethodStr is
',self.WatchedDecorationMethodStr)
                        print('')
                        '''

                        #first bind
                        self.bind(
                                                True,
                                                switch,
                                                "",
                                                switch.__name__,
[('WatchDoBoolKeyStr',self.WatchedDoBoolKeyStr)],
**{'ObservingWrapMethodStr':self.WatchedDecorationMethodStr}
                                        )

                        #Now make the amalgam
                        setattr(
                                        self.DoClass,
                                        self.SwitchingWrapMethodStr,
                                        getattr(
                                                self.DoClass,
                                                self.BindedDecorationMethodStr
                                        )
                                )

                        #Check
                        if hasattr(self.DoClass,'setSwitch')==False:
                                setattr(
                                                self.DoClass,
                                                setSwitch.__name__,
                                                setSwitch
                                        )
#</DefineClass>


```

<small>
View the Switcher sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Classors/Switcher"
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
from ShareYourSystem.Classors import Switcher,Attester
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass with decorated make by a Switcher
@Switcher.SwitcherClass(**{
    'SwitchingIsBool':True,
    #'ObservingWrapMethodStr':'do_make'
    #'ObservingWrapMethodStr':'superDo_make'
    'SwitchingWrapMethodStr':'make'
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

#Definition an instance
MyMaker=MakerClass()

#Print
print('Before make, MyMaker is ')
SYS._print(MyMaker)

#make once
MyMaker.make(3.)

#Print
print('After the first make, MyMaker is ')
SYS._print(MyMaker)

#make again
MyMaker.make(5.)

#Print
print('After the second make, MyMaker is ')
SYS._print(MyMaker)

#make again
print('Now we switch')
MyMaker.setSwitch()

#Print
print('After the switch MyMaker is ')
SYS._print(MyMaker)

#make again
MyMaker.make(7.)

#Print
print('After the third make, MyMaker is ')
SYS._print(MyMaker)

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.make is '+str(MakerClass.make),
        'MyMaker is '+SYS._str(
            MyMaker,**{'RepresentingAlineaIsBool':False}
        ),
    ]
)

#Print



```


```console
>>>
Before make, MyMaker is
< (MakerClass), 4538485392>
   /{
   /  '<New><Instance>IdInt' : 4538485392
   /  '<Spe><Class>MadeMyInt' : 0
   /  '<Spe><Class>MakingMyFloat' : 1.0
   /}
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyMaker is
< (MakerClass), 4538485392>
   /{
   /  '<New><Instance>IdInt' : 4538485392
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
After the second make, MyMaker is
< (MakerClass), 4538485392>
   /{
   /  '<New><Instance>IdInt' : 4538485392
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
Now we switch
After the switch MyMaker is
< (MakerClass), 4538485392>
   /{
   /  '<New><Instance>IdInt' : 4538485392
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
self.MakingMyFloat is 7.0
self.MadeMyInt is 3

After the third make, MyMaker is
< (MakerClass), 4538485392>
   /{
   /  '<New><Instance>IdInt' : 4538485392
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}


*****Start of the Attest *****

MakerClass.make is <unbound method MakerClass.switch_watch_superDo_make>

------

MyMaker is < (MakerClass), 4538485392>
   /{
   /  '<New><Instance>IdInt' : 4538485392
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}

*****End of the Attest *****



```

