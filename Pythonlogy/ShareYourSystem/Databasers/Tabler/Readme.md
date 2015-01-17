

<!--
FrozenIsBool False
-->

#Tabler

##Doc
----


>
> The Tabler defines TablesClass instances able to set in a hdf5 structure
> a table at a certain node, taking in account the order of already created
tables.
>
>

----

<small>
View the Tabler notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Tabler.ipynb)
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


The Tabler defines TablesClass instances able to set in a hdf5 structure
a table at a certain node, taking in account the order of already created
tables.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Databasers.Tabularer"
DecorationModuleStr="ShareYourSystem.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
#</ImportSpecificModules>

#<DefineLocals>
TablingOrderStr='xx'
#</DefineLocals>

#<DefineClass>
@DecorationClass(**{'ClassingSwitchMethodStrsList':['table']})
class TablerClass(
                                        BaseClass,
                                ):

        #Definition
        RepresentingKeyStrsList=[
'TabledKeyStr',
'TabledInt',
'TabledTable'
                                                                ]

        def default_init(self,
                                                _TabledKeyStr="",
                                                _TabledInt=-1,
                                                _TabledTable=None,
                                                **_KwargVariablesDict
                                                ):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def do_table(self):

                #debug
                '''
                self.debug(('self.',self,['ModelingSealTuplesList']))
                '''

                #<NotHook>
                #tabular first
                self.tabular()
                #</NotHook>

                #debug
                '''
                self.debug(
                                        [
                                                'We are going to look if this is
a new table or not...In order to index it',
                                                ('self.',self,[
        'ModeledKeyStr',
        'ModeledClass',
        'TabularedKeyStrsList',
        'TabularedSuffixStr',
        'TabledKeyStr'
])
                                        ]
                                )
                '''

                #Get the suffix Strs of all the tables and their index
                TabledList=SYS.unzip(map(
                                lambda __StrsList:
                                (
                                        __StrsList[1],
                                        TablingOrderStr.join(__StrsList[2:])
                                ),
                                map(
                                                lambda __TabledKeyStr:
__TabledKeyStr.split(TablingOrderStr),
                                                self.TabularedKeyStrsList
                                        )
                        ),[0,1])

                #debug
                '''
                self.debug(('vars ',vars(),['TabledList']))
                '''

                #Unpack if it is possible
                if len(TabledList)>0:

                        #Unpack
                        [TabledIntsTuple,TabledSuffixStrsList]=TabledList

                        #debug
                        '''
                        self.debug(
                                                [
                                                        'There are already some
tables',
                                                        'TabledSuffixStrsList is
'+str(TabledSuffixStrsList),
                                                        "self.TabularedSuffixStr
is "+str(
self.TabularedSuffixStr)
                                                ]
                                        )
                        '''

                        if self.TabularedSuffixStr not in TabledSuffixStrsList:

                                #Increment the IndexStr
                                IndexInt=max(map(int,TabledIntsTuple))+1

                                #Strify
                                IndexStr=str(IndexInt)

                                #debug
                                '''
                                self.debug('IndexStr of this new table is
'+str(IndexStr))
                                '''

                        else:

                                #Get the already setted one
                                IndexStr=self.TabularedKeyStrsList[
TabledSuffixStrsList.index(self.TabularedSuffixStr)
                                        ].split(TablingOrderStr)[1]

                                #Intify
                                IndexInt=(int)(IndexStr)

                                #debug
                                '''
                                self.debug('IndexStr of this not new table is
'+str(IndexStr))
                                '''

                else:

                        #debug
                        '''
                        self.debug('There are no tables here')
                        '''

                        #set to empty lists
                        [TabledIntsTuple,TabledSuffixStrsList]=[[],[]]

                        #Init the list
                        IndexInt=0

                        #Strify
                        IndexStr="0"

                #Bind with TabledKeyStr setting
                self.TabledKeyStr=TablingOrderStr+IndexStr+TablingOrderStr+self.
TabularedSuffixStr

                #set the TabularedInt
                self.TabledInt=IndexInt

                #debug
                '''
                self.debug("self.TabledKeyStr is "+str(self.TabledKeyStr))
                '''

                #debug
                '''
                self.debug(
                                        [
                                                'Here we create the table or get
it depending if it is new or not',
                                                'self.TabledKeyStr is
'+self.TabledKeyStr,
'self.TabularedFilePointedVariable!=None is
'+str(self.TabularedFilePointedVariable!=None)
                                        ]
                                )
                '''

                #Check
                if self.TabledKeyStr!="" and
self.TabularedFilePointedVariable!=None:

                        #debug
                        '''
                        self.debug(
                                                [
('self.',self,['TabledKeyStr','TabularedKeyStrsList'])
                                                ]
                                        )
                        '''

                        #Create the Table if not already
                        if self.TabledKeyStr not in self.TabularedKeyStrsList:

                                #debug
                                '''
                                self.debug(
                                                        [
                                                                'The table not
exists',
                                                        ]
                                                )
                                '''

                                #Create the Table in the hdf5
self.TabledTable=self.TabularedFilePointedVariable.create_table(
        self.TabularedGroup,
        self.TabledKeyStr,
        self.ModeledClass,
        self.ModeledClass.__doc__
        if self.ModeledClass.__doc__!=None
        else "This is the "+self.ModeledClass.__name__
)

                                #Append in the
