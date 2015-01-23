

<!--
FrozenIsBool False
-->

#Shaper

##Doc
----


>
> Shaper instances help for storing data in formated tables :
> if the shape of a rowed variable is depending on other flexible int attribute
> in the environment, it then build or set another table with the good format
> size to store again.
>
>

----

<small>
View the Shaper notebook on [NbViewer](http://nbviewer.ipython.org/url/shareyour
system.ouvaton.org/Shaper.ipynb)
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


Shaper instances help for storing data in formated tables :
if the shape of a rowed variable is depending on other flexible int attribute
in the environment, it then build or set another table with the good format
size to store again.

"""

#<DefineAugmentation>
import ShareYourSystem as SYS
BaseModuleStr="ShareYourSystem.Standards.Modelers.Recoverer"
DecorationModuleStr="ShareYourSystem.Standards.Classors.Classer"
SYS.setSubModule(globals())
#</DefineAugmentation>

#<ImportSpecificModules>
import copy
import collections
import numpy
from ShareYourSystem.Standards.Modelers import Modeler,Tabularer,Tabler,Flusher
#</ImportSpecificModules>

#<DefineLocals>
ShapingJoiningStr='__'
ShapingTuplingStr='_'
#</DefineLocals>

#<DefineClass>
@DecorationClass(
        **{
                'ClassingSwitchMethodStrsList':[
                        'shape',
                        'model',
                        'tabular'
                ]
        }
)
class ShaperClass(BaseClass):

        #Definition
        RepresentingKeyStrsList=[
'ShapingDimensionTuplesList',
'ShapedSealGetKeyStrsList',
'ShapedSealDimensionGetKeyStrsListsList',
'ShapedIndexIntsList',
'ShapedDimensionGetKeyStrsList',
'ShapedDimensionIntsList',
'ShapedStr'
                                                                ]

        def default_init(self,
                                        _ShapingDimensionTuplesList=None,
                                        _ShapedSealGetKeyStrsList=None,
_ShapedSealDimensionGetKeyStrsListsList=None,
                                        _ShapedIndexIntsList=None,
                                        _ShapedDimensionGetKeyStrsList=None,
                                        _ShapedDimensionIntsList=None,
                                        _ShapedStr="",
                                        **_KwargVariablesDict):

                #Call the parent init method
                BaseClass.__init__(self,**_KwargVariablesDict)

        def mimic_model(self):

                #debug
                '''
                self.debug(
                                        [
                                                'self.shape is
'+SYS._str(self.shape)
                                        ]
                        )
                '''

                #<NotHook>
                #database and shape first
                '''
                self.debug('We database first')
                '''
                self.database()
                '''
                self.debug(
                                        [
                                                'We shape first',
                                                'self.shape is '+str(self.shape)
                                        ]
                                )
                '''
                self.shape()
                #</NotHook>

                #Get the new DatabasedKeyStr
                if self.ShapedStr!="":

                        #debug
                        '''
                        self.debug(
                                                [
                                                        'We set the new
DatabasedKeyStr',
('self.',self,['ShapedStr','ModeledSuffixStr'])
                                                ]
                                        )
                        '''

                        #set
self.DatabasedKeyStr=self.ShapedStr+ShapingJoiningStr+self.ModeledSuffixStr

                else:
                        self.DatabasedKeyStr=self.ModeledSuffixStr

                #debug
                '''
                self.debug(
                                        [
                                                'We set the new DatabasedKeyStr',
('self.',self,['ShapedStr','DatabasedKeyStr'])
                                        ]
                                )
                '''

                #Check
                if self.DatabasedModelClassesOrderedDict==None:
                        self.DatabasedModelClassesOrderedDict=collections.OrderedDict()

                #Unnzip
                DatabasedGetKeyStrsList=SYS.unzip(self.DatabasingSealTuplesList,[0])

                #debug
                '''
                self.debug(
                                        [
                                                ('Now change the shape of the
shaping cols'),
('self.',self,['ShapedSealDimensionGetKeyStrsListsList'])
                                        ]
                                )
                '''

                ShapedDatabasingSealTuplesList=map(
                                self.DatabasingSealTuplesList.__getitem__,
                                self.ShapedIndexIntsList
                        )

                #debug
                '''
                self.debug(
                                        'ShapedDatabasingSealTuplesList is
'+str(ShapedDatabasingSealTuplesList)
                                )
                '''

                #set the shaping cols
                map(
                                lambda
__ShapedIndexInt,__ShapedDatabasingSealTuple:
                                self.DatabasingSealTuplesList.__setitem__(
                                        __ShapedIndexInt,
                                        __ShapedDatabasingSealTuple
                                ),
                                self.ShapedIndexIntsList,
                                map(
                                        lambda
__ShapedDatabasingSealTuple,__ShapedSealDimensionGetKeyStrsList:
                                        (
                                                __ShapedDatabasingSealTuple[0],
                                                __ShapedDatabasingSealTuple[1],
__ShapedDatabasingSealTuple[2].__class__(
shape=self.NodePointDeriveNoder.pick(
__ShapedSealDimensionGetKeyStrsList)
                                                )
                                        ),
                                        ShapedDatabasingSealTuplesList,
self.ShapedSealDimensionGetKeyStrsListsList
                                )
                        )

                #debug
                '''
                self.debug("Now self.DatabasingSealTuplesList is "+str(
                        self.DatabasingSealTuplesList))
                '''

                #<NotHook>
                #model then
                Modeler.ModelerClass.model(self)
                #</NotHook>

        def mimic_tabular(self):

                #<NotHook>
                #tabular first
                Tabularer.TabularerClass.tabular(self)
                #</NotHook>

                #debug
                '''
                self.debug(
                                        [
                                                'We add the ShapedStr to the
TabularedSuffix Str ?',
                                                ('self.',self,[
        'TabularedSuffixStr',
        'ShapedStr'
])
                                        ]
                                )
                '''

                #Add the ShapedStr
                if self.ShapedStr!="":

                        #debug
                        '''
                        self.debug(' ShapingJoiningStr not in
self.TabularedSuffixStr is '+str( ShapingJoiningStr not in
self.TabularedSuffixStr))
                        '''

                        if ShapingJoiningStr not in self.TabularedSuffixStr:

                                #debug
                                '''
                                self.debug('Yes we add')
                                '''

                                #Add
self.TabularedSuffixStr=self.ShapedStr+ShapingJoiningStr+self.TabularedSuffixStr

                        #debug
                        '''
                        self.debug("self.TabularedSuffixStr is
"+self.TabularedSuffixStr)
                        '''

        def mimic_flush(self):

                #debug
                '''
                self.debug(
                                        [
                                                ('self.',self,[
        'We check the good dimensions of the shaping variables'
        'TabledKeyStr',
        'TabledTable'
])
                                        ]
                        )
                '''

                try:

                        #<NotHook>
                        #flush first
                        BaseClass.flush(self)
                        #</NotHook>

                except ValueError:

                        #Definition the FlushedOldDimensionIntsListsList
                        FlushedOldDimensionIntsList=map(
                                        lambda
__ShapedSealDimensionGetKeyStrsList:
                                        self.NodePointDeriveNoder.pick(
__ShapedSealDimensionGetKeyStrsList),
self.ShapedSealDimensionGetKeyStrsListsList
                                        )

                        #Definition the FlushedNewDimensionIntsListsList
                        FlushedNewDimensionIntsListsList=map(
                lambda __ShapedSealGetKeyStr:
                list(
                                numpy.shape(
self.NodePointDeriveNoder[__ShapedSealGetKeyStr]
                                )
                ),
                self.ShapedSealGetKeyStrsList
        )

                        #debug
                        '''
                        self.debug(('vars ',vars(),[
        'FlushedOldDimensionIntsList',
        'FlushedNewDimensionIntsListsList'
]))
                        '''

                        #set the shaping attributes to their new values
                        map(
                                        lambda __ShapedSealDimensionGetKeyStrsLi
st,__FlushedOldDimensionList,__FlushedNewDimensionList:
                                        self.__setitem__(
                                                'ShapedErrorBool',
                                                True
                                                ).NodePointDeriveNoder.update(
                                                zip(
__ShapedSealDimensionGetKeyStrsList,
__FlushedNewDimensionList
                                                        )
                                        ) if
__FlushedNewDimensionList!=__FlushedOldDimensionList
                                        else None,
self.ShapedSealDimensionGetKeyStrsListsList,
                                        FlushedOldDimensionIntsList,
                                        FlushedNewDimensionIntsListsList
                                        )

                        #debug
                        '''
                        self.debug('We reset some methods')
                        '''

                        #reboot
                        self.reboot(['Model','Shape','Tabular','Table'])


                        #Table
                        self.table()

                        #debug
                        '''
                        self.debug('Ok table again is done, so now we flush')
                        '''

                        #<NotHook>
                        #flush first
                        BaseClass.flush(self)
                        #</NotHook>

        def do_shape(self):

                #debug
                '''
                self.debug(
                                        [
                                                'We shape here',
#("self.",self,['ShapingDimensionTuplesList'])
                                        ]
                                )
                '''

                #Check
                if len(self.ShapingDimensionTuplesList)>0:

                        #set
                        [
                                self.ShapedSealGetKeyStrsList,
                                self.ShapedSealDimensionGetKeyStrsListsList
                        ]=SYS.unzip(self.ShapingDimensionTuplesList,[0,1])

                        #Flat and set
                        self.ShapedDimensionGetKeyStrsList=list(
                                set(
                                        SYS.flat(
self.ShapedSealDimensionGetKeyStrsListsList
                                                )
                                        )
                                )

                else:

                        #Default
                        self.ShapedSealGetKeyStrsList=[]
                        self.ShapedDimensionGetKeyStrsList=[]
                        self.ShapedSealDimensionGetKeyStrsListsList=[]

                #debug
                '''
                self.debug(("self.",self,[
'ShapedSealGetKeyStrsList',
'ShapedDimensionGetKeyStrsList'
                                                                ]))
                '''

                #Definition
                DatabasedGetKeyStrsList=SYS.unzip(self.DatabasingSealTuplesList,[0])

                #set
                self.ShapedIndexIntsList=map(
                                lambda __ShapedSealGetKeyStr:
DatabasedGetKeyStrsList.index(__ShapedSealGetKeyStr),
                                self.ShapedSealGetKeyStrsList
                        )

                #Check
                if hasattr(self,'NodePointDeriveNoder') and
self.NodePointDeriveNoder!=None:

                        #Pick
self.ShapedDimensionIntsList=self.NodePointDeriveNoder.pick(
                                self.ShapedDimensionGetKeyStrsList
                        )

                else:

                        #Default
                        self.ShapedDimensionIntsList=[]


                #debug
                '''
                self.debug(("self.",self,['ShapedDimensionIntsList']))
                '''

                #Bind with DatabasedShapedStr setting
                self.ShapedStr=ShapingJoiningStr.join(
                                                                        map(
        lambda __ShapedSealGetKeyStr,__ShapedDimensionVariable:
        ShapingJoiningStr+str(
                __ShapedSealGetKeyStr
                )+ShapingTuplingStr+str(
                __ShapedDimensionVariable),
        self.ShapedDimensionGetKeyStrsList,
        self.ShapedDimensionIntsList
)
                )

                #debug
                '''
                self.debug(('self.',self,['ShapedStr']))
                '''
#</DefineClass>


```

<small>
View the Shaper sources on <a href="https://github.com/Ledoux/ShareYourSystem/tr
ee/master/Pythonlogy/ShareYourSystem/Databasers/Shaper"
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
from ShareYourSystem.Standards.Modelers import Shaper

#Definition a structure
MyStructurer=Structurer.StructurerClass().collect(
    "Datome",
    "Things",
    Shaper.ShaperClass().update(
        [
            ('Attr_DatabasingSealTuplesList',
                [
                    ('MyInt','MyInt',tables.Int64Col()),
                    ('MyStr','MyStr',tables.StringCol(10)),
                    ('MyIntsList','MyIntsList',tables.Int64Col(shape=[3]))
                ]
            ),
            ('Attr_RowingGetStrsList',
                ['MyInt','MyStr']
            ),
            ('ShapingDimensionTuplesList',
                [
                    ('MyIntsList',['UnitsInt'])
                ]
            )
        ]
    )
)

MyStructurer.update(
    [
        ('MyInt',0),
        ('MyStr',"hello"),
        ('UnitsInt',3),
        ('MyIntsList',[0,0,1])
    ]
)['<Datome>ThingsShaper'].flush()

MyStructurer.update(
    [
        ('MyInt',1),
        ('MyStr',"bonjour"),
        ('MyIntsList',[0,0,1])
    ]
)['<Datome>ThingsShaper'].flush()


MyStructurer.update(
    [
        ('MyInt',1),
        ('MyStr',"ola"),
        ('MyIntsList',[0,1])
    ]
)['<Datome>ThingsShaper'].flush()

#Definition the AttestedStr
SYS._attest(
    [
        'MyStructurer is '+SYS._str(
        MyStructurer,
        **{
            'RepresentingAlineaIsBool':False,
            'RepresentingBaseKeyStrsListBool':False
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

MyStructurer is < (StructurerClass), 4563996560>
   /{
   /  '<New><Instance>DatomeCollectionOrderedDict' :
   /   /{
   /   /  'ThingsShaper' : < (ShaperClass), 4556968080>
   /   /   /{
   /   /   /  '<New><Instance>IdInt' : 4556968080
   /   /   /  '<New><Instance>NewtorkAttentionStr' :
   /   /   /  '<New><Instance>NewtorkCatchStr' :
   /   /   /  '<New><Instance>NewtorkCollectionStr' :
   /   /   /  '<New><Instance>NodeCollectionStr' : Datome
   /   /   /  '<New><Instance>NodeIndexInt' : 0
   /   /   /  '<New><Instance>NodeKeyStr' : ThingsShaper
   /   /   /  '<New><Instance>NodePointDeriveNoder' : {...}< (StructurerClass),
4563996560>
   /   /   /  '<New><Instance>NodePointOrderedDict' : {...}< (OrderedDict),
4563689008>
   /   /   /  '<New><Instance>ShapedErrorBool' : True
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
   /   /   /   /   /  2 : Int64Col(shape=(2,), dflt=0, pos=None)
   /   /   /   /   /)
   /   /   /   /]
   /   /   /  '<New><Instance>_RowingGetStrsList' : ['MyInt', 'MyStr']
   /   /   /  '<Spe><Instance>ShapedDimensionGetKeyStrsList' : ['UnitsInt']
   /   /   /  '<Spe><Instance>ShapedDimensionIntsList' : [2]
   /   /   /  '<Spe><Instance>ShapedIndexIntsList' : [2]
   /   /   /  '<Spe><Instance>ShapedSealDimensionGetKeyStrsListsList' :
   /   /   /   /(
   /   /   /   /  0 : ['UnitsInt']
   /   /   /   /)
   /   /   /  '<Spe><Instance>ShapedSealGetKeyStrsList' : ('MyIntsList',)
   /   /   /  '<Spe><Instance>ShapedStr' : __UnitsInt_2
   /   /   /  '<Spe><Instance>ShapingDimensionTuplesList' :
   /   /   /   /[
   /   /   /   /  0 :
   /   /   /   /   /(
   /   /   /   /   /  0 : MyIntsList
   /   /   /   /   /  1 : {...}< (list), 4556829112>
   /   /   /   /   /)
   /   /   /   /]
   /   /   /}
   /   /}
   /  '<New><Instance>IdInt' : 4563996560
   /  '<New><Instance>MyInt' : 1
   /  '<New><Instance>MyIntsList' : [0, 1]
   /  '<New><Instance>MyStr' : ola
   /  '<New><Instance>NewtorkAttentionStr' :
   /  '<New><Instance>NewtorkCatchStr' :
   /  '<New><Instance>NewtorkCollectionStr' :
   /  '<New><Instance>NodeCollectionStr' : Globals
   /  '<New><Instance>NodeIndexInt' : -1
   /  '<New><Instance>NodeKeyStr' : TopStructurer
   /  '<New><Instance>NodePointDeriveNoder' : None
   /  '<New><Instance>NodePointOrderedDict' : None
   /  '<New><Instance>UnitsInt' : 2
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

