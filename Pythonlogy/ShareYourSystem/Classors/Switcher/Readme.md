

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
< (MakerClass), 4348604688>
   /{
   /  '<New><Instance>IdInt' : 4348604688
   /  '<Spe><Class>MadeMyInt' : 0
   /  '<Spe><Class>MakingMyFloat' : 1.0
   /}
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyMaker is
< (MakerClass), 4348604688>
   /{
   /  '<New><Instance>IdInt' : 4348604688
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
After the second make, MyMaker is
< (MakerClass), 4348604688>
   /{
   /  '<New><Instance>IdInt' : 4348604688
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
Now we switch
After the switch MyMaker is
< (MakerClass), 4348604688>
   /{
   /  '<New><Instance>IdInt' : 4348604688
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}
self.MakingMyFloat is 7.0
self.MadeMyInt is 3

After the third make, MyMaker is
< (MakerClass), 4348604688>
   /{
   /  '<New><Instance>IdInt' : 4348604688
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}


*****Start of the Attest *****

MakerClass.make is <unbound method MakerClass.switch_watch_superDo_make>

------

MyMaker is < (MakerClass), 4348604688>
   /{
   /  '<New><Instance>IdInt' : 4348604688
   /  '<Spe><Instance>MadeMyInt' : 7
   /  '<Spe><Instance>MakingMyFloat' : 7.0
   /}

*****End of the Attest *****



```

