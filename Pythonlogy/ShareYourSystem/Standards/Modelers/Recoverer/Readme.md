

<!--
FrozenIsBool False
-->

#Recoverer

##Doc
----


>
> Findoer (sorry Finder is already an important module in python standards, so
just to be sure to not override...)
> instances helps to find in a hdf5 table RowedVariablesList corresponding to
the FindingConditionTuplesList.
>
>

----

<small>
View the Recoverer notebook on [NbViewer](http://nbviewer.ipython.org/url/sharey
oursystem.ouvaton.org/Recoverer.ipynb)
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


Findoer (sorry Finder is already an important module in python standards, so
just to be sure to not override...)
instances helps to find in a hdf5 table RowedVariablesList corresponding to the
FindingConditionTuplesList.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Findoer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
from ShareYourSystem.Functers import Argumenter,Hooker
#</ImportSpecificModules>

#<DefineClass>
@DecorationClass()
class RecovererClass(
                                                BaseClass
                                ):

        #Definition
        RepresentingKeyStrsList=[
'RecoveredDict'
                                                                ]

        def default_init(self,
                                                _RecoveredDict=None,
                                                **_KwargVariablesDict
                                        ):
                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        #@Hooker.HookerClass(**{'HookingAfterVariablesList':[{'MethodCallingStr'
:"find"}]})
        #@Argumenter.ArgumenterClass()
        def do_recover(self):

                #debug
                '''
                self.debug(
                                        [
                                                'Is the self.RecoveredDict
already setted ?',
                                                'len(self.RecoveredDict) is
'+str(len(self.RecoveredDict))
                                        ]
                        )
                '''

                #<NotHook>
                #find first
                self.find()
                #</NotHook>

                #Check
                if len(self.RecoveredDict)==0:

                        #debug
                        '''
                        self.debug(
                                                [
                                                        'The RecoveredDict is
not yet setted',
                                                        'Look if we have found
only one FilteredRowedDict',
'len(self.FoundFilterRowDictsList) is '+str(len(self.FoundFilterRowDictsList))
                                                ]
                                        )
                        '''

                        #Check
                        if len(self.FoundFilterRowDictsList)==1:

                                #debug
                                '''
                                self.debug('It is good, there is one solution
!')
                                '''

                                #set the RecoveredDict
self.RecoveredDict.update(self.FoundFilterRowDictsList[0])

                #debug
                '''
                self.debug(
                                        [
                                                'Now we update with the
self.RecoveredDict',
                                                'self.RecoveredDict is
'+str(self.RecoveredDict)
                                        ]
                                )
                '''

                #set the RetrievingIndexesList and retrieve
                self.RetrievingIndexesList=(
0,
self.RecoveredDict['RowInt']
                                                                        )

                #Now we can retrieve
                self.retrieve()

                #<NotHook>
                #Return self
                #return self
                #</NotHook>

#</DefineClass>

```

<small>
View the Recoverer sources on <a href="https://github.com/Ledoux/ShareYourSystem
/tree/master/Pythonlogy/ShareYourSystem/Databasers/Recoverer"
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
import operator,tables

import ShareYourSystem as SYS
from ShareYourSystem.Standards.Noders import Structurer
from ShareYourSystem.Standards.Modelers import Recoverer

#Definition of a Structurer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
    "Datome",
    "Things",
    Recoverer.RecovererClass().update(
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
            ('Attr_RowingGetStrsList',['MyInt','MyStr','MyIntsList'])
        ]
    )
)

MyStructurer.update(
            [
                ('MyInt',1),
                ('MyStr',"bonjour"),
                ('MyIntsList',[0,0,1])
            ]
)['<Datome>ThingsRecoverer'].flush()

MyStructurer.update(
            [
                ('MyInt',0),
                ('MyStr',"guten tag"),
                ('MyIntsList',[0,0,1])
            ]
)['<Datome>ThingsRecoverer'].flush()

MyStructurer.update(
            [
                ('MyInt',1),
                ('MyStr',"bonjour"),
                ('MyIntsList',[0,0,0])
            ]
)['<Datome>ThingsRecoverer'].flush()

#Retrieve
MyStructurer['<Datome>ThingsRecoverer'].recover(
                                                **{
'FindingConditionTuplesList':
                                                        [
('MyInt',(operator.eq,1)),
('MyIntsList',(SYS.getIsEqualBool,[0,0,1]))
                                                        ]
                                                }
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

MyStructurer is < (StructurerClass), 4563970576>
   /{
   /  '<New><Instance>DatomeCollectionOrderedDict' :
   /   /{
   /   /  'ThingsRecoverer' : < (RecovererClass), 4563970512>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4563970512
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Datome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ThingsRecoverer
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4563970576>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4564034208>
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
   /   /   /  '<New><Instance>_RowingGetStrsList' : ['MyInt', 'MyStr',
'MyIntsList']
   /   /   /  '<Spe><Instance>RecoveredDict' :
   /   /   /   /{
   /   /   /   /  'RowInt' : 0
   /   /   /   /  'MyInt' : 1
   /   /   /   /  'MyIntsList' : array([0, 0, 1])
   /   /   /   /  'MyStr' : bonjour
   /   /   /   /}
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4563970576
   /  '<New><Instance>MyInt' : 1
   /  '<New><Instance>MyIntsList' : array([0, 0, 1])
   /  '<New><Instance>MyStr' : bonjour
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