self.ModeledDict['TabularedKeyStrsList']
self.TabularedKeyStrsList.append(self.TabledKeyStr)

                        else:

                                #debug
                                '''
                                self.debug(
                                                                [
                                                                        'The
table exists',
"self.TabularedGroup is "+str(self.TabularedGroup)
                                                                ]
                                                        )
                                '''

                                #Else just get it
self.TabledTable=self.TabularedGroup._f_getChild(self.TabledKeyStr)

                        #set the in the TablesOrderedDict
self.TabularedOrderedDict[self.TabledKeyStr]=self.TabledTable

                        #debug
                        '''
                        self.debug("self.TabularedOrderedDict is
"+str(self.TabularedOrderedDict))
                        '''

                #debug
                '''
                self.debug(
                                        [
                                                'Table is done here...',
('self.',self,['TabledTable','TabularedFilePointedVariable'])
                                        ]
                                )
                '''

                #<NotHook>
                #Return
                #return self
                #</NotHook>

#</DefineClass>

```

<small>
View the Tabler sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Databasers/Tabler"
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
from ShareYourSystem.Noders import Structurer
from ShareYourSystem.Databasers import Tabler

#Definition of a Structurer instance with a noded datar
MyStructurer=Structurer.StructurerClass().collect(
    "Datome",
    "Things",
    Tabler.TablerClass().__setitem__(
        'Attr_ModelingSealTuplesList',
        [
            #GetStr #ColumnStr #Col
            ('MyInt','MyInt',tables.Int64Col()),
            ('MyStr','MyStr',tables.StringCol(10)),
            ('MyIntsList','MyIntsList',(tables.Int64Col(shape=3)))
        ]
    )
)

#Tabular in it
MyStructurer['<Datome>ThingsTabler'].table()

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
        'hdf5 file is : '+MyStructurer.hdfview().hdfclose().HdformatedStr
    ]
)

#Print



```


```console
>>>


*****Start of the Attest *****

MyStructurer is < (StructurerClass), 4563970960>
   /{
   /  '<New><Instance>DatomeCollectionOrderedDict' :
   /   /{
   /   /  'ThingsTabler' : < (TablerClass), 4563970768>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4563970768
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Datome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ThingsTabler
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4563970960>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4561445832>
   /   /   /  '<New><Instance>_ModelingSealTuplesList' :
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
   /   /   /  '<Spe><Instance>TabledInt' : 0
   /   /   /  '<Spe><Instance>TabledKeyStr' : xx0xxThingsTablerTable
   /   /   /  '<Spe><Instance>TabledTable' : /xx0xxThingsTablerTable (Table(0,))
'This is the ThingsTablerModelClass'
  description := {
  "ModeledInt": Int64Col(shape=(), dflt=0, pos=0),
  "MyInt": Int64Col(shape=(), dflt=0, pos=1),
  "MyIntsList": Int64Col(shape=(3,), dflt=0, pos=2),
  "MyStr": StringCol(itemsize=10, shape=(), dflt='', pos=3)}
  byteorder := 'little'
  chunkshape := (1310,)
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4563970960
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
        (0) {ModeledInt=0, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"},
        (1) {ModeledInt=1, MyInt=0, MyIntsList=[0,0,1], MyStr="guten tag"},
        (2) {ModeledInt=2, MyInt=1, MyIntsList=[0,0,0], MyStr="bonjour"}
/xx0xxThingsFlusherTable Dataset {2/Inf}
    Data:
        (0) {ModeledInt=0, MyInt=1, MyIntsList=[2,4,6], MyStr="bonjour"},
        (1) {ModeledInt=1, MyInt=0, MyIntsList=[0,0,0], MyStr="hello"}
/xx0xxThingsRecovererTable Dataset {3/Inf}
    Data:
        (0) {ModeledInt=0, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"},
        (1) {ModeledInt=1, MyInt=0, MyIntsList=[0,0,1], MyStr="guten tag"},
        (2) {ModeledInt=2, MyInt=1, MyIntsList=[0,0,0], MyStr="bonjour"}
/xx0xxThingsRetrieverTable Dataset {2/Inf}
    Data:
        (0) {ModeledInt=0, MyInt=1, MyIntsList=[2,4,6], MyStr="bonjour"},
        (1) {ModeledInt=1, MyInt=0, MyIntsList=[0,0,0], MyStr="guten tag"}
/xx0xxThingsRowerTable   Dataset {0/Inf}
    Data:

/xx0xxThingsTablerTable  Dataset {0/Inf}
    Data:

/xx0xx__UnitsInt_3__ThingsMergerTable Dataset {2/Inf}
    Data:
        (0) {ModeledInt=0, MyInt=0, MyIntsList=[0,0,1], MyStr="hello"},
        (1) {ModeledInt=1, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"}
/xx0xx__UnitsInt_3__ThingsShaperTable Dataset {2/Inf}
    Data:
        (0) {ModeledInt=0, MyInt=0, MyIntsList=[0,0,1], MyStr="hello"},
        (1) {ModeledInt=1, MyInt=1, MyIntsList=[0,0,1], MyStr="bonjour"}
/xx1xx__UnitsInt_2__ThingsMergerTable Dataset {1/Inf}
    Data:
        (0) {ModeledInt=0, MyInt=0, MyIntsList=[0,0], MyStr=""}
/xx1xx__UnitsInt_2__ThingsShaperTable Dataset {1/Inf}
    Data:
        (0) {ModeledInt=0, MyInt=0, MyIntsList=[0,0], MyStr=""}


*****End of the Attest *****



```

