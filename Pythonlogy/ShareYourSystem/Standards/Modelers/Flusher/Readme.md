

<!--
FrozenIsBool False
-->

#Flusher

##Doc
----


>
> Flusher instances can flush a RowedVariablesList into a table
> checking maybe before if this line is new in the table or not
> depending on identifying items.
>
>

----

<small>
View the Flusher notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyou
rsystem.ouvaton.org/Flusher.ipynb)
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


Flusher instances can flush a RowedVariablesList into a table
checking maybe before if this line is new in the table or not
depending on identifying items.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
import collections
BaseModuleStr="ShareYourSystem.Standards.Modelers.Rower"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class FlusherClass(
                                        BaseClass,
                                ):

        #Definition
        RepresentingKeyStrsList=[
'FlushedNotRowGetStrsList',
'FlushedNotRowColumnStrsList',
'FlushedNotRowPickOrderedDict',
'FlushedIndexInt'
                                                                ]

        def default_init(self,
                                        _FlushedNotRowGetStrsList=None,
                                        _FlushedNotRowColumnStrsList=None,
                                        _FlushedNotRowPickOrderedDict=None,
                                        _FlushedIndexInt=-1,
                                        **_KwargVariablesDict
                                        ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def setRowingGetStrsList(self,_SettingValueVariable):

                #Hook
                BaseClass.setRowingGetStrsList(self,_SettingValueVariable)

                #Bind
                self.FlushedNotRowGetStrsList=list(set(SYS.unzip(
                        self.DatabasingSealTuplesList,[0]
                ))-set(self.RowingGetStrsList))

                #set
                self.FlushedNotRowColumnStrsList=map(
                        lambda __NotRowGetStr:
                        self.RowedGetStrToColumnStrOrderedDict[__NotRowGetStr],
                        self.FlushedNotRowGetStrsList
                )
        RowingGetStrsList=property(
BaseClass.RowingGetStrsList.fget,
setRowingGetStrsList,
BaseClass.RowingGetStrsList.fdel,
BaseClass.RowingGetStrsList.__doc__
                                                                )


        def do_flush(self):
                """ """

                #debug
                '''
                self.debug('row maybe before...')
                '''

                #<NotHook>
                #row first
                self.row()
                #</NotHook>

                #debug
                '''
                self.debug(
                                        ('self.',self,['RowedIsBool'])
                                )
                self.NodePointDeriveNoder.debug([
                                ('NOTE : ...ParentSpeaking...')
                        ])
                '''

                """
                map(
                                lambda __InitVariable:
                                setattr(
                                        self,
                                        __KeyStr,
SYS.getInitiatedVariableWithKeyStr(__KeyStr)
                                ) if __InitVariable==None else None,
                                map(
                                                lambda __KeyStr:
                                                (
                                                        __KeyStr,
                                                        getattr(self,__KeyStr)
                                                ),
                                                [
'FlushedNotRowPickOrderedDict',
'FlushedNotRowGetStrsList',
'FlushedNotRowGetStrsList',
'FlushedNotRowPickOrderedDict'
                                                ]
                                        )
                        )
                """

                #debug
                '''
                self.debug(('self.',self,['FlushedNotRowPickOrderedDict']))
                '''

                #Append and row if it is new
                if self.RowedIsBool==False:

                        #Check
                        if self.TabledTable!=None:

                                #debug
                                '''
                                self.debug('This is a new row')
                                '''

                                #Get the row
                                Row=None
                                Row=self.TabledTable.row

                                #debug
                                '''
self.debug(('self.',self,['FlushedNotRowPickOrderedDict']))
                                '''

                                #Pick and update
                                self.FlushedNotRowPickOrderedDict.update(
                                zip(
                                        self.FlushedNotRowColumnStrsList,
                                        self.NodePointDeriveNoder.pick(
                                                self.FlushedNotRowGetStrsList
                                                )
                                        )
                                )

                                #debug
                                '''
                                self.debug(('self.',self,[
        'RowedPickOrderedDict',
        'FlushedNotRowPickOrderedDict'
]))
                                '''

                                #Definition the FlushedItemTuplesList
                                FlushedItemTuplesList=[
('RowInt',self.RowedIndexInt)
]+self.RowedPickOrderedDict.items(
)+self.FlushedNotRowPickOrderedDict.items()

                                #import tables
                                #print(tables.tableextension.Row)

                                #debug
                                '''
                                self.debug(
                                                        [
                                                                'This is a new
row',
                                                                'Colnames are :
'+str(self.TabledTable.colnames),
'FlushedItemTuplesList is '+str(FlushedItemTuplesList),
'self.TabledTable is '+str(dir(self.TabledTable)),
'self.DatabasedModelClass is '+(str(self.DatabasedModelClass.columns) if
hasattr(self.DatabasedModelClass,'columns') else ""),
                                                                'Row is
'+str(dir(Row)),
                                                                'Row.table is
'+str(Row.table),
'TabularedTablesOrderedDict is '+str(self.TabularedTablesOrderedDict)
                                                        ]
                                                )
                                '''

                                #set
                                map(
                                                lambda __FlushingTuple:
Row.__setitem__(*__FlushingTuple),
                                                FlushedItemTuplesList
                                        )

                                #debug
                                '''
                                self.debug('The Row setting was good, so append
flush')
                                '''

                                #Append and Flush
                                Row.append()
                                self.TabledTable.flush()

                else:

                        #debug
                        '''
                        self.debug(
                                                [
                                                        'This is maybe not an
IdentifyingFlusher',
                                                        'Or it is already
rowed',
                                                        'self.FlushedIsBoolsList
is '+str(self.FlushedIsBoolsList)
                                                ]
                                        )
                        '''
                        pass

                #<NotHook>
                #Return self
                #return self
                #</NotHook>

#</DefineClass>

```

<small>
View the Flusher sources on <a href="https://github.com/Ledoux/ShareYourSystem/t
ree/master/Pythonlogy/ShareYourSystem/Databasers/Flusher"
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
from ShareYourSystem.Standards.Modelers import Flusher

#Definition of a Structurer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
    "Datome",
    "Things",
    Flusher.FlusherClass().update(
        [
            (
                'Attr_DatabasingSealTuplesList',
                [
                    #GetStr #ColumnStr #Col
                    ('MyInt','MyInt',tables.Int64Col()),
                    ('MyStr','MyStr',tables.StringCol(10)),
                    ('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
                ]
            ),
            ('Attr_RowingGetStrsList',['MyInt'])
        ]
    )
)

#Definition a structure with a db
MyStructurer.update(
            [
                ('MyInt',1),
                ('MyStr',"bonjour"),
                ('MyIntsList',[2,4,6])
            ]
).command(
    _UpdateList=[('flush',{'LiargVariablesList':[]})],
    **{'GatheringVariablesList':['<Datome>ThingsFlusher']}
).update(
            [
                ('MyInt',0),
                ('MyStr',"hello"),
                ('MyIntsList',[0,0,0])
            ]
).command(
    _UpdateList=[('flush',{'LiargVariablesList':[]})],
)

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

MyStructurer is < (StructurerClass), 4563962256>
   /{
   /  '<New><Instance>DatomeCollectionOrderedDict' :
   /   /{
   /   /  'ThingsFlusher' : < (FlusherClass), 4563961296>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4563961296
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Datome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ThingsFlusher
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4563962256>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4563687232>
   /   /   /  '<New><Instance>_DatabasingSealTuplesList' :
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
   /   /   /  '<New><Instance>_RowingGetStrsList' : ['MyInt']
   /   /   /  '<Spe><Class>FlushedIndexInt' : -1
   /   /   /  '<Spe><Instance>FlushedNotRowColumnStrsList' : ['MyStr',
'MyIntsList']
   /   /   /  '<Spe><Instance>FlushedNotRowGetStrsList' : ['MyStr',
'MyIntsList']
   /   /   /  '<Spe><Instance>FlushedNotRowPickOrderedDict' :
   /   /   /   /{
   /   /   /   /}
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4563962256
   /  '<New><Instance>MyInt' : 0
   /  '<New><Instance>MyIntsList' : [0, 0, 0]
   /  '<New><Instance>MyStr' : hello
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
/xx0xxThingsFlusherTable Dataset {2/Inf}
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

