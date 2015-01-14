

<!--
FrozenIsBool False
-->

#Binder

##Doc
----


>
> Binder...
>
>

----

<small>
View the Binder notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Binder.ipynb)
</small>




<!---
FrozenIsBool True
-->

##Example

Here this is to check that the class checks that
this is useless to watch a watch method, therefore it
just lets it as the first version.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Binder
from ShareYourSystem.Objects import Initiator
import operator

#Define a Unbound method like function
def foo(_InstanceVariable,*_LiargVariablesList,**_KwargVariablesDict):

    #print
    print('In the foo function ')
    print('_KwargVariablesDict is ')
    print(_KwargVariablesDict)
    print('')

    #get the wrapped method
    WrapUnboundMethod=getattr(
        getattr(
            SYS,
            _KwargVariablesDict['BindDoClassStr']
        ),
        _KwargVariablesDict['BindObserveWrapMethodStr']
    )

    #call
    WrapUnboundMethod(_InstanceVariable,10.*_InstanceVariable.MakingMyFloat)


#Definition a MakerClass decorated by the BinderClass
@Binder.BinderClass(**{
    'ObservingWrapMethodStr':'make',
    'BindingIsBool':True,
    'BindingDecorationUnboundMethod':foo,
    'BindingItemTuplesList':[('MyFooInt',1)]
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
        pass

    def do_make(self):

        #Print
        print('I make')

        #cast
        self.MadeMyInt=int(self.MakingMyFloat)

#Definition and do a first make
MyMaker=MakerClass().make(3.)

#Use the other binded method that is completely fooooo
MyMaker.foo_make()

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.foo is '+str(MakerClass.foo),
        'MakerClass.foo_make is '+str(MakerClass.foo_make),
        'MyMaker is '+SYS._str(
        MyMaker,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        )
    ]
)

#Print










```


```console
>>>
I make
In the foo function
_KwargVariablesDict is
{'MyFooInt': '1', 'BindDoClassStr': 'MakerClass', 'BindObserveWrapMethodStr':
'make'}

I make


*****Start of the Attest *****

MakerClass.foo is <unbound method MakerClass.foo>

------

MakerClass.foo_make is <unbound method MakerClass.foo_make>

------

MyMaker is < (MakerClass), 4348360528>
   /{
   /  '<New><Instance>IdInt' : 4348360528
   /  '<Spe><Instance>MadeMyInt' : 30
   /  '<Spe><Instance>MakingMyFloat' : 30.0
   /}

*****End of the Attest *****



```

