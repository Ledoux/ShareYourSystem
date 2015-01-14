

<!--
FrozenIsBool False
-->

#Propertiser

##Doc
----


>
> The Propertiser is an augmented Defaultor because it will set defaults
attributes
> possibly in properties for the new-style decorated classes. This can set
objects
> with high controlling features thanks to the binding
>
>

----

<small>
View the Propertiser notebook on [NbViewer](http://nbviewer.ipython.org/url/shar
eyoursystem.ouvaton.org/Propertiser.ipynb)
</small>




<!---
FrozenIsBool True
-->

##Example

Going back to the Doer cell when we invented a very minimalist Maker.
We now define its MakingMyFloat as a property that can be then defined as
a "binding" attribute thanks to the setMakingMyFloat method definition,
that will be linked to the fset attribute of the property object.

```python
#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Classors import Propertiser,Attester
from ShareYourSystem.Objects import Initiator

#Definition a MakerClass decorated by the PropertiserClass
@Propertiser.PropertiserClass()
class MakerClass(Initiator.InitiatorClass):

    def default_init(self,
            _MakingMyFloat={
                            'DefaultingSetType':property,
                            'PropertizingInitVariable':3.,
                            'PropertizingDocStr':'I am doing the thing here'
                            },
            _MakingMyList={
                            'DefaultingSetType':property,
                            'PropertizingInitVariable':[],
                            'PropertizingDocStr':'I am doing the thing here'
                            },
            _MakingMyInt={'DefaultingSetType':int},
            _MadeMyInt=0
        ):
        pass

    #Definition a binding function
    def setMakingMyFloat(self,_SettingValueVariable):

        #Print
        #print('I am going to make the job directly !')

        #set the value of the "hidden" property variable
        self._MakingMyFloat=_SettingValueVariable

        #Bind with MadeInt setting
        self.MadeMyInt=int(self._MakingMyFloat)

    #Definition a binding function
    def setMakingMyList(self,_SettingValueVariable):

        #set the value of the "hidden" property variable
        self._MakingMyList=_SettingValueVariable+['Hellllllo']


#Definition a default instance
DefaultMaker=MakerClass()

#Definition a special instance
SpecialMaker=MakerClass(_MakingMyFloat=5,_MakingMyList=[4])

#Definition the AttestedStr
SYS._attest(
    [
        'MakerClass.PropertizedDefaultTuplesList is '+SYS._str(
            MakerClass.PropertizedDefaultTuplesList),
        'What are you saying DefaultMaker ?',
        'DefaultMaker.__dict__ is '+str(DefaultMaker.__dict__),
        'DefaultMaker.MakingMyFloat is '+str(DefaultMaker.MakingMyFloat),
        'DefaultMaker.MakingMyList is '+str(DefaultMaker.MakingMyList),
        'DefaultMaker.MadeMyInt is '+str(DefaultMaker.MadeMyInt),
        'What are you saying SpecialMaker ?',
        'SpecialMaker.__dict__ is '+str(SpecialMaker.__dict__),
        'SpecialMaker.MakingMyFloat is '+str(SpecialMaker.MakingMyFloat),
        'SpecialMaker.MakingMyList is '+str(SpecialMaker.MakingMyList),
        'SpecialMaker.MadeMyInt is '+str(SpecialMaker.MadeMyInt),
    ]
)

#Print


```


```console
>>>


*****Start of the Attest *****

MakerClass.PropertizedDefaultTuplesList is
   /[
   /  0 :
   /   /(
   /   /  0 : MakingMyFloat
   /   /  1 : <property object at 0x104319730>
   /   /)
   /  1 :
   /   /(
   /   /  0 : MakingMyList
   /   /  1 : <property object at 0x104319788>
   /   /)
   /]

------

What are you saying DefaultMaker ?

------

DefaultMaker.__dict__ is {'IdInt': 4365305040}

------

DefaultMaker.MakingMyFloat is 3.0

------

DefaultMaker.MakingMyList is []

------

DefaultMaker.MadeMyInt is 0

------

What are you saying SpecialMaker ?

------

SpecialMaker.__dict__ is {'IdInt': 4365305232, 'MadeMyInt': 5, '_MakingMyFloat':
5, '_MakingMyList': [4, 'Hellllllo']}

------

SpecialMaker.MakingMyFloat is 5

------

SpecialMaker.MakingMyList is [4, 'Hellllllo']

------

SpecialMaker.MadeMyInt is 5

*****End of the Attest *****



```

