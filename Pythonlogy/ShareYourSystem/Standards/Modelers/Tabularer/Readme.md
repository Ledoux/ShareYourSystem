

<!--
FrozenIsBool False
-->

#Tabularer

##Doc
----


>
> The Tabularer helps to define names for setting Tables in a hdf5 structure,
> given the names of predefined models.
>
>

----

<small>
View the Tabularer notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Tabularer.ipynb)
</small>




<!--
FrozenIsBool False
-->

##Code

----

<ClassDocStr>

----

```python
# -*- coding: utf-8 -*-
"""


<DefineSource>
@Date : Fri Nov 14 13:20:38 2014 \n
@Author : Erwan Ledoux \n\n
</DefineSource>


The Tabularer helps to define names for setting Tables in a hdf5 structure,
given the names of predefined models.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Modeler"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import collections
import importlib
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['tabular']})
class TabularerClass(
                                        BaseClass
                                ):

        #Definition
        RepresentingKeyStrsList=[
'TabularedGroupVariable',
'TabularedTopFileVariable',
'TabularedSuffixStr',
'TabularedTableKeyStrsList',
'TabularedTablesOrderedDict'
                                                                ]

        def default_init(self,
                                        _TabularedGroupVariable=None,
                                        _TabularedTopFileVariable=None,
                                        _TabularedSuffixStr="",
                                        _TabularedTableKeyStrsList=None,
                                        _TabularedTablesOrderedDict=None,
                                        **_KwargVariablesDict
                                ):

                #Call the parent __init__ method
                BaseClass.__init__(self,**_KwargVariablesDict)


        def do_tabular(self):
                """ """

                #debug
                '''
                self.debug(
                                [
                                        ('self.',self,[
'ModelingDescriptionTuplesList',
                                                        'ModeledDescriptionClass',
'WatchModelWithModelerBool',
'WatchModelWithJoinerBool'
                                                ]),
                                        'self.model is '+SYS._str(self.model)
                                ]
                        )
                '''

                #<NotHook>
                #model first
                self.model()
                #</NotHook>

                #debug
                '''
                self.debug(
                                        [
('self.',self,['ModelingDescriptionTuplesList','ModeledDescriptionClass']),
('self.ModeledDeriveControllerVariable!=None is
'+str(self.ModeledDeriveControllerVariable!=None))
                                        ]
                                )
                '''

                #Maybe we have to hdformat first
                if self.ModeledDeriveControllerVariable!=None:

                        #Check
                        if
self.ModeledDeriveControllerVariable.HdformatedFileVariable==None:

                                #debug
                                '''
                                self.debug('We have to hdformat first...')
                                '''

                                #Hdformat
self.ModeledDeriveControllerVariable.hdformat()
#self.ModeledDeriveControllerVariable.structure()

                        #Link
                        self.TabularedTopFileVariable=self.ModeledPointDer
iveStorerVariable.HdformatedFileVariable
self.GroupedPathStr=self.ModeledDeriveControllerVariable.GroupedPathStr

                        #debug
                        '''
                        self.debug(('self.',self,[
'HdformatedFileVariable',
'ModelingDescriptionTuplesList',
'ModeledDescriptionClass'
                                                                        ]))
                        '''

                        #Check
                        if self.TabularedTopFileVariable!=None:

                                #debug
                                '''
                                self.debug(
                                                        [
                                                                'Looking for
names of tables here',
('self.',self,['GroupedPathStr'])
                                                        ]
                                                )
                                '''

                                #Definition Tabulared attributes
self.TabularedGroupVariable=self.TabularedTopFileVariable.getNode(
                                        self.GroupedPathStr)

                                #debug
                                '''
self.debug(('self.',self,['ModeledSuffixStr']))
                                '''

                                #set
                                self.TabularedSuffixStr='Model'.join(self.Databa
sedSuffixStr.split('Model')[:-1])+'Table'

                                #debug
                                '''
                                self.debug(
                                                        [
                                                                ('looking for
tables with the same suffix Str as : '),
('self.',self,['TabularedSuffixStr'])
                                                        ]
                                                )
                                '''

                                #Get and sort
                                self.TabularedTableKeyStrsList=sorted(
                                        filter(
                                                        lambda __KeyStr:
__KeyStr.endswith(self.TabularedSuffixStr),
self.TabularedGroupVariable._v_leaves.keys()
                                                )
                                )

                                self.TabularedTablesOrderedDict.update(
                                        map(
                                                        lambda
__TabularedKeyStr:
                                                        (
__TabularedKeyStr,
self.TabularedGroupVariable._f_getChild(__TabularedKeyStr)
                                                        ),
self.TabularedTableKeyStrsList
                                                )
                                )

                                #debug
                                '''
                                self.debug(("self.",self,[
        'TabularedSuffixStr',
        'TabularedTableKeyStrsList'
        ]))
                                '''

                #<NotHook>
                #Return
                #return self
                #</NotHook>

#</DefineClass>

```

