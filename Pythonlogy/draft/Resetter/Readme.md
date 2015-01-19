

<!--
FrozenIsBool False
-->

#Resetter

##Doc
----


>
> The Resetter
>
>

----

<small>
View the Resetter notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyo
ursystem.ouvaton.org/Resetter.ipynb)
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


The Resetter

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
def getResetBool(_InstanceVariable,**_KwargVariablesDict):

        #get and return
        return
getattr(_InstanceVariable,'_'+_KwargVariablesDict['ResetDoBoolKeyStr'])

def setResetBool(_InstanceVariable,_ValueVariable,**_KwargVariablesDict):

        #Debug
        '''
        print('l 37 Resetter')
        print('We are in the setResetBool')
        print('_KwargVariablesDict is ')
        print(_KwargVariablesDict)
        print('')
        '''

        #Alias
        HideResetDoBoolKeyStr='_'+_KwargVariablesDict['ResetDoBoolKeyStr']

        #Check
        if hasattr(
                        _InstanceVariable,
                        HideResetDoBoolKeyStr
                        )==False:
                _InstanceVariable.__setattr__(HideResetDoBoolKeyStr,False)

        #get
        ResetDoBool=getattr(
                        _InstanceVariable,
                        _KwargVariablesDict['ResetDoBoolKeyStr']
                        )

        #Debug
        '''
        print('l 58 Resetter')
        print("_KwargVariablesDict['ResetDoBoolKeyStr'] is
",_KwargVariablesDict['ResetDoBoolKeyStr'])
        print('ResetDoBool is ',ResetDoBool)
        print('')
        '''

        #check
        if ResetDoBool==True and _ValueVariable==False:

                #Debug
                '''
                print('l 69 Resetter')
                print('Yes we reset')
                print('')
                '''

                #map
                map(
                                lambda __DefaultSetTuple:
                                _InstanceVariable.__setattr__(
                                                __DefaultSetTuple[0],
                                                __DefaultSetTuple[1]
                                ),
                                #self.DoClass.DefaultAttributeItemTuplesList
                                getattr(
                                        SYS,
                                        _KwargVariablesDict['BindDoClassStr']
                                ).DoneAttributeVariablesOrderedDict.items()
                        )

        #set
        _InstanceVariable.__setattr__(
                HideResetDoBoolKeyStr,
                _ValueVariable
                )

def delResetBool(_InstanceVariable,**_KwargVariablesDict):

        #delete
_InstanceVariable.__delattr__('_'+_KwargVariablesDict['ResetDoBoolKeyStr'])
#</DefineFunctions>

