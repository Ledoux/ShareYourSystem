

<!--
FrozenIsBool False
-->

#Doer

##Doc
----


>
> The Doer defines instances that are going to decorate a big family of classes
in this framework.
> Staying on the idea, that one module should associate
> one class, now a decorated class by a Doer should have a NameStr that is
> a DoStr and express also method a method with the name
<DoStr>[0].lower()+<DoStr>[1:]
> All the attributes that are controlling this method process are
<DoingStr><MiddleStr><TypeStr>
> and all the ones resetted during the method are <DoneStr><MiddleStr><TypeStr>.
> This helps a lot for defining a fisrt level of objects that are acting like
input-output controllers.
>
>

----

<small>
View the Doer notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyoursy
stem.ouvaton.org/Doer.ipynb)
</small>




<!---
FrozenIsBool True
-->

##Example

It is possible to re set the Doing or Done attributes

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Doer,Attester
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass decorated by the DefaultorClass
@Doer.DoerClass()
class MakerClass(Initiator.InitiatorClass):

    def default_init(self,
                _MakingMyFloat=1.,
                _MakingMyList=None,
                _MakingFirstInt={'DefaultingSetType':int},
                _MakingSecondInt=0,
                _MadeMyInt=0,
                _MadeMyList=None,
                ):
        pass

    def do_make(self):

        #print
        print('Maker : I am going to make')
        print('self.MakingMyFloat is ',self.MakingMyFloat)
        print('')

        #set
        self.MadeMyInt=int(self.MakingMyFloat)

        #Return self
        #return self

#Definition of an instance and make
MyMaker=MakerClass(
    _MakingMyList=['hello'],
    **{'MakingFirstInt':3}
    ).superDo_make(
        3.,['bonjour'],
        _SecondInt=5
    )

print('MyMaker is ')
SYS._print(MyMaker)

print('we reset doing')
MyMaker.setDoing(MakerClass)

print('MyMaker after set doing is ')
SYS._print(MyMaker)

#Add
AttestingStrsList=[
        'MyMaker.__dict__ is '+SYS._str(MyMaker.__dict__,
            **{'RepresentingAlineaIsBool':False})
    ]

#Definition
SYS._attest(AttestingStrsList)

#Print


```


```console
>>>
Maker : I am going to make
('self.MakingMyFloat is ', 3.0)

MyMaker is
<MakerClass object at 0x103288990>
we reset doing
MyMaker after set doing is
<MakerClass object at 0x103288990>


*****Start of the Attest *****

MyMaker.__dict__ is
   /{
   /  'IdInt' : 4347955600
   /  'MadeMyInt' : 3
   /  'MadeMyList' : []
   /  'MakingFirstInt' : 0
   /  'MakingMyFloat' : 1.0
   /  'MakingMyList' : []
   /  'MakingSecondInt' : 0
   /}

*****End of the Attest *****



```

