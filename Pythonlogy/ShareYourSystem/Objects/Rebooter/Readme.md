
#Rebooter


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Rebooter





<!--
FrozenIsBool False
-->

View the Rebooter sources on [Github](https://github.com/Ledoux/ShareYourSystem/
tree/master/ShareYourSystem/Objects/Installer)




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
from ShareYourSystem.Classors import Classer
from ShareYourSystem.Objects import Rebooter

#Definition
@Classer.ClasserClass(**
{
    'ClassingSwitchMethodStrsList':['make']
})
class MakerClass(Rebooter.RebooterClass):

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
        Rebooter.RebooterClass.__init__(self,**_KwarVariablesDict)

    #<DefineDoMethod>
    def do_make(self):

        #print
        print('I am in the do_make of the Maker')

        #cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition
@Classer.ClasserClass(**{
    'ClassingSwitchMethodStrsList':["make"]
})
class BuilderClass(MakerClass):

    #Definition
    RepresentingKeyStrsList=[
                            ]

    def default_init(self,
                    **_KwarVariablesDict
                ):
        MakerClass.__init__(self,**_KwarVariablesDict)

    def mimic_make(self):

        #print
        print('I am in the mimic_make of the Builder')

        #call the parent method
        MakerClass.make(self)

        #cast
        self.MadeMyInt+=10

    #<DefineDoMethod>
    def do_build(self):
        pass


#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    ]
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    '_WatchMakeWithMakerBool'
    ]
})

#make again
MyBuilder.make(5.)

#Print
print('After the second make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    '_WatchMakeWithMakerBool'
    ]
})


#make again
print('Now we reboot')
MyBuilder.reboot(['Make'])

#Print
print('After the reboot, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
    '_WatchMakeWithMakerBool'
    ]
})

#make again
MyBuilder.make(8.)

#Definition the AttestedStr
SYS._attest(
    [
        'MyBuilder is '+SYS._str(
        MyBuilder,
        **{
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':[
                'MakingMyFloat',
                'MadeMyInt',
                '_WatchMakeWithMakerBool',
                'RebootedWatchBoolKeyStrsList'
            ]
            }
        )
    ]
)

```


```console
>>>
Doer l.132 : DoerStr is Maker
DoStr is Make
DoMethodStr is make
DoingStr is Making
DoneStr is Made

Doer l.132 : DoerStr is Builder
DoStr is Build
DoMethodStr is build
DoingStr is Building
DoneStr is Built

Before make, MyBuilder is
< (BuilderClass), 4556059088>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 0.0
   /  '<New><Instance>IdString' : 4556059088
   /}
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}

I am in the mimic_make of the Builder
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_make', 'WatchDoBoolKeyStr':
'WatchMakeWithMakerBool', 'BindDoClassStr': 'MakerClass'}

I am in the do_make of the Maker
After the first make, MyBuilder is
< (BuilderClass), 4556059088>
   /{
   /  '<New><Instance>IdString' : 4556059088
   /  '<New><Instance>WatchMakeWithBuilderBool' : True
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True
   /}
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}

After the second make, MyBuilder is
< (BuilderClass), 4556059088>
   /{
   /  '<New><Instance>IdString' : 4556059088
   /  '<New><Instance>WatchMakeWithBuilderBool' : True
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True
   /}
Now we reboot
After the reboot, MyBuilder is
< (BuilderClass), 4556059088>
   /{
   /  '<New><Instance>IdString' : 4556059088
   /  '<New><Instance>WatchMakeWithBuilderBool' : False
   /  '<Spe><Instance>MadeMyInt' : 0
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : False
   /}
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superMimic_switch_watch_superDo_make',
'WatchDoBoolKeyStr': 'WatchMakeWithBuilderBool', 'BindDoClassStr':
'BuilderClass'}

I am in the mimic_make of the Builder
l 35
In the switch function
_KwargVariablesDict is
{'BindObserveWrapMethodStr': 'watch_superDo_make', 'WatchDoBoolKeyStr':
'WatchMakeWithMakerBool', 'BindDoClassStr': 'MakerClass'}

I am in the do_make of the Maker


*****Start of the Attest *****

MyBuilder is < (BuilderClass), 4556059088>
   /{
   /  '<New><Instance>IdString' : 4556059088
   /  '<New><Instance>WatchMakeWithBuilderBool' : True
   /  '<Spe><Instance>MadeMyInt' : 18
   /  '<Spe><Instance>MakingMyFloat' : 8.0
   /  '<Spe><Instance>RebootedWatchBoolKeyStrsList' :
['WatchMakeWithBuilderBool', '_WatchMakeWithMakerBool']
   /  '<Spe><Instance>_WatchMakeWithMakerBool' : True
   /}

*****End of the Attest *****



```

