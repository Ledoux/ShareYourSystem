
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
< (BuilderClass), 4348537808>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Base><Class>MakingMyFloat' : 0.0
   /  '<New><Instance>IdInt' : 4348537808
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /}
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyBuilder is
< (BuilderClass), 4348537808>
   /{
   /  '<New><Instance>IdInt' : 4348537808
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
self.MakingMyFloat is 5.0
self.MadeMyInt is 3

After the second make, MyBuilder is
< (BuilderClass), 4348537808>
   /{
   /  '<New><Instance>IdInt' : 4348537808
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 5
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
Now we reset
After the reset MyBuilder is
< (BuilderClass), 4348537808>
   /{
   /  '<New><Instance>IdInt' : 4348537808
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 0
   /  '<Spe><Instance>MakingMyFloat' : 5.0
   /}
self.MakingMyFloat is 7.0
self.MadeMyInt is 0

After the third make, MyBuilder is
< (BuilderClass), 4348537808>
   /{
   /  '<New><Instance>IdInt' : 4348537808
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}


*****Start of the Attest *****

BuilderClass.WatchMakeWithMakerBool is <property object at 0x10330ccb0>

------

BuilderClass.setResetBoolWithMaker_ is <unbound method
BuilderClass.setResetBoolWithMaker_>

------

BuilderClass.make is <unbound method BuilderClass.watch_superDo_make>

------

MyBuilder is < (BuilderClass), 4348537808>
   /{
   /  '<New><Instance>IdInt' : 4348537808
   /  '<Spe><Class>BuildingMyStr' :
   /  '<Spe><Class>BuiltMyStr' :
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}

*****End of the Attest *****



```

