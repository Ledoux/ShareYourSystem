
#Representer


@Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Representer is an important module for beginning to visualize the structures
of the instanced variables in the environnment. The idea is to use the indenting
representation like in the json.dump function but with a more suitable (but
maybe dirty) access to the AlineaStr of each lines of the output, depending
on the state of the variables. Instances that are created from the decorated
class have a __repr__ method, helping for mentionning for the represented
attributes where do they come from : <Spe> (resp. <Base>) is they were defined
at the level of the \_\_class\_\_ and <Instance> (resp. <Class>) if they are
getted from the <InstanceVariable>.__dict__ (resp.
<InstanceVariable>.__class__.__dict__)





<!---
FrozenIsBool True
-->

##Example

First is presented the global functions _print or represent that helps for
printing
in the console any kind of variables.

```python
#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Classors import Representer

#Represent a dict
Dict={
    'ParentDict':
        {
        'ChildDict':
            {
                'MyInt':0
            },
        'MyStr':'hello'
        }
    }

#Represent a TuplesList
TuplesList=[
                (
                    'ParentTuplesList',
                    [
                        (
                            'ChildDict',
                            {
                                'MyInt':0
                            }
                        )
                    ]
                ),
                ('MyStr','hello')
            ]

#Definition the AttestedStr
SYS._attest(
    [
        'Dict is'+Representer.represent(Dict),
        'TuplesList is'+Representer.represent(TuplesList)
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

Dict is
   /{
   /  'ParentDict' :
   /   /{
   /   /  'ChildDict' :
   /   /   /{
   /   /   /  'MyInt' : 0
   /   /   /}
   /   /  'MyStr' : hello
   /   /}
   /}

------

TuplesList is
   /[
   /  0 :
   /   /(
   /   /  0 : ParentTuplesList
   /   /  1 :
   /   /   /[
   /   /   /  0 :
   /   /   /   /(
   /   /   /   /  0 : ChildDict
   /   /   /   /  1 :
   /   /   /   /   /{
   /   /   /   /   /  'MyInt' : 0
   /   /   /   /   /}
   /   /   /   /)
   /   /   /]
   /   /)
   /  1 : ('MyStr', 'hello')
   /]

*****End of the Attest *****




```



<!---
FrozenIsBool True
-->

##Example

Then classes that are decorated by the representer have now a special __repr__
method.

```python
#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Classors import Representer
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
ParentMaker.ChildMaker=MakerClass()

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
        'SimpleMaker is '+SimpleMaker.__repr__(),
        'ParentMaker is '+ParentMaker.__repr__(),
        'ParentBuilder is '+SimpleBuilder.__repr__()
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

SimpleMaker is < (MakerClass), 4478454096>
   /{
   /  '<Class>MadeMyInt' : 0
   /  '<Spe><Instance>MakingMyFloat' : 2.0
   /}

------

ParentMaker is < (MakerClass), 4478454160>
   /{
   /  '<Class>MadeMyInt' : 0
   /  '<New><Instance>ChildMaker' : < (MakerClass), 4478454224>
   /   /{
   /   /  '<Class>MadeMyInt' : 0
   /   /}
   /}

------

ParentBuilder is < (BuilderClass), 4478454544>
   /{
   /  '<Base><Class>MadeMyInt' : 0
   /  '<Class>BuiltMyStr' : None
   /  '<Spe><Instance>MakingMyFloat' : 2.0
   /}

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the RepresenterClass are :


```python




```


```console
>>>


```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the instances

A default call of an instance gives :


```python





```


```console
>>>


```

