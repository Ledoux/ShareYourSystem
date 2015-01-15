

<!--
FrozenIsBool False
-->

#Representer

##Doc
----


>
> The Representer is an important module for beginning to visualize
> the structures of the instanced variables in the environnment.
> The idea is to use the indenting representation like in the json.dump
> function but with a more suitable (but maybe dirty) access to the
> AlineaStr of each lines of the output, depending on the state
> of the variables. Instances that are created from the decorated class have
> a __repr__ method, helping for mentionning for the represented attributes
where
> do they come from : <Spe> (resp. <Base>) is they were defined at the level of
the \_\_class\_\_
> and <Instance> (resp. <Class>) if they are getted from the
<InstanceVariable>.__dict__
> (resp. <InstanceVariable>.__class__.__dict__)
>
>

----

<small>
View the Representer notebook on [NbViewer](http://nbviewer.ipython.org/url/shar
eyoursystem.ouvaton.org/Representer.ipynb)
</small>




<!---
FrozenIsBool True
-->

##Example

Then classes that are decorated by the representer have now a special __repr__
method.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Representer,Attester
from ShareYourSystem.Objects import Initiator

#Represent a simple object
@Representer.RepresenterClass()
class MakerClass(Initiator.InitiatorClass):

    RepresentingKeyStrsList=['MadeMyInt']

    def default_init(self,
                        _MakingMyFloat=0.,
                        _MadeMyInt=0
                    ):
        pass

#Definition a simple instance
SimpleMaker=MakerClass(_MakingMyFloat=2.)

#Represent a structured instance
ParentMaker=MakerClass()
ParentMaker.FirstChildMaker=MakerClass()
ParentMaker.CircularChildMaker=MakerClass()
ParentMaker.CircularChildMaker.ParentMaker=ParentMaker
ParentMaker.CircularChildMaker.SelfMaker=ParentMaker.CircularChildMaker

#Definition a derived class from the MakerClass
@Representer.RepresenterClass()
class BuilderClass(MakerClass):

    RepresentingKeyStrsList=['BuiltMyStr']

    def default_init(self,
                        _BuildingMyStr='hello',
                        _BuiltMyStr='None'
                    ):
        pass

#Definition a simple instance
SimpleBuilder=BuilderClass(_MakingMyFloat=2.)

#Definition the AttestedStr
SYS._attest(
    [
        'SimpleMaker is '+SYS._str(SimpleMaker),
        'ParentMaker is '+SYS._str(ParentMaker),
        'SimpleBuilder is '+SYS._str(SimpleBuilder)
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

SimpleMaker is < (MakerClass), 4347994448>
   /{
   /  '<New><Instance>IdInt' : 4347994448
   /  '<Spe><Class>MadeMyInt' : 0
   /}

------

ParentMaker is < (MakerClass), 4347994640>
   /{
   /  '<New><Instance>CircularChildMaker' : < (MakerClass), 4347995472>
   /   /{
   /   /  '<New><Instance>IdInt' : 4347995472
   /   /  '<New><Instance>ParentMaker' : {...}< (MakerClass), 4347994640>
   /   /  '<New><Instance>SelfMaker' : {...}< (MakerClass), 4347995472>
   /   /  '<Spe><Class>MadeMyInt' : 0
   /   /}
   /  '<New><Instance>FirstChildMaker' : < (MakerClass), 4347996624>
   /   /{
   /   /  '<New><Instance>IdInt' : 4347996624
   /   /  '<Spe><Class>MadeMyInt' : 0
   /   /}
   /  '<New><Instance>IdInt' : 4347994640
   /  '<Spe><Class>MadeMyInt' : 0
   /}

------

SimpleBuilder is < (BuilderClass), 4347996688>
   /{
   /  '<New><Instance>IdInt' : 4347996688
   /  '<Spe><Class>BuiltMyStr' : None
   /}

*****End of the Attest *****



```

