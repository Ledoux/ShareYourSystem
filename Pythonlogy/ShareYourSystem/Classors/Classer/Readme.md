

<!--
FrozenIsBool False
-->

#Classer

##Doc
----


>
> The Classer
>
>

----

<small>
View the Classer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Classer.ipynb)
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


The Classer

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Classors.Mimicker"
DecorationModuleStr="ShareYourSystem.Classors.Tester"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
Mimicker=BaseModule
#</ImportSpecificModules>

#<Define_Class>
@DecorationClass()
class ClasserClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
                                                'ClassingSwitchMethodStrsList'
                                        ]

        def default_init(self,
_ClassingSwitchMethodStrsList=None,
                                                **_KwargVariablesDict
                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def __call__(self,_Class):

                #Call the parent method
                Mimicker.MimickerClass.__bases__[0].__call__(self,_Class)

                #class
                self._class()

                #Return
                return _Class

        def do__class(self):

                #Definition the MethodsList
                ClassedFunctionsList=SYS._filter(
                        lambda __ListedVariable:
                                type(__ListedVariable).__name__=="function"
                                if hasattr(__ListedVariable,'__name__')
                                else False,
                                self.DoClass.__dict__.values()
                )

                #debug
                '''
                print('l 66 Classer')
                print("ClassedFunctionsList is ",WatchedFunctionsList)
                print('Set all the mimick methods')
                print('')
                '''

                #Get all the hooking methods
                ClassedMimickFunctionsList=SYS._filter(
                        lambda __ListedVariable:
                        __ListedVariable.__name__.startswith(
                                        Mimicker.MimickingWrapPrefixStr
                        )
                        if hasattr(__ListedVariable,'__name__')
                        else False,
                        ClassedFunctionsList
                )

                #debug
                '''
                print('l 82 Classer')
                print("ClassedMimickFunctionsList is
",ClassedMimickFunctionsList)
                print('')
                '''

                #map
                map(
                                lambda __ClassedMimickFunction:
                                self.mimic(
                                        Mimicker.MimickingWrapPrefixStr.join(
__ClassedMimickFunction.__name__.split(
Mimicker.MimickingWrapPrefixStr)[1:]
                                                )
                                ),
                                ClassedMimickFunctionsList
                        )

                #debug
                '''
                print('l 104 Classer')
                print('set the switch functions')
                print('self.ClassingSwitchMethodStrsList is
',self.ClassingSwitchMethodStrsList)
                print('self.DoClass.DoMethodStr is ',self.DoClass.DoMethodStr)
                print('')
                '''

                #map
                map(
                                lambda __ClassingSwitchUnboundMethodStr:
                                self.switch(
                                        True,
                                        __ClassingSwitchUnboundMethodStr
                                ),
                                self.ClassingSwitchMethodStrsList
                        )
#</DefineClass>


```

<small>
View the Classer sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Classors/Classer"
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
from ShareYourSystem.Classors import Doer,Classer
from ShareYourSystem.Objects import Initiator
import operator

#Definition
@Classer.ClasserClass(**{
    'ClassingSwitchMethodStrsList':[
        'make'
    ]
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
        Initiator.InitiatorClass.__init__(self,**_KwarVariablesDict)

    def do_make(self):

        #print
        print('I am in the do_make of the Maker')

        #cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition
@Classer.ClasserClass(**{
    'ClassingSwitchMethodStrsList':[
        'make'
    ]
}
)
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

    def do_build(self):
        pass

#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt'
    ]
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt'
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
    ]
})

#make again
print('Now we switch')
MyBuilder.setSwitch('Builder',['Make'])
MyBuilder.callAllMro('setSwitch',['Make'])

#Print
print('After the switch MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt'
    ]
})

#make again
MyBuilder.make(7.)

#Print
print('After the third make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt'
    ]
})

#Definition the AttestedStr
SYS._attest(
    [
        'BuilderClass.WatchMakeWithMakerBool is
'+str(BuilderClass.WatchMakeWithMakerBool),
        'BuilderClass.make is '+str(BuilderClass.make),
        'BuilderClass.build is '+str(BuilderClass.build),
        'MyBuilder is '+SYS._str(
        MyBuilder,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':[
                'MakingMyFloat',
                'MadeMyInt',
            ]
        }
        )
    ]
)

#Print





```


```console
>>>
Before make, MyBuilder is
< (BuilderClass), 4538551440>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 0.0
   /  '<New><Instance>IdInt' : 4538551440
   /}
I am in the mimic_make of the Builder
I am in the do_make of the Maker
After the first make, MyBuilder is
< (BuilderClass), 4538551440>
   /{
   /  '<New><Instance>IdInt' : 4538551440
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
After the second make, MyBuilder is
< (BuilderClass), 4538551440>
   /{
   /  '<New><Instance>IdInt' : 4538551440
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
Now we switch
After the switch MyBuilder is
< (BuilderClass), 4538551440>
   /{
   /  '<New><Instance>IdInt' : 4538551440
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
I am in the mimic_make of the Builder
I am in the do_make of the Maker
After the third make, MyBuilder is
< (BuilderClass), 4538551440>
   /{
   /  '<New><Instance>IdInt' : 4538551440
   /  '<Spe><Instance>MadeMyInt' : 17
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}


*****Start of the Attest *****

BuilderClass.WatchMakeWithMakerBool is False

------

BuilderClass.make is <unbound method
BuilderClass.switch_watch_superMimic_switch_watch_superDo_make>

------

BuilderClass.build is <unbound method BuilderClass.superDo_build>

------

MyBuilder is < (BuilderClass), 4538551440>
   /{
   /  '<New><Instance>IdInt' : 4538551440
   /  '<Spe><Instance>MadeMyInt' : 17
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}

*****End of the Attest *****



```

