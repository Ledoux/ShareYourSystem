

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
< (MakerClass), 4348129040>
   /{
   /  '<New><Instance>IdInt' : 4348129040
   /  '<Spe><Class>MadeMyInt' : 0
   /  '<Spe><Class>MakingMyFloat' : 1.0
   /}
self.MakingMyFloat is 3.0
self.MadeMyInt is 0

After the first make, MyBuilder is
< (MakerClass), 4348129040>
   /{
   /  '<New><Instance>IdInt' : 4348129040
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}


*****Start of the Attest *****

BuilderClass.make is <unbound method BuilderClass.watch_superDo_make>

------

MyBuilder is < (MakerClass), 4348129040>
   /{
   /  '<New><Instance>IdInt' : 4348129040
   /  '<Spe><Instance>MadeMyInt' : 3
   /  '<Spe><Instance>MakingMyFloat' : 3.0
   /}

*****End of the Attest *****



```

