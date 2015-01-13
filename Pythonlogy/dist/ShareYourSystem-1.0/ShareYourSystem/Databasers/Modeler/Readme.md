
#Modeler
 @Date : Fri Nov 14 13:20:38 2014

@Author : Erwan Ledoux



The Modeler defines the model to be stored in a database like Django or PyTable.
Here are defined the relations between attributes of an instance and their
corresponding types in the databased structures.





<!---
FrozenIsBool True
-->

##Example

Let's create an empty class, which will automatically receive
special attributes from the decorating ClassorClass,
specially the NameStr, that should be the ClassStr
without the TypeStr in the end.

```python

#ImportModules
import tables
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Modeler

#Definition a Modeler instance
MyModeler=Modeler.ModelerClass().model([
                                        ('MyInt',tables.Int64Col()),
                                        ('MyStr',tables.StrCol(10)),
                                        ('MyIntsList',tables.Int64Col(shape=3))
                                ],**{'DatabasingKeyStr':'Things'})

#Definition the AttestedStr
SYS._attest(
    [
        'MyModeler is '+SYS._str(
        MyModeler,
        **{
            'RepresentingBaseKeyStrsListBool':False
        }
        ),
        'Modeler.ModeledClass.__dict__ is '+str(
        MyModeler.ModeledClass.__dict__ if MyModeler.ModeledClass!=None else
MyModeler.ModeledClass)
    ]
)

#Print



```


```console
>>>

    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx
    l.79 :
    *****
    I am with []
    *****

    ---- Start of the method :
SwitcherFunc@Argumenter.ArgumenterFunc@Modeler.model in Switcher/__init__.pyc
----

    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx


    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx
    ////////////////////////////////
    Modeler/__init__.py model
    From <Str> <module>
    ////////////////////////////////

    l.90 :
    *****
    I am with []
    *****
    self.ModelingSealTuplesList is
       /[
       /  0 :
       /   /(
       /   /  0 : MyInt
       /   /  1 : Int64Col(shape=(), dflt=0, pos=None)
       /   /)
       /  1 :
       /   /(
       /   /  0 : MyStr
       /   /  1 : StrCol(itemsize=10, shape=(), dflt='', pos=None)
       /   /)
       /  2 :
       /   /(
       /   /  0 : MyIntsList
       /   /  1 : Int64Col(shape=(3,), dflt=0, pos=None)
       /   /)
       /]

    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx


    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx
    l.101 :
    *****
    I am with []
    *****
    self.DatabasingKeyStr is Things
    self.DatabasedSuffixStr is ThingsModel

    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx


    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx
    l.95 :
    *****
    I am with []
    *****

    ---- End of the method :
SwitcherFunc@Argumenter.ArgumenterFunc@Modeler.model in Switcher/__init__.pyc
----

    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxx



*****Start of the Attest *****

MyModeler is     < (ModelerClass), 4487894480>
       /{
       /  '<New><Class>SwitchedClassDatabaseBool' : True
       /  '<New><Class>SwitchedClassModelBool' : True
       /  '<New><Class>SwitchingDatabaseBool' : False
       /  '<New><Class>SwitchingModelBool' : False
       /  '<New><Instance>SwitchingDatabaseBool' : True
       /  '<New><Instance>SwitchingModelBool' : True
       /  '<Spe><Class>ModeledClassesOrderedDict' :
       /   /{
       /   /  'ThingsModel' : <class 'tables.description.ThingsModelClass'>
       /   /}
       /  '<Spe><Instance>ModeledClass' : <class
'tables.description.ThingsModelClass'>
       /  '<Spe><Instance>ModeledKeyStr' : ThingsModel
       /  '<Spe><Instance>ModelingSealTuplesList' :
       /   /[
       /   /  0 :
   /   /   /(
   /   /   /  0 : MyInt
   /   /   /  1 : Int64Col(shape=(), dflt=0, pos=None)
   /   /   /)
       /   /  1 :
   /   /   /(
   /   /   /  0 : MyStr
   /   /   /  1 : StrCol(itemsize=10, shape=(), dflt='', pos=None)
   /   /   /)
       /   /  2 :
   /   /   /(
   /   /   /  0 : MyIntsList
   /   /   /  1 : Int64Col(shape=(3,), dflt=0, pos=None)
   /   /   /)
       /   /]
       /}

------

Modeler.ModeledClass.__dict__ is {'__module__': 'tables.description', '__doc__':
None, 'columns': {'MyStr': StrCol(itemsize=10, shape=(), dflt='',
pos=None), 'MyIntsList': Int64Col(shape=(3,), dflt=0, pos=None), 'MyInt':
Int64Col(shape=(), dflt=0, pos=None), 'ModeledInt': Int64Col(shape=(), dflt=0,
pos=None)}}

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the class

Special attributes of the ModelerClass are :


```python



#ImportModules
import ShareYourSystem as SYS
from ShareYourSystem.Objects import Modeler

#Definition the AttestedStr
SYS._attest(
    [
        'DefaultAttributeItemTuplesList is '+SYS._str(
            Modeler.ModelerClass.DefaultAttributeItemTuplesList,
            **{'RepresentingAlineaIsBool':False}
        )
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

DefaultAttributeItemTuplesList is
   /[
   /  0 :
   /   /(
   /   /  0 : ModelingSealTuplesList
   /   /  1 : []
   /   /)
   /  1 :
   /   /(
   /   /  0 : ModeledClassesOrderedDict
   /   /  1 :
   /   /   /{
   /   /   /}
   /   /)
   /  2 : ('ModeledClass', None)
   /  3 : ('ModeledKeyStr', '')
   /]

*****End of the Attest *****




```



<!--
FrozenIsBool False
-->

##More Descriptions at the level of the instances

A default call of an instance gives :


```python



#ImportModules
from ShareYourSystem.Classors import Attester
from ShareYourSystem.Objects import Modeler

#Definition the AttestedStr
SYS._attest(
    [
        Modeler.ModelerClass()
    ]
)

#Print




```


```console
>>>


*****Start of the Attest *****

< (ModelerClass), 4500475088>
   /{
   /  '<Spe><Class>ModeledClass' : None
   /  '<Spe><Class>ModeledClassesOrderedDict' :
   /   /{
   /   /}
   /  '<Spe><Class>ModeledKeyStr' :
   /  '<Spe><Class>ModelingSealTuplesList' : []
   /}

*****End of the Attest *****




```