#<DefineClass>
@DecorationClass()
class ResetterClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
        ]

        def default_init(self,
                                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent method
                Observer.ObserverClass.__bases__[0].__call__(self,_Class)

                #reset
                self.reset()

                #Return
                return _Class

        def do_reset(self):

                #watch first
self.watch(True,**{'ObservingWrapMethodStr':self.DoClass.DoMethodStr})

                #set to the class
                """
                self.DoClass.ResetDoBoolKeyStr='Reset'+'Watch'.join(
                        self.WatchedDoBoolKeyStr.split('Watch')[1:])
                """
                self.DoClass.ResetDoBoolKeyStr=self.WatchedDoBoolKeyStr

                #Debug
                '''
                print('Resetter l 125')
                print('self.WatchedDoBoolKeyStr is ',self.WatchedDoBoolKeyStr)
                print('self.DoClass.ResetDoBoolKeyStr is
',self.DoClass.ResetDoBoolKeyStr)
                print('Now we bind')
                '''

                #map binds
                ResettedBindDecorationUnboundMethodsList=map(
                                lambda __Function:
                                self.bind(
                                                        True,
                                                        __Function,
                                                        "",
__Function.__name__+'With'+self.DoClass.NameStr,
[('ResetDoBoolKeyStr',self.DoClass.ResetDoBoolKeyStr)],
**{'ObservingWrapMethodStr':""}
                                        ).BindedDecorationUnboundMethod,
                                [getResetBool,setResetBool,delResetBool]
                        )

                #Set
                setattr(
                                        self.DoClass,
                                        self.DoClass.ResetDoBoolKeyStr,
                                        property(
*ResettedBindDecorationUnboundMethodsList
                                        )
                                )

                #Add to the KeyStrsList
                self.DoClass.KeyStrsList+=[
self.DoClass.ResetDoBoolKeyStr,
'ResetDoBoolKeyStr'
                                                                ]
#</DefineClass>


```

<small>
View the Resetter sources on <a href="https://github.com/Ledoux/ShareYourSystem/
tree/master/Pythonlogy/ShareYourSystem/Classors/Resetter"
target="_blank">Github</a>
</small>



```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Resetter,Attester
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass with decorated make by a Switcher
@Resetter.ResetterClass()
class MakerClass(Initiator.InitiatorClass):

    #Definition
    RepresentingKeyStrsList=[
                                'MakingMyFloat',
                                'MadeMyInt'
                            ]

    def default_init(self,
                _MakingMyFloat=0.,
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

#Definition a MakerClass with decorated make by a Switcher
@Resetter.ResetterClass()
class BuilderClass(MakerClass):

    #Definition
    RepresentingKeyStrsList=[
                                'BuildingMyStr',
                                'BuiltMyStr'
                            ]

    def default_init(self,
                _BuildingMyStr="",
                _BuiltMyStr=""
                ):
        MakerClass.__init__(self)

    def do_build(self):
        #set
        pass

#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make again
MyBuilder.make(5.)

#Print
print('After the second make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make again
print('Now we reset')
MyBuilder.WatchMakeWithMakerBool=False

#Print
print('After the reset MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#make again
MyBuilder.make(7.)

#Print
print('After the third make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':['MakingMyFloat','MadeMyInt']
})

#Definition the AttestedStr
SYS._attest(
    [
        'BuilderClass.WatchMakeWithMakerBool is
'+str(BuilderClass.WatchMakeWithMakerBool),
        'BuilderClass.setResetBoolWithMaker_ is
'+str(BuilderClass.setResetBoolWithMaker_),
        'BuilderClass.make is '+str(BuilderClass.make),
        'MyBuilder is '+SYS._str(
            MyBuilder,**{
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':[
                'MakingMyFloat','MadeMyInt'
            ]
            }
        ),
    ]
)

#Print



```


```console
>>>
Before make, MyBuilder is
< (BuilderClass), 4538483472>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 0.0
   /  '<New><Instance>IdInt' : 4538483472
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /}
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyBuilder is
< (BuilderClass), 4538483472>
   /{
   /  '<New><Instance>IdInt' : 4538483472
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
self.MakingMyFloat is 5.0
self.MadeMyInt is 3

After the second make, MyBuilder is
< (BuilderClass), 4538483472>
   /{
   /  '<New><Instance>IdInt' : 4538483472
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 5
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
Now we reset
After the reset MyBuilder is
< (BuilderClass), 4538483472>
   /{
   /  '<New><Instance>IdInt' : 4538483472
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 0
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
self.MakingMyFloat is 7.0
self.MadeMyInt is 0

After the third make, MyBuilder is
< (BuilderClass), 4538483472>
   /{
   /  '<New><Instance>IdInt' : 4538483472
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}


*****Start of the Attest *****

BuilderClass.WatchMakeWithMakerBool is <property object at 0x10e8362b8>

------

BuilderClass.setResetBoolWithMaker_ is <unbound method
BuilderClass.setResetBoolWithMaker_>

------

BuilderClass.make is <unbound method BuilderClass.watch_superDo_make>

------

MyBuilder is < (BuilderClass), 4538483472>
   /{
   /  '<New><Instance>IdInt' : 4538483472
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}

*****End of the Attest *****



```