<small>
View the Tabularer sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Databasers/Tabularer"
target="_blank">Github</a>
</small>




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
from ShareYourSystem.Standards.Noders import Structurer
from ShareYourSystem.Standards.Modelers import Tabularer

#Definition of a Storer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
    "Datome",
    "Things",
    Tabularer.TabularerClass().__setitem__(
        'Attr_ModelingDescriptionTuplesList',
        [
            #GetStr #ColumnStr #Col
            ('MyInt','MyInt',tables.Int64Col()),
            ('MyStr','MyStr',tables.StringCol(10)),
            ('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
        ]
    )
)

#Build a structure with a database
MyStructurer['<Datome>ThingsTabularer'].tabular()

#Definition the AttestedStr
SYS._attest(
    [
        'MyStructurer is '+SYS._str(
        MyStructurer,
        **{
            'RepresentingBaseKeyStrsListBool':False,
            'RepresentingAlineaIsBool':False
        }
        ),
        'hdf5 file is : '+MyStructurer.hdfview().hdfclose().HdformatedConsoleStr
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyStructurer is < (StructurerClass), 4563976400>
   /{
   /  '<New><Instance>DatomeCollectionOrderedDict' :
   /   /{
   /   /  'ThingsTabularer' : < (TabularerClass), 4563977872>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4563977872
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Datome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ThingsTabularer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4563976400>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4561219120>
   /   /   /  '<New><Instance>_ModelingDescriptionTuplesList' :
   /   /   /   /[
   /   /   /   /  0 :
   /   /   /   /   /(
   /   /   /   /   /  0 : MyInt
   /   /   /   /   /  1 : MyInt
   /   /   /   /   /  2 : Int64Col(shape=(), dflt=0, pos=None)
   /   /   /   /   /)
   /   /   /   /  1 :
   /   /   /   /   /(
   /   /   /   /   /  0 : MyStr
   /   /   /   /   /  1 : MyStr
   /   /   /   /   /  2 : StringCol(itemsize=10, shape=(), dflt='', pos=None)
   /   /   /   /   /)
   /   /   /   /  2 :
   /   /   /   /   /(
   /   /   /   /   /  0 : MyIntsList
   /   /   /   /   /  1 : MyIntsList
   /   /   /   /   /  2 : Int64Col(shape=(3,), dflt=0, pos=None)
   /   /   /   /   /)
   /   /   /   /]
   /   /   /  '<Spe><Instance>TabularedTopFileVariable' :
File(filename=/Users/ledoux/Documents/ShareYourSystem/Structures.hdf5, title='',
mode='r+', root_uep='/', filters=Filters(complevel=0, shuffle=False,
fletcher32=False, least_significant_digit=None))
/ (RootGroup) ''
/xx0xxThingsFindoerTable (Table(3,)) 'This is the ThingsFindoerModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx0xxThingsInserterTable (Table(2,)) 'This is the ThingsInserterModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx0xxThingsRecovererTable (Table(3,)) 'This is the ThingsRecovererModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx0xxThingsRetrieverTable (Table(2,)) 'This is the ThingsRetrieverModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx0xxThingsRowerTable (Table(0,)) 'This is the ThingsRowerModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx0xxThingsTablerTable (Table(0,)) 'This is the ThingsTablerModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx0xx__UnitsInt_3__ThingsMergerTable (Table(2,)) 'This is the
__UnitsInt_3__ThingsMergerModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx0xx__UnitsInt_3__ThingsShaperTable (Table(2,)) 'This is the
__UnitsInt_3__ThingsShaperModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
/xx1xx__UnitsInt_2__ThingsMergerTable (Table(1,)) 'This is the
__UnitsInt_2__ThingsMergerModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(2,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1560,)
/xx1xx__UnitsInt_2__ThingsShaperTable (Table(1,)) 'This is the
__UnitsInt_2__ThingsShaperModelClass'
  description := {
  "RowInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(2,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1560,)
/TopStructurer (Group) ''
/TopStructurer/FirstChildStructurer (Group) ''
/TopStructurer/SecondChildStructurer (Group) ''
/TopStructurer/SecondChildStructurer/OtherGrandChildStructurer (Group) ''
/TopStructurer/FirstChildStructurer/GrandChildStructurer (Group) ''

   /   /   /  '<Spe><Instance>TabularedGroupVariable' : / (RootGroup) ''
  children := ['xx1xx__UnitsInt_2__ThingsMergerTable' (Table),
'xx0xx__UnitsInt_3__ThingsShaperTable' (Table), 'xx0xxThingsRetrieverTable'
(Table), 'xx0xxThingsInserterTable' (Table),
'xx1xx__UnitsInt_2__ThingsShaperTable' (Table),
'xx0xx__UnitsInt_3__ThingsMergerTable' (Table), 'TopStructurer' (Group),
'xx0xxThingsRecovererTable' (Table), 'xx0xxThingsFindoerTable' (Table),
'xx0xxThingsRowerTable' (Table), 'xx0xxThingsTablerTable' (Table)]
   /   /   /  '<Spe><Instance>TabularedTableKeyStrsList' : []
   /   /   /  '<Spe><Instance>TabularedTablesOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /  '<Spe><Instance>TabularedSuffixStr' : ThingsTabularerTable
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4563976400
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopStructurer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<Spe><Class>StructuringBeforeUpdateList' : None
   /  '<Spe><Class>StructuringNodeCollectionStrsList' : []
   /}

------

hdf5 file is : /                        Group
/TopStructurer           Group
/TopStructurer/FirstChildStructurer Group
/TopStructurer/FirstChildStructurer/GrandChildStructurer Group
/TopStructurer/SecondChildStructurer Group
/TopStructurer/SecondChildStructurer/OtherGrandChildStructurer Group
/xx0xxThingsFindoerTable Dataset {3/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,1], MyStr="guten tag"},
        (2) {RowInt=2, MyInt=1, MyIntsList=[0,0,0], MyStr="bonjour"}
/xx0xxThingsInserterTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[2,4,6], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,0], MyStr="hello"}
/xx0xxThingsRecovererTable Dataset {3/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,1], MyStr="guten tag"},
        (2) {RowInt=2, MyInt=1, MyIntsList=[0,0,0], MyStr="bonjour"}
/xx0xxThingsRetrieverTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=1, MyIntsList=[2,4,6], MyStr="bonjour"},
        (1) {RowInt=1, MyInt=0, MyIntsList=[0,0,0], MyStr="guten tag"}
/xx0xxThingsRowerTable   Dataset {0/Inf}
    Data:

/xx0xxThingsTablerTable  Dataset {0/Inf}
    Data:

/xx0xx__UnitsInt_3__ThingsMergerTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0,1], MyStr="hello"},
        (1) {RowInt=1, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"}
/xx0xx__UnitsInt_3__ThingsShaperTable Dataset {2/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0,1], MyStr="hello"},
        (1) {RowInt=1, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"}
/xx1xx__UnitsInt_2__ThingsMergerTable Dataset {1/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0], MyStr=""}
/xx1xx__UnitsInt_2__ThingsShaperTable Dataset {1/Inf}
    Data:
        (0) {RowInt=0, MyInt=0, MyIntsList=[0,0], MyStr=""}


*****End of the Attest *****



```

