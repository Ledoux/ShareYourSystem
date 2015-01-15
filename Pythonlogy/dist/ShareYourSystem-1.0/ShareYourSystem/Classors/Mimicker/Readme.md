

<!---
FrozenIsBool True
-->

##Example

It is possible to cumulate mimick and switch properties...
Note that only the do_make is a switched method as the
mimic_make continue to work after the first call of make.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Switcher,Mimicker
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass with decorated make by a Switcher
@Switcher.SwitcherClass(**{
    'SwitchingIsBool':True,
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

#Definition
@Mimicker.MimickerClass(**{
    'MimickingDoMethodStr':"make"
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

    def do_build(self):
        pass


#Definition an instance
MyBuilder=BuilderClass()

#Print
print('Before make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt']
})

#make once
MyBuilder.make(3.)

#Print
print('After the first make, MyBuilder is ')
SYS._print(MyBuilder,**{
    'RepresentingKeyStrsList':[
    'MakingMyFloat',
    'MadeMyInt',
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
MyBuilder.setSwitch('Maker',['Make'])

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
    'MadeMyInt',
    'WatchMakeWithMakerBool']
})

#Definition the AttestedStr
SYS._attest(
    [
        'BuilderClass.WatchMakeWithMakerBool is
'+str(BuilderClass.WatchMakeWithMakerBool),
        'BuilderClass.make is '+str(BuilderClass.make),
        'MyBuilder is '+SYS._str(
            MyBuilder,**{
            'RepresentingAlineaIsBool':False,
            'RepresentingKeyStrsList':[
            'MakingMyFloat',
            'MadeMyInt'
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
< (BuilderClass), 4348662928>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 1.0
   /  '<New><Instance>IdInt' : 4348662928
   /}
I am in the mimic_make of the Builder
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyBuilder is
< (BuilderClass), 4348662928>
   /{
   /  '<New><Instance>IdInt' : 4348662928
   /  '<Spe><Instance>MadeMyInt' : 13
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
I am in the mimic_make of the Builder
After the second make, MyBuilder is
< (BuilderClass), 4348662928>
   /{
   /  '<New><Instance>IdInt' : 4348662928
   /  '<Spe><Instance>MadeMyInt' : 23
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
Now we switch
After the switch MyBuilder is
< (BuilderClass), 4348662928>
   /{
   /  '<New><Instance>IdInt' : 4348662928
   /  '<Spe><Instance>MadeMyInt' : 23
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
I am in the mimic_make of the Builder
self.MakingMyFloat is 7.0
self.MadeMyInt is 23

After the third make, MyBuilder is
< (BuilderClass), 4348662928>
   /{
   /  '<New><Instance>IdInt' : 4348662928
   /  '<Spe><Instance>MadeMyInt' : 17
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /  '<Spe><Instance>WatchMakeWithMakerBool' : True
   /}


*****Start of the Attest *****

BuilderClass.WatchMakeWithMakerBool is False

------

BuilderClass.make is <unbound method
BuilderClass.superMimic_switch_watch_superDo_make>

------

MyBuilder is < (BuilderClass), 4348662928>
   /{
   /  '<New><Instance>IdInt' : 4348662928
   /  '<Spe><Instance>MadeMyInt' : 17
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}

*****End of the Attest *****



```

